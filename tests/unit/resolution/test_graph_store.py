"""Tests for ResolvedEntity graph storage."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest

from music_attribution.resolution.graph_store import GraphStore
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    EntityTypeEnum,
    ResolutionMethodEnum,
    SourceEnum,
)
from music_attribution.schemas.normalized import IdentifierBundle
from music_attribution.schemas.resolved import (
    ResolutionDetails,
    ResolvedEntity,
    SourceReference,
)


def _make_resolved_entity(name: str, entity_type: EntityTypeEnum = EntityTypeEnum.ARTIST) -> ResolvedEntity:
    """Create a ResolvedEntity for testing."""
    return ResolvedEntity(
        entity_type=entity_type,
        canonical_name=name,
        identifiers=IdentifierBundle(mbid=str(uuid.uuid4())),
        source_records=[
            SourceReference(
                record_id=uuid.uuid4(),
                source=SourceEnum.MUSICBRAINZ,
                source_id=str(uuid.uuid4()),
                agreement_score=0.95,
            ),
        ],
        resolution_method=ResolutionMethodEnum.EXACT_ID,
        resolution_confidence=0.95,
        resolution_details=ResolutionDetails(matched_identifiers=["mbid:abc"]),
        assurance_level=AssuranceLevelEnum.LEVEL_2,
        resolved_at=datetime.now(UTC),
    )


@pytest.fixture
def store() -> GraphStore:
    """Create a GraphStore for testing."""
    return GraphStore()


class TestGraphStore:
    """Tests for ResolvedEntity graph storage."""

    async def test_store_and_retrieve_entity(self, store) -> None:
        """Test storing and retrieving a ResolvedEntity."""
        entity = _make_resolved_entity("The Beatles")
        await store.add_entity(entity)
        retrieved = await store.get_entity(entity.entity_id)
        assert retrieved is not None
        assert retrieved.canonical_name == "The Beatles"

    async def test_add_and_query_relationship(self, store) -> None:
        """Test adding relationships and querying related entities."""
        artist = _make_resolved_entity("The Beatles")
        recording = _make_resolved_entity("Hey Jude", EntityTypeEnum.RECORDING)
        await store.add_entity(artist)
        await store.add_entity(recording)
        await store.add_relationship(
            artist.entity_id,
            recording.entity_id,
            "PERFORMED",
            {"role": "performer"},
        )
        related = await store.find_related(artist.entity_id, "PERFORMED", depth=1)
        assert len(related) == 1
        assert related[0].canonical_name == "Hey Jude"

    async def test_find_related_artists_via_shared_recordings(self, store) -> None:
        """Test finding related artists through shared recordings."""
        artist_a = _make_resolved_entity("John Lennon")
        artist_b = _make_resolved_entity("Paul McCartney")
        recording = _make_resolved_entity("Come Together", EntityTypeEnum.RECORDING)

        await store.add_entity(artist_a)
        await store.add_entity(artist_b)
        await store.add_entity(recording)
        await store.add_relationship(artist_a.entity_id, recording.entity_id, "PERFORMED", {})
        await store.add_relationship(artist_b.entity_id, recording.entity_id, "PERFORMED", {})

        # Artist A's PERFORMED entities should include the recording
        related = await store.find_related(artist_a.entity_id, "PERFORMED", depth=1)
        assert len(related) == 1
        assert related[0].entity_id == recording.entity_id

    async def test_shortest_path(self, store) -> None:
        """Test finding shortest path between entities."""
        a = _make_resolved_entity("A")
        b = _make_resolved_entity("B")
        c = _make_resolved_entity("C")
        await store.add_entity(a)
        await store.add_entity(b)
        await store.add_entity(c)
        await store.add_relationship(a.entity_id, b.entity_id, "RELATED", {})
        await store.add_relationship(b.entity_id, c.entity_id, "RELATED", {})

        path = await store.shortest_path(a.entity_id, c.entity_id)
        assert len(path) == 3  # A -> B -> C
        assert path[0].entity_id == a.entity_id
        assert path[-1].entity_id == c.entity_id

    async def test_entity_not_found_returns_none(self, store) -> None:
        """Test that querying nonexistent entity returns None."""
        result = await store.get_entity(uuid.uuid4())
        assert result is None
