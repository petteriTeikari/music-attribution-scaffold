"""Text search service for attribution records.

Provides LIKE-based text search across attribution record JSONB fields.
On PostgreSQL, this could be upgraded to use tsvector + GIN indexes
for much better performance. The LIKE fallback works on both
PostgreSQL and SQLite for development/testing.
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
    """Text search across attribution records.

    Uses LIKE queries on JSONB fields for cross-database compatibility.
    Searches through credits (role_detail) and provenance_chain text.
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

        Args:
            query: Search string (empty returns all records).
            limit: Maximum results to return.
            offset: Number of results to skip.
            session: Active async database session.

        Returns:
            Matching attribution records sorted by confidence descending.
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
