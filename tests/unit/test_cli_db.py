"""Tests for CLI database management commands."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


@pytest.fixture
async def db_engine():
    """Create an in-memory SQLite database with attribution table."""
    from music_attribution.db.models import AttributionRecordModel

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)

    yield engine
    await engine.dispose()


class TestCliDb:
    """Tests for CLI database commands."""

    async def test_cli_seed_creates_data(self, db_engine) -> None:
        """seed command populates database with Imogen Heap data."""
        from sqlalchemy import func, select
        from sqlalchemy.ext.asyncio import async_sessionmaker

        from music_attribution.cli.db import run_seed
        from music_attribution.db.models import AttributionRecordModel

        factory = async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)

        await run_seed(factory)

        async with factory() as session:
            result = await session.execute(select(func.count()).select_from(AttributionRecordModel))
            count = result.scalar()
            assert count == 8

    async def test_cli_status_shows_counts(self, db_engine) -> None:
        """status command returns table counts."""
        from sqlalchemy.ext.asyncio import async_sessionmaker

        from music_attribution.cli.db import run_seed, run_status

        factory = async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)

        await run_seed(factory)

        status = await run_status(factory)
        assert status["attribution_records"] == 8

    async def test_cli_reset_clears_data(self, db_engine) -> None:
        """reset command clears all data."""
        from sqlalchemy import func, select
        from sqlalchemy.ext.asyncio import async_sessionmaker

        from music_attribution.cli.db import run_reset, run_seed
        from music_attribution.db.models import AttributionRecordModel

        factory = async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)

        await run_seed(factory)
        await run_reset(factory)

        async with factory() as session:
            result = await session.execute(select(func.count()).select_from(AttributionRecordModel))
            count = result.scalar()
            assert count == 0
