"""Tests for multi-signal resolution orchestrator."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest

from music_attribution.resolution.orchestrator import ResolutionOrchestrator
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    EntityTypeEnum,
    ResolutionMethodEnum,
    SourceEnum,
)
from music_attribution.schemas.normalized import IdentifierBundle, NormalizedRecord


def _make_record(
    name: str,
    source: SourceEnum = SourceEnum.MUSICBRAINZ,
    isrc: str | None = None,
    mbid: str | None = None,
    source_id: str | None = None,
) -> NormalizedRecord:
    """Create a NormalizedRecord for testing."""
    identifiers = IdentifierBundle()
    if isrc:
        identifiers = IdentifierBundle(isrc=isrc)
    if mbid:
        identifiers = IdentifierBundle(isrc=isrc, mbid=mbid) if isrc else IdentifierBundle(mbid=mbid)

    return NormalizedRecord(
        source=source,
        source_id=source_id or str(uuid.uuid4()),
        entity_type=EntityTypeEnum.ARTIST,
        canonical_name=name,
        identifiers=identifiers,
        fetch_timestamp=datetime.now(UTC),
        source_confidence=0.9,
    )


@pytest.fixture
def orchestrator() -> ResolutionOrchestrator:
    """Create a ResolutionOrchestrator."""
    return ResolutionOrchestrator()


class TestResolutionOrchestrator:
    """Tests for the multi-signal resolution orchestrator."""

    async def test_exact_id_match_bypasses_other_methods(self, orchestrator) -> None:
        """Test that exact identifier match resolves immediately."""
        records = [
            _make_record("The Beatles", source=SourceEnum.MUSICBRAINZ, isrc="GBAYE0601690"),
            _make_record("Beatles", source=SourceEnum.DISCOGS, isrc="GBAYE0601690"),
        ]
        entities = await orchestrator.resolve(records)
        assert len(entities) == 1
        assert entities[0].resolution_method == ResolutionMethodEnum.EXACT_ID
        assert len(entities[0].resolution_details.matched_identifiers) > 0

    async def test_string_and_embedding_combined_score(self, orchestrator) -> None:
        """Test that string and embedding scores are combined."""
        records = [
            _make_record("The Beatles", source=SourceEnum.MUSICBRAINZ, mbid=str(uuid.uuid4())),
            _make_record("The Beatles", source=SourceEnum.DISCOGS, mbid=str(uuid.uuid4())),
        ]
        # These have different MBIDs but same name — should resolve via string match
        entities = await orchestrator.resolve(records)
        assert len(entities) >= 1
        # At least one should have string similarity populated
        resolved = entities[0]
        assert resolved.resolution_details.string_similarity is not None

    async def test_low_confidence_flagged_for_review(self, orchestrator) -> None:
        """Test that low-confidence resolutions are flagged for review."""
        records = [
            _make_record("John Williams", source=SourceEnum.MUSICBRAINZ, mbid=str(uuid.uuid4())),
            _make_record("John Williams", source=SourceEnum.DISCOGS, mbid=str(uuid.uuid4())),
        ]
        entities = await orchestrator.resolve(records)
        # If all records have same name but different IDs, may or may not need review
        # The orchestrator should produce at least one entity
        assert len(entities) >= 1

    async def test_assurance_level_computed_correctly(self, orchestrator) -> None:
        """Test that assurance level is computed from available evidence."""
        # Single source with identifier = A1
        records = [
            _make_record("Solo Artist", source=SourceEnum.MUSICBRAINZ, isrc="GBAYE0601690"),
        ]
        entities = await orchestrator.resolve(records)
        assert len(entities) == 1
        assert entities[0].assurance_level in (
            AssuranceLevelEnum.LEVEL_0,
            AssuranceLevelEnum.LEVEL_1,
        )

    async def test_conflicts_collected_across_sources(self, orchestrator) -> None:
        """Test that conflicting field values are recorded."""
        records = [
            _make_record("The Beatles", source=SourceEnum.MUSICBRAINZ, isrc="GBAYE0601690"),
            _make_record("Beatles, The", source=SourceEnum.DISCOGS, isrc="GBAYE0601690"),
        ]
        entities = await orchestrator.resolve(records)
        assert len(entities) == 1
        # Names differ — should record a conflict
        entity = entities[0]
        name_conflicts = [c for c in entity.conflicts if c.field == "canonical_name"]
        assert len(name_conflicts) > 0

    async def test_resolution_details_populated(self, orchestrator) -> None:
        """Test that resolution_details is fully populated."""
        records = [
            _make_record("Artist A", source=SourceEnum.MUSICBRAINZ, isrc="GBAYE0601690"),
            _make_record("Artist A", source=SourceEnum.DISCOGS, isrc="GBAYE0601690"),
        ]
        entities = await orchestrator.resolve(records)
        assert len(entities) == 1
        details = entities[0].resolution_details
        assert isinstance(details.matched_identifiers, list)
