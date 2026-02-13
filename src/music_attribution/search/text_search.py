"""Text search service for attribution records.

Provides LIKE-based text search across attribution record JSONB fields
(credits and provenance_chain). This is the simplest search modality
in the hybrid search stack, designed for cross-database compatibility.

On PostgreSQL, this could be upgraded to use ``tsvector`` + GIN indexes
for significantly better performance on large datasets. The current
LIKE-based approach works identically on both PostgreSQL and SQLite,
ensuring consistent behaviour between production and unit tests.

Classes
-------
TextSearchService
    Async search service with paginated LIKE queries.

See Also
--------
music_attribution.search.hybrid_search : Uses this as modality 1.
music_attribution.search.vector_search : Complementary vector modality.
"""

from __future__ import annotations

import logging

from sqlalchemy import cast, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.types import String

from music_attribution.attribution.persistence import _model_to_record
from music_attribution.db.models import AttributionRecordModel
from music_attribution.schemas.attribution import AttributionRecord

logger = logging.getLogger(__name__)


class TextSearchService:
    """Text search across attribution records using LIKE queries.

    Searches through the stringified JSONB ``credits`` and
    ``provenance_chain`` columns for substring matches. Results are
    sorted by confidence score descending with pagination support.

    This service is stateless and can be instantiated freely.

    Notes
    -----
    The LIKE approach has O(n) performance on the full table. For
    production datasets, upgrade to PostgreSQL ``tsvector`` columns
    with GIN indexes and ``ts_rank`` scoring.
    """

    async def search(
        self,
        query: str,
        *,
        limit: int = 50,
        offset: int = 0,
        session: AsyncSession,
    ) -> list[AttributionRecord]:
        """Search attribution records by text query.

        An empty query returns all records (useful for browsing).
        Non-empty queries perform case-sensitive LIKE matching on the
        stringified ``credits`` and ``provenance_chain`` JSONB columns.

        Parameters
        ----------
        query : str
            Search string. Empty string returns all records with
            pagination.
        limit : int, optional
            Maximum number of results to return. Default is 50.
        offset : int, optional
            Number of results to skip for pagination. Default is 0.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[AttributionRecord]
            Matching attribution records (Pydantic BO-3 objects)
            sorted by confidence score descending.
        """
        if not query.strip():
            # Empty query: return all records with pagination
            stmt = (
                select(AttributionRecordModel)
                .order_by(AttributionRecordModel.confidence_score.desc())
                .offset(offset)
                .limit(limit)
            )
        else:
            # Search within JSONB credits text (contains role_detail, names, etc.)
            search_pattern = f"%{query}%"
            stmt = (
                select(AttributionRecordModel)
                .where(
                    cast(AttributionRecordModel.credits, String).like(search_pattern)
                    | cast(AttributionRecordModel.provenance_chain, String).like(search_pattern)
                )
                .order_by(AttributionRecordModel.confidence_score.desc())
                .offset(offset)
                .limit(limit)
            )

        result = await session.execute(stmt)
        models = result.scalars().all()
        return [_model_to_record(m) for m in models]
