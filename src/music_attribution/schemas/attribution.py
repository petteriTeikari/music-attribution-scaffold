"""AttributionRecord boundary object schema (BO-3).

Output of the Attribution Engine pipeline. A complete attribution record
for a musical work/recording with calibrated confidence scores and
conformal prediction sets.
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
    """Attribution credit for an entity."""

    entity_id: uuid.UUID
    role: CreditRoleEnum
    role_detail: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    sources: list[SourceEnum] = Field(default_factory=list)
    assurance_level: AssuranceLevelEnum


class ConformalSet(BaseModel):
    """Conformal prediction set at specified coverage level."""

    coverage_level: float = Field(gt=0.0, lt=1.0)
    prediction_sets: dict[str, list[CreditRoleEnum]] = Field(default_factory=dict)
    set_sizes: dict[str, int] = Field(default_factory=dict)
    marginal_coverage: float = Field(ge=0.0, le=1.0)
    calibration_error: float = Field(ge=0.0)
    calibration_method: str
    calibration_set_size: int = Field(ge=0)


# Provenance event detail types (discriminated union)


class FetchEventDetails(BaseModel):
    """Details for FETCH provenance events."""

    type: Literal["fetch"] = "fetch"
    source: SourceEnum
    source_id: str
    records_fetched: int = Field(ge=0)
    rate_limited: bool = False


class ResolveEventDetails(BaseModel):
    """Details for RESOLVE provenance events."""

    type: Literal["resolve"] = "resolve"
    method: str
    records_input: int = Field(ge=0)
    entities_output: int = Field(ge=0)
    confidence_range: tuple[float, float] = (0.0, 1.0)


class ScoreEventDetails(BaseModel):
    """Details for SCORE provenance events."""

    type: Literal["score"] = "score"
    previous_confidence: float | None = None
    new_confidence: float = Field(ge=0.0, le=1.0)
    scoring_method: str


class ReviewEventDetails(BaseModel):
    """Details for REVIEW provenance events."""

    type: Literal["review"] = "review"
    reviewer_id: str
    feedback_card_id: uuid.UUID
    corrections_applied: int = Field(ge=0)


class UpdateEventDetails(BaseModel):
    """Details for UPDATE provenance events."""

    type: Literal["update"] = "update"
    previous_version: int = Field(ge=1)
    new_version: int = Field(ge=1)
    fields_changed: list[str] = Field(default_factory=list)
    trigger: str


class FeedbackEventDetails(BaseModel):
    """Details for FEEDBACK provenance events."""

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


class ProvenanceEvent(BaseModel):
    """Audit trail event."""

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
    """Complete attribution record for a musical work/recording.

    This is the primary boundary object produced by the Attribution Engine
    and consumed by the API/MCP Server and Chat Interface pipelines.
    """

    schema_version: str = "1.0.0"
    attribution_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    work_entity_id: uuid.UUID
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
