"""Tests for pipeline feedback channels."""

from __future__ import annotations

import uuid

from music_attribution.schemas.enums import PipelineFeedbackTypeEnum, SourceEnum
from music_attribution.schemas.pipeline_feedback import PipelineFeedback


class TestPipelineFeedback:
    """Tests for pipeline feedback signals."""

    def test_refetch_signal_targets_specific_source_and_entity(self) -> None:
        """Test that REFETCH signal includes source and entity IDs."""
        entity_id = uuid.uuid4()
        feedback = PipelineFeedback(
            source_pipeline="entity-resolution",
            target_pipeline="data-engineering",
            feedback_type=PipelineFeedbackTypeEnum.REFETCH,
            entity_ids=[entity_id],
            details="Source DISCOGS data is inconsistent for this entity",
            target_source=SourceEnum.DISCOGS,
        )
        assert feedback.feedback_type == PipelineFeedbackTypeEnum.REFETCH
        assert entity_id in feedback.entity_ids
        assert feedback.target_source == SourceEnum.DISCOGS

    def test_recalibrate_signal_includes_actual_vs_predicted(self) -> None:
        """Test that RECALIBRATE signal includes calibration data."""
        feedback = PipelineFeedback(
            source_pipeline="attribution-engine",
            target_pipeline="entity-resolution",
            feedback_type=PipelineFeedbackTypeEnum.RECALIBRATE,
            entity_ids=[uuid.uuid4()],
            details="Resolution confidence was 0.9 but actual accuracy is 0.6",
            predicted_confidence=0.9,
            actual_accuracy=0.6,
        )
        assert feedback.feedback_type == PipelineFeedbackTypeEnum.RECALIBRATE
        assert feedback.predicted_confidence == 0.9
        assert feedback.actual_accuracy == 0.6

    def test_dispute_signal_links_to_attribution_id(self) -> None:
        """Test that DISPUTE signal links to specific attribution."""
        attribution_id = uuid.uuid4()
        feedback = PipelineFeedback(
            source_pipeline="api-server",
            target_pipeline="attribution-engine",
            feedback_type=PipelineFeedbackTypeEnum.DISPUTE,
            entity_ids=[],
            details="User disputes this attribution",
            attribution_id=attribution_id,
        )
        assert feedback.feedback_type == PipelineFeedbackTypeEnum.DISPUTE
        assert feedback.attribution_id == attribution_id

    def test_stale_signal_triggers_re_processing(self) -> None:
        """Test that STALE signal includes staleness information."""
        entity_id = uuid.uuid4()
        feedback = PipelineFeedback(
            source_pipeline="quality-monitor",
            target_pipeline="data-engineering",
            feedback_type=PipelineFeedbackTypeEnum.STALE,
            entity_ids=[entity_id],
            details="Data older than 90 days, re-fetch recommended",
        )
        assert feedback.feedback_type == PipelineFeedbackTypeEnum.STALE
        assert len(feedback.entity_ids) == 1
