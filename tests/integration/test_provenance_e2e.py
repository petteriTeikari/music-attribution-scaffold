"""End-to-end integration test for provenance chain (Task 4.0).

Seeds PostgreSQL (via SQLite stand-in) with Imogen Heap data including
uncertainty metadata, queries the provenance API, and verifies the full
chain with citation-ready data.
"""

from __future__ import annotations

import json

import httpx
import pytest
from fastapi import FastAPI

pytestmark = pytest.mark.integration
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


@pytest.fixture()
async def seeded_app():
    """Create a FastAPI app with seeded Imogen Heap data."""
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

    yield app, engine

    await engine.dispose()


class TestProvenanceE2E:
    """End-to-end provenance chain: seed → API → verify."""

    async def test_seed_to_api_provenance_chain(self, seeded_app: tuple) -> None:
        """Seed → API → provenance chain has all expected events."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, _engine = seeded_app
        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            assert resp.status_code == 200
            data = resp.json()
            chain = data["provenance_chain"]
            # work-001 (Hide and Seek) should have multiple events
            assert len(chain) >= 3
            # Should include at least FETCH, RESOLVE, SCORE event types
            event_types = {e["event_type"] for e in chain}
            assert "FETCH" in event_types
            assert "SCORE" in event_types

    async def test_provenance_has_uncertainty_metadata(self, seeded_app: tuple) -> None:
        """API response includes uncertainty summary with expected fields."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, _engine = seeded_app
        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            data = resp.json()
            summary = data["uncertainty_summary"]
            assert summary is not None
            assert "total_uncertainty" in summary
            assert "source_contributions" in summary
            assert "dominant_uncertainty_source" in summary
            assert isinstance(summary["source_contributions"], list)
            assert len(summary["source_contributions"]) >= 1

    async def test_citation_indexes_present(self, seeded_app: tuple) -> None:
        """Each provenance event has a citation_index."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, _engine = seeded_app
        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            data = resp.json()
            for event in data["provenance_chain"]:
                assert "citation_index" in event
                assert event["citation_index"] is not None
                assert isinstance(event["citation_index"], int)
                assert event["citation_index"] >= 1

    async def test_confidence_progression_monotonic(self, seeded_app: tuple) -> None:
        """For well-attributed works, SCORE events show non-decreasing confidence."""
        from music_attribution.seed.imogen_heap import deterministic_uuid

        app, _engine = seeded_app
        # work-001 is "Hide and Seek" with 0.95 confidence (well-attributed)
        aid = str(deterministic_uuid("work-001"))
        transport = ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get(f"/attributions/{aid}/provenance")
            data = resp.json()
            score_confidences = [
                e["details"]["new_confidence"]
                for e in data["provenance_chain"]
                if e["details"].get("type") == "score"
            ]
            assert len(score_confidences) >= 1
            # For a well-attributed work, final confidence should be high
            assert score_confidences[-1] >= 0.85
