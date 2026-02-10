"""Attribution query endpoints."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException, Query, Request

from music_attribution.schemas.attribution import AttributionRecord

router = APIRouter()


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
    attributions: dict[uuid.UUID, AttributionRecord] = request.app.state.attributions
    record = attributions.get(work_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Attribution not found")
    return record.model_dump(mode="json")


@router.get("/attributions/")
async def list_attributions(
    request: Request,
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> list[dict]:
    """List attribution records with pagination.

    Args:
        request: FastAPI request with app state.
        limit: Maximum number of results.
        offset: Number of records to skip.

    Returns:
        List of attribution records.
    """
    attributions: dict[uuid.UUID, AttributionRecord] = request.app.state.attributions
    records = list(attributions.values())
    paginated = records[offset : offset + limit]
    return [r.model_dump(mode="json") for r in paginated]
