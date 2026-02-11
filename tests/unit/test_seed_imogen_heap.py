"""Tests for Imogen Heap seed data loader."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from music_attribution.db.models import AttributionRecordModel


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
    """Create an in-memory async SQLite database with attribution table."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)

    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    await engine.dispose()


class TestSeedImogenHeap:
    """Tests for seed_imogen_heap loader."""

    async def test_seed_creates_8_records(self, async_session: AsyncSession) -> None:
        """Seed creates exactly 8 attribution records matching mock data."""
        from sqlalchemy import func, select

        from music_attribution.seed.imogen_heap import seed_imogen_heap

        await seed_imogen_heap(async_session)

        result = await async_session.execute(select(func.count()).select_from(AttributionRecordModel))
        count = result.scalar()
        assert count == 8

    async def test_confidence_scores_match(self, async_session: AsyncSession) -> None:
        """Confidence scores match the mock data exactly."""
        from sqlalchemy import select

        from music_attribution.seed.imogen_heap import seed_imogen_heap

        await seed_imogen_heap(async_session)

        result = await async_session.execute(
            select(AttributionRecordModel.confidence_score).order_by(AttributionRecordModel.confidence_score.desc())
        )
        scores = [row[0] for row in result.all()]
        expected = [0.95, 0.91, 0.82, 0.72, 0.58, 0.35, 0.28, 0.0]
        assert scores == expected

    async def test_idempotent(self, async_session: AsyncSession) -> None:
        """Running seed twice doesn't duplicate records."""
        from sqlalchemy import func, select

        from music_attribution.seed.imogen_heap import seed_imogen_heap

        await seed_imogen_heap(async_session)
        await seed_imogen_heap(async_session)

        result = await async_session.execute(select(func.count()).select_from(AttributionRecordModel))
        count = result.scalar()
        assert count == 8

    async def test_deterministic_uuids(self) -> None:
        """UUIDs are deterministic (same seed produces same IDs)."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        uuid1 = deterministic_uuid("work-001")
        uuid2 = deterministic_uuid("work-001")
        assert uuid1 == uuid2

        # Different inputs produce different UUIDs
        uuid3 = deterministic_uuid("work-002")
        assert uuid1 != uuid3

    async def test_provenance_chains_preserved(self, async_session: AsyncSession) -> None:
        """Provenance chains are stored with event details."""
        import json

        from sqlalchemy import select

        from music_attribution.seed.imogen_heap import deterministic_uuid, seed_imogen_heap

        await seed_imogen_heap(async_session)

        # Hide and Seek has 6 provenance events
        work_001_id = deterministic_uuid("work-001")
        result = await async_session.execute(
            select(AttributionRecordModel).where(AttributionRecordModel.attribution_id == work_001_id)
        )
        record = result.scalar_one()
        chain = record.provenance_chain
        if isinstance(chain, str):
            chain = json.loads(chain)
        assert len(chain) == 6
