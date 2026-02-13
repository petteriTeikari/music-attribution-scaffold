"""Pipeline feedback channels for continuous improvement.

Defines reverse-flow signals between pipelines, enabling the system
to self-correct over time:

* **ER -> DE** (REFETCH): "Source X data is consistently wrong, re-fetch."
* **AE -> ER** (RECALIBRATE): "Resolution confidence was miscalibrated."
* **API -> AE** (DISPUTE): "Dispute received, re-evaluate this attribution."
* **Any -> Any** (STALE): "Record has not been refreshed within its
  expected freshness window."

These signals are distinct from ``FeedbackCard`` (which captures
human expert feedback). ``PipelineFeedback`` is machine-to-machine
signalling within the pipeline architecture.

See Also
--------
music_attribution.schemas.feedback : Human expert feedback (FeedbackCard).
music_attribution.schemas.enums.PipelineFeedbackTypeEnum : Signal types.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from pydantic import BaseModel, Field

from music_attribution.schemas.enums import PipelineFeedbackTypeEnum, SourceEnum


class PipelineFeedback(BaseModel):
    """Feedback signal between pipelines for continuous improvement.

    A machine-to-machine signal that one pipeline sends to another when
    it detects a condition that requires corrective action. These signals
    form the self-correction loop in the five-pipeline architecture.

    Attributes
    ----------
    feedback_id : uuid.UUID
        Unique identifier for this feedback signal. Auto-generated
        UUIDv4.
    source_pipeline : str
        Name of the pipeline sending the signal (e.g.,
        ``"entity_resolution"``, ``"attribution_engine"``).
    target_pipeline : str
        Name of the pipeline that should act on the signal (e.g.,
        ``"data_engineering"``, ``"entity_resolution"``).
    feedback_type : PipelineFeedbackTypeEnum
        Type of feedback signal (REFETCH, RECALIBRATE, DISPUTE, STALE).
    entity_ids : list of uuid.UUID
        UUIDs of the entities affected by this feedback signal.
    details : str
        Human-readable description of the issue (e.g., "MusicBrainz
        artist name changed for 3 entities in batch xyz").
    created_at : datetime
        UTC timestamp when the signal was created. Auto-generated.
    target_source : SourceEnum or None
        For REFETCH signals: which data source needs re-fetching.
    attribution_id : uuid.UUID or None
        For DISPUTE signals: UUID of the disputed ``AttributionRecord``.
    predicted_confidence : float or None
        For RECALIBRATE signals: the confidence the resolution pipeline
        predicted, range [0.0, 1.0].
    actual_accuracy : float or None
        For RECALIBRATE signals: the actual accuracy observed
        downstream, range [0.0, 1.0]. The gap between
        ``predicted_confidence`` and ``actual_accuracy`` measures
        miscalibration.

    Examples
    --------
    >>> signal = PipelineFeedback(
    ...     source_pipeline="attribution_engine",
    ...     target_pipeline="entity_resolution",
    ...     feedback_type=PipelineFeedbackTypeEnum.RECALIBRATE,
    ...     details="Resolution confidence 0.92 but actual accuracy 0.71",
    ...     predicted_confidence=0.92,
    ...     actual_accuracy=0.71,
    ... )
    """

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
