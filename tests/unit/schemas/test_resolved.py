"""Tests for ResolvedEntity boundary object schema."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from music_attribution.schemas.resolved import ResolvedEntity


class TestResolvedEntity:
    """Tests for ResolvedEntity boundary object."""

    def _valid_kwargs(self) -> dict:
        """Return minimal valid kwargs for ResolvedEntity."""
        return {
            "entity_type": "ARTIST",
            "canonical_name": "Test Artist",
            "identifiers": {"isni": "0000000121032683"},
            "source_records": [
                {
                    "record_id": str(uuid.uuid4()),
                    "source": "MUSICBRAINZ",
                    "source_id": "mbid-456",
                    "agreement_score": 0.95,
                }
            ],
            "resolution_method": "EXACT_ID",
            "resolution_confidence": 0.95,
            "resolution_details": {"matched_identifiers": ["isni"]},
            "assurance_level": "LEVEL_2",
            "resolved_at": datetime.now(UTC),
        }

    def test_resolved_entity_valid_creation(self) -> None:
        """Test that a valid ResolvedEntity can be created."""
        entity = ResolvedEntity(**self._valid_kwargs())
        assert entity.canonical_name == "Test Artist"
        assert entity.entity_id is not None
        assert entity.schema_version == "1.0.0"

    def test_resolved_entity_assurance_level_ordering(self) -> None:
        """Test that A0 < A1 < A2 < A3 assurance levels are orderable."""
        from music_attribution.schemas.enums import AssuranceLevelEnum

        levels = [
            AssuranceLevelEnum.LEVEL_0,
            AssuranceLevelEnum.LEVEL_1,
            AssuranceLevelEnum.LEVEL_2,
            AssuranceLevelEnum.LEVEL_3,
        ]
        for i in range(len(levels) - 1):
            assert levels[i].value < levels[i + 1].value

    def test_resolved_entity_conflict_severity_levels(self) -> None:
        """Test that conflict severity levels exist and are distinct."""
        from music_attribution.schemas.enums import ConflictSeverityEnum

        assert len(ConflictSeverityEnum) == 4
        expected = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
        actual = {e.value for e in ConflictSeverityEnum}
        assert actual == expected

    def test_resolved_entity_resolution_confidence_bounds(self) -> None:
        """Test that resolution_confidence must be between 0.0 and 1.0."""
        kwargs = self._valid_kwargs()

        kwargs["resolution_confidence"] = -0.1
        with pytest.raises(ValidationError):
            ResolvedEntity(**kwargs)

        kwargs["resolution_confidence"] = 1.1
        with pytest.raises(ValidationError):
            ResolvedEntity(**kwargs)

    def test_resolved_entity_needs_review_requires_reason(self) -> None:
        """Test that needs_review=True requires review_reason."""
        kwargs = self._valid_kwargs()
        kwargs["needs_review"] = True
        kwargs["review_reason"] = None
        with pytest.raises(ValidationError):
            ResolvedEntity(**kwargs)

    def test_resolved_entity_requires_source_records(self) -> None:
        """Test that source_records must be non-empty."""
        kwargs = self._valid_kwargs()
        kwargs["source_records"] = []
        with pytest.raises(ValidationError):
            ResolvedEntity(**kwargs)
