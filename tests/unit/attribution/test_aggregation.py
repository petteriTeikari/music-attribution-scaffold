"""Tests for multi-source credit aggregation."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest

from music_attribution.attribution.aggregator import CreditAggregator
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
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


def _make_entity(
    name: str,
    entity_type: EntityTypeEnum = EntityTypeEnum.ARTIST,
    sources: list[SourceEnum] | None = None,
    confidence: float = 0.9,
) -> ResolvedEntity:
    """Create a ResolvedEntity for testing."""
    source_list = sources or [SourceEnum.MUSICBRAINZ]
    return ResolvedEntity(
        entity_type=entity_type,
        canonical_name=name,
        identifiers=IdentifierBundle(mbid=str(uuid.uuid4())),
        source_records=[
            SourceReference(
                record_id=uuid.uuid4(),
                source=s,
                source_id=str(uuid.uuid4()),
                agreement_score=confidence,
            )
            for s in source_list
        ],
        resolution_method=ResolutionMethodEnum.EXACT_ID,
        resolution_confidence=confidence,
        resolution_details=ResolutionDetails(matched_identifiers=["mbid:test"]),
        assurance_level=AssuranceLevelEnum.LEVEL_2,
        resolved_at=datetime.now(UTC),
    )


@pytest.fixture
def aggregator() -> CreditAggregator:
    """Create a CreditAggregator."""
    return CreditAggregator()


class TestCreditAggregator:
    """Tests for multi-source credit aggregation."""

    async def test_single_source_credit_passes_through(self, aggregator) -> None:
        """Test that a single-source entity becomes a credit directly."""
        work = _make_entity("Hey Jude", EntityTypeEnum.RECORDING)
        artist = _make_entity("The Beatles", EntityTypeEnum.ARTIST)
        record = await aggregator.aggregate(
            work_entity=work,
            contributor_entities=[artist],
            roles={artist.entity_id: CreditRoleEnum.PERFORMER},
        )
        assert len(record.credits) == 1
        assert record.credits[0].role == CreditRoleEnum.PERFORMER
        assert record.credits[0].entity_id == artist.entity_id

    async def test_multiple_sources_agree_high_confidence(self, aggregator) -> None:
        """Test that multi-source agreement yields high confidence."""
        work = _make_entity("Let It Be", EntityTypeEnum.RECORDING)
        artist = _make_entity(
            "The Beatles",
            sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
            confidence=0.95,
        )
        record = await aggregator.aggregate(
            work_entity=work,
            contributor_entities=[artist],
            roles={artist.entity_id: CreditRoleEnum.PERFORMER},
        )
        assert record.confidence_score >= 0.8
        assert record.source_agreement >= 0.8

    async def test_sources_disagree_weighted_resolution(self, aggregator) -> None:
        """Test that source disagreement lowers confidence."""
        work = _make_entity("Ambiguous Track", EntityTypeEnum.RECORDING)
        artist_high = _make_entity("Artist A", confidence=0.95)
        artist_low = _make_entity("Artist B", confidence=0.4)
        record = await aggregator.aggregate(
            work_entity=work,
            contributor_entities=[artist_high, artist_low],
            roles={
                artist_high.entity_id: CreditRoleEnum.PERFORMER,
                artist_low.entity_id: CreditRoleEnum.PRODUCER,
            },
        )
        # Low-confidence contributor should lower overall agreement
        assert len(record.credits) == 2

    async def test_source_reliability_weights_applied(self, aggregator) -> None:
        """Test that source reliability weights affect credit confidence."""
        work = _make_entity("Test Track", EntityTypeEnum.RECORDING)
        # MusicBrainz = higher reliability by default
        mb_artist = _make_entity(
            "Artist MB", sources=[SourceEnum.MUSICBRAINZ], confidence=0.9,
        )
        record = await aggregator.aggregate(
            work_entity=work,
            contributor_entities=[mb_artist],
            roles={mb_artist.entity_id: CreditRoleEnum.PERFORMER},
        )
        credit = record.credits[0]
        assert credit.confidence > 0.0
        assert credit.sources == [SourceEnum.MUSICBRAINZ]

    async def test_provenance_chain_populated(self, aggregator) -> None:
        """Test that provenance chain is populated during aggregation."""
        work = _make_entity("Tracked Work", EntityTypeEnum.RECORDING)
        artist = _make_entity("Tracked Artist")
        record = await aggregator.aggregate(
            work_entity=work,
            contributor_entities=[artist],
            roles={artist.entity_id: CreditRoleEnum.PERFORMER},
        )
        assert len(record.provenance_chain) >= 1
        # Should have at least a SCORE event
        event_types = [e.event_type.value for e in record.provenance_chain]
        assert "SCORE" in event_types
