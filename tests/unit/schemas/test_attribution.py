"""Tests for AttributionRecord boundary object schema."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from music_attribution.schemas.attribution import AttributionRecord


class TestAttributionRecord:
    """Tests for AttributionRecord boundary object."""

    def _valid_kwargs(self) -> dict:
        """Return minimal valid kwargs for AttributionRecord."""
        entity_id = uuid.uuid4()
        return {
            "work_entity_id": str(uuid.uuid4()),
            "credits": [
                {
                    "entity_id": str(entity_id),
                    "role": "PERFORMER",
                    "confidence": 0.95,
                    "sources": ["MUSICBRAINZ"],
                    "assurance_level": "LEVEL_1",
                }
            ],
            "assurance_level": "LEVEL_1",
            "confidence_score": 0.9,
            "conformal_set": {
                "coverage_level": 0.9,
                "prediction_sets": {},
                "set_sizes": {},
                "marginal_coverage": 0.91,
                "calibration_error": 0.03,
                "calibration_method": "APS",
                "calibration_set_size": 100,
            },
            "source_agreement": 0.85,
            "provenance_chain": [],
            "needs_review": False,
            "review_priority": 0.1,
            "created_at": datetime.now(UTC),
            "updated_at": datetime.now(UTC),
            "version": 1,
        }

    def test_attribution_record_valid_creation(self) -> None:
        """Test that a valid AttributionRecord can be created."""
        record = AttributionRecord(**self._valid_kwargs())
        assert record.attribution_id is not None
        assert record.confidence_score == 0.9
        assert record.schema_version == "1.0.0"

    def test_attribution_record_conformal_set_coverage(self) -> None:
        """Test that conformal_set coverage_level must be in (0.0, 1.0)."""
        kwargs = self._valid_kwargs()

        kwargs["conformal_set"]["coverage_level"] = 0.0
        with pytest.raises(ValidationError):
            AttributionRecord(**kwargs)

        kwargs["conformal_set"]["coverage_level"] = 1.0
        with pytest.raises(ValidationError):
            AttributionRecord(**kwargs)

    def test_attribution_record_version_increments(self) -> None:
        """Test that version must be >= 1."""
        kwargs = self._valid_kwargs()
        kwargs["version"] = 0
        with pytest.raises(ValidationError):
            AttributionRecord(**kwargs)

    def test_attribution_record_provenance_chain_ordering(self) -> None:
        """Test that provenance_chain events can be created with timestamps."""
        now = datetime.now(UTC)
        kwargs = self._valid_kwargs()
        kwargs["provenance_chain"] = [
            {
                "event_type": "FETCH",
                "timestamp": now,
                "agent": "data-pipeline",
                "details": {
                    "type": "fetch",
                    "source": "MUSICBRAINZ",
                    "source_id": "mbid-123",
                    "records_fetched": 5,
                    "rate_limited": False,
                },
            }
        ]
        record = AttributionRecord(**kwargs)
        assert len(record.provenance_chain) == 1

    def test_attribution_record_requires_credits(self) -> None:
        """Test that credits must be non-empty."""
        kwargs = self._valid_kwargs()
        kwargs["credits"] = []
        with pytest.raises(ValidationError):
            AttributionRecord(**kwargs)

    def test_attribution_record_updated_after_created(self) -> None:
        """Test that updated_at must be >= created_at."""
        kwargs = self._valid_kwargs()
        kwargs["created_at"] = datetime(2026, 2, 10, 12, 0, 0, tzinfo=UTC)
        kwargs["updated_at"] = datetime(2026, 2, 9, 12, 0, 0, tzinfo=UTC)
        with pytest.raises(ValidationError):
            AttributionRecord(**kwargs)
