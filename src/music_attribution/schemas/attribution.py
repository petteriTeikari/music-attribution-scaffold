"""AttributionRecord boundary object schema (BO-3).

Output of the Attribution Engine pipeline. A complete attribution record
for a musical work/recording with calibrated confidence scores, conformal
prediction sets, and a full provenance chain.

The ``AttributionRecord`` is the third boundary object in the five-pipeline
architecture and the primary output consumed by the API/MCP Server and
Chat Interface pipelines. It carries the complete audit trail of how an
attribution was constructed, enabling transparent confidence communication
to end users.

See Also
--------
music_attribution.schemas.resolved : The preceding boundary object.
music_attribution.schemas.feedback : Reverse-flow feedback from users.
music_attribution.schemas.uncertainty : Uncertainty decomposition models.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    sections 5-6.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    ProvenanceEventTypeEnum,
    SourceEnum,
)
from music_attribution.schemas.uncertainty import (
    StepUncertainty,
    UncertaintyAwareProvenance,
)


class Credit(BaseModel):
    """Attribution credit for a single entity-role pair.

    Represents one line item in the attribution: a specific entity
    (artist, producer, etc.) credited in a specific role on a musical
    work or recording. Each credit carries its own confidence score
    and assurance level, independent of the overall record.

    Attributes
    ----------
    entity_id : uuid.UUID
        UUID of the ``ResolvedEntity`` receiving this credit.
    entity_name : str
        Display name of the credited entity. Defaults to empty string;
        populated for API/UI convenience.
    role : CreditRoleEnum
        The role in which the entity is credited (e.g., PERFORMER,
        SONGWRITER, PRODUCER).
    role_detail : str or None
        Additional role detail not captured by the enum (e.g.,
        ``"lead vocals"``, ``"bass guitar"``).
    confidence : float
        Confidence in this specific credit assignment, range [0.0, 1.0].
        May differ from the overall record confidence.
    sources : list of SourceEnum
        Data sources that corroborate this credit. More sources
        generally yield higher confidence.
    assurance_level : AssuranceLevelEnum
        A0-A3 assurance level for this specific credit.

    Examples
    --------
    >>> credit = Credit(
    ...     entity_id=uuid.uuid4(),
    ...     entity_name="Imogen Heap",
    ...     role=CreditRoleEnum.PERFORMER,
    ...     role_detail="lead vocals, keyboards",
    ...     confidence=0.95,
    ...     sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
    ...     assurance_level=AssuranceLevelEnum.LEVEL_2,
    ... )
    """

    entity_id: uuid.UUID
    entity_name: str = ""
    role: CreditRoleEnum
    role_detail: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    sources: list[SourceEnum] = Field(default_factory=list)
    assurance_level: AssuranceLevelEnum


class ConformalSet(BaseModel):
    """Conformal prediction set at a specified coverage level.

    Instead of a single point prediction for each credit role, conformal
    prediction produces a *set* of plausible roles that contains the true
    role with a guaranteed probability (the coverage level). Smaller sets
    indicate higher confidence. See Teikari (2026), section 5.

    Attributes
    ----------
    coverage_level : float
        Target coverage probability, range (0.0, 1.0) exclusive.
        Typical values: 0.90 (90% coverage) or 0.95 (95% coverage).
    prediction_sets : dict of str to list of CreditRoleEnum
        Mapping of entity ID (as string) to the set of plausible roles
        for that entity. Smaller sets = more certain attribution.
    set_sizes : dict of str to int
        Mapping of entity ID to the cardinality of their prediction set.
        A set size of 1 means the role is unambiguous at the given
        coverage level.
    marginal_coverage : float
        Observed marginal coverage on the calibration set, range
        [0.0, 1.0]. Should be close to ``coverage_level`` if well
        calibrated.
    calibration_error : float
        Absolute difference between ``coverage_level`` and
        ``marginal_coverage``. Lower is better. Non-negative.
    calibration_method : str
        Name of the calibration method used (e.g., ``"split_conformal"``,
        ``"jackknife_plus"``).
    calibration_set_size : int
        Number of examples in the calibration set. Larger sets give
        tighter coverage guarantees. Non-negative.

    Examples
    --------
    >>> conformal = ConformalSet(
    ...     coverage_level=0.90,
    ...     prediction_sets={"entity-uuid": [CreditRoleEnum.PERFORMER]},
    ...     set_sizes={"entity-uuid": 1},
    ...     marginal_coverage=0.91,
    ...     calibration_error=0.01,
    ...     calibration_method="split_conformal",
    ...     calibration_set_size=500,
    ... )
    """

    coverage_level: float = Field(gt=0.0, lt=1.0)
    prediction_sets: dict[str, list[CreditRoleEnum]] = Field(default_factory=dict)
    set_sizes: dict[str, int] = Field(default_factory=dict)
    marginal_coverage: float = Field(ge=0.0, le=1.0)
    calibration_error: float = Field(ge=0.0)
    calibration_method: str
    calibration_set_size: int = Field(ge=0)


# Provenance event detail types (discriminated union)


class FetchEventDetails(BaseModel):
    """Details for FETCH provenance events.

    Records metadata about a data fetch operation from an external source
    as part of the provenance chain.

    Attributes
    ----------
    type : Literal["fetch"]
        Discriminator field for the ``EventDetails`` union. Always
        ``"fetch"``.
    source : SourceEnum
        The data source that was queried.
    source_id : str
        Source-specific query identifier or endpoint.
    records_fetched : int
        Number of records returned by the fetch. Non-negative.
    rate_limited : bool
        Whether the fetch was rate-limited by the source API.
    """

    type: Literal["fetch"] = "fetch"
    source: SourceEnum
    source_id: str
    records_fetched: int = Field(ge=0)
    rate_limited: bool = False


class ResolveEventDetails(BaseModel):
    """Details for RESOLVE provenance events.

    Records metadata about an entity resolution step, including the
    method used and the reduction ratio (input records to output entities).

    Attributes
    ----------
    type : Literal["resolve"]
        Discriminator field. Always ``"resolve"``.
    method : str
        Name of the resolution method or algorithm used.
    records_input : int
        Number of ``NormalizedRecord`` instances fed into resolution.
        Non-negative.
    entities_output : int
        Number of ``ResolvedEntity`` instances produced. Non-negative.
        Should be <= ``records_input``.
    confidence_range : tuple of (float, float)
        (min, max) confidence range across all output entities.
        Defaults to ``(0.0, 1.0)``.
    """

    type: Literal["resolve"] = "resolve"
    method: str
    records_input: int = Field(ge=0)
    entities_output: int = Field(ge=0)
    confidence_range: tuple[float, float] = (0.0, 1.0)


class ScoreEventDetails(BaseModel):
    """Details for SCORE provenance events.

    Records a confidence scoring or recalibration step, showing how
    the confidence value changed.

    Attributes
    ----------
    type : Literal["score"]
        Discriminator field. Always ``"score"``.
    previous_confidence : float or None
        Confidence before this scoring step, range [0.0, 1.0]. None
        for the initial scoring event.
    new_confidence : float
        Confidence after this scoring step, range [0.0, 1.0].
    scoring_method : str
        Name of the scoring/calibration method applied (e.g.,
        ``"source_weighted_average"``, ``"platt_scaling"``).
    """

    type: Literal["score"] = "score"
    previous_confidence: float | None = None
    new_confidence: float = Field(ge=0.0, le=1.0)
    scoring_method: str


class ReviewEventDetails(BaseModel):
    """Details for REVIEW provenance events.

    Records that a human reviewer examined the attribution and
    optionally applied corrections from a ``FeedbackCard``.

    Attributes
    ----------
    type : Literal["review"]
        Discriminator field. Always ``"review"``.
    reviewer_id : str
        Identifier of the reviewer who performed the review.
    feedback_card_id : uuid.UUID
        UUID of the ``FeedbackCard`` that was applied.
    corrections_applied : int
        Number of field corrections accepted from the feedback card.
        Non-negative. Zero means the reviewer confirmed the record
        without changes.
    """

    type: Literal["review"] = "review"
    reviewer_id: str
    feedback_card_id: uuid.UUID
    corrections_applied: int = Field(ge=0)


class UpdateEventDetails(BaseModel):
    """Details for UPDATE provenance events.

    Records a version bump on the attribution record, including which
    fields changed and what triggered the update.

    Attributes
    ----------
    type : Literal["update"]
        Discriminator field. Always ``"update"``.
    previous_version : int
        Version number before this update. Minimum 1.
    new_version : int
        Version number after this update. Minimum 1. Should be
        ``previous_version + 1``.
    fields_changed : list of str
        Names of fields that were modified in this update.
    trigger : str
        What triggered the update (e.g., ``"feedback_accepted"``,
        ``"source_refresh"``, ``"conflict_resolved"``).
    """

    type: Literal["update"] = "update"
    previous_version: int = Field(ge=1)
    new_version: int = Field(ge=1)
    fields_changed: list[str] = Field(default_factory=list)
    trigger: str


class FeedbackEventDetails(BaseModel):
    """Details for FEEDBACK provenance events.

    Records that a ``FeedbackCard`` was processed by the Attribution
    Engine and its corrections were either accepted or rejected.

    Attributes
    ----------
    type : Literal["feedback"]
        Discriminator field. Always ``"feedback"``.
    feedback_card_id : uuid.UUID
        UUID of the ``FeedbackCard`` that was processed.
    overall_assessment : float
        The reviewer's overall assessment score from the feedback card,
        range [0.0, 1.0].
    corrections_count : int
        Number of corrections in the feedback card. Non-negative.
    accepted : bool
        Whether the feedback was accepted and applied to the
        attribution record.
    """

    type: Literal["feedback"] = "feedback"
    feedback_card_id: uuid.UUID
    overall_assessment: float = Field(ge=0.0, le=1.0)
    corrections_count: int = Field(ge=0)
    accepted: bool


EventDetails = Annotated[
    FetchEventDetails
    | ResolveEventDetails
    | ScoreEventDetails
    | ReviewEventDetails
    | UpdateEventDetails
    | FeedbackEventDetails,
    Field(discriminator="type"),
]
"""Discriminated union of provenance event detail types.

Uses Pydantic's discriminator field (``type``) to deserialize into the
correct detail class. Each variant corresponds to a
``ProvenanceEventTypeEnum`` value.
"""


class ProvenanceEvent(BaseModel):
    """Single event in the attribution provenance audit trail.

    Each ``ProvenanceEvent`` records one discrete action that contributed
    to or modified an attribution record. The chain of events forms an
    immutable audit trail enabling full transparency of how an
    attribution was constructed and refined.

    Attributes
    ----------
    event_type : ProvenanceEventTypeEnum
        High-level event type (FETCH, RESOLVE, SCORE, REVIEW, UPDATE,
        FEEDBACK).
    timestamp : datetime
        UTC timestamp when this event occurred. Must be timezone-aware.
    agent : str
        Identifier of the software agent or human that performed this
        action (e.g., ``"etl-musicbrainz-v1.2"``, ``"reviewer-jdoe"``).
    details : EventDetails
        Typed event details (discriminated union). The concrete type
        matches ``event_type``.
    feedback_card_id : uuid.UUID or None
        UUID of the associated ``FeedbackCard``, if this event was
        triggered by user feedback.
    step_uncertainty : StepUncertainty or None
        Uncertainty decomposition for this specific pipeline step,
        if available.
    citation_index : int or None
        1-based citation index for referencing this event in chat
        responses. None if not cited. Minimum 1 when set.
    """

    event_type: ProvenanceEventTypeEnum
    timestamp: datetime
    agent: str
    details: EventDetails
    feedback_card_id: uuid.UUID | None = None
    step_uncertainty: StepUncertainty | None = None
    citation_index: int | None = Field(default=None, ge=1)

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v: datetime) -> datetime:
        """Timestamp must be timezone-aware."""
        if v.tzinfo is None:
            msg = "timestamp must be timezone-aware (UTC)"
            raise ValueError(msg)
        return v


class AttributionRecord(BaseModel):
    """Complete attribution record for a musical work or recording.

    The ``AttributionRecord`` is the third boundary object (BO-3) in the
    five-pipeline architecture and the primary deliverable of the
    Attribution Engine. It is consumed by the API/MCP Server (for
    permission queries) and the Chat Interface (for user-facing
    attribution display).

    Each record contains: (1) a list of credits with per-credit
    confidence, (2) conformal prediction sets providing coverage
    guarantees, (3) an immutable provenance chain, and (4) an optional
    uncertainty summary. See Teikari (2026), sections 5-6.

    Attributes
    ----------
    schema_version : str
        Semantic version of the AttributionRecord schema. Defaults to
        ``"1.0.0"``.
    attribution_id : uuid.UUID
        Unique identifier for this attribution record. Auto-generated
        UUIDv4.
    work_entity_id : uuid.UUID
        UUID of the ``ResolvedEntity`` (work or recording) that this
        attribution describes.
    work_title : str
        Display title of the work. Populated for API/UI convenience.
    artist_name : str
        Display name of the primary artist. Populated for API/UI
        convenience.
    credits : list of Credit
        Attribution credits. Must contain at least one credit. Each
        credit links an entity to a role with confidence scoring.
    assurance_level : AssuranceLevelEnum
        Overall A0-A3 assurance level for this attribution record,
        determined by the weakest link in the evidence chain.
    confidence_score : float
        Overall calibrated confidence score, range [0.0, 1.0].
        Aggregated from per-credit confidences and source agreement.
    conformal_set : ConformalSet
        Conformal prediction set providing coverage guarantees on
        role assignments.
    source_agreement : float
        Degree of agreement across data sources, range [0.0, 1.0].
        1.0 = all sources agree on all credits; 0.0 = total
        disagreement.
    provenance_chain : list of ProvenanceEvent
        Ordered list of provenance events forming the audit trail.
        Events are appended chronologically.
    uncertainty_summary : UncertaintyAwareProvenance or None
        Aggregated uncertainty decomposition across all pipeline steps.
        None if uncertainty tracking is not enabled.
    needs_review : bool
        Flag indicating this record requires human review before
        being surfaced to end users.
    review_priority : float
        Priority score for the review queue, range [0.0, 1.0].
        Higher values = more urgent review needed.
    created_at : datetime
        UTC timestamp when this record was first created. Must be
        timezone-aware.
    updated_at : datetime
        UTC timestamp of the most recent update. Must be
        timezone-aware. Must be >= ``created_at``.
    version : int
        Monotonically increasing version number. Minimum 1. Bumped
        on every update.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> record = AttributionRecord(
    ...     work_entity_id=uuid.uuid4(),
    ...     work_title="Hide and Seek",
    ...     artist_name="Imogen Heap",
    ...     credits=[
    ...         Credit(
    ...             entity_id=uuid.uuid4(),
    ...             entity_name="Imogen Heap",
    ...             role=CreditRoleEnum.PERFORMER,
    ...             confidence=0.95,
    ...             sources=[SourceEnum.MUSICBRAINZ, SourceEnum.DISCOGS],
    ...             assurance_level=AssuranceLevelEnum.LEVEL_2,
    ...         ),
    ...     ],
    ...     assurance_level=AssuranceLevelEnum.LEVEL_2,
    ...     confidence_score=0.92,
    ...     conformal_set=ConformalSet(
    ...         coverage_level=0.90,
    ...         marginal_coverage=0.91,
    ...         calibration_error=0.01,
    ...         calibration_method="split_conformal",
    ...         calibration_set_size=500,
    ...     ),
    ...     source_agreement=0.88,
    ...     review_priority=0.1,
    ...     created_at=datetime.now(UTC),
    ...     updated_at=datetime.now(UTC),
    ...     version=1,
    ... )

    See Also
    --------
    ResolvedEntity : The preceding boundary object from Entity Resolution.
    FeedbackCard : Reverse-flow feedback for calibration updates.
    """

    schema_version: str = "1.0.0"
    attribution_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    work_entity_id: uuid.UUID
    work_title: str = ""
    artist_name: str = ""
    credits: list[Credit] = Field(min_length=1)
    assurance_level: AssuranceLevelEnum
    confidence_score: float = Field(ge=0.0, le=1.0)
    conformal_set: ConformalSet
    source_agreement: float = Field(ge=0.0, le=1.0)
    provenance_chain: list[ProvenanceEvent] = Field(default_factory=list)
    uncertainty_summary: UncertaintyAwareProvenance | None = None
    needs_review: bool = False
    review_priority: float = Field(ge=0.0, le=1.0)
    created_at: datetime
    updated_at: datetime
    version: int = Field(ge=1)

    @field_validator("created_at", "updated_at")
    @classmethod
    def validate_timestamps(cls, v: datetime) -> datetime:
        """Timestamps must be timezone-aware."""
        if v.tzinfo is None:
            msg = "Timestamps must be timezone-aware (UTC)"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_updated_after_created(self) -> AttributionRecord:
        """updated_at must be >= created_at."""
        if self.updated_at < self.created_at:
            msg = "updated_at must be >= created_at"
            raise ValueError(msg)
        return self
