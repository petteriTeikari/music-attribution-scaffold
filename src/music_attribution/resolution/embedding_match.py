"""Embedding-based semantic matching for entity resolution.

Uses sentence-transformers to embed entity names/metadata and finds
semantically similar entities via cosine similarity. Handles cases
string matching misses: translations, very different spellings.
"""

from __future__ import annotations

import logging
import math
from typing import Any

logger = logging.getLogger(__name__)


class EmbeddingMatcher:
    """Semantic entity matching using sentence-transformer embeddings.

    Embeds entity names into dense vectors and finds similar entities
    via cosine similarity. Supports in-memory storage and pgvector.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        self._model_name = model_name
        self._model: Any = None
        self._embeddings: dict[str, list[float]] = {}

    def _get_model(self) -> Any:
        """Lazy-load the sentence-transformer model."""
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer

                self._model = SentenceTransformer(self._model_name)
            except ImportError:
                logger.warning("sentence-transformers not available")
                raise
        return self._model

    async def embed(self, text: str) -> list[float]:
        """Embed a single text string.

        Args:
            text: Text to embed (entity name, metadata, etc.).

        Returns:
            List of floats representing the embedding vector.
        """
        model = self._get_model()
        result = model.encode([text])
        return [float(v) for v in result[0]]

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple texts in a batch.

        Args:
            texts: List of texts to embed.

        Returns:
            List of embedding vectors.
        """
        model = self._get_model()
        results = model.encode(texts)
        return [[float(v) for v in row] for row in results]

    async def store_embedding(self, entity_id: str, embedding: list[float]) -> None:
        """Store an embedding for later similarity search.

        Args:
            entity_id: Unique identifier for the entity.
            embedding: Embedding vector to store.
        """
        self._embeddings[entity_id] = embedding

    async def find_similar(
        self, query_embedding: list[float], top_k: int = 5,
    ) -> list[tuple[str, float]]:
        """Find the most similar stored embeddings.

        Args:
            query_embedding: The query embedding vector.
            top_k: Number of top results to return.

        Returns:
            List of (entity_id, similarity_score) tuples, sorted descending.
        """
        scored: list[tuple[str, float]] = []
        for entity_id, stored_embedding in self._embeddings.items():
            score = self.cosine_similarity(query_embedding, stored_embedding)
            scored.append((entity_id, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    @staticmethod
    def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
        """Compute cosine similarity between two vectors.

        Args:
            vec_a: First vector.
            vec_b: Second vector.

        Returns:
            Cosine similarity score between -1 and 1.
        """
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b, strict=True))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)
