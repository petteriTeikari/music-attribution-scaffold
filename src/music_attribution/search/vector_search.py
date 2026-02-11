"""Vector similarity search service for entity embeddings.

Uses pgvector cosine distance on PostgreSQL. Falls back to Python-side
cosine similarity on SQLite (unit tests). Production deployments use
HNSW indexes for sub-linear search performance.
"""

from __future__ import annotations

import json
import logging
import math
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import EntityEmbeddingModel, ResolvedEntityModel

logger = logging.getLogger(__name__)


def _cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Compute cosine similarity between two vectors.

    Returns:
        Score between -1 and 1 (clamped to 0-1 for search results).
    """
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b, strict=True))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def _parse_embedding(raw: object) -> list[float]:
    """Parse embedding from database storage format.

    PostgreSQL returns a HalfVector via pgvector; SQLite stores as JSON string.
    """
    if isinstance(raw, (list, tuple)):
        return [float(v) for v in raw]
    if isinstance(raw, str):
        return [float(v) for v in json.loads(raw)]
    # pgvector HalfVector — convert via .to_list()
    if hasattr(raw, "to_list"):
        return [float(v) for v in raw.to_list()]
    msg = f"Unexpected embedding type: {type(raw)}"
    raise TypeError(msg)


class VectorSearchService:
    """Vector similarity search across entity embeddings.

    Fetches embeddings from the database and computes cosine similarity.
    On PostgreSQL with pgvector, the <=> operator can be used for
    index-accelerated search (HNSW). This implementation uses Python-side
    computation for cross-database compatibility in tests.
    """

    async def find_similar(
        self,
        entity_id: uuid.UUID,
        *,
        limit: int = 10,
        threshold: float = 0.0,
        entity_type: str | None = None,
        session: AsyncSession,
    ) -> list[tuple[uuid.UUID, float]]:
        """Find entities with similar embeddings.

        Args:
            entity_id: UUID of the query entity.
            limit: Maximum number of results.
            threshold: Minimum cosine similarity (0-1).
            entity_type: Optional filter to restrict results by entity type.
            session: Active async database session.

        Returns:
            List of (entity_id, similarity_score) tuples sorted by
            similarity descending. The query entity is excluded.
        """
        # Fetch the query entity's embedding
        query_stmt = select(EntityEmbeddingModel.embedding).where(
            EntityEmbeddingModel.entity_id == entity_id,
        )
        result = await session.execute(query_stmt)
        query_embedding_raw = result.scalar_one_or_none()

        if query_embedding_raw is None:
            logger.warning("No embedding found for entity %s", entity_id)
            return []

        query_embedding = _parse_embedding(query_embedding_raw)

        # Fetch candidate embeddings (excluding the query entity)
        if entity_type is not None:
            # Join with resolved_entities to filter by type
            candidates_stmt = (
                select(EntityEmbeddingModel.entity_id, EntityEmbeddingModel.embedding)
                .join(
                    ResolvedEntityModel,
                    EntityEmbeddingModel.entity_id == ResolvedEntityModel.entity_id,
                )
                .where(
                    EntityEmbeddingModel.entity_id != entity_id,
                    ResolvedEntityModel.entity_type == entity_type,
                )
            )
        else:
            candidates_stmt = select(
                EntityEmbeddingModel.entity_id,
                EntityEmbeddingModel.embedding,
            ).where(EntityEmbeddingModel.entity_id != entity_id)

        result = await session.execute(candidates_stmt)
        candidates = result.all()

        # Compute similarities
        scored: list[tuple[uuid.UUID, float]] = []
        for candidate_id, candidate_embedding_raw in candidates:
            candidate_embedding = _parse_embedding(candidate_embedding_raw)
            similarity = _cosine_similarity(query_embedding, candidate_embedding)
            # Clamp to [0, 1] range for search results
            similarity = max(0.0, min(1.0, similarity))
            if similarity >= threshold:
                scored.append((candidate_id, similarity))

        # Sort by similarity descending
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:limit]
