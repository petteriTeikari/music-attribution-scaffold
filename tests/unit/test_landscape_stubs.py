"""Tests for commercial landscape stub schemas (Task B3).

Validates TrainingInfluence, TemporalSegment, StemInfluence, and
ComplianceAttestation Pydantic models can be instantiated and validate correctly.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from music_attribution.schemas.compliance import ComplianceAttestation
from music_attribution.schemas.enums import (
    AttributionMethodEnum,
    CertificationTypeEnum,
    MediaTypeEnum,
)
from music_attribution.schemas.training_attribution import (
    StemInfluence,
    TemporalSegment,
    TrainingInfluence,
)


class TestTrainingInfluence:
    """Tests for TrainingInfluence model (Task B3)."""

    def test_training_influence_model_creates(self) -> None:
        """Verify TrainingInfluence can be instantiated with valid data."""
        obj = TrainingInfluence(
            source_work_id="isrc:GBAYE0601498",
            target_model_id="model-001",
            method=AttributionMethodEnum.INFLUENCE_FUNCTIONS,
            influence_percentage=12.5,
            confidence=0.87,
        )
        assert obj.source_work_id == "isrc:GBAYE0601498"
        assert obj.influence_percentage == 12.5
        assert obj.confidence == 0.87

    def test_training_influence_validates_percentage(self) -> None:
        """Verify influence_percentage must be 0-100."""
        with pytest.raises(Exception):  # noqa: B017
            TrainingInfluence(
                source_work_id="isrc:GBAYE0601498",
                target_model_id="model-001",
                method=AttributionMethodEnum.EMBEDDING_SIMILARITY,
                influence_percentage=150.0,
                confidence=0.5,
            )

    def test_training_influence_validates_confidence(self) -> None:
        """Verify confidence must be 0-1."""
        with pytest.raises(Exception):  # noqa: B017
            TrainingInfluence(
                source_work_id="isrc:GBAYE0601498",
                target_model_id="model-001",
                method=AttributionMethodEnum.WATERMARK_DETECTION,
                influence_percentage=10.0,
                confidence=1.5,
            )


class TestTemporalSegment:
    """Tests for TemporalSegment model (Task B3)."""

    def test_temporal_segment_model_creates(self) -> None:
        """Verify TemporalSegment can be instantiated."""
        obj = TemporalSegment(
            start_seconds=30.0,
            end_seconds=45.5,
            influence_weight=0.75,
        )
        assert obj.start_seconds == 30.0
        assert obj.end_seconds == 45.5
        assert obj.influence_weight == 0.75


class TestStemInfluence:
    """Tests for StemInfluence model (Task B3)."""

    def test_stem_influence_model_creates(self) -> None:
        """Verify StemInfluence can be instantiated."""
        obj = StemInfluence(
            stem_type="vocals",
            media_type=MediaTypeEnum.AUDIO,
            influence_weight=0.6,
        )
        assert obj.stem_type == "vocals"
        assert obj.media_type == MediaTypeEnum.AUDIO


class TestComplianceAttestation:
    """Tests for ComplianceAttestation model (Task B3)."""

    def test_compliance_attestation_model_creates(self) -> None:
        """Verify ComplianceAttestation can be instantiated with valid data."""
        obj = ComplianceAttestation(
            certification_type=CertificationTypeEnum.FAIRLY_TRAINED_LICENSED,
            issuer="Fairly Trained Inc.",
            issued_at=datetime(2026, 1, 15, tzinfo=UTC),
            valid_until=datetime(2027, 1, 15, tzinfo=UTC),
            scope="Full catalog",
        )
        assert obj.certification_type == CertificationTypeEnum.FAIRLY_TRAINED_LICENSED
        assert obj.issuer == "Fairly Trained Inc."
