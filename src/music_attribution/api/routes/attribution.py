"""Attribution query endpoints backed by async PostgreSQL repository."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from music_attribution.attribution.persistence import AsyncAttributionRepository
from music_attribution.schemas.attribution import AttributionRecord

router = APIRouter()


async def _get_session(request: Request) -> AsyncSession:
    """Get an async session from the app's session factory."""
    factory: async_sessionmaker[AsyncSession] = request.app.state.async_session_factory
    return factory()


@router.get("/attributions/work/{work_id}")
async def get_attribution_by_work_id(
    request: Request,
    work_id: uuid.UUID,
) -> dict:
    """Get attribution record by work entity ID.

    Args:
        request: FastAPI request with app state.
        work_id: Work entity UUID.

    Returns:
        Attribution record as JSON.
    """
    # Try database first, fall back to in-memory for backward compatibility
    if hasattr(request.app.state, "async_session_factory"):
        repo = AsyncAttributionRepository()
        async with await _get_session(request) as session:
            record = await repo.find_by_work_entity_id(work_id, session)
            if record is not None:
                return record.model_dump(mode="json")

    # Fallback: in-memory dict (legacy tests)
    attributions: dict[uuid.UUID, AttributionRecord] = getattr(request.app.state, "attributions", {})
    fallback_record = attributions.get(work_id)
    if fallback_record is None:
        raise HTTPException(status_code=404, detail="Attribution not found")
    return fallback_record.model_dump(mode="json")


@router.get("/attributions/")
async def list_attributions(
    request: Request,
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    needs_review: bool | None = Query(default=None),
    assurance_level: str | None = Query(default=None),
) -> list[dict]:
    """List attribution records with pagination, filtering, and sorting.

    Args:
        request: FastAPI request with app state.
        limit: Maximum number of results.
        offset: Number of records to skip.
        needs_review: Filter by needs_review flag.
        assurance_level: Filter by assurance level (e.g., LEVEL_3).

    Returns:
        List of attribution records sorted by confidence descending.
    """
    if hasattr(request.app.state, "async_session_factory"):
        repo = AsyncAttributionRepository()
        async with await _get_session(request) as session:
            if needs_review is True:
                records = await repo.find_needs_review(limit=limit, session=session)
                return [r.model_dump(mode="json") for r in records]

            all_records = await repo.list_all(
                offset=offset, limit=limit, session=session
            )

            # Apply assurance_level filter if specified
            if assurance_level is not None:
                all_records = [
                    r for r in all_records if r.assurance_level.value == assurance_level
                ]

            # Sort by confidence descending
            all_records.sort(key=lambda r: r.confidence_score, reverse=True)

            return [r.model_dump(mode="json") for r in all_records]

    # Fallback: in-memory dict (legacy tests)
    attributions = getattr(request.app.state, "attributions", {})
    records = list(attributions.values())
    paginated = records[offset : offset + limit]
    return [r.model_dump(mode="json") for r in paginated]
