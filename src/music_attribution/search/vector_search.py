"""Vector similarity search service for entity embeddings.

Provides cosine similarity search across entity embeddings stored in
the ``entity_embeddings`` table. On PostgreSQL with pgvector, the
``<=>`` (cosine distance) operator can be used with HNSW indexes for
sub-linear search performance. This implementation uses Python-side
cosine computation for cross-database compatibility with SQLite in
unit tests.

Functions
---------
_cosine_similarity
    Compute cosine similarity between two vectors.
_parse_embedding
    Parse embeddings from various database storage formats.

Classes
-------
VectorSearchService
    Async service for finding similar entities by embedding distance.

See Also
--------
music_attribution.search.hybrid_search : Uses this as modality 2.
music_attribution.db.models.EntityEmbeddingModel : Embedding storage.
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
    """Compute cosine similarity between two float vectors.

    Uses a pure-Python dot-product implementation for cross-database
    compatibility (no numpy dependency). For production workloads,
    pgvector's ``<=>`` operator provides hardware-accelerated distance.

    Parameters
    ----------
    vec_a : list[float]
        First vector.
    vec_b : list[float]
        Second vector (must have the same length as ``vec_a``).

    Returns
    -------
    float
        Cosine similarity score. Mathematically in [-1, 1], but
        callers typically clamp to [0, 1] for search ranking.
    """
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b, strict=True))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def _parse_embedding(raw: object) -> list[float]:
    """Parse an embedding vector from database storage format.

    Handles three storage formats depending on the database backend:

    - **PostgreSQL + pgvector**: Returns a ``HalfVector`` object with
      a ``.to_list()`` method.
    - **SQLite**: Returns a JSON string that must be deserialised.
    - **In-memory / test fixtures**: Returns a Python ``list`` or
      ``tuple`` directly.

    Parameters
    ----------
    raw : object
        Raw embedding value from the ORM column.

    Returns
    -------
    list[float]
        Parsed embedding as a list of Python floats.

    Raises
    ------
    TypeError
        If the raw value does not match any known storage format.
    """
    if isinstance(raw, list | tuple):
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

    Fetches embeddings from the ``entity_embeddings`` table and computes
    cosine similarity in Python. On PostgreSQL with pgvector, the
    ``<=>`` operator with HNSW indexes provides hardware-accelerated
    approximate nearest neighbour search. This Python-side implementation
    ensures cross-database compatibility for unit tests on SQLite.

    The service is stateless and can be instantiated freely.
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
        """Find entities with similar embeddings to a given entity.

        Fetches the query entity's embedding, then computes cosine
        similarity against all candidate embeddings in the database.
        Results are filtered by minimum threshold, optionally filtered
        by entity type, and sorted by similarity descending.

        Parameters
        ----------
        entity_id : uuid.UUID
            UUID of the query entity whose embedding is the reference.
        limit : int, optional
            Maximum number of results to return. Default is 10.
        threshold : float, optional
            Minimum cosine similarity (0.0--1.0) for inclusion in
            results. Default is 0.0 (include all).
        entity_type : str | None, optional
            If provided, restricts candidate entities to this type
            (e.g. ``"artist"``, ``"work"``). Requires a join with
            ``resolved_entities``.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[tuple[uuid.UUID, float]]
            List of ``(entity_id, similarity_score)`` tuples sorted by
            similarity descending. The query entity is excluded from
            results. Similarity scores are clamped to [0.0, 1.0].
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
