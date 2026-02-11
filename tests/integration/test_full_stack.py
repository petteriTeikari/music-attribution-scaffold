"""Full-stack integration tests: FastAPI → SQLite → seed data → API responses.

Verifies the complete data flow from HTTP request through the API layer
to the database and back. Uses SQLite for fast CI without Docker.
Mark with @pytest.mark.integration for selective running.
"""

from __future__ import annotations

import json

import httpx
import pytest
from fastapi import FastAPI
from httpx import ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


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

pytestmark = pytest.mark.integration


@pytest.fixture
async def test_client():
    """Create a FastAPI test client backed by a seeded SQLite database."""
    from datetime import UTC, datetime

    from music_attribution.api.routes.attribution import router as attribution_router
    from music_attribution.api.routes.permissions import router as permissions_router
    from music_attribution.db.models import (
        AttributionRecordModel,
        AuditLogModel,
        EdgeModel,
        EntityEmbeddingModel,
        PermissionBundleModel,
        ResolvedEntityModel,
    )
    from music_attribution.seed.imogen_heap import deterministic_uuid, seed_imogen_heap

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)
        await conn.run_sync(ResolvedEntityModel.__table__.create)
        await conn.run_sync(PermissionBundleModel.__table__.create)
        await conn.run_sync(AuditLogModel.__table__.create)
        await conn.run_sync(EntityEmbeddingModel.__table__.create)
        await conn.run_sync(EdgeModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with factory() as session:
        # Seed attribution records
        await seed_imogen_heap(session)

        # Seed resolved entity for Imogen Heap (needed for permission FK)
        ih_id = deterministic_uuid("artist-imogen-heap")
        entity = ResolvedEntityModel(
            entity_id=ih_id,
            entity_type="ARTIST",
            canonical_name="Imogen Heap",
            alternative_names=json.dumps([]),
            identifiers=json.dumps({}),
            source_records=json.dumps([{"source": "test", "record_id": str(ih_id)}]),
            resolution_method="test",
            resolution_confidence=0.9,
            resolution_details=json.dumps({}),
            assurance_level="LEVEL_3",
            conflicts=json.dumps([]),
            needs_review=False,
            resolved_at=datetime.now(UTC),
        )
        session.add(entity)

        # Seed permission bundle: streaming=ALLOW, voice_cloning=DENY
        perm_bundle = PermissionBundleModel(
            entity_id=ih_id,
            scope="CATALOG",
            permissions=json.dumps(
                [
                    {"permission_type": "STREAM", "value": "ALLOW", "conditions": []},
                    {"permission_type": "VOICE_CLONING", "value": "DENY", "conditions": []},
                    {"permission_type": "AI_TRAINING", "value": "ASK", "conditions": []},
                ]
            ),
            effective_from=datetime.now(UTC),
            delegation_chain=json.dumps([]),
            default_permission="ASK",
            created_by=ih_id,
            updated_at=datetime.now(UTC),
            version=1,
        )
        session.add(perm_bundle)
        await session.commit()

    # Create FastAPI app with both routers
    app = FastAPI()
    app.include_router(attribution_router)
    app.include_router(permissions_router)
    app.state.async_session_factory = factory

    # Add health endpoint
    @app.get("/health")
    async def health() -> dict:
        return {"status": "healthy"}

    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

    await engine.dispose()


class TestFullStackIntegration:
    """Full-stack integration tests: API → Database → Response."""

    async def test_health_endpoint(self, test_client: httpx.AsyncClient) -> None:
        """/health returns 200."""
        resp = await test_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "healthy"

    async def test_list_works_returns_8(self, test_client: httpx.AsyncClient) -> None:
        """/attributions/ returns 8 Imogen Heap works."""
        resp = await test_client.get("/attributions/", params={"limit": 50})
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 8

    async def test_get_work_hide_and_seek(self, test_client: httpx.AsyncClient) -> None:
        """Hide and Seek: confidence 0.95, assurance LEVEL_3."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        work_id = str(deterministic_uuid("work-hide-and-seek"))
        resp = await test_client.get(f"/attributions/work/{work_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["confidence_score"] == 0.95
        assert data["assurance_level"] == "LEVEL_3"

    async def test_sort_by_confidence_desc(self, test_client: httpx.AsyncClient) -> None:
        """Works are ordered by confidence score descending."""
        resp = await test_client.get("/attributions/", params={"limit": 50})
        data = resp.json()
        scores = [w["confidence_score"] for w in data]
        assert scores == sorted(scores, reverse=True)

    async def test_filter_needs_review(self, test_client: httpx.AsyncClient) -> None:
        """needs_review=true returns works that need review."""
        resp = await test_client.get("/attributions/", params={"needs_review": "true", "limit": 50})
        data = resp.json()
        # Headlock (0.58), Just for Now (0.35), 2-1 (0.28), Blanket (0.0)
        assert len(data) == 4
        for work in data:
            assert work["needs_review"] is True

    async def test_permission_check_streaming(self, test_client: httpx.AsyncClient) -> None:
        """Streaming permission for Imogen Heap returns ALLOW."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        ih_id = str(deterministic_uuid("artist-imogen-heap"))
        resp = await test_client.post(
            "/permissions/check",
            json={"entity_id": ih_id, "permission_type": "STREAM"},
        )
        assert resp.status_code == 200
        assert resp.json()["result"] == "ALLOW"

    async def test_permission_check_voice_cloning(self, test_client: httpx.AsyncClient) -> None:
        """Voice cloning permission for Imogen Heap returns DENY."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        ih_id = str(deterministic_uuid("artist-imogen-heap"))
        resp = await test_client.post(
            "/permissions/check",
            json={"entity_id": ih_id, "permission_type": "VOICE_CLONING"},
        )
        assert resp.status_code == 200
        assert resp.json()["result"] == "DENY"

    async def test_search_works(self, test_client: httpx.AsyncClient) -> None:
        """Search for 'vocoder' returns results including Hide and Seek."""
        resp = await test_client.get("/attributions/search", params={"q": "vocoder"})
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) >= 1
        # Hide and Seek has role_detail "Lead vocals, vocoder arrangement"
        attr_ids = [r["attribution"]["attribution_id"] for r in data]
        from music_attribution.seed.imogen_heap import deterministic_uuid

        hide_seek_id = str(deterministic_uuid("work-001"))
        assert hide_seek_id in attr_ids
