"""Embedding-based semantic matching for entity resolution.

Stage 3 of the resolution cascade. Uses sentence-transformers to embed
entity names and metadata into dense vectors and finds semantically similar
entities via cosine similarity. Handles cases that string matching misses:

- Translations (``"Die Fledermaus"`` ~ ``"The Bat"``)
- Very different spellings of the same name
- Contextual metadata similarity (genre, collaborators)

The default model (``all-MiniLM-L6-v2``) produces 384-dimensional embeddings
suitable for fast cosine similarity search. In production, embeddings are
stored in PostgreSQL via pgvector ``halfvec(768)`` for efficient approximate
nearest-neighbor queries.

Notes
-----
This module implements the semantic similarity layer described in
Teikari (2026), Section 4.3. It fires only for records that were not
resolved by identifier matching (Stage 1) or string similarity (Stage 2).

See Also
--------
music_attribution.resolution.string_similarity : Stage 2 (runs before this).
music_attribution.resolution.embedding_service : Persistence layer for pgvector.
music_attribution.resolution.splink_linkage : Stage 4 (probabilistic linkage).
"""

from __future__ import annotations

import logging
import math
from typing import Any

logger = logging.getLogger(__name__)


class EmbeddingMatcher:
    """Semantic entity matching using sentence-transformer embeddings.

    Embeds entity names into dense vectors and finds similar entities
    via cosine similarity. Supports in-memory storage for development
    and pgvector for production deployments.

    The model is lazy-loaded on first use to avoid heavy import-time
    dependencies when the embedding stage is not needed.

    Parameters
    ----------
    model_name : str, optional
        Sentence-transformer model to use. Default is ``"all-MiniLM-L6-v2"``,
        a lightweight model with good quality-speed tradeoff.

    Attributes
    ----------
    _model_name : str
        Name of the sentence-transformer model.
    _model : Any
        Lazy-loaded ``SentenceTransformer`` instance.
    _embeddings : dict[str, list[float]]
        In-memory embedding store (entity_id -> vector).

    See Also
    --------
    music_attribution.resolution.embedding_service : Production persistence via pgvector.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        self._model_name = model_name
        self._model: Any = None
        self._embeddings: dict[str, list[float]] = {}

    def _get_model(self) -> Any:
        """Lazy-load the sentence-transformer model.

        Defers the expensive ``sentence_transformers`` import and model
        download until the first call. Subsequent calls return the cached
        instance.

        Returns
        -------
        SentenceTransformer
            The loaded sentence-transformer model.

        Raises
        ------
        ImportError
            If ``sentence-transformers`` is not installed.
        """
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer

                self._model = SentenceTransformer(self._model_name)
            except ImportError:
                logger.warning("sentence-transformers not available")
                raise
        return self._model

    async def embed(self, text: str) -> list[float]:
        """Embed a single text string into a dense vector.

        Parameters
        ----------
        text : str
            Text to embed (entity name, metadata string, etc.).

        Returns
        -------
        list[float]
            Embedding vector. Dimensionality depends on the model
            (384 for ``all-MiniLM-L6-v2``).
        """
        model = self._get_model()
        result = model.encode([text])
        return [float(v) for v in result[0]]

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple texts in a single batch for efficiency.

        Batch encoding is significantly faster than calling ``embed()``
        in a loop because the model can parallelize across inputs.

        Parameters
        ----------
        texts : list[str]
            List of texts to embed.

        Returns
        -------
        list[list[float]]
            List of embedding vectors, one per input text.
        """
        model = self._get_model()
        results = model.encode(texts)
        return [[float(v) for v in row] for row in results]

    async def store_embedding(self, entity_id: str, embedding: list[float]) -> None:
        """Store an embedding in the in-memory index for later similarity search.

        In production, use ``EmbeddingService.store_embedding()`` for
        pgvector-backed persistence instead.

        Parameters
        ----------
        entity_id : str
            Unique identifier for the entity.
        embedding : list[float]
            Embedding vector to store.
        """
        self._embeddings[entity_id] = embedding

    async def find_similar(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ) -> list[tuple[str, float]]:
        """Find the most similar stored embeddings via brute-force cosine search.

        Performs exhaustive comparison against all stored embeddings. For
        production-scale deployments, use pgvector's approximate nearest
        neighbor index instead.

        Parameters
        ----------
        query_embedding : list[float]
            The query embedding vector.
        top_k : int, optional
            Number of top results to return. Default is 5.

        Returns
        -------
        list[tuple[str, float]]
            Top-k results as ``(entity_id, cosine_similarity)`` tuples,
            sorted by similarity descending.
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

        Defined as ``dot(a, b) / (||a|| * ||b||)``. Returns 0.0 if
        either vector has zero magnitude.

        Parameters
        ----------
        vec_a : list[float]
            First vector.
        vec_b : list[float]
            Second vector (must have same dimensionality as ``vec_a``).

        Returns
        -------
        float
            Cosine similarity in range [-1.0, 1.0]. For normalized
            sentence-transformer outputs, values are typically in [0, 1].

        Raises
        ------
        ValueError
            If vectors have different lengths (via ``zip(..., strict=True)``).
        """
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b, strict=True))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)
