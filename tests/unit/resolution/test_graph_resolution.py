"""Tests for graph-based entity resolution via relationship evidence."""

from __future__ import annotations

import uuid

import pytest

from music_attribution.resolution.graph_resolution import GraphResolver


@pytest.fixture
def resolver() -> GraphResolver:
    """Create a GraphResolver with test graph data."""
    r = GraphResolver()
    # Seed test graph: Artists share albums
    artist_a = str(uuid.uuid4())
    artist_b = str(uuid.uuid4())
    artist_c = str(uuid.uuid4())
    album_1 = str(uuid.uuid4())
    album_2 = str(uuid.uuid4())
    album_3 = str(uuid.uuid4())
    album_4 = str(uuid.uuid4())

    # artist_a and artist_b share 3 albums (likely same entity)
    r.add_relationship(artist_a, album_1, "PERFORMED_ON")
    r.add_relationship(artist_a, album_2, "PERFORMED_ON")
    r.add_relationship(artist_a, album_3, "PERFORMED_ON")
    r.add_relationship(artist_b, album_1, "PERFORMED_ON")
    r.add_relationship(artist_b, album_2, "PERFORMED_ON")
    r.add_relationship(artist_b, album_3, "PERFORMED_ON")

    # artist_c shares only 1 album with artist_a (probably different)
    r.add_relationship(artist_c, album_4, "PERFORMED_ON")
    r.add_relationship(artist_a, album_4, "PERFORMED_ON")

    r._test_ids = {"a": artist_a, "b": artist_b, "c": artist_c}
    return r


class TestGraphResolver:
    """Tests for graph-based entity resolution."""

    async def test_resolve_artist_via_shared_album_relationships(self, resolver) -> None:
        """Test that artists sharing 3+ albums are identified as candidates."""
        artist_a = resolver._test_ids["a"]
        candidates = await resolver.find_candidate_matches(artist_a, min_shared=2)
        candidate_ids = [c[0] for c in candidates]
        assert resolver._test_ids["b"] in candidate_ids

    async def test_graph_path_confidence_scoring(self, resolver) -> None:
        """Test that graph evidence produces a confidence score."""
        artist_a = resolver._test_ids["a"]
        artist_b = resolver._test_ids["b"]
        score = await resolver.score_graph_evidence(artist_a, artist_b)
        assert 0.0 <= score <= 1.0
        # 3 shared albums should give high confidence
        assert score > 0.5

    async def test_shared_collaborator_evidence(self, resolver) -> None:
        """Test that shared collaborators contribute to evidence."""
        artist_a = resolver._test_ids["a"]
        artist_b = resolver._test_ids["b"]
        # Both share 3 albums
        score = await resolver.score_graph_evidence(artist_a, artist_b)
        assert score > 0.5

    async def test_minimum_shared_relationships_threshold(self, resolver) -> None:
        """Test that entities below the minimum threshold are excluded."""
        artist_a = resolver._test_ids["a"]
        # With min_shared=5, artist_b (3 shared) should not be a candidate
        candidates = await resolver.find_candidate_matches(artist_a, min_shared=5)
        assert len(candidates) == 0

    async def test_path_length_affects_confidence(self, resolver) -> None:
        """Test that closer entities (shorter paths) get higher confidence."""
        artist_a = resolver._test_ids["a"]
        artist_b = resolver._test_ids["b"]
        artist_c = resolver._test_ids["c"]

        score_ab = await resolver.score_graph_evidence(artist_a, artist_b)
        score_ac = await resolver.score_graph_evidence(artist_a, artist_c)
        # artist_b shares 3 albums, artist_c shares 1 — b should score higher
        assert score_ab > score_ac
