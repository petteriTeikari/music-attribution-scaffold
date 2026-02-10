"""Tests for data quality gate (Pandera validation)."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest

from music_attribution.etl.quality_gate import DataQualityGate, QualityReport
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
)


def _make_record(
    source: SourceEnum = SourceEnum.MUSICBRAINZ,
    source_id: str | None = None,
    entity_type: EntityTypeEnum = EntityTypeEnum.RECORDING,
    name: str = "Test Track",
    isrc: str | None = "USRC12345678",
    mbid: str | None = "test-mbid-123",
) -> NormalizedRecord:
    """Helper to create a NormalizedRecord for testing."""
    return NormalizedRecord(
        source=source,
        source_id=source_id or str(uuid.uuid4()),
        entity_type=entity_type,
        canonical_name=name,
        identifiers=IdentifierBundle(isrc=isrc, mbid=mbid),
        fetch_timestamp=datetime.now(UTC),
        source_confidence=0.9,
    )


@pytest.fixture
def gate() -> DataQualityGate:
    """Create a DataQualityGate with default config."""
    return DataQualityGate()


@pytest.fixture
def good_batch() -> list[NormalizedRecord]:
    """Create a batch of records that passes quality checks."""
    return [
        _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-1", name="Track A"),
        _make_record(source=SourceEnum.DISCOGS, source_id="dg-1", name="Track B", mbid=None, isrc="USRC12345679"),
        _make_record(source=SourceEnum.MUSICBRAINZ, source_id="mb-2", name="Track C"),
        _make_record(source=SourceEnum.FILE_METADATA, source_id="fm-1", name="Track D", mbid=None, isrc="USRC12345680"),
    ]


class TestDataQualityGate:
    """Tests for data quality gate."""

    def test_rejects_batch_with_zero_identifiers(self, gate) -> None:
        """Test that a batch where no record has any identifier is rejected."""
        bad_batch = [
            NormalizedRecord(
                source=SourceEnum.FILE_METADATA,
                source_id=str(uuid.uuid4()),
                entity_type=EntityTypeEnum.ARTIST,
                canonical_name=f"Artist {i}",
                identifiers=IdentifierBundle(),
                fetch_timestamp=datetime.now(UTC),
                source_confidence=0.5,
            )
            for i in range(5)
        ]
        report = gate.validate_batch(bad_batch)
        assert isinstance(report, QualityReport)
        id_check = [c for c in report.checks if c.check_name == "identifier_coverage"]
        assert len(id_check) == 1
        assert id_check[0].status == "fail"

    def test_warns_on_low_identifier_coverage(self, gate) -> None:
        """Test that a batch with low identifier coverage gets a warning."""
        # 4 records, only 1 with identifiers (use FILE_METADATA source which allows empty ids)
        batch = [
            _make_record(source_id="r1", isrc="USRC12345678"),
            _make_record(source=SourceEnum.FILE_METADATA, source_id="r2", isrc=None, mbid=None),
            _make_record(source=SourceEnum.FILE_METADATA, source_id="r3", isrc=None, mbid=None),
            _make_record(source=SourceEnum.FILE_METADATA, source_id="r4", isrc=None, mbid=None),
        ]
        for r in batch[1:]:
            r.entity_type = EntityTypeEnum.ARTIST
        report = gate.validate_batch(batch)
        id_check = [c for c in report.checks if c.check_name == "identifier_coverage"]
        assert len(id_check) == 1
        assert id_check[0].status in ("warn", "fail")

    def test_rejects_duplicate_source_ids(self, gate) -> None:
        """Test that duplicate source+source_id combinations are detected."""
        batch = [
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="same-id"),
            _make_record(source=SourceEnum.MUSICBRAINZ, source_id="same-id"),
        ]
        report = gate.validate_batch(batch)
        dup_check = [c for c in report.checks if c.check_name == "no_duplicates"]
        assert len(dup_check) == 1
        assert dup_check[0].status == "fail"

    def test_validates_source_distribution(self, gate, good_batch) -> None:
        """Test that source distribution check works."""
        report = gate.validate_batch(good_batch)
        dist_check = [c for c in report.checks if c.check_name == "source_distribution"]
        assert len(dist_check) == 1
        # With 3 different sources, should pass
        assert dist_check[0].status == "pass"

    def test_generates_quality_report(self, gate, good_batch) -> None:
        """Test that a full quality report is generated."""
        report = gate.validate_batch(good_batch)
        assert isinstance(report, QualityReport)
        assert report.records_in == 4
        assert report.records_passed >= 0
        assert report.overall_status in ("pass", "warn", "fail")
        assert len(report.checks) >= 3  # At least 3 check types
        assert report.batch_id is not None
        assert report.timestamp is not None
