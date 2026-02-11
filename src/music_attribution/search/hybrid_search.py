"""Hybrid search with Reciprocal Rank Fusion (RRF).

Combines three search modalities:
1. Full-text search (LIKE on JSONB fields)
2. Vector similarity search (cosine distance on entity embeddings)
3. Graph context (edge neighbors of matched entities)

Results are fused using RRF: score = Σ(1 / (k + rank_i)) across modalities.
"""

from __future__ import annotations

import logging
import uuid
from typing import NamedTuple

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import AttributionRecordModel, EdgeModel, EntityEmbeddingModel
from music_attribution.resolution.embedding_match import EmbeddingMatcher
from music_attribution.schemas.attribution import AttributionRecord
from music_attribution.search.text_search import TextSearchService
from music_attribution.search.vector_search import _cosine_similarity, _parse_embedding

logger = logging.getLogger(__name__)

# RRF constant (standard value from the original RRF paper)
RRF_K = 60


class HybridSearchResult(NamedTuple):
    """A single hybrid search result with fused score."""

    record: AttributionRecord
    rrf_score: float


class HybridSearchService:
    """Hybrid search combining text, vector, and graph modalities via RRF."""

    def __init__(self) -> None:
        self._text_search = TextSearchService()
        self._matcher = EmbeddingMatcher()

    async def search(
        self,
        query: str,
        *,
        limit: int = 50,
        session: AsyncSession,
    ) -> list[HybridSearchResult]:
        """Run hybrid search across all modalities.

        Args:
            query: Search query text.
            limit: Maximum results to return.
            session: Active async database session.

        Returns:
            Ranked list of HybridSearchResult sorted by RRF score descending.
        """
        # Collect per-attribution_id rank from each modality
        # rank is 1-based position in that modality's result list
        text_ranks: dict[uuid.UUID, int] = {}
        vector_ranks: dict[uuid.UUID, int] = {}
        graph_ranks: dict[uuid.UUID, int] = {}

        # --- Modality 1: Text search ---
        text_results = await self._text_search.search(
            query, limit=limit * 2, session=session,
        )
        for rank, record in enumerate(text_results, start=1):
            text_ranks[record.attribution_id] = rank

        # --- Modality 2: Vector similarity search ---
        vector_entity_ids = await self._vector_search_by_query(query, limit=limit, session=session)
        # Map entity_ids to attribution_ids
        vector_attribution_ids = await self._entities_to_attributions(
            [eid for eid, _ in vector_entity_ids], session=session,
        )
        for rank, attr_id in enumerate(vector_attribution_ids, start=1):
            if attr_id not in vector_ranks:
                vector_ranks[attr_id] = rank

        # --- Modality 3: Graph context ---
        # Find graph neighbors of entities from vector search
        matched_entity_ids = {eid for eid, _ in vector_entity_ids}
        neighbor_entity_ids = await self._graph_neighbors(matched_entity_ids, session=session)
        neighbor_attribution_ids = await self._entities_to_attributions(
            list(neighbor_entity_ids), session=session,
        )
        for rank, attr_id in enumerate(neighbor_attribution_ids, start=1):
            if attr_id not in graph_ranks:
                graph_ranks[attr_id] = rank

        # --- RRF Fusion ---
        all_attribution_ids = set(text_ranks) | set(vector_ranks) | set(graph_ranks)
        scored: list[tuple[uuid.UUID, float]] = []
        for attr_id in all_attribution_ids:
            score = 0.0
            if attr_id in text_ranks:
                score += 1.0 / (RRF_K + text_ranks[attr_id])
            if attr_id in vector_ranks:
                score += 1.0 / (RRF_K + vector_ranks[attr_id])
            if attr_id in graph_ranks:
                score += 1.0 / (RRF_K + graph_ranks[attr_id])
            scored.append((attr_id, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        top_ids = scored[:limit]

        # Fetch full attribution records for top results
        record_map: dict[uuid.UUID, AttributionRecord] = {}
        for record in text_results:
            record_map[record.attribution_id] = record

        # Fetch any records not already in text_results
        missing_ids = [aid for aid, _ in top_ids if aid not in record_map]
        if missing_ids:
            from music_attribution.attribution.persistence import _model_to_record

            stmt = select(AttributionRecordModel).where(
                AttributionRecordModel.attribution_id.in_(missing_ids),
            )
            result = await session.execute(stmt)
            for model in result.scalars().all():
                record_map[model.attribution_id] = _model_to_record(model)

        return [
            HybridSearchResult(record=record_map[attr_id], rrf_score=score)
            for attr_id, score in top_ids
            if attr_id in record_map
        ]

    async def _vector_search_by_query(
        self,
        query: str,
        *,
        limit: int,
        session: AsyncSession,
    ) -> list[tuple[uuid.UUID, float]]:
        """Embed query text and find similar entity embeddings.

        Returns:
            List of (entity_id, similarity) sorted by similarity descending.
        """
        query_embedding = await self._matcher.embed(query)

        # Fetch all entity embeddings
        stmt = select(EntityEmbeddingModel.entity_id, EntityEmbeddingModel.embedding)
        result = await session.execute(stmt)
        candidates = result.all()

        scored: list[tuple[uuid.UUID, float]] = []
        for entity_id, raw_embedding in candidates:
            candidate_embedding = _parse_embedding(raw_embedding)
            similarity = _cosine_similarity(query_embedding, candidate_embedding)
            similarity = max(0.0, min(1.0, similarity))
            scored.append((entity_id, similarity))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:limit]

    async def _entities_to_attributions(
        self,
        entity_ids: list[uuid.UUID],
        *,
        session: AsyncSession,
    ) -> list[uuid.UUID]:
        """Map entity IDs to attribution record IDs.

        An entity appears in attribution records via the credits JSONB
        (as entity_id in credit entries) or as work_entity_id.
        For efficiency, we check work_entity_id and credits text.
        """
        if not entity_ids:
            return []

        from sqlalchemy import ColumnElement, String, cast, or_

        conditions: list[ColumnElement[bool]] = []
        for eid in entity_ids:
            eid_str = str(eid)
            conditions.append(
                cast(AttributionRecordModel.credits, String).like(f"%{eid_str}%"),
            )
            conditions.append(AttributionRecordModel.work_entity_id == eid)

        stmt = (
            select(AttributionRecordModel.attribution_id)
            .where(or_(*conditions))
            .order_by(AttributionRecordModel.confidence_score.desc())
        )
        result = await session.execute(stmt)
        return [row[0] for row in result.all()]

    async def _graph_neighbors(
        self,
        entity_ids: set[uuid.UUID],
        *,
        session: AsyncSession,
    ) -> set[uuid.UUID]:
        """Find 1-hop graph neighbors of the given entities."""
        if not entity_ids:
            return set()

        from sqlalchemy import or_

        stmt = select(EdgeModel.from_entity_id, EdgeModel.to_entity_id).where(
            or_(
                EdgeModel.from_entity_id.in_(entity_ids),
                EdgeModel.to_entity_id.in_(entity_ids),
            ),
        )
        result = await session.execute(stmt)
        neighbors: set[uuid.UUID] = set()
        for from_id, to_id in result.all():
            neighbors.add(from_id)
            neighbors.add(to_id)

        # Exclude the original entities
        return neighbors - entity_ids
