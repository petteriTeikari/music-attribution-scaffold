"""Attribution query endpoints backed by async PostgreSQL repository.

Provides CRUD-style read endpoints for attribution records:

* ``GET /api/v1/attributions/work/{work_id}`` — single attribution by work ID
* ``GET /api/v1/attributions/`` — paginated list with optional filters
* ``GET /api/v1/attributions/{attribution_id}/provenance`` — provenance chain
* ``GET /api/v1/attributions/search`` — hybrid search via RRF fusion

All endpoints return JSON representations of ``AttributionRecord``
domain objects.  The provenance endpoint exposes the full evidence chain
with uncertainty metadata, enabling *Perplexity-style* inline source
references (see companion paper, Section 5.2).

Notes
-----
Sessions are obtained from ``app.state.async_session_factory`` via the
``_get_session`` helper rather than ``Depends`` — this keeps the router
self-contained without requiring the caller to wire up a dependency
override.
"""

from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from music_attribution.attribution.persistence import AsyncAttributionRepository

router = APIRouter()


async def _get_session(request: Request) -> AsyncSession:
    """Get an async session from the application's session factory.

    Parameters
    ----------
    request : Request
        FastAPI request object with access to ``app.state``.

    Returns
    -------
    AsyncSession
        A new async database session (caller must use it as a context
        manager to ensure proper cleanup).
    """
    factory: async_sessionmaker[AsyncSession] = request.app.state.async_session_factory
    return factory()


@router.get("/attributions/work/{work_id}")
async def get_attribution_by_work_id(
    request: Request,
    work_id: uuid.UUID,
) -> dict:
    """Get a single attribution record by work entity ID.

    ``GET /api/v1/attributions/work/{work_id}``

    Looks up the attribution record associated with a specific musical
    work entity.  Returns 404 if no attribution exists for the given ID.

    Parameters
    ----------
    request : Request
        FastAPI request with access to ``app.state``.
    work_id : uuid.UUID
        UUID of the work entity to look up.

    Returns
    -------
    dict
        JSON-serializable attribution record.

    Raises
    ------
    HTTPException
        404 if no attribution is found for the given ``work_id``.
    """
    repo = AsyncAttributionRepository()
    async with await _get_session(request) as session:
        record = await repo.find_by_work_entity_id(work_id, session)
        if record is None:
            raise HTTPException(status_code=404, detail="Attribution not found")
        return record.model_dump(mode="json")


@router.get("/attributions/")
async def list_attributions(
    request: Request,
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    needs_review: bool | None = Query(default=None),
    assurance_level: str | None = Query(default=None),
) -> list[dict]:
    """List attribution records with pagination, filtering, and sorting.

    ``GET /api/v1/attributions/``

    Returns attribution records ordered by confidence score (descending).
    Supports pagination via ``limit``/``offset`` and optional filtering
    by ``needs_review`` flag or ``assurance_level`` tier (A0-A3).

    Parameters
    ----------
    request : Request
        FastAPI request with access to ``app.state``.
    limit : int, optional
        Maximum number of records to return (1-100), by default 50.
    offset : int, optional
        Number of records to skip for pagination, by default 0.
    needs_review : bool or None, optional
        If ``True``, return only records flagged for human review.
        If ``None`` (default), no review filter is applied.
    assurance_level : str or None, optional
        Filter by assurance level value (e.g., ``"LEVEL_3"`` for
        artist-verified).  Maps to the A0-A3 tiered provenance system
        described in the companion paper (Section 3).

    Returns
    -------
    list[dict]
        JSON-serializable list of attribution records sorted by
        confidence score descending.
    """
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


@router.get("/attributions/{attribution_id}/provenance")
async def get_provenance(
    request: Request,
    attribution_id: uuid.UUID,
) -> dict:
    """Get the full provenance chain with uncertainty metadata.

    ``GET /api/v1/attributions/{attribution_id}/provenance``

    Returns the ordered provenance chain (evidence trail) and the
    uncertainty summary for a specific attribution record.  This data
    enables *Perplexity-style* inline source references in the frontend,
    where each claim can be traced back to its originating data source.

    The uncertainty summary includes conformal prediction intervals and
    source agreement metrics (see companion paper, Section 5.2).

    Parameters
    ----------
    request : Request
        FastAPI request with access to ``app.state``.
    attribution_id : uuid.UUID
        UUID of the attribution record whose provenance is requested.

    Returns
    -------
    dict
        Dictionary with keys:

        * ``attribution_id`` : str — UUID as string.
        * ``provenance_chain`` : list[dict] — ordered evidence entries.
        * ``uncertainty_summary`` : dict or None — calibration metadata.

    Raises
    ------
    HTTPException
        404 if no attribution record exists for the given ID.
    """
    repo = AsyncAttributionRepository()
    async with await _get_session(request) as session:
        record = await repo.find_by_id(attribution_id, session)
        if record is None:
            raise HTTPException(status_code=404, detail="Attribution not found")
        return {
            "attribution_id": str(record.attribution_id),
            "provenance_chain": [e.model_dump(mode="json") for e in record.provenance_chain],
            "uncertainty_summary": (
                record.uncertainty_summary.model_dump(mode="json") if record.uncertainty_summary else None
            ),
        }


@router.get("/attributions/search")
async def search_attributions(
    request: Request,
    q: str = Query(default="", max_length=500, description="Search query"),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[dict]:
    """Hybrid search across attribution records using RRF fusion.

    ``GET /api/v1/attributions/search``

    Combines three retrieval signals via Reciprocal Rank Fusion (RRF):

    1. Full-text search (PostgreSQL ``tsvector``)
    2. Vector similarity (pgvector cosine distance)
    3. Graph context (entity relationship traversal)

    This multi-signal approach reduces the risk of any single retrieval
    method dominating results.

    Parameters
    ----------
    request : Request
        FastAPI request with access to ``app.state``.
    q : str, optional
        Search query string, by default ``""``.
    limit : int, optional
        Maximum number of results to return (1-100), by default 20.

    Returns
    -------
    list[dict]
        List of dictionaries, each containing:

        * ``attribution`` : dict — full attribution record.
        * ``rrf_score`` : float — fused relevance score (higher is better).
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
