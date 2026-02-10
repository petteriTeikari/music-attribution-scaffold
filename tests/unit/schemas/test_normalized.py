"""Tests for NormalizedRecord boundary object schema."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta

import pytest
from pydantic import ValidationError

from music_attribution.schemas.normalized import NormalizedRecord


class TestNormalizedRecord:
    """Tests for NormalizedRecord boundary object."""

    def _valid_kwargs(self) -> dict:
        """Return minimal valid kwargs for NormalizedRecord."""
        return {
            "source": "MUSICBRAINZ",
            "source_id": "mbid-123",
            "entity_type": "RECORDING",
            "canonical_name": "Test Song",
            "identifiers": {"isrc": "USRC17607839"},
            "fetch_timestamp": datetime.now(UTC),
            "source_confidence": 0.9,
        }

    def test_normalized_record_valid_creation(self) -> None:
        """Test that a valid NormalizedRecord can be created."""
        record = NormalizedRecord(**self._valid_kwargs())
        assert record.canonical_name == "Test Song"
        assert record.source == "MUSICBRAINZ"
        assert record.record_id is not None
        assert record.schema_version == "1.0.0"

    def test_normalized_record_rejects_empty_name(self) -> None:
        """Test that empty canonical_name is rejected."""
        kwargs = self._valid_kwargs()
        kwargs["canonical_name"] = "   "
        with pytest.raises(ValidationError):
            NormalizedRecord(**kwargs)

    def test_normalized_record_rejects_future_timestamp(self) -> None:
        """Test that fetch_timestamp far in the future is rejected."""
        kwargs = self._valid_kwargs()
        kwargs["fetch_timestamp"] = datetime.now(UTC) + timedelta(seconds=120)
        with pytest.raises(ValidationError):
            NormalizedRecord(**kwargs)

    def test_normalized_record_requires_timezone_aware_datetime(self) -> None:
        """Test that naive datetime is rejected for fetch_timestamp."""
        kwargs = self._valid_kwargs()
        kwargs["fetch_timestamp"] = datetime(2026, 1, 1, 12, 0, 0)  # noqa: DTZ001
        with pytest.raises(ValidationError):
            NormalizedRecord(**kwargs)

    def test_normalized_record_source_confidence_bounds(self) -> None:
        """Test that source_confidence must be between 0.0 and 1.0."""
        kwargs = self._valid_kwargs()

        kwargs["source_confidence"] = -0.1
        with pytest.raises(ValidationError):
            NormalizedRecord(**kwargs)

        kwargs["source_confidence"] = 1.1
        with pytest.raises(ValidationError):
            NormalizedRecord(**kwargs)

    def test_normalized_record_requires_at_least_one_identifier(self) -> None:
        """Test that machine sources require at least one identifier."""
        kwargs = self._valid_kwargs()
        kwargs["identifiers"] = {}  # all None
        with pytest.raises(ValidationError):
            NormalizedRecord(**kwargs)

    def test_normalized_record_artist_input_allows_empty_identifiers(self) -> None:
        """Test that ARTIST_INPUT source allows empty identifiers."""
        kwargs = self._valid_kwargs()
        kwargs["source"] = "ARTIST_INPUT"
        kwargs["identifiers"] = {}
        record = NormalizedRecord(**kwargs)
        assert record.source == "ARTIST_INPUT"

    def test_normalized_record_serializes_to_json(self) -> None:
        """Test JSON serialization works."""
        record = NormalizedRecord(**self._valid_kwargs())
        json_str = record.model_dump_json()
        assert isinstance(json_str, str)
        data = json.loads(json_str)
        assert data["canonical_name"] == "Test Song"

    def test_normalized_record_roundtrip_json(self) -> None:
        """Test JSON roundtrip (serialize then deserialize)."""
        original = NormalizedRecord(**self._valid_kwargs())
        json_str = original.model_dump_json()
        restored = NormalizedRecord.model_validate_json(json_str)
        assert restored.canonical_name == original.canonical_name
        assert restored.source == original.source
        assert restored.record_id == original.record_id
