"""Embedding generation and persistence service.

Generates sentence-transformer embeddings and stores them in the
entity_embeddings table via pgvector halfvec(768). Builds on the
existing EmbeddingMatcher for model loading and encoding.
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

    Uses sentence-transformers (all-MiniLM-L6-v2) to generate 768-dim
    embeddings and stores them in PostgreSQL via pgvector halfvec.
    """

    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self._matcher = EmbeddingMatcher(model_name=model_name)
        self._model_name = model_name

    def generate_embedding(self, text: str) -> list[float]:
        """Generate a 768-dimensional embedding for text.

        Args:
            text: Input text to embed.

        Returns:
            768-element list of floats.
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

        Args:
            canonical_name: Primary entity name.
            entity_type: Entity type (e.g., ARTIST, WORK).
            alternative_names: Optional list of alternative names.

        Returns:
            Formatted text string.
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

        Args:
            entity_id: Entity UUID.
            embedding: 768-dimensional embedding vector.
            session: Active async database session.
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
