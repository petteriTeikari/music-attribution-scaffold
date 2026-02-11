"""Tests for uncertainty-aware provenance schema models.

Tasks 1.0–1.2 from end-to-end-mvp-plan.xml.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError


class TestUncertaintyEnums:
    """Tests for uncertainty-related enums (Task 1.0)."""

    def test_uncertainty_source_enum_values(self) -> None:
        """UncertaintySourceEnum has expected string values."""
        from music_attribution.schemas.enums import UncertaintySourceEnum

        assert UncertaintySourceEnum.INTRINSIC == "INTRINSIC"
        assert UncertaintySourceEnum.EXTRINSIC == "EXTRINSIC"
        assert UncertaintySourceEnum.ALEATORIC == "ALEATORIC"
        assert UncertaintySourceEnum.EPISTEMIC == "EPISTEMIC"

    def test_uncertainty_dimension_enum_values(self) -> None:
        """UncertaintyDimensionEnum has 4 dimensions from Liu (2025)."""
        from music_attribution.schemas.enums import UncertaintyDimensionEnum

        assert UncertaintyDimensionEnum.INPUT == "INPUT"
        assert UncertaintyDimensionEnum.REASONING == "REASONING"
        assert UncertaintyDimensionEnum.PARAMETER == "PARAMETER"
        assert UncertaintyDimensionEnum.PREDICTION == "PREDICTION"

    def test_confidence_method_enum_completeness(self) -> None:
        """ConfidenceMethodEnum has all 8 expected methods."""
        from music_attribution.schemas.enums import ConfidenceMethodEnum

        expected = {
            "SELF_REPORT",
            "MULTI_SAMPLE",
            "LOGPROB",
            "ENSEMBLE",
            "CONFORMAL",
            "SOURCE_WEIGHTED",
            "HUMAN_RATED",
            "HTC",
        }
        actual = {m.value for m in ConfidenceMethodEnum}
        assert actual == expected

    def test_calibration_status_enum_values(self) -> None:
        """CalibrationStatusEnum has expected values."""
        from music_attribution.schemas.enums import CalibrationStatusEnum

        assert CalibrationStatusEnum.CALIBRATED == "CALIBRATED"
        assert CalibrationStatusEnum.UNCALIBRATED == "UNCALIBRATED"
        assert CalibrationStatusEnum.PENDING == "PENDING"

    def test_confidence_trend_enum_values(self) -> None:
        """ConfidenceTrendEnum has 4 trend types."""
        from music_attribution.schemas.enums import ConfidenceTrendEnum

        expected = {"INCREASING", "DECREASING", "STABLE", "VOLATILE"}
        actual = {m.value for m in ConfidenceTrendEnum}
        assert actual == expected


class TestStepUncertainty:
    """Tests for StepUncertainty Pydantic model (Task 1.0)."""

    def test_step_uncertainty_valid_construction(self) -> None:
        """StepUncertainty accepts valid fields and validates constraints."""
        from music_attribution.schemas.uncertainty import StepUncertainty

        su = StepUncertainty(
            step_id="etl-musicbrainz",
            step_name="MusicBrainz ETL",
            step_index=0,
            stated_confidence=0.85,
            calibrated_confidence=0.82,
            intrinsic_uncertainty=0.05,
            extrinsic_uncertainty=0.08,
            total_uncertainty=0.13,
            confidence_method="SOURCE_WEIGHTED",
        )
        assert su.step_id == "etl-musicbrainz"
        assert su.step_index == 0
        assert su.total_uncertainty == pytest.approx(0.13)

    def test_step_uncertainty_confidence_range(self) -> None:
        """stated_confidence and calibrated_confidence constrained to [0, 1]."""
        from music_attribution.schemas.uncertainty import StepUncertainty

        with pytest.raises(ValidationError):
            StepUncertainty(
                step_id="test",
                step_name="test",
                step_index=0,
                stated_confidence=1.5,  # invalid
                calibrated_confidence=0.8,
                intrinsic_uncertainty=0.05,
                extrinsic_uncertainty=0.1,
                total_uncertainty=0.15,
                confidence_method="SELF_REPORT",
            )

        with pytest.raises(ValidationError):
            StepUncertainty(
                step_id="test",
                step_name="test",
                step_index=0,
                stated_confidence=0.8,
                calibrated_confidence=-0.1,  # invalid
                intrinsic_uncertainty=0.05,
                extrinsic_uncertainty=0.1,
                total_uncertainty=0.15,
                confidence_method="SELF_REPORT",
            )

    def test_total_uncertainty_consistency(self) -> None:
        """total_uncertainty >= intrinsic_uncertainty (by definition)."""
        from music_attribution.schemas.uncertainty import StepUncertainty

        with pytest.raises(ValidationError):
            StepUncertainty(
                step_id="test",
                step_name="test",
                step_index=0,
                stated_confidence=0.8,
                calibrated_confidence=0.75,
                intrinsic_uncertainty=0.20,
                extrinsic_uncertainty=0.05,
                total_uncertainty=0.15,  # < intrinsic, invalid
                confidence_method="SELF_REPORT",
            )

    def test_step_uncertainty_json_roundtrip(self) -> None:
        """model_dump_json() → model_validate_json() preserves all fields."""
        from music_attribution.schemas.uncertainty import StepUncertainty

        original = StepUncertainty(
            step_id="resolution-embedding",
            step_name="Embedding Resolution",
            step_index=2,
            stated_confidence=0.90,
            calibrated_confidence=0.87,
            intrinsic_uncertainty=0.03,
            extrinsic_uncertainty=0.07,
            total_uncertainty=0.10,
            confidence_method="ENSEMBLE",
            preceding_step_ids=["etl-musicbrainz", "etl-discogs"],
        )
        json_str = original.model_dump_json()
        restored = StepUncertainty.model_validate_json(json_str)
        assert restored == original
        assert restored.preceding_step_ids == ["etl-musicbrainz", "etl-discogs"]

    def test_step_uncertainty_optional_dimensions(self) -> None:
        """Optional 4-D uncertainty fields (Liu 2025) default to None."""
        from music_attribution.schemas.uncertainty import StepUncertainty

        su = StepUncertainty(
            step_id="test",
            step_name="test",
            step_index=0,
            stated_confidence=0.8,
            calibrated_confidence=0.75,
            intrinsic_uncertainty=0.1,
            extrinsic_uncertainty=0.1,
            total_uncertainty=0.2,
            confidence_method="SELF_REPORT",
        )
        assert su.input_uncertainty is None
        assert su.reasoning_uncertainty is None
        assert su.parameter_uncertainty is None
        assert su.prediction_uncertainty is None


class TestSourceContribution:
    """Tests for SourceContribution model (Task 1.1)."""

    def test_source_contribution_valid(self) -> None:
        """SourceContribution accepts source name, confidence, calibration quality."""
        from music_attribution.schemas.uncertainty import SourceContribution

        sc = SourceContribution(
            source="MUSICBRAINZ",
            confidence=0.92,
            weight=0.35,
            calibration_quality=0.88,
            record_count=15,
        )
        assert sc.source == "MUSICBRAINZ"
        assert sc.weight == pytest.approx(0.35)

    def test_source_contribution_human_flag(self) -> None:
        """is_human=True for human reviewers, False for machine sources."""
        from music_attribution.schemas.uncertainty import SourceContribution

        machine = SourceContribution(
            source="MUSICBRAINZ",
            confidence=0.9,
            weight=0.3,
            calibration_quality=0.85,
            is_human=False,
        )
        assert machine.is_human is False

        human = SourceContribution(
            source="ARTIST_INPUT",
            confidence=0.95,
            weight=0.4,
            calibration_quality=0.90,
            is_human=True,
        )
        assert human.is_human is True

    def test_source_contribution_json_roundtrip(self) -> None:
        """JSON round-trip preserves all fields."""
        from music_attribution.schemas.uncertainty import SourceContribution

        original = SourceContribution(
            source="DISCOGS",
            confidence=0.78,
            weight=0.25,
            calibration_quality=0.70,
            record_count=8,
            is_human=False,
        )
        json_str = original.model_dump_json()
        restored = SourceContribution.model_validate_json(json_str)
        assert restored == original


class TestCalibrationMetadata:
    """Tests for CalibrationMetadata model (Task 1.1)."""

    def test_calibration_metadata_ece_range(self) -> None:
        """ECE is non-negative float."""
        from music_attribution.schemas.uncertainty import CalibrationMetadata

        cm = CalibrationMetadata(
            expected_calibration_error=0.05,
            calibration_set_size=100,
            status="CALIBRATED",
        )
        assert cm.expected_calibration_error >= 0.0

        with pytest.raises(ValidationError):
            CalibrationMetadata(
                expected_calibration_error=-0.01,
                calibration_set_size=100,
                status="CALIBRATED",
            )

    def test_calibration_metadata_json_roundtrip(self) -> None:
        """JSON round-trip preserves all fields."""
        from music_attribution.schemas.uncertainty import CalibrationMetadata

        original = CalibrationMetadata(
            expected_calibration_error=0.03,
            calibration_set_size=250,
            status="CALIBRATED",
            method="temperature_scaling",
        )
        json_str = original.model_dump_json()
        restored = CalibrationMetadata.model_validate_json(json_str)
        assert restored == original


class TestOverconfidenceReport:
    """Tests for OverconfidenceReport model (Task 1.1)."""

    def test_overconfidence_report_gap_calculation(self) -> None:
        """overconfidence_gap = stated - actual (can be negative)."""
        from music_attribution.schemas.uncertainty import OverconfidenceReport

        report = OverconfidenceReport(
            stated_confidence=0.95,
            actual_accuracy=0.80,
            overconfidence_gap=0.15,
            th_score=0.12,
        )
        assert report.overconfidence_gap == pytest.approx(0.15)

        # Underconfident case
        under = OverconfidenceReport(
            stated_confidence=0.70,
            actual_accuracy=0.85,
            overconfidence_gap=-0.15,
        )
        assert under.overconfidence_gap < 0

    def test_overconfidence_report_optional_scores(self) -> None:
        """TH-Score, H-Score, ECI are optional."""
        from music_attribution.schemas.uncertainty import OverconfidenceReport

        report = OverconfidenceReport(
            stated_confidence=0.90,
            actual_accuracy=0.85,
            overconfidence_gap=0.05,
        )
        assert report.th_score is None
        assert report.h_score is None
        assert report.eci is None


class TestTrajectoryCalibration:
    """Tests for TrajectoryCalibration model (Task 1.1)."""

    def test_trajectory_calibration_trend_enum(self) -> None:
        """ConfidenceTrendEnum: INCREASING, DECREASING, STABLE, VOLATILE."""
        from music_attribution.schemas.uncertainty import TrajectoryCalibration

        tc = TrajectoryCalibration(
            trajectory_id="pipeline-run-001",
            step_count=4,
            confidence_trend="INCREASING",
            initial_confidence=0.60,
            final_confidence=0.92,
        )
        assert tc.confidence_trend == "INCREASING"

    def test_trajectory_calibration_htc_vector(self) -> None:
        """htc_feature_vector is optional list[float] of length 48 when provided."""
        from music_attribution.schemas.uncertainty import TrajectoryCalibration

        tc = TrajectoryCalibration(
            trajectory_id="pipeline-run-002",
            step_count=3,
            confidence_trend="STABLE",
            initial_confidence=0.85,
            final_confidence=0.87,
            htc_feature_vector=[0.1] * 48,
        )
        assert len(tc.htc_feature_vector) == 48

        with pytest.raises(ValidationError):
            TrajectoryCalibration(
                trajectory_id="test",
                step_count=2,
                confidence_trend="STABLE",
                initial_confidence=0.8,
                final_confidence=0.8,
                htc_feature_vector=[0.1] * 10,  # Wrong length
            )

    def test_trajectory_calibration_json_roundtrip(self) -> None:
        """JSON round-trip preserves all fields."""
        from music_attribution.schemas.uncertainty import TrajectoryCalibration

        original = TrajectoryCalibration(
            trajectory_id="pipeline-run-003",
            step_count=5,
            confidence_trend="DECREASING",
            initial_confidence=0.95,
            final_confidence=0.72,
        )
        json_str = original.model_dump_json()
        restored = TrajectoryCalibration.model_validate_json(json_str)
        assert restored == original


class TestProvenanceEventExtension:
    """Tests for ProvenanceEvent uncertainty extension (Task 1.2)."""

    def test_provenance_event_backward_compatible(self) -> None:
        """Existing ProvenanceEvent without uncertainty fields still validates."""
        from datetime import UTC, datetime

        from music_attribution.schemas.attribution import ProvenanceEvent

        event = ProvenanceEvent(
            event_type="FETCH",
            timestamp=datetime.now(UTC),
            agent="etl-musicbrainz",
            details={
                "type": "fetch",
                "source": "MUSICBRAINZ",
                "source_id": "abc-123",
                "records_fetched": 5,
            },
        )
        assert event.step_uncertainty is None
        assert event.citation_index is None

    def test_provenance_event_with_step_uncertainty(self) -> None:
        """ProvenanceEvent with step_uncertainty field validates."""
        from datetime import UTC, datetime

        from music_attribution.schemas.attribution import ProvenanceEvent
        from music_attribution.schemas.uncertainty import StepUncertainty

        su = StepUncertainty(
            step_id="etl-musicbrainz",
            step_name="MusicBrainz ETL",
            step_index=0,
            stated_confidence=0.85,
            calibrated_confidence=0.82,
            intrinsic_uncertainty=0.05,
            extrinsic_uncertainty=0.08,
            total_uncertainty=0.13,
            confidence_method="SOURCE_WEIGHTED",
        )
        event = ProvenanceEvent(
            event_type="FETCH",
            timestamp=datetime.now(UTC),
            agent="etl-musicbrainz",
            details={
                "type": "fetch",
                "source": "MUSICBRAINZ",
                "source_id": "abc-123",
                "records_fetched": 5,
            },
            step_uncertainty=su,
        )
        assert event.step_uncertainty is not None
        assert event.step_uncertainty.step_id == "etl-musicbrainz"

    def test_provenance_event_citation_index(self) -> None:
        """citation_index is optional positive int."""
        from datetime import UTC, datetime

        from music_attribution.schemas.attribution import ProvenanceEvent

        event = ProvenanceEvent(
            event_type="FETCH",
            timestamp=datetime.now(UTC),
            agent="etl-musicbrainz",
            details={
                "type": "fetch",
                "source": "MUSICBRAINZ",
                "source_id": "abc-123",
                "records_fetched": 5,
            },
            citation_index=1,
        )
        assert event.citation_index == 1

    def test_attribution_record_uncertainty_provenance(self) -> None:
        """AttributionRecord accepts optional uncertainty_summary field."""
        import uuid
        from datetime import UTC, datetime

        from music_attribution.schemas.attribution import (
            AttributionRecord,
            ConformalSet,
            Credit,
        )
        from music_attribution.schemas.uncertainty import (
            UncertaintyAwareProvenance,
        )

        record = AttributionRecord(
            work_entity_id=uuid.uuid4(),
            credits=[
                Credit(
                    entity_id=uuid.uuid4(),
                    role="PERFORMER",
                    confidence=0.9,
                    sources=["MUSICBRAINZ"],
                    assurance_level="LEVEL_2",
                ),
            ],
            assurance_level="LEVEL_2",
            confidence_score=0.9,
            conformal_set=ConformalSet(
                coverage_level=0.95,
                marginal_coverage=0.94,
                calibration_error=0.01,
                calibration_method="lac",
                calibration_set_size=100,
            ),
            source_agreement=0.85,
            needs_review=False,
            review_priority=0.1,
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
            version=1,
            uncertainty_summary=UncertaintyAwareProvenance(
                total_uncertainty=0.10,
            ),
        )
        assert record.uncertainty_summary is not None
        assert record.uncertainty_summary.total_uncertainty == pytest.approx(0.10)

    def test_existing_mock_data_still_valid(self) -> None:
        """Imogen Heap mock data validates against updated schema."""
        from music_attribution.seed.imogen_heap import _build_works

        records = _build_works()
        assert len(records) == 8
        for rec in records:
            # All existing records valid — uncertainty_summary is optional
            assert rec.attribution_id is not None
