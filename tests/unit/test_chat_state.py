"""Tests for chat agent state model."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from music_attribution.chat.state import AttributionAgentState, CorrectionPreview


class TestCorrectionPreview:
    """Tests for CorrectionPreview model."""

    def test_valid_correction_preview(self) -> None:
        preview = CorrectionPreview(
            field="assurance_level",
            current_value="LEVEL_1",
            suggested_value="LEVEL_2",
            reason="Multiple sources agree",
            confidence_in_correction=0.85,
        )
        assert preview.field == "assurance_level"
        assert preview.confidence_in_correction == 0.85

    def test_confidence_bounds(self) -> None:
        with pytest.raises(ValidationError):
            CorrectionPreview(
                field="role",
                current_value="x",
                suggested_value="y",
                reason="test",
                confidence_in_correction=1.5,
            )


class TestAttributionAgentState:
    """Tests for AttributionAgentState model."""

    def test_default_state(self) -> None:
        state = AttributionAgentState()
        assert state.current_work_id is None
        assert state.confidence_score is None
        assert state.review_queue_size == 0
        assert state.pending_correction is None
        assert state.explanation_text is None

    def test_full_state(self) -> None:
        state = AttributionAgentState(
            current_work_id="abc-123",
            current_work_title="Hide and Seek",
            confidence_score=0.85,
            review_queue_size=5,
            explanation_text="High confidence based on 3 matching sources",
            last_search_query="imogen heap",
            last_search_count=8,
        )
        assert state.current_work_id == "abc-123"
        assert state.confidence_score == 0.85
        assert state.review_queue_size == 5

    def test_state_with_correction(self) -> None:
        state = AttributionAgentState(
            pending_correction=CorrectionPreview(
                field="assurance_level",
                current_value="LEVEL_1",
                suggested_value="LEVEL_2",
                reason="Discogs confirms credit",
                confidence_in_correction=0.9,
            ),
        )
        assert state.pending_correction is not None
        assert state.pending_correction.suggested_value == "LEVEL_2"

    def test_confidence_score_bounds(self) -> None:
        with pytest.raises(ValidationError):
            AttributionAgentState(confidence_score=1.5)

    def test_negative_queue_size_rejected(self) -> None:
        with pytest.raises(ValidationError):
            AttributionAgentState(review_queue_size=-1)

    def test_serialization_roundtrip(self) -> None:
        state = AttributionAgentState(
            current_work_id="test-id",
            confidence_score=0.72,
            review_queue_size=3,
        )
        data = state.model_dump()
        restored = AttributionAgentState.model_validate(data)
        assert restored == state
