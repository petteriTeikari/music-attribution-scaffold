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

            all_records = await repo.list_all(offset=offset, limit=limit, session=session)

            # Apply assurance_level filter if specified
            if assurance_level is not None:
                all_records = [r for r in all_records if r.assurance_level.value == assurance_level]

            # Sort by confidence descending
            all_records.sort(key=lambda r: r.confidence_score, reverse=True)

            return [r.model_dump(mode="json") for r in all_records]

    # Fallback: in-memory dict (legacy tests)
    attributions = getattr(request.app.state, "attributions", {})
    records = list(attributions.values())
    paginated = records[offset : offset + limit]
    return [r.model_dump(mode="json") for r in paginated]


@router.get("/attributions/{attribution_id}/provenance")
async def get_provenance(
    request: Request,
    attribution_id: uuid.UUID,
) -> dict:
    """Get full provenance chain with uncertainty metadata for an attribution.

    Returns the provenance chain, uncertainty summary, and citation-ready data
    for Perplexity-like inline source references.

    Args:
        request: FastAPI request with app state.
        attribution_id: Attribution record UUID.

    Returns:
        Provenance chain with uncertainty metadata.
    """
    if hasattr(request.app.state, "async_session_factory"):
        repo = AsyncAttributionRepository()
        async with await _get_session(request) as session:
            record = await repo.find_by_id(attribution_id, session)
            if record is not None:
                return {
                    "attribution_id": str(record.attribution_id),
                    "provenance_chain": [e.model_dump(mode="json") for e in record.provenance_chain],
                    "uncertainty_summary": (
                        record.uncertainty_summary.model_dump(mode="json") if record.uncertainty_summary else None
                    ),
                }

    # Fallback: in-memory dict (legacy tests)
    attributions: dict[uuid.UUID, AttributionRecord] = getattr(request.app.state, "attributions", {})
    for record in attributions.values():
        if record.attribution_id == attribution_id:
            return {
                "attribution_id": str(record.attribution_id),
                "provenance_chain": [e.model_dump(mode="json") for e in record.provenance_chain],
                "uncertainty_summary": (
                    record.uncertainty_summary.model_dump(mode="json") if record.uncertainty_summary else None
                ),
            }

    raise HTTPException(status_code=404, detail="Attribution not found")


@router.get("/attributions/search")
async def search_attributions(
    request: Request,
    q: str = Query(default="", description="Search query"),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[dict]:
    """Hybrid search across attribution records using RRF fusion.

    Combines full-text search, vector similarity, and graph context.

    Args:
        request: FastAPI request with app state.
        q: Search query string.
        limit: Maximum number of results.

    Returns:
        List of results with attribution record and RRF score.
    """
    from music_attribution.search.hybrid_search import HybridSearchService

    service = HybridSearchService()
    async with await _get_session(request) as session:
        results = await service.search(q, limit=limit, session=session)
        return [
            {
                "attribution": r.record.model_dump(mode="json"),
                "rrf_score": r.rrf_score,
            }
            for r in results
        ]
