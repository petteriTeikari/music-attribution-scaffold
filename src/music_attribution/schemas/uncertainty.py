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

from pydantic import BaseModel, Field, model_validator

from music_attribution.schemas.enums import (
    ConfidenceMethodEnum,
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
