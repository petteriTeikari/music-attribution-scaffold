"""FeedbackCard boundary object schema (BO-4).

Structured feedback from domain experts (artists, managers, musicologists,
producers). Flows from Chat Interface back into Attribution Engine for
calibration updates. Ref: Zhou et al., 2023 — FeedbackCards.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum


class Correction(BaseModel):
    """A specific correction to an attribution field."""

    field: str
    current_value: str
    corrected_value: str
    entity_id: uuid.UUID | None = None
    confidence_in_correction: float = Field(ge=0.0, le=1.0)
    evidence: str | None = None


class FeedbackCard(BaseModel):
    """Structured feedback from a domain expert.

    This is the primary boundary object flowing from the Chat Interface
    back into the Attribution Engine for calibration updates.
    """

    schema_version: str = "1.0.0"
    feedback_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    attribution_id: uuid.UUID
    reviewer_id: str
    reviewer_role: ReviewerRoleEnum
    attribution_version: int = Field(ge=1)
    corrections: list[Correction] = Field(default_factory=list)
    overall_assessment: float = Field(ge=0.0, le=1.0)
    center_bias_flag: bool = False
    free_text: str | None = None
    evidence_type: EvidenceTypeEnum
    submitted_at: datetime

    @field_validator("submitted_at")
    @classmethod
    def validate_submitted_at(cls, v: datetime) -> datetime:
        """submitted_at must be timezone-aware."""
        if v.tzinfo is None:
            msg = "submitted_at must be timezone-aware (UTC)"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_content_not_empty(self) -> FeedbackCard:
        """A feedback card must have corrections or free_text."""
        if not self.corrections and self.free_text is None:
            msg = "FeedbackCard must have non-empty corrections or non-None free_text"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def validate_center_bias(self) -> FeedbackCard:
        """Set center_bias_flag if overall_assessment is in [0.45, 0.55]."""
        if 0.45 <= self.overall_assessment <= 0.55:
            object.__setattr__(self, "center_bias_flag", True)
        return self
