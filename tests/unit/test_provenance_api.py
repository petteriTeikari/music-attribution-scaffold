"""Tests for provenance API endpoint (Task 2.0)."""

from __future__ import annotations

import json
import uuid

import httpx
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

    _original_process = HALFVEC.bind_processor

    def _patched_bind_processor(self, dialect):  # noqa: ANN001, ANN202
        if dialect.name == "sqlite":

            def process(value):  # noqa: ANN001, ANN202
                if value is None:
                    return None
                if isinstance(value, list | tuple):
                    return json.dumps([float(v) for v in value])
                return str(value)

            return process
        return _original_process(self, dialect)

    HALFVEC.bind_processor = _patched_bind_processor  # type: ignore[assignment]


_register_sqlite_type_compilers()


async def _create_seeded_app() -> tuple[FastAPI, object]:
    """Create a FastAPI app with seeded database."""
    from music_attribution.api.routes.attribution import router
    from music_attribution.db.models import AttributionRecordModel
    from music_attribution.seed.imogen_heap import seed_imogen_heap

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with factory() as session:
        await seed_imogen_heap(session)
        await session.commit()

    app = FastAPI()
    app.include_router(router)
    app.state.async_session_factory = factory  # type: ignore[attr-defined]

    return app, engine


class TestProvenanceAPI:
    """Tests for GET /attributions/{attribution_id}/provenance."""

    async def test_get_provenance_returns_chain(self) -> None:
        """GET /provenance returns list of ProvenanceEvent with uncertainty."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, engine = await _create_seeded_app()
        try:
            aid = str(deterministic_uuid("work-001"))
            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get(f"/attributions/{aid}/provenance")
                assert resp.status_code == 200
                data = resp.json()
                assert "provenance_chain" in data
                assert isinstance(data["provenance_chain"], list)
                assert len(data["provenance_chain"]) >= 1
        finally:
            await engine.dispose()

    async def test_get_provenance_includes_citations(self) -> None:
        """Response includes citation_index on each event."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, engine = await _create_seeded_app()
        try:
            aid = str(deterministic_uuid("work-001"))
            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get(f"/attributions/{aid}/provenance")
                data = resp.json()
                for event in data["provenance_chain"]:
                    assert "citation_index" in event
                    assert event["citation_index"] is not None
        finally:
            await engine.dispose()

    async def test_get_provenance_includes_uncertainty_summary(self) -> None:
        """Response includes top-level uncertainty summary."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, engine = await _create_seeded_app()
        try:
            aid = str(deterministic_uuid("work-001"))
            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get(f"/attributions/{aid}/provenance")
                data = resp.json()
                assert "uncertainty_summary" in data
                assert data["uncertainty_summary"] is not None
                assert "total_uncertainty" in data["uncertainty_summary"]
        finally:
            await engine.dispose()

    async def test_get_provenance_404_for_unknown_id(self) -> None:
        """Returns 404 for non-existent attribution_id."""
        app, engine = await _create_seeded_app()
        try:
            unknown = str(uuid.uuid4())
            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get(f"/attributions/{unknown}/provenance")
                assert resp.status_code == 404
        finally:
            await engine.dispose()

    async def test_provenance_response_shape_matches_frontend_types(self) -> None:
        """Response JSON shape matches frontend TypeScript types."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, engine = await _create_seeded_app()
        try:
            aid = str(deterministic_uuid("work-001"))
            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get(f"/attributions/{aid}/provenance")
                data = resp.json()
                # Verify expected shape
                assert "provenance_chain" in data
                assert "uncertainty_summary" in data
                assert "attribution_id" in data
                # Verify chain event shape
                event = data["provenance_chain"][0]
                assert "event_type" in event
                assert "timestamp" in event
                assert "agent" in event
                assert "details" in event
                assert "citation_index" in event
        finally:
            await engine.dispose()
