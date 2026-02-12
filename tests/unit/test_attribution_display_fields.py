"""Tests for display fields added to AttributionRecord and Credit schemas.

These fields (work_title, artist_name, entity_name) are needed by the frontend
but were missing from the backend schema. They have empty string defaults for
backward compatibility.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest

from music_attribution.schemas.attribution import AttributionRecord, Credit
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    SourceEnum,
)


@pytest.mark.unit
class TestCreditDisplayFields:
    """Tests for Credit.entity_name display field."""

    def test_credit_has_entity_name_field(self) -> None:
        """Credit model accepts entity_name parameter."""
        credit = Credit(
            entity_id=uuid.uuid4(),
            entity_name="Imogen Heap",
            role=CreditRoleEnum.PERFORMER,
            confidence=0.95,
            sources=[SourceEnum.MUSICBRAINZ],
            assurance_level=AssuranceLevelEnum.LEVEL_2,
        )
        assert credit.entity_name == "Imogen Heap"

    def test_credit_entity_name_defaults_to_empty_string(self) -> None:
        """Credit.entity_name defaults to empty string for backward compat."""
        credit = Credit(
            entity_id=uuid.uuid4(),
            role=CreditRoleEnum.PERFORMER,
            confidence=0.95,
            sources=[SourceEnum.MUSICBRAINZ],
            assurance_level=AssuranceLevelEnum.LEVEL_2,
        )
        assert credit.entity_name == ""

    def test_credit_entity_name_in_json_dump(self) -> None:
        """entity_name appears in JSON serialization."""
        credit = Credit(
            entity_id=uuid.uuid4(),
            entity_name="Guy Sigsworth",
            role=CreditRoleEnum.PRODUCER,
            confidence=0.85,
            sources=[SourceEnum.DISCOGS],
            assurance_level=AssuranceLevelEnum.LEVEL_1,
        )
        data = credit.model_dump(mode="json")
        assert "entity_name" in data
        assert data["entity_name"] == "Guy Sigsworth"


def _make_minimal_record(**overrides: object) -> AttributionRecord:
    """Create a minimal valid AttributionRecord for testing."""
    now = datetime.now(UTC)
    defaults: dict = {
        "work_entity_id": uuid.uuid4(),
        "credits": [
            Credit(
                entity_id=uuid.uuid4(),
                role=CreditRoleEnum.PERFORMER,
                confidence=0.9,
                sources=[SourceEnum.MUSICBRAINZ],
                assurance_level=AssuranceLevelEnum.LEVEL_2,
            )
        ],
        "assurance_level": AssuranceLevelEnum.LEVEL_2,
        "confidence_score": 0.85,
        "conformal_set": {
            "coverage_level": 0.9,
            "marginal_coverage": 0.88,
            "calibration_error": 0.02,
            "calibration_method": "platt",
            "calibration_set_size": 100,
        },
        "source_agreement": 0.8,
        "needs_review": False,
        "review_priority": 0.5,
        "created_at": now,
        "updated_at": now,
        "version": 1,
    }
    defaults.update(overrides)
    return AttributionRecord(**defaults)


@pytest.mark.unit
class TestAttributionRecordDisplayFields:
    """Tests for work_title and artist_name display fields."""

    def test_attribution_record_has_work_title_field(self) -> None:
        """AttributionRecord accepts work_title parameter."""
        record = _make_minimal_record(work_title="Hide and Seek")
        assert record.work_title == "Hide and Seek"

    def test_attribution_record_has_artist_name_field(self) -> None:
        """AttributionRecord accepts artist_name parameter."""
        record = _make_minimal_record(artist_name="Imogen Heap")
        assert record.artist_name == "Imogen Heap"

    def test_display_fields_default_to_empty_string(self) -> None:
        """work_title and artist_name default to empty string."""
        record = _make_minimal_record()
        assert record.work_title == ""
        assert record.artist_name == ""

    def test_display_fields_included_in_json_dump(self) -> None:
        """Display fields appear in JSON serialization."""
        record = _make_minimal_record(
            work_title="Goodnight and Go",
            artist_name="Imogen Heap",
        )
        data = record.model_dump(mode="json")
        assert data["work_title"] == "Goodnight and Go"
        assert data["artist_name"] == "Imogen Heap"


@pytest.mark.unit
class TestAttributionRecordModelDisplayColumns:
    """Tests that the ORM model has work_title and artist_name columns."""

    def test_model_has_work_title_column(self) -> None:
        """AttributionRecordModel has a work_title column."""
        from music_attribution.db.models import AttributionRecordModel

        assert hasattr(AttributionRecordModel, "work_title")

    def test_model_has_artist_name_column(self) -> None:
        """AttributionRecordModel has an artist_name column."""
        from music_attribution.db.models import AttributionRecordModel

        assert hasattr(AttributionRecordModel, "artist_name")

    def test_record_to_model_includes_display_fields(self) -> None:
        """_record_to_model copies display fields to model."""
        from music_attribution.attribution.persistence import _record_to_model

        record = _make_minimal_record(work_title="Hide and Seek", artist_name="Imogen Heap")
        model = _record_to_model(record)
        assert model.work_title == "Hide and Seek"
        assert model.artist_name == "Imogen Heap"

    def test_model_to_record_restores_display_fields(self) -> None:
        """_model_to_record reads display fields from model."""
        from music_attribution.attribution.persistence import _model_to_record, _record_to_model

        record = _make_minimal_record(work_title="Goodnight and Go", artist_name="Imogen Heap")
        model = _record_to_model(record)
        restored = _model_to_record(model)
        assert restored.work_title == "Goodnight and Go"
        assert restored.artist_name == "Imogen Heap"


@pytest.mark.unit
class TestSeedDataDisplayFields:
    """Tests that seed data populates display fields."""

    def test_seed_data_populates_work_title(self) -> None:
        """Seed module creates records with work_title set."""
        from music_attribution.seed.imogen_heap import build_imogen_heap_records

        records = build_imogen_heap_records()
        for record in records:
            assert record.work_title != "", f"work_title empty for {record.attribution_id}"

    def test_seed_data_populates_artist_name(self) -> None:
        """Seed module creates records with artist_name set."""
        from music_attribution.seed.imogen_heap import build_imogen_heap_records

        records = build_imogen_heap_records()
        for record in records:
            assert record.artist_name == "Imogen Heap"

    def test_seed_data_populates_entity_name_on_credits(self) -> None:
        """Seed module creates credits with entity_name set."""
        from music_attribution.seed.imogen_heap import build_imogen_heap_records

        records = build_imogen_heap_records()
        for record in records:
            for credit in record.credits:
                assert credit.entity_name != "", (
                    f"entity_name empty for credit {credit.entity_id} in record {record.attribution_id}"
                )
