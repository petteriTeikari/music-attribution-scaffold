"""Tests for database-backed attribution API routes."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


@pytest.fixture
async def seeded_app():
    """Create a FastAPI app with SQLite backend seeded with Imogen Heap data."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    from music_attribution.api.app import create_app
    from music_attribution.db.models import AttributionRecordModel
    from music_attribution.seed.imogen_heap import seed_imogen_heap

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    # Seed data
    async with factory() as session:
        await seed_imogen_heap(session)
        await session.commit()

    # Create app and override state
    app = create_app()
    app.state.async_engine = engine
    app.state.async_session_factory = factory

    yield app

    await engine.dispose()


@pytest.fixture
def client(seeded_app):
    """Create a test client from the seeded app."""
    from httpx import ASGITransport, AsyncClient

    return AsyncClient(transport=ASGITransport(app=seeded_app), base_url="http://test")


class TestDbBackedAttributionRoutes:
    """Tests for attribution routes backed by database."""

    async def test_get_work_by_id_returns_attribution(self, client) -> None:
        """Existing endpoint returns attribution from database."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        # work_entity_id for "Hide and Seek"
        hide_and_seek_id = deterministic_uuid("work-hide-and-seek")

        async with client:
            response = await client.get(f"/api/v1/attributions/work/{hide_and_seek_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["confidence_score"] == 0.95

    async def test_get_work_by_id_404_not_found(self, client) -> None:
        """Missing work returns 404."""
        import uuid

        fake_id = uuid.uuid4()

        async with client:
            response = await client.get(f"/api/v1/attributions/work/{fake_id}")

        assert response.status_code == 404

    async def test_list_attributions_paginated(self, client) -> None:
        """List endpoint returns paginated results from database."""
        async with client:
            response = await client.get("/api/v1/attributions/?limit=3&offset=0")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3

    async def test_list_attributions_sorted_by_confidence(self, client) -> None:
        """Default sort is by confidence descending."""
        async with client:
            response = await client.get("/api/v1/attributions/?limit=8")

        assert response.status_code == 200
        data = response.json()
        scores = [r["confidence_score"] for r in data]
        assert scores == sorted(scores, reverse=True)

    async def test_filter_needs_review(self, client) -> None:
        """Filter by needs_review=true returns only flagged records."""
        async with client:
            response = await client.get("/api/v1/attributions/?needs_review=true")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        # All returned records should have needs_review=True
        for record in data:
            assert record["needs_review"] is True

    async def test_filter_by_assurance_level(self, client) -> None:
        """Filter by assurance level returns matching records."""
        async with client:
            response = await client.get("/api/v1/attributions/?assurance_level=LEVEL_3")

        assert response.status_code == 200
        data = response.json()
        for record in data:
            assert record["assurance_level"] == "LEVEL_3"

    async def test_response_includes_provenance(self, client) -> None:
        """Response includes provenance_chain for each record."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        # work_entity_id for "Hide and Seek"
        hide_and_seek_id = deterministic_uuid("work-hide-and-seek")

        async with client:
            response = await client.get(f"/api/v1/attributions/work/{hide_and_seek_id}")

        assert response.status_code == 200
        data = response.json()
        assert "provenance_chain" in data
        assert len(data["provenance_chain"]) == 6
