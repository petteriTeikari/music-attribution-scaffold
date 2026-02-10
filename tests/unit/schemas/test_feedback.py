"""Tests for FeedbackCard boundary object schema."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from music_attribution.schemas.feedback import FeedbackCard


class TestFeedbackCard:
    """Tests for FeedbackCard boundary object."""

    def _valid_kwargs(self) -> dict:
        """Return minimal valid kwargs for FeedbackCard."""
        return {
            "attribution_id": str(uuid.uuid4()),
            "reviewer_id": "artist-001",
            "reviewer_role": "ARTIST",
            "attribution_version": 1,
            "corrections": [
                {
                    "field": "role",
                    "current_value": "PERFORMER",
                    "corrected_value": "SONGWRITER",
                    "confidence_in_correction": 0.9,
                }
            ],
            "overall_assessment": 0.7,
            "evidence_type": "MEMORY",
            "submitted_at": datetime.now(UTC),
        }

    def test_feedback_card_valid_creation(self) -> None:
        """Test that a valid FeedbackCard can be created."""
        card = FeedbackCard(**self._valid_kwargs())
        assert card.feedback_id is not None
        assert card.reviewer_role == "ARTIST"
        assert card.schema_version == "1.0.0"

    def test_feedback_card_vas_center_bias_warning(self) -> None:
        """Test that score == 0.5 triggers center_bias_flag."""
        kwargs = self._valid_kwargs()
        kwargs["overall_assessment"] = 0.5
        card = FeedbackCard(**kwargs)
        assert card.center_bias_flag is True

    def test_feedback_card_no_center_bias_outside_range(self) -> None:
        """Test that scores outside [0.45, 0.55] don't trigger center_bias_flag."""
        kwargs = self._valid_kwargs()
        kwargs["overall_assessment"] = 0.7
        card = FeedbackCard(**kwargs)
        assert card.center_bias_flag is False

    def test_feedback_card_correction_types(self) -> None:
        """Test that corrections can be created with various fields."""
        kwargs = self._valid_kwargs()
        kwargs["corrections"] = [
            {
                "field": "role",
                "current_value": "PERFORMER",
                "corrected_value": "SONGWRITER",
                "confidence_in_correction": 0.9,
            },
            {
                "field": "canonical_name",
                "current_value": "John Smith",
                "corrected_value": "John A. Smith",
                "entity_id": str(uuid.uuid4()),
                "confidence_in_correction": 1.0,
                "evidence": "Liner notes show full name",
            },
        ]
        card = FeedbackCard(**kwargs)
        assert len(card.corrections) == 2

    def test_feedback_card_requires_content(self) -> None:
        """Test that empty corrections and no free_text is rejected."""
        kwargs = self._valid_kwargs()
        kwargs["corrections"] = []
        kwargs["free_text"] = None
        with pytest.raises(ValidationError):
            FeedbackCard(**kwargs)

    def test_feedback_card_overall_assessment_bounds(self) -> None:
        """Test that overall_assessment must be between 0.0 and 1.0."""
        kwargs = self._valid_kwargs()
        kwargs["overall_assessment"] = 1.5
        with pytest.raises(ValidationError):
            FeedbackCard(**kwargs)
