"""Tests for text search service."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


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
async def seeded_session():
    """Create a seeded in-memory database."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    from music_attribution.db.models import AttributionRecordModel
    from music_attribution.seed.imogen_heap import seed_imogen_heap

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with factory() as session:
        await seed_imogen_heap(session)
        await session.commit()

    async with factory() as session:
        yield session

    await engine.dispose()


class TestTextSearch:
    """Tests for TextSearchService."""

    async def test_search_by_role_detail(self, seeded_session: AsyncSession) -> None:
        """Search for 'vocoder arrangement' returns Hide and Seek (role_detail match)."""
        from music_attribution.search.text_search import TextSearchService

        service = TextSearchService()
        results = await service.search("vocoder arrangement", session=seeded_session)
        assert len(results) >= 1
        assert any(r.confidence_score == 0.95 for r in results)

    async def test_search_by_agent_name(self, seeded_session: AsyncSession) -> None:
        """Search for agent name in provenance chain returns results."""
        from music_attribution.search.text_search import TextSearchService

        service = TextSearchService()
        results = await service.search("etl-musicbrainz", session=seeded_session)
        assert len(results) >= 1

    async def test_search_no_results(self, seeded_session: AsyncSession) -> None:
        """Search for nonexistent term returns empty list."""
        from music_attribution.search.text_search import TextSearchService

        service = TextSearchService()
        results = await service.search("nonexistent_xyz_query", session=seeded_session)
        assert len(results) == 0

    async def test_search_with_pagination(self, seeded_session: AsyncSession) -> None:
        """Search respects limit parameter."""
        from music_attribution.search.text_search import TextSearchService

        service = TextSearchService()
        results = await service.search("", limit=3, session=seeded_session)
        assert len(results) <= 3

    async def test_search_returns_attribution_records(self, seeded_session: AsyncSession) -> None:
        """Search results are AttributionRecord instances."""
        from music_attribution.schemas.attribution import AttributionRecord
        from music_attribution.search.text_search import TextSearchService

        service = TextSearchService()
        results = await service.search("", limit=1, session=seeded_session)
        assert len(results) == 1
        assert isinstance(results[0], AttributionRecord)
