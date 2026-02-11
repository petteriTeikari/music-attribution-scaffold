"""Uncertainty-aware provenance schema models.

Based on academic grounding:
- UProp (Duan 2025, arXiv:2506.17419): intrinsic/extrinsic decomposition
- Liu (2025, arXiv:2503.15850): 4-dimensional uncertainty framework
- Yáñez (2025, Patterns): confidence-weighted source integration
- Tian (2025, arXiv:2508.06225): TH-Score overconfidence detection
- Tripathi (2025, arXiv:2506.23464): H-Score, ECI metrics
- Zhang (2026, arXiv:2601.15778): trajectory-level calibration (HTC)
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import (
    CalibrationStatusEnum,
    ConfidenceMethodEnum,
    ConfidenceTrendEnum,
    SourceEnum,
    UncertaintySourceEnum,
)


class StepUncertainty(BaseModel):
    """Per-step uncertainty decomposition (UProp, Duan 2025).

    Tracks intrinsic (data noise) and extrinsic (model/pipeline) uncertainty
    for each processing step, plus optional 4-D decomposition (Liu 2025).
    """

    step_id: str
    step_name: str
    step_index: int = Field(ge=0)

    stated_confidence: float = Field(ge=0.0, le=1.0)
    calibrated_confidence: float = Field(ge=0.0, le=1.0)

    intrinsic_uncertainty: float = Field(ge=0.0, le=1.0)
    extrinsic_uncertainty: float = Field(ge=0.0, le=1.0)
    total_uncertainty: float = Field(ge=0.0, le=1.0)

    # Optional 4-D decomposition (Liu 2025)
    input_uncertainty: float | None = Field(default=None, ge=0.0, le=1.0)
    reasoning_uncertainty: float | None = Field(default=None, ge=0.0, le=1.0)
    parameter_uncertainty: float | None = Field(default=None, ge=0.0, le=1.0)
    prediction_uncertainty: float | None = Field(default=None, ge=0.0, le=1.0)

    uncertainty_sources: list[UncertaintySourceEnum] = Field(default_factory=list)
    confidence_method: ConfidenceMethodEnum
    preceding_step_ids: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_total_ge_intrinsic(self) -> StepUncertainty:
        """total_uncertainty must be >= intrinsic_uncertainty."""
        if self.total_uncertainty < self.intrinsic_uncertainty:
            msg = "total_uncertainty must be >= intrinsic_uncertainty"
            raise ValueError(msg)
        return self


class SourceContribution(BaseModel):
    """Per-source confidence with calibration quality (Yáñez 2025).

    Tracks how much each data source contributed to the final attribution,
    with calibration quality indicating how reliable that source's
    confidence estimates are.
    """

    source: SourceEnum
    confidence: float = Field(ge=0.0, le=1.0)
    weight: float = Field(ge=0.0, le=1.0)
    calibration_quality: float = Field(ge=0.0, le=1.0)
    record_count: int = Field(default=0, ge=0)
    is_human: bool = False


class CalibrationMetadata(BaseModel):
    """Per-step calibration metrics (Tian 2025 TH-Score).

    Records calibration quality for confidence scores, including
    expected calibration error (ECE), calibration set size, and method.
    """

    expected_calibration_error: float = Field(ge=0.0)
    calibration_set_size: int = Field(ge=0)
    status: CalibrationStatusEnum
    method: str | None = None


class OverconfidenceReport(BaseModel):
    """Overconfidence detection (Tripathi 2025 H-Score, ECI).

    Detects when stated confidence exceeds actual accuracy.
    overconfidence_gap can be negative (underconfident).
    """

    stated_confidence: float = Field(ge=0.0, le=1.0)
    actual_accuracy: float = Field(ge=0.0, le=1.0)
    overconfidence_gap: float  # stated - actual, can be negative
    th_score: float | None = None
    h_score: float | None = None
    eci: float | None = None


class TrajectoryCalibration(BaseModel):
    """Trajectory-level calibration (Zhang 2026, HTC).

    Tracks confidence dynamics across pipeline steps, detecting
    patterns like monotonic increase, decrease, or volatility.
    """

    trajectory_id: str
    step_count: int = Field(ge=1)
    confidence_trend: ConfidenceTrendEnum
    initial_confidence: float = Field(ge=0.0, le=1.0)
    final_confidence: float = Field(ge=0.0, le=1.0)
    htc_feature_vector: list[float] | None = None

    @field_validator("htc_feature_vector")
    @classmethod
    def validate_htc_vector_length(cls, v: list[float] | None) -> list[float] | None:
        """HTC feature vector must be length 48 when provided."""
        if v is not None and len(v) != 48:
            msg = "htc_feature_vector must be length 48"
            raise ValueError(msg)
        return v


class UncertaintyAwareProvenance(BaseModel):
    """Top-level uncertainty summary for an AttributionRecord.

    Aggregates step-level uncertainties, source contributions, and
    calibration metadata into a single summary attached to each record.
    """

    steps: list[StepUncertainty] = Field(default_factory=list)
    source_contributions: list[SourceContribution] = Field(default_factory=list)
    calibration: CalibrationMetadata | None = None
    overconfidence: OverconfidenceReport | None = None
    trajectory: TrajectoryCalibration | None = None
    total_uncertainty: float = Field(default=0.0, ge=0.0, le=1.0)
    dominant_uncertainty_source: UncertaintySourceEnum | None = None
