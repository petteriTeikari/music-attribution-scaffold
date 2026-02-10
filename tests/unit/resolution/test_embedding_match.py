"""Tests for embedding-based semantic matching."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from music_attribution.resolution.embedding_match import EmbeddingMatcher


@pytest.fixture
def matcher() -> EmbeddingMatcher:
    """Create an EmbeddingMatcher with mocked model."""
    return EmbeddingMatcher(model_name="all-MiniLM-L6-v2")


class TestEmbeddingMatcher:
    """Tests for embedding-based semantic matching."""

    async def test_embed_entity_name(self, matcher) -> None:
        """Test that entity names are embedded to fixed-length vectors."""
        with patch.object(matcher, "_get_model") as mock_model:
            mock_model.return_value.encode.return_value = [[0.1] * 384]
            embedding = await matcher.embed("The Beatles")
            assert isinstance(embedding, list)
            assert len(embedding) == 384
            assert all(isinstance(v, float) for v in embedding)

    async def test_similar_entities_high_cosine_similarity(self, matcher) -> None:
        """Test that similar entity names have high cosine similarity."""
        # Mock model to return similar embeddings for similar names
        beatles_embed = [0.9, 0.1, 0.0] + [0.0] * 381
        beatles_alt = [0.85, 0.15, 0.0] + [0.0] * 381

        with patch.object(matcher, "_get_model") as mock_model:
            mock_model.return_value.encode.side_effect = [
                [beatles_embed],
                [beatles_alt],
            ]
            emb1 = await matcher.embed("The Beatles")
            emb2 = await matcher.embed("Beatles, The")
            score = matcher.cosine_similarity(emb1, emb2)
            assert score > 0.9

    async def test_different_entities_low_cosine_similarity(self, matcher) -> None:
        """Test that different entity names have low cosine similarity."""
        beatles_embed = [0.9, 0.1, 0.0] + [0.0] * 381
        mozart_embed = [0.0, 0.1, 0.9] + [0.0] * 381

        with patch.object(matcher, "_get_model") as mock_model:
            mock_model.return_value.encode.side_effect = [
                [beatles_embed],
                [mozart_embed],
            ]
            emb1 = await matcher.embed("The Beatles")
            emb2 = await matcher.embed("Wolfgang Amadeus Mozart")
            score = matcher.cosine_similarity(emb1, emb2)
            assert score < 0.5

    async def test_find_similar_returns_ranked_results(self, matcher) -> None:
        """Test that find_similar returns candidates ranked by similarity."""
        query_embed = [0.9, 0.1, 0.0] + [0.0] * 381

        # Mock stored embeddings with known similarities
        stored = {
            "id-1": [0.85, 0.15, 0.0] + [0.0] * 381,  # High similarity
            "id-2": [0.0, 0.1, 0.9] + [0.0] * 381,  # Low similarity
            "id-3": [0.7, 0.3, 0.0] + [0.0] * 381,  # Medium similarity
        }
        matcher._embeddings = stored

        results = await matcher.find_similar(query_embed, top_k=2)
        assert len(results) == 2
        # Results should be sorted by similarity descending
        assert results[0][1] >= results[1][1]
        # Top result should be id-1 (most similar)
        assert results[0][0] == "id-1"

    async def test_batch_embedding_performance(self, matcher) -> None:
        """Test that batch embedding works for multiple texts."""
        texts = [f"Artist {i}" for i in range(10)]

        with patch.object(matcher, "_get_model") as mock_model:
            mock_model.return_value.encode.return_value = [[0.1] * 384 for _ in range(10)]
            embeddings = await matcher.embed_batch(texts)
            assert len(embeddings) == 10
            assert all(len(e) == 384 for e in embeddings)
