"""Embedding generation and persistence service.

Generates sentence-transformer embeddings and stores them in the
``entity_embeddings`` table via pgvector ``halfvec(768)``. Builds on the
existing ``EmbeddingMatcher`` for model loading and encoding.

This service bridges the gap between the in-memory ``EmbeddingMatcher``
(used for development/testing) and production PostgreSQL storage. It
handles:

- Embedding generation from formatted entity text.
- Idempotent storage (skips if embedding already exists for entity + model).
- Entity text formatting for consistent embedding input.

Notes
-----
The ``all-MiniLM-L6-v2`` model produces 384-dimensional embeddings, but
the pgvector column is configured as ``halfvec(768)`` to accommodate
potential model upgrades without schema migration.

See Also
--------
music_attribution.resolution.embedding_match : In-memory embedding matcher.
music_attribution.db.models.EntityEmbeddingModel : SQLAlchemy ORM model.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import EntityEmbeddingModel
from music_attribution.resolution.embedding_match import EmbeddingMatcher

logger = logging.getLogger(__name__)

MODEL_NAME = "all-MiniLM-L6-v2"
MODEL_VERSION = "1.0.0"


class EmbeddingService:
    """Service for generating and persisting entity embeddings.

    Uses sentence-transformers (``all-MiniLM-L6-v2``) to generate dense
    embeddings and stores them in PostgreSQL via pgvector ``halfvec``.
    Delegates model loading to ``EmbeddingMatcher`` for consistency.

    Parameters
    ----------
    model_name : str, optional
        Sentence-transformer model name. Default is ``MODEL_NAME``
        (``"all-MiniLM-L6-v2"``).

    Attributes
    ----------
    _matcher : EmbeddingMatcher
        Underlying matcher used for model loading and encoding.
    _model_name : str
        Model name for database record tracking.
    """

    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self._matcher = EmbeddingMatcher(model_name=model_name)
        self._model_name = model_name

    def generate_embedding(self, text: str) -> list[float]:
        """Generate a dense embedding vector for text.

        Parameters
        ----------
        text : str
            Input text to embed (typically formatted via ``format_entity_text``).

        Returns
        -------
        list[float]
            Embedding vector. Dimensionality depends on the model
            (384 for ``all-MiniLM-L6-v2``).

        Raises
        ------
        ImportError
            If ``sentence-transformers`` is not installed.
        """
        model = self._matcher._get_model()  # noqa: SLF001
        result = model.encode([text])
        return [float(v) for v in result[0]]

    @staticmethod
    def format_entity_text(
        canonical_name: str,
        entity_type: str,
        alternative_names: list[str] | None = None,
    ) -> str:
        """Format entity fields into text suitable for embedding.

        Produces a pipe-separated string combining entity type, canonical
        name, and any alternative names. This format gives the
        sentence-transformer model enough context to produce discriminative
        embeddings.

        Parameters
        ----------
        canonical_name : str
            Primary entity name.
        entity_type : str
            Entity type string (e.g., ``"ARTIST"``, ``"WORK"``).
        alternative_names : list[str] | None, optional
            Alternative names to include in the embedding text.

        Returns
        -------
        str
            Formatted text string (e.g.,
            ``"ARTIST: Bjork | Also known as: Bjork Gudmundsdottir"``).
        """
        parts = [f"{entity_type}: {canonical_name}"]
        if alternative_names:
            parts.append(f"Also known as: {', '.join(alternative_names)}")
        return " | ".join(parts)

    async def store_embedding(
        self,
        entity_id: uuid.UUID,
        embedding: list[float],
        *,
        session: AsyncSession,
    ) -> None:
        """Store an embedding in the database, skipping if already exists.

        Performs an idempotent upsert: if an embedding already exists for
        this ``(entity_id, model_name)`` pair, the call is a no-op.

        Parameters
        ----------
        entity_id : uuid.UUID
            Entity UUID to associate the embedding with.
        embedding : list[float]
            Dense embedding vector to store.
        session : AsyncSession
            Active async database session. The caller is responsible
            for committing the transaction.
        """
        # Check if embedding already exists for this entity + model
        stmt = select(EntityEmbeddingModel).where(
            EntityEmbeddingModel.entity_id == entity_id,
            EntityEmbeddingModel.model_name == self._model_name,
        )
        result = await session.execute(stmt)
        if result.scalar_one_or_none() is not None:
            logger.debug("Embedding already exists for entity %s, skipping", entity_id)
            return

        model = EntityEmbeddingModel(
            entity_id=entity_id,
            model_name=self._model_name,
            model_version=MODEL_VERSION,
            embedding=embedding,
            created_at=datetime.now(UTC),
        )
        session.add(model)
