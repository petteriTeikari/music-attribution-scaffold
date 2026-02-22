"""Tests for AttributionRecord persistence repository."""

from __future__ import annotations

import uuid

import pytest

from music_attribution.attribution.persistence import AttributionRecordRepository
from music_attribution.schemas.attribution import AttributionRecord
from tests.factories import make_attribution as _make_attribution_base


def _make_attribution(
    work_id: uuid.UUID | None = None,
    needs_review: bool = False,
    review_priority: float = 0.1,
) -> AttributionRecord:
    """Create an AttributionRecord for testing."""

    return _make_attribution_base(
        work_entity_id=work_id or uuid.uuid4(),
        needs_review=needs_review,
        review_priority=review_priority,
    )


class TestAttributionRecordRepository:
    """Tests for AttributionRecordRepository."""

    @pytest.fixture
    def repo(self) -> AttributionRecordRepository:
        """Create an in-memory repository."""
        return AttributionRecordRepository()

    async def test_store_attribution_record(self, repo: AttributionRecordRepository) -> None:
        """Test storing and retrieving an attribution record."""
        record = _make_attribution()
        stored_id = await repo.store(record)

        assert stored_id == record.attribution_id

        retrieved = await repo.find_by_id(stored_id)
        assert retrieved is not None
        assert retrieved.attribution_id == record.attribution_id
        assert retrieved.work_entity_id == record.work_entity_id

    async def test_version_increments_on_update(self, repo: AttributionRecordRepository) -> None:
        """Test that version increments when a record is updated."""
        record = _make_attribution()
        await repo.store(record)

        assert record.version == 1

        updated_id = await repo.update(record)
        updated = await repo.find_by_id(updated_id)
        assert updated is not None
        assert updated.version == 2
        assert updated.updated_at >= record.updated_at

    async def test_query_by_work_entity_id(self, repo: AttributionRecordRepository) -> None:
        """Test querying attribution by work entity ID."""
        work_id = uuid.uuid4()
        record = _make_attribution(work_id=work_id)
        await repo.store(record)

        # Also store another record with different work_id
        other = _make_attribution()
        await repo.store(other)

        found = await repo.find_by_work_entity_id(work_id)
        assert found is not None
        assert found.work_entity_id == work_id

    async def test_query_needs_review(self, repo: AttributionRecordRepository) -> None:
        """Test querying records that need review, sorted by priority."""
        # Store records with different review flags and priorities
        r1 = _make_attribution(needs_review=True, review_priority=0.3)
        r2 = _make_attribution(needs_review=True, review_priority=0.9)
        r3 = _make_attribution(needs_review=False, review_priority=0.5)
        r4 = _make_attribution(needs_review=True, review_priority=0.6)

        for r in [r1, r2, r3, r4]:
            await repo.store(r)

        results = await repo.find_needs_review(limit=10)

        # Only records with needs_review=True
        assert len(results) == 3
        # Sorted by review_priority descending (highest priority first)
        assert results[0].review_priority == 0.9
        assert results[1].review_priority == 0.6
        assert results[2].review_priority == 0.3

    async def test_provenance_chain_appended_on_update(self, repo: AttributionRecordRepository) -> None:
        """Test that provenance chain gets an update event appended."""
        record = _make_attribution()
        assert len(record.provenance_chain) == 0

        await repo.store(record)
        updated_id = await repo.update(record)
        updated = await repo.find_by_id(updated_id)

        assert updated is not None
        assert len(updated.provenance_chain) == 1
        assert updated.provenance_chain[0].event_type.value == "UPDATE"
