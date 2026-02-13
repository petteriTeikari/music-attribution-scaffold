"""Hybrid search with Reciprocal Rank Fusion (RRF).

Combines three search modalities into a single ranked result set:

1. **Text search** -- LIKE queries on JSONB credits and provenance
   fields (via ``TextSearchService``).
2. **Vector similarity** -- cosine distance on entity embeddings
   (via ``EmbeddingMatcher``), mapped back to attribution records.
3. **Graph context** -- 1-hop edge neighbours of vector-matched
   entities, providing relational context expansion.

Results from each modality are fused using Reciprocal Rank Fusion::

    RRF_score(d) = sum(1 / (k + rank_i(d))) for each modality i

where ``k = 60`` (standard value from Cormack et al., 2009). This
produces a robust combined ranking that is insensitive to score
scale differences between modalities.

Classes
-------
HybridSearchResult
    Named tuple pairing an ``AttributionRecord`` with its RRF score.
HybridSearchService
    Orchestrates the three modalities and performs RRF fusion.

See Also
--------
music_attribution.search.text_search : Text modality.
music_attribution.search.vector_search : Vector modality.
music_attribution.db.models.EdgeModel : Graph edges for context.
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
    """A single hybrid search result with fused RRF score.

    Attributes
    ----------
    record : AttributionRecord
        Full attribution record (BO-3 boundary object).
    rrf_score : float
        Reciprocal Rank Fusion score (higher = more relevant).
        Not bounded to [0, 1]; maximum theoretical value is
        ``3 / (k + 1)`` when a document ranks first in all modalities.
    """

    record: AttributionRecord
    rrf_score: float


class HybridSearchService:
    """Hybrid search combining text, vector, and graph modalities via RRF.

    Orchestrates three independent search modalities and fuses their
    rankings using Reciprocal Rank Fusion. Each modality produces a
    ranked list of attribution record IDs; the RRF algorithm combines
    these into a single ranking without requiring score normalisation.

    The service is stateless -- each ``search()`` call runs all three
    modalities independently and fuses the results.

    Attributes
    ----------
    _text_search : TextSearchService
        LIKE-based text search on JSONB fields.
    _matcher : EmbeddingMatcher
        Embedding model for query vectorisation.
    """

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
        """Run hybrid search across all three modalities with RRF fusion.

        Execution order:

        1. Text search (LIKE on credits and provenance JSONB).
        2. Vector search (embed query, cosine similarity on entity
           embeddings, map entity IDs to attribution IDs).
        3. Graph context (1-hop neighbours of vector-matched entities,
           mapped to attribution IDs).
        4. RRF fusion across all modalities.
        5. Fetch full ``AttributionRecord`` objects for top results.

        Parameters
        ----------
        query : str
            Free-text search query.
        limit : int, optional
            Maximum number of results to return. Default is 50.
        session : AsyncSession
            Active async database session for all queries.

        Returns
        -------
        list[HybridSearchResult]
            Ranked list of results sorted by RRF score descending.
            Each result pairs an ``AttributionRecord`` with its
            fused score.
        """
        # Collect per-attribution_id rank from each modality
        # rank is 1-based position in that modality's result list
        text_ranks: dict[uuid.UUID, int] = {}
        vector_ranks: dict[uuid.UUID, int] = {}
        graph_ranks: dict[uuid.UUID, int] = {}

        # --- Modality 1: Text search ---
        text_results = await self._text_search.search(
            query,
            limit=limit * 2,
            session=session,
        )
        for rank, record in enumerate(text_results, start=1):
            text_ranks[record.attribution_id] = rank

        # --- Modality 2: Vector similarity search ---
        vector_entity_ids = await self._vector_search_by_query(query, limit=limit, session=session)
        # Map entity_ids to attribution_ids
        vector_attribution_ids = await self._entities_to_attributions(
            [eid for eid, _ in vector_entity_ids],
            session=session,
        )
        for rank, attr_id in enumerate(vector_attribution_ids, start=1):
            if attr_id not in vector_ranks:
                vector_ranks[attr_id] = rank

        # --- Modality 3: Graph context ---
        # Find graph neighbors of entities from vector search
        matched_entity_ids = {eid for eid, _ in vector_entity_ids}
        neighbor_entity_ids = await self._graph_neighbors(matched_entity_ids, session=session)
        neighbor_attribution_ids = await self._entities_to_attributions(
            list(neighbor_entity_ids),
            session=session,
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
        """Embed the query text and find similar entity embeddings.

        Uses the ``EmbeddingMatcher`` to vectorise the query, then
        computes cosine similarity against all entity embeddings in
        the database. Similarity scores are clamped to [0.0, 1.0].

        Parameters
        ----------
        query : str
            Search query text to embed.
        limit : int
            Maximum number of similar entities to return.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[tuple[uuid.UUID, float]]
            List of ``(entity_id, similarity)`` sorted by similarity
            descending, truncated to ``limit``.
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
        """Map resolved entity IDs to attribution record IDs.

        An entity can appear in attribution records in two places:

        1. As ``work_entity_id`` (the work itself).
        2. Inside the ``credits`` JSONB array (as ``entity_id`` in
           individual credit entries).

        For cross-database compatibility, the credits check uses
        ``LIKE`` on the stringified JSONB rather than PostgreSQL-specific
        JSONB operators.

        Parameters
        ----------
        entity_ids : list[uuid.UUID]
            Entity UUIDs to map.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[uuid.UUID]
            Attribution record UUIDs that reference any of the given
            entities, ordered by confidence score descending.
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
        """Find 1-hop graph neighbours of the given entities.

        Queries the ``edges`` table for any edge where the given
        entities appear as either source or target. Returns the set
        of neighbour entity IDs, excluding the input entities.

        Parameters
        ----------
        entity_ids : set[uuid.UUID]
            Seed entity UUIDs to expand.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        set[uuid.UUID]
            Neighbour entity UUIDs (excluding the input set).
        """
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
