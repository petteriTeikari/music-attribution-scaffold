"""Pipeline feedback channels for continuous improvement.

Defines reverse-flow signals between pipelines:
- ER -> DE: "source X data is consistently wrong, re-fetch"
- AE -> ER: "resolution confidence was miscalibrated"
- API -> AE: "dispute received, re-evaluate this attribution"
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from pydantic import BaseModel, Field

from music_attribution.schemas.enums import PipelineFeedbackTypeEnum, SourceEnum


class PipelineFeedback(BaseModel):
    """Feedback signal between pipelines for continuous improvement."""

    feedback_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    source_pipeline: str
    target_pipeline: str
    feedback_type: PipelineFeedbackTypeEnum
    entity_ids: list[uuid.UUID] = Field(default_factory=list)
    details: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Optional fields for specific feedback types
    target_source: SourceEnum | None = None  # For REFETCH signals
    attribution_id: uuid.UUID | None = None  # For DISPUTE signals
    predicted_confidence: float | None = None  # For RECALIBRATE signals
    actual_accuracy: float | None = None  # For RECALIBRATE signals
