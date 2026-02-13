"""Uncertainty-aware provenance schema models.

Provides decomposed uncertainty tracking for every step of the attribution
pipeline. These models are attached to ``ProvenanceEvent`` and
``AttributionRecord`` objects, enabling transparent communication of *why*
a confidence score is what it is, not just *what* it is.

Academic grounding:

* **UProp** (Duan 2025, arXiv:2506.17419) -- intrinsic/extrinsic
  decomposition of uncertainty propagation across pipeline steps.
* **Liu** (2025, arXiv:2503.15850) -- 4-dimensional uncertainty framework
  (input, reasoning, parameter, prediction).
* **Yanez** (2025, Patterns) -- confidence-weighted source integration
  for multi-source fusion.
* **Tian** (2025, arXiv:2508.06225) -- TH-Score for overconfidence
  detection in LLM-based systems.
* **Tripathi** (2025, arXiv:2506.23464) -- H-Score and Expected
  Calibration Improvement (ECI) metrics.
* **Zhang** (2026, arXiv:2601.15778) -- trajectory-level Holistic
  Trajectory Calibration (HTC).

See Also
--------
music_attribution.schemas.attribution : Uses these models in provenance.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 5 (uncertainty framework).
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

    Tracks intrinsic (data noise) and extrinsic (model/pipeline)
    uncertainty for each processing step in the attribution pipeline,
    plus an optional 4-dimensional decomposition (Liu 2025). This
    enables fine-grained analysis of where uncertainty enters and
    accumulates.

    The ``total_uncertainty`` must be >= ``intrinsic_uncertainty``
    (validated at runtime), since total includes both intrinsic and
    extrinsic components.

    Attributes
    ----------
    step_id : str
        Unique identifier for this pipeline step (e.g.,
        ``"etl-musicbrainz"``, ``"resolution-fuzzy"``).
    step_name : str
        Human-readable name of the pipeline step (e.g.,
        ``"MusicBrainz ETL"``, ``"Fuzzy String Resolution"``).
    step_index : int
        Zero-based position of this step in the pipeline sequence.
    stated_confidence : float
        Raw confidence before calibration, range [0.0, 1.0].
    calibrated_confidence : float
        Confidence after post-hoc calibration, range [0.0, 1.0].
        May differ significantly from ``stated_confidence`` if the
        step exhibits systematic over- or under-confidence.
    intrinsic_uncertainty : float
        Uncertainty from the input data itself (noise, conflicts,
        missing fields), range [0.0, 1.0].
    extrinsic_uncertainty : float
        Uncertainty from the model/algorithm (embedding limitations,
        threshold sensitivity), range [0.0, 1.0].
    total_uncertainty : float
        Combined uncertainty, range [0.0, 1.0]. Must be >=
        ``intrinsic_uncertainty``.
    input_uncertainty : float or None
        4-D decomposition: input dimension (Liu 2025), range
        [0.0, 1.0]. None if 4-D decomposition not computed.
    reasoning_uncertainty : float or None
        4-D decomposition: reasoning dimension, range [0.0, 1.0].
    parameter_uncertainty : float or None
        4-D decomposition: parameter dimension, range [0.0, 1.0].
    prediction_uncertainty : float or None
        4-D decomposition: prediction dimension, range [0.0, 1.0].
    uncertainty_sources : list of UncertaintySourceEnum
        Classification of uncertainty sources active in this step
        (INTRINSIC, EXTRINSIC, ALEATORIC, EPISTEMIC).
    confidence_method : ConfidenceMethodEnum
        Method used to produce the confidence estimate for this step.
    preceding_step_ids : list of str
        IDs of pipeline steps that feed into this step. Used for
        UProp uncertainty propagation tracking.

    Examples
    --------
    >>> step = StepUncertainty(
    ...     step_id="etl-musicbrainz",
    ...     step_name="MusicBrainz ETL",
    ...     step_index=0,
    ...     stated_confidence=0.87,
    ...     calibrated_confidence=0.82,
    ...     intrinsic_uncertainty=0.10,
    ...     extrinsic_uncertainty=0.05,
    ...     total_uncertainty=0.15,
    ...     confidence_method=ConfidenceMethodEnum.SELF_REPORT,
    ... )
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
    """Per-source confidence with calibration quality (Yanez 2025).

    Tracks how much each data source contributed to the final attribution,
    with calibration quality indicating how reliable that source's
    confidence estimates historically are. Sources with higher
    ``calibration_quality`` receive higher weights in the aggregation.

    Attributes
    ----------
    source : SourceEnum
        The data source (e.g., MUSICBRAINZ, DISCOGS, ARTIST_INPUT).
    confidence : float
        This source's confidence in its contribution, range [0.0, 1.0].
    weight : float
        Normalised weight of this source in the final aggregation,
        range [0.0, 1.0]. Weights across all sources sum to 1.0.
    calibration_quality : float
        Historical calibration quality of this source's confidence
        estimates, range [0.0, 1.0]. 1.0 = perfectly calibrated
        (stated confidence matches empirical accuracy).
    record_count : int
        Number of records this source contributed to the attribution.
        Non-negative.
    is_human : bool
        Whether this source is human-provided (e.g., ARTIST_INPUT).
        Human sources may receive preferential weighting for subjective
        fields.

    Examples
    --------
    >>> contrib = SourceContribution(
    ...     source=SourceEnum.MUSICBRAINZ,
    ...     confidence=0.90,
    ...     weight=0.45,
    ...     calibration_quality=0.85,
    ...     record_count=3,
    ... )
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
    expected calibration error (ECE), calibration set size, and the
    method used. Lower ECE indicates better calibration (stated
    confidence matches empirical accuracy).

    Attributes
    ----------
    expected_calibration_error : float
        Expected Calibration Error (ECE), the average absolute
        difference between confidence and accuracy across bins.
        Non-negative. Lower is better; 0.0 = perfectly calibrated.
    calibration_set_size : int
        Number of examples used for calibration. Larger sets give
        more reliable ECE estimates. Non-negative.
    status : CalibrationStatusEnum
        Current calibration status (CALIBRATED, UNCALIBRATED, PENDING).
    method : str or None
        Name of the calibration method used (e.g., ``"platt_scaling"``,
        ``"isotonic_regression"``, ``"temperature_scaling"``). None
        if uncalibrated.

    Examples
    --------
    >>> cal = CalibrationMetadata(
    ...     expected_calibration_error=0.03,
    ...     calibration_set_size=500,
    ...     status=CalibrationStatusEnum.CALIBRATED,
    ...     method="platt_scaling",
    ... )
    """

    expected_calibration_error: float = Field(ge=0.0)
    calibration_set_size: int = Field(ge=0)
    status: CalibrationStatusEnum
    method: str | None = None


class OverconfidenceReport(BaseModel):
    """Overconfidence detection report (Tripathi 2025 H-Score, ECI).

    Detects when stated confidence exceeds actual accuracy, a common
    failure mode in LLM-based systems. The ``overconfidence_gap`` is
    the primary diagnostic: positive = overconfident, negative =
    underconfident, zero = perfectly calibrated.

    Attributes
    ----------
    stated_confidence : float
        The system's stated confidence, range [0.0, 1.0].
    actual_accuracy : float
        Empirically measured accuracy on a validation set,
        range [0.0, 1.0].
    overconfidence_gap : float
        ``stated_confidence - actual_accuracy``. Positive values
        indicate overconfidence; negative values indicate
        underconfidence. Can range from -1.0 to 1.0.
    th_score : float or None
        TH-Score from Tian (2025). Measures hallucination tendency.
        None if not computed.
    h_score : float or None
        H-Score from Tripathi (2025). Measures honesty of confidence
        estimates. None if not computed.
    eci : float or None
        Expected Calibration Improvement (ECI) from Tripathi (2025).
        How much calibration could be improved. None if not computed.

    Examples
    --------
    >>> report = OverconfidenceReport(
    ...     stated_confidence=0.92,
    ...     actual_accuracy=0.85,
    ...     overconfidence_gap=0.07,
    ...     th_score=0.12,
    ... )
    """

    stated_confidence: float = Field(ge=0.0, le=1.0)
    actual_accuracy: float = Field(ge=0.0, le=1.0)
    overconfidence_gap: float  # stated - actual, can be negative
    th_score: float | None = None
    h_score: float | None = None
    eci: float | None = None


class TrajectoryCalibration(BaseModel):
    """Trajectory-level calibration (Zhang 2026, HTC).

    Tracks confidence dynamics across the full pipeline, treating the
    sequence of confidence scores at each step as a *trajectory*. The
    trajectory shape (increasing, decreasing, stable, volatile) is a
    powerful signal for calibration: volatile trajectories often indicate
    unreliable final confidence.

    The optional ``htc_feature_vector`` is a 48-dimensional feature vector
    extracted from the trajectory for use with the HTC calibration method.

    Attributes
    ----------
    trajectory_id : str
        Unique identifier for this trajectory (typically matches the
        attribution record ID).
    step_count : int
        Number of pipeline steps in the trajectory. Minimum 1.
    confidence_trend : ConfidenceTrendEnum
        Classified trend of confidence across steps (INCREASING,
        DECREASING, STABLE, VOLATILE).
    initial_confidence : float
        Confidence at the first pipeline step, range [0.0, 1.0].
    final_confidence : float
        Confidence at the last pipeline step, range [0.0, 1.0].
    htc_feature_vector : list of float or None
        48-dimensional feature vector for HTC calibration (Zhang 2026).
        Must be exactly length 48 when provided. None if HTC is not
        used.

    Examples
    --------
    >>> traj = TrajectoryCalibration(
    ...     trajectory_id="attr-12345",
    ...     step_count=4,
    ...     confidence_trend=ConfidenceTrendEnum.INCREASING,
    ...     initial_confidence=0.65,
    ...     final_confidence=0.92,
    ... )
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

    Aggregates step-level uncertainties, source contributions,
    calibration metadata, overconfidence diagnostics, and trajectory
    calibration into a single summary. Attached to each
    ``AttributionRecord`` as ``uncertainty_summary``.

    This is the primary structure for answering "why is the confidence
    what it is?" -- enabling transparent uncertainty communication to
    end users and downstream systems.

    Attributes
    ----------
    steps : list of StepUncertainty
        Per-step uncertainty decomposition for each pipeline step.
        Ordered by ``step_index``.
    source_contributions : list of SourceContribution
        Per-source confidence and weight breakdown. Shows how much
        each data source influenced the final score.
    calibration : CalibrationMetadata or None
        Overall calibration metrics for the record's confidence score.
        None if calibration has not been performed.
    overconfidence : OverconfidenceReport or None
        Overconfidence diagnostic report. None if not computed.
    trajectory : TrajectoryCalibration or None
        Trajectory-level calibration data (HTC). None if trajectory
        analysis was not performed.
    total_uncertainty : float
        Aggregated total uncertainty across all steps, range [0.0, 1.0].
        Defaults to 0.0.
    dominant_uncertainty_source : UncertaintySourceEnum or None
        The primary source of uncertainty in this record (INTRINSIC,
        EXTRINSIC, ALEATORIC, or EPISTEMIC). None if not determined.

    Examples
    --------
    >>> summary = UncertaintyAwareProvenance(
    ...     total_uncertainty=0.18,
    ...     dominant_uncertainty_source=UncertaintySourceEnum.EPISTEMIC,
    ... )

    See Also
    --------
    AttributionRecord : Parent record containing this summary.
    StepUncertainty : Per-step decomposition detail.
    """

    steps: list[StepUncertainty] = Field(default_factory=list)
    source_contributions: list[SourceContribution] = Field(default_factory=list)
    calibration: CalibrationMetadata | None = None
    overconfidence: OverconfidenceReport | None = None
    trajectory: TrajectoryCalibration | None = None
    total_uncertainty: float = Field(default=0.0, ge=0.0, le=1.0)
    dominant_uncertainty_source: UncertaintySourceEnum | None = None
