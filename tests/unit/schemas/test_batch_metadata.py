"""Tests for batch metadata envelope and drift detection."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from music_attribution.quality.drift_detector import DriftDetector, DriftReport
from music_attribution.schemas.batch import BatchEnvelope, BatchMetadata, ConfidenceStats
from music_attribution.schemas.enums import SourceEnum


def _make_batch_metadata(
    count: int = 100,
    mean_conf: float = 0.85,
    std_conf: float = 0.1,
    coverage: float = 0.9,
    sources: dict[SourceEnum, int] | None = None,
) -> BatchMetadata:
    """Create a BatchMetadata for testing."""
    return BatchMetadata(
        batch_id=uuid.uuid4(),
        record_count=count,
        source_distribution=sources or {SourceEnum.MUSICBRAINZ: count},
        confidence_stats=ConfidenceStats(
            mean=mean_conf,
            std=std_conf,
            min_val=mean_conf - 2 * std_conf,
            max_val=min(mean_conf + 2 * std_conf, 1.0),
            median=mean_conf,
            count=count,
        ),
        identifier_coverage=coverage,
        created_at=datetime.now(UTC),
    )


class TestBatchMetadata:
    """Tests for batch metadata schemas."""

    def test_batch_metadata_computes_statistics(self) -> None:
        """Test that ConfidenceStats has mean/std/min/max/median."""
        meta = _make_batch_metadata(count=50, mean_conf=0.8, std_conf=0.15)
        assert meta.confidence_stats.mean == 0.8
        assert meta.confidence_stats.std == 0.15
        assert meta.confidence_stats.count == 50
        assert meta.record_count == 50
        assert meta.identifier_coverage == 0.9

    def test_batch_envelope_wraps_records(self) -> None:
        """Test that BatchEnvelope wraps records with metadata."""
        meta = _make_batch_metadata(count=3)
        records = ["record1", "record2", "record3"]
        envelope = BatchEnvelope(metadata=meta, records=records)
        assert len(envelope.records) == 3
        assert envelope.metadata.record_count == 3

    def test_batch_id_enables_downstream_tracing(self) -> None:
        """Test that batch_id is a valid UUID for tracing."""
        meta = _make_batch_metadata()
        assert isinstance(meta.batch_id, uuid.UUID)


class TestDriftDetector:
    """Tests for drift detection."""

    def test_drift_detection_flags_anomalous_batch(self) -> None:
        """Test that significant confidence shift is detected as drift."""
        baseline = _make_batch_metadata(mean_conf=0.85, std_conf=0.1)
        current = _make_batch_metadata(mean_conf=0.55, std_conf=0.2)  # Big drop
        detector = DriftDetector()
        report = detector.check(current, baseline)
        assert isinstance(report, DriftReport)
        assert report.is_drifted

    def test_no_drift_for_similar_batches(self) -> None:
        """Test that similar batches are not flagged as drift."""
        baseline = _make_batch_metadata(mean_conf=0.85, std_conf=0.1)
        current = _make_batch_metadata(mean_conf=0.84, std_conf=0.11)
        detector = DriftDetector()
        report = detector.check(current, baseline)
        assert not report.is_drifted

    def test_source_distribution_change_detected(self) -> None:
        """Test that changed source distribution is detected."""
        baseline = _make_batch_metadata(
            sources={SourceEnum.MUSICBRAINZ: 90, SourceEnum.DISCOGS: 10},
        )
        current = _make_batch_metadata(
            sources={SourceEnum.MUSICBRAINZ: 10, SourceEnum.DISCOGS: 90},
        )
        detector = DriftDetector()
        report = detector.check(current, baseline)
        assert report.source_distribution_changed

    def test_identifier_coverage_drift(self) -> None:
        """Test that identifier coverage change is tracked."""
        baseline = _make_batch_metadata(coverage=0.95)
        current = _make_batch_metadata(coverage=0.5)
        detector = DriftDetector()
        report = detector.check(current, baseline)
        assert abs(report.identifier_coverage_delta) > 0.3
