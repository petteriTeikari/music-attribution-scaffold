"""FeedbackCard boundary object schema (BO-4).

Structured feedback from domain experts (artists, managers, musicologists,
producers). Flows from the Chat Interface back into the Attribution Engine
for calibration updates. Ref: Zhou et al., 2023 -- FeedbackCards.

The ``FeedbackCard`` is the primary reverse-flow boundary object in the
five-pipeline architecture, enabling human-in-the-loop calibration. When
a domain expert reviews an attribution and provides corrections, these
are captured in a ``FeedbackCard`` that feeds back into the Attribution
Engine for confidence recalibration.

See Also
--------
music_attribution.schemas.attribution : The AttributionRecord being reviewed.
Teikari, P. (2026). *Music Attribution with Transparent Confidence*,
    section 6.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum


class Correction(BaseModel):
    """A specific correction to an attribution field.

    Represents a single field-level correction proposed by a reviewer.
    Each correction includes the current (incorrect) value, the proposed
    corrected value, and the reviewer's confidence in their correction.

    Attributes
    ----------
    field : str
        Name of the field being corrected (e.g., ``"role"``,
        ``"entity_name"``, ``"confidence"``).
    current_value : str
        The current (incorrect) value of the field as a string.
    corrected_value : str
        The proposed correct value as a string.
    entity_id : uuid.UUID or None
        UUID of the specific entity this correction applies to, if the
        correction is entity-specific (e.g., correcting a credit role).
        None for record-level corrections.
    confidence_in_correction : float
        The reviewer's confidence that their correction is accurate,
        range [0.0, 1.0]. Higher values from authoritative reviewers
        (e.g., the artist) carry more weight during recalibration.
    evidence : str or None
        Free-text description of the evidence supporting this
        correction (e.g., ``"Listed in vinyl liner notes, track 3"``).

    Examples
    --------
    >>> correction = Correction(
    ...     field="role",
    ...     current_value="PERFORMER",
    ...     corrected_value="PRODUCER",
    ...     entity_id=uuid.uuid4(),
    ...     confidence_in_correction=0.95,
    ...     evidence="Confirmed in studio session notes",
    ... )
    """

    field: str
    current_value: str
    corrected_value: str
    entity_id: uuid.UUID | None = None
    confidence_in_correction: float = Field(ge=0.0, le=1.0)
    evidence: str | None = None


class FeedbackCard(BaseModel):
    """Structured feedback from a domain expert (BO-4).

    The ``FeedbackCard`` is the reverse-flow boundary object in the
    five-pipeline architecture, flowing from the Chat Interface back
    into the Attribution Engine. It captures structured corrections
    and an overall assessment from a domain expert who reviewed an
    ``AttributionRecord``.

    A valid ``FeedbackCard`` must contain either corrections or free-text
    (or both). The ``center_bias_flag`` is automatically set when the
    overall assessment falls in the [0.45, 0.55] range, indicating
    potential anchoring bias toward the midpoint.

    Attributes
    ----------
    schema_version : str
        Semantic version of the FeedbackCard schema. Defaults to
        ``"1.0.0"``.
    feedback_id : uuid.UUID
        Unique identifier for this feedback card. Auto-generated UUIDv4.
    attribution_id : uuid.UUID
        UUID of the ``AttributionRecord`` being reviewed.
    reviewer_id : str
        Identifier of the reviewer (may be an email, username, or
        external ID).
    reviewer_role : ReviewerRoleEnum
        Domain expertise of the reviewer (ARTIST, MANAGER,
        MUSICOLOGIST, PRODUCER, FAN).
    attribution_version : int
        Version of the ``AttributionRecord`` at the time of review.
        Minimum 1. Prevents stale feedback on updated records.
    corrections : list of Correction
        Specific field-level corrections proposed by the reviewer.
        May be empty if only free-text feedback is provided.
    overall_assessment : float
        Reviewer's overall assessment of the attribution quality,
        range [0.0, 1.0]. 0.0 = completely wrong; 1.0 = perfect.
    center_bias_flag : bool
        Automatically set to True if ``overall_assessment`` is in
        [0.45, 0.55], indicating potential anchoring bias.
    free_text : str or None
        Free-text feedback for nuances not captured by structured
        corrections.
    evidence_type : EvidenceTypeEnum
        Type of evidence supporting the feedback (LINER_NOTES, MEMORY,
        DOCUMENT, SESSION_NOTES, OTHER).
    submitted_at : datetime
        UTC timestamp when the feedback was submitted. Must be
        timezone-aware.

    Examples
    --------
    >>> from datetime import datetime, UTC
    >>> card = FeedbackCard(
    ...     attribution_id=uuid.uuid4(),
    ...     reviewer_id="imogen.heap@example.com",
    ...     reviewer_role=ReviewerRoleEnum.ARTIST,
    ...     attribution_version=1,
    ...     corrections=[
    ...         Correction(
    ...             field="role",
    ...             current_value="PERFORMER",
    ...             corrected_value="SONGWRITER",
    ...             confidence_in_correction=1.0,
    ...         ),
    ...     ],
    ...     overall_assessment=0.7,
    ...     evidence_type=EvidenceTypeEnum.MEMORY,
    ...     submitted_at=datetime.now(UTC),
    ... )

    See Also
    --------
    AttributionRecord : The record being reviewed.
    Correction : Individual field-level corrections.
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
