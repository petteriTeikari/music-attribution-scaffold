"""Tests for identifier-based exact matching."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest

from music_attribution.resolution.identifier_match import IdentifierMatcher
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    EntityTypeEnum,
    SourceEnum,
)
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
)
from music_attribution.schemas.resolved import ResolvedEntity


def _make_record(
    source: SourceEnum = SourceEnum.MUSICBRAINZ,
    source_id: str | None = None,
    name: str = "Test Track",
    isrc: str | None = "GBAYE0601690",
    mbid: str | None = "mb-123",
    isni: str | None = None,
    entity_type: EntityTypeEnum = EntityTypeEnum.RECORDING,
) -> NormalizedRecord:
    """Create a NormalizedRecord for testing."""
    return NormalizedRecord(
        source=source,
        source_id=source_id or str(uuid.uuid4()),
        entity_type=entity_type,
        canonical_name=name,
        identifiers=IdentifierBundle(isrc=isrc, mbid=mbid, isni=isni),
        fetch_timestamp=datetime.now(UTC),
        source_confidence=0.9,
    )


@pytest.fixture
def matcher() -> IdentifierMatcher:
    """Create an IdentifierMatcher."""
    return IdentifierMatcher()


class TestIdentifierMatcher:
    """Tests for identifier-based exact matching."""

    def test_exact_isrc_match_resolves(self, matcher) -> None:
        """Test that two records with the same ISRC are resolved together."""
        records = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", isrc="GBAYE0601690"),
            _make_record(source=SourceEnum.DISCOGS, source_id="dg-1", isrc="GBAYE0601690", mbid=None),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1
        assert isinstance(entities[0], ResolvedEntity)
        assert len(entities[0].source_records) == 2

    def test_exact_iswc_match_resolves(self, matcher) -> None:
        """Test that two records with the same ISWC are resolved together."""
        r1 = NormalizedRecord(
            source=SourceEnum.MUSICBRAINZ,
            source_id="mb-1",
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name="Test Work",
            identifiers=IdentifierBundle(iswc="T-010.434.007-7"),
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.9,
        )
        r2 = NormalizedRecord(
            source=SourceEnum.DISCOGS,
            source_id="dg-1",
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name="Test Work",
            identifiers=IdentifierBundle(iswc="T-010.434.007-7"),
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.9,
        )
        entities = matcher.match([r1, r2])
        assert len(entities) == 1

    def test_exact_isni_match_resolves(self, matcher) -> None:
        """Test that two records with the same ISNI are resolved together."""
        records = [
            _make_record(
                source=SourceEnum.MUSICBRAINZ,
                source_id="mb-1",
                entity_type=EntityTypeEnum.ARTIST,
                isni="0000000121707484",
                isrc=None,
            ),
            _make_record(
                source=SourceEnum.DISCOGS,
                source_id="dg-1",
                entity_type=EntityTypeEnum.ARTIST,
                isni="0000000121707484",
                isrc=None,
                mbid=None,
            ),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1

    def test_mbid_match_resolves(self, matcher) -> None:
        """Test that two records with the same MBID are resolved."""
        records = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", mbid="shared-mbid"),
            _make_record(source=SourceEnum.ACOUSTID, source_id="ac-1", mbid="shared-mbid", isrc=None),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1

    def test_no_shared_identifiers_returns_none(self, matcher) -> None:
        """Test that records with no shared identifiers produce separate entities."""
        records = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", isrc="ISRC1", mbid="mbid-1"),
            _make_record(source=SourceEnum.DISCOGS, source_id="dg-1", isrc="ISRC2", mbid=None),
        ]
        entities = matcher.match(records)
        assert len(entities) == 2

    def test_conflicting_other_fields_still_resolves_on_id_match(self, matcher) -> None:
        """Test that records with matching IDs but different names still resolve."""
        records = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", name="Come Together", isrc="GBAYE0601690"),
            _make_record(
                source=SourceEnum.DISCOGS,
                source_id="dg-1",
                name="Come Together (Remastered)",
                isrc="GBAYE0601690",
                mbid=None,
            ),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1
        # Should record the name conflict
        assert len(entities[0].conflicts) >= 1

    def test_assurance_level_A1_for_single_source_id_match(self, matcher) -> None:
        """Test A1 assurance for single-source ID match."""
        records = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", isrc="GBAYE0601690"),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1
        assert entities[0].assurance_level == AssuranceLevelEnum.LEVEL_1

    def test_assurance_level_A2_for_multi_source_cross_reference(self, matcher) -> None:
        """Test A2 assurance for same ID confirmed in multiple sources."""
        records = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", isrc="GBAYE0601690"),
            _make_record(source=SourceEnum.DISCOGS, source_id="dg-1", isrc="GBAYE0601690", mbid=None),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1
        assert entities[0].assurance_level == AssuranceLevelEnum.LEVEL_2

    def test_assurance_level_A3_for_identity_verified_isni(self, matcher) -> None:
        """Test A3 assurance for ISNI + cross-registry + no conflicts."""
        records = [
            _make_record(
                source=SourceEnum.MUSICBRAINZ,
                source_id="mb-1",
                entity_type=EntityTypeEnum.ARTIST,
                name="The Beatles",
                isni="0000000121707484",
                isrc=None,
            ),
            _make_record(
                source=SourceEnum.DISCOGS,
                source_id="dg-1",
                entity_type=EntityTypeEnum.ARTIST,
                name="The Beatles",
                isni="0000000121707484",
                isrc=None,
                mbid=None,
            ),
        ]
        entities = matcher.match(records)
        assert len(entities) == 1
        assert entities[0].assurance_level == AssuranceLevelEnum.LEVEL_3
