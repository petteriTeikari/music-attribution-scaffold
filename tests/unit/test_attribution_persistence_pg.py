"""Tests for async PostgreSQL attribution repository."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from music_attribution.db.models import AttributionRecordModel
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
)
from music_attribution.schemas.enums import AssuranceLevelEnum, CreditRoleEnum, ProvenanceEventTypeEnum, SourceEnum


def _make_record(
    *,
    work_entity_id: uuid.UUID | None = None,
    confidence: float = 0.85,
    needs_review: bool = False,
    review_priority: float = 0.5,
) -> AttributionRecord:
    """Create a minimal valid AttributionRecord for testing."""
    now = datetime.now(UTC)
    return AttributionRecord(
        work_entity_id=work_entity_id or uuid.uuid4(),
        credits=[
            Credit(
                entity_id=uuid.uuid4(),
                role=CreditRoleEnum.PERFORMER,
                confidence=confidence,
                sources=[SourceEnum.MUSICBRAINZ],
                assurance_level=AssuranceLevelEnum.LEVEL_2,
            ),
        ],
        assurance_level=AssuranceLevelEnum.LEVEL_2,
        confidence_score=confidence,
        conformal_set=ConformalSet(
            coverage_level=0.9,
            prediction_sets={},
            set_sizes={},
            marginal_coverage=0.91,
            calibration_error=0.02,
            calibration_method="lac",
            calibration_set_size=100,
        ),
        source_agreement=0.8,
        needs_review=needs_review,
        review_priority=review_priority,
        created_at=now,
        updated_at=now,
        version=1,
    )


def _register_sqlite_type_compilers() -> None:
    """Register JSONB and HALFVEC compilation for SQLite dialect (test-only)."""
    from pgvector.sqlalchemy import HALFVEC
    from sqlalchemy.dialects.postgresql import JSONB
    from sqlalchemy.ext.compiler import compiles

    @compiles(JSONB, "sqlite")  # type: ignore[misc]
    def _compile_jsonb_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "JSON"

    @compiles(HALFVEC, "sqlite")  # type: ignore[misc]
    def _compile_halfvec_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "TEXT"


_register_sqlite_type_compilers()


@pytest.fixture
async def async_session():
    """Create an in-memory async SQLite database with attribution_records table."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)

    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    await engine.dispose()


class TestAsyncAttributionRepository:
    """Tests for AsyncAttributionRepository."""

    async def test_store_and_retrieve_by_id(self, async_session: AsyncSession) -> None:
        """Round-trip: store → find_by_id returns equivalent record."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()
        record = _make_record()

        stored_id = await repo.store(record, async_session)
        assert stored_id == record.attribution_id

        found = await repo.find_by_id(record.attribution_id, async_session)
        assert found is not None
        assert found.attribution_id == record.attribution_id
        assert found.confidence_score == record.confidence_score
        assert found.version == 1

    async def test_store_and_retrieve_by_work_entity_id(self, async_session: AsyncSession) -> None:
        """Lookup by work_entity_id returns correct record."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()
        work_id = uuid.uuid4()
        record = _make_record(work_entity_id=work_id)

        await repo.store(record, async_session)

        found = await repo.find_by_work_entity_id(work_id, async_session)
        assert found is not None
        assert found.work_entity_id == work_id

    async def test_update_increments_version(self, async_session: AsyncSession) -> None:
        """Update increments version from 1 to 2."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()
        record = _make_record()

        await repo.store(record, async_session)
        await repo.update(record, async_session)

        found = await repo.find_by_id(record.attribution_id, async_session)
        assert found is not None
        assert found.version == 2

    async def test_update_appends_provenance_event(self, async_session: AsyncSession) -> None:
        """Update appends a provenance event to the chain."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()
        record = _make_record()
        assert len(record.provenance_chain) == 0

        await repo.store(record, async_session)
        await repo.update(record, async_session)

        found = await repo.find_by_id(record.attribution_id, async_session)
        assert found is not None
        assert len(found.provenance_chain) == 1
        assert found.provenance_chain[0].event_type == ProvenanceEventTypeEnum.UPDATE

    async def test_find_needs_review(self, async_session: AsyncSession) -> None:
        """find_needs_review returns only records with needs_review=True."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()

        r1 = _make_record(needs_review=True, review_priority=0.9)
        r2 = _make_record(needs_review=False)
        r3 = _make_record(needs_review=True, review_priority=0.3)

        await repo.store(r1, async_session)
        await repo.store(r2, async_session)
        await repo.store(r3, async_session)

        results = await repo.find_needs_review(limit=10, session=async_session)
        assert len(results) == 2
        assert all(r.needs_review for r in results)

    async def test_find_needs_review_respects_limit(self, async_session: AsyncSession) -> None:
        """find_needs_review respects the limit parameter."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()

        for _ in range(5):
            await repo.store(_make_record(needs_review=True), async_session)

        results = await repo.find_needs_review(limit=2, session=async_session)
        assert len(results) == 2

    async def test_list_with_pagination(self, async_session: AsyncSession) -> None:
        """list_all with offset/limit returns correct slice."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()

        for _ in range(5):
            await repo.store(_make_record(), async_session)

        page1 = await repo.list_all(limit=2, offset=0, session=async_session)
        page2 = await repo.list_all(limit=2, offset=2, session=async_session)
        page3 = await repo.list_all(limit=2, offset=4, session=async_session)

        assert len(page1) == 2
        assert len(page2) == 2
        assert len(page3) == 1
        # No overlap between pages
        ids_1 = {r.attribution_id for r in page1}
        ids_2 = {r.attribution_id for r in page2}
        assert ids_1.isdisjoint(ids_2)

    async def test_find_by_id_not_found(self, async_session: AsyncSession) -> None:
        """find_by_id returns None for nonexistent ID."""
        from music_attribution.attribution.persistence import AsyncAttributionRepository

        repo = AsyncAttributionRepository()
        result = await repo.find_by_id(uuid.uuid4(), async_session)
        assert result is None
