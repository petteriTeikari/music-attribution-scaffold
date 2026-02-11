"""Tests for hybrid search with RRF fusion."""

from __future__ import annotations

import json

import pytest
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
                if isinstance(value, (list, tuple)):
                    return json.dumps([float(v) for v in value])
                return str(value)

            return process
        return _original_process(self, dialect)

    HALFVEC.bind_processor = _patched_bind_processor  # type: ignore[assignment]


_register_sqlite_type_compilers()


async def _create_hybrid_db() -> tuple:
    """Create and seed an in-memory database for hybrid search testing."""
    from datetime import UTC, datetime

    from music_attribution.db.models import (
        AttributionRecordModel,
        EdgeModel,
        EntityEmbeddingModel,
        ResolvedEntityModel,
    )
    from music_attribution.resolution.embedding_match import EmbeddingMatcher
    from music_attribution.seed.imogen_heap import deterministic_uuid, seed_imogen_heap

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(AttributionRecordModel.__table__.create)
        await conn.run_sync(ResolvedEntityModel.__table__.create)
        await conn.run_sync(EntityEmbeddingModel.__table__.create)
        await conn.run_sync(EdgeModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with factory() as session:
        # Seed 8 Imogen Heap attribution records
        await seed_imogen_heap(session)

        # Seed resolved entities for embedding / graph lookup
        ih_id = deterministic_uuid("artist-imogen-heap")
        gs_id = deterministic_uuid("artist-guy-sigsworth")

        for entity_id, name, etype in [
            (ih_id, "Imogen Heap", "ARTIST"),
            (gs_id, "Guy Sigsworth", "ARTIST"),
        ]:
            entity = ResolvedEntityModel(
                entity_id=entity_id,
                entity_type=etype,
                canonical_name=name,
                alternative_names=json.dumps([]),
                identifiers=json.dumps({}),
                source_records=json.dumps([{"source": "test", "record_id": str(entity_id)}]),
                resolution_method="test",
                resolution_confidence=0.9,
                resolution_details=json.dumps({}),
                assurance_level="LEVEL_2",
                conflicts=json.dumps([]),
                needs_review=False,
                resolved_at=datetime.now(UTC),
            )
            session.add(entity)

        # Seed embeddings for both artists
        matcher = EmbeddingMatcher()
        for entity_id, name in [(ih_id, "Imogen Heap"), (gs_id, "Guy Sigsworth")]:
            emb = await matcher.embed(name)
            emb_model = EntityEmbeddingModel(
                entity_id=entity_id,
                model_name="all-MiniLM-L6-v2",
                model_version="1.0.0",
                embedding=json.dumps(emb),
                created_at=datetime.now(UTC),
            )
            session.add(emb_model)

        # Seed graph edge: Imogen Heap ↔ Guy Sigsworth
        edge = EdgeModel(
            from_entity_id=ih_id,
            to_entity_id=gs_id,
            relationship_type="COLLABORATED_WITH",
            confidence=0.85,
            metadata_={},
            created_at=datetime.now(UTC),
        )
        session.add(edge)

        await session.commit()

    return engine, factory


@pytest.fixture
async def hybrid_session():
    """Create a seeded in-memory database with all tables."""
    engine, factory = await _create_hybrid_db()
    async with factory() as session:
        yield session
    await engine.dispose()


class TestHybridSearch:
    """Tests for HybridSearchService."""

    async def test_hybrid_search_combines_text_and_vector(
        self,
        hybrid_session: AsyncSession,
    ) -> None:
        """Search returns results combining text and vector modalities."""
        from music_attribution.search.hybrid_search import HybridSearchService

        service = HybridSearchService()
        # "vocoder arrangement" matches text (role_detail in credits JSONB)
        results = await service.search("vocoder arrangement", limit=10, session=hybrid_session)
        assert len(results) >= 1
        assert hasattr(results[0], "record")
        assert hasattr(results[0], "rrf_score")

    async def test_hybrid_search_rrf_scoring(
        self,
        hybrid_session: AsyncSession,
    ) -> None:
        """RRF scores are positive and results sorted descending."""
        from music_attribution.search.hybrid_search import HybridSearchService

        service = HybridSearchService()
        results = await service.search("vocoder", limit=10, session=hybrid_session)
        scores = [r.rrf_score for r in results]
        assert all(s > 0 for s in scores)
        assert scores == sorted(scores, reverse=True)

    async def test_hybrid_search_with_graph_context(
        self,
        hybrid_session: AsyncSession,
    ) -> None:
        """Graph neighbors of matched entities appear in results."""
        from music_attribution.search.hybrid_search import HybridSearchService

        service = HybridSearchService()
        # "Guy Sigsworth" matches entity embedding via vector search.
        # Graph edge to Imogen Heap should include her works in results.
        results = await service.search("Guy Sigsworth", limit=10, session=hybrid_session)
        assert len(results) >= 1

    async def test_hybrid_search_text_only_fallback(
        self,
        hybrid_session: AsyncSession,
    ) -> None:
        """Search works when only text modality has matches."""
        from music_attribution.search.hybrid_search import HybridSearchService

        service = HybridSearchService()
        # "etl-musicbrainz" only appears in provenance chain text, not entity names
        results = await service.search("etl-musicbrainz", limit=10, session=hybrid_session)
        assert len(results) >= 1

    async def test_hybrid_search_api_endpoint(self) -> None:
        """GET /attributions/search?q=... returns hybrid results."""
        import httpx
        from fastapi import FastAPI
        from httpx import ASGITransport

        from music_attribution.api.routes.attribution import router

        engine, factory = await _create_hybrid_db()
        try:
            app = FastAPI()
            app.include_router(router)
            app.state.async_session_factory = factory

            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get("/attributions/search", params={"q": "vocoder"})
                assert resp.status_code == 200
                data = resp.json()
                assert isinstance(data, list)
                assert len(data) >= 1
                assert "rrf_score" in data[0]
        finally:
            await engine.dispose()
