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
