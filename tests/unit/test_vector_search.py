"""Tests for vector similarity search service."""

from __future__ import annotations

import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


def _register_sqlite_type_compilers() -> None:
    """Register JSONB and HALFVEC compilation for SQLite dialect (test-only)."""
    import json

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


@pytest.fixture
async def async_session():
    """Create an in-memory SQLite database with required tables."""
    import json
    from datetime import UTC, datetime

    from sqlalchemy.ext.asyncio import async_sessionmaker

    from music_attribution.db.models import EntityEmbeddingModel, ResolvedEntityModel
    from music_attribution.resolution.embedding_match import EmbeddingMatcher

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(ResolvedEntityModel.__table__.create)
        await conn.run_sync(EntityEmbeddingModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    # Seed 3 entities with embeddings
    matcher = EmbeddingMatcher()
    names = [
        ("entity-a", "Imogen Heap", "ARTIST"),
        ("entity-b", "Frou Frou", "ARTIST"),
        ("entity-c", "Hide and Seek", "WORK"),
    ]

    async with factory() as session:
        for key, name, etype in names:
            eid = uuid.uuid5(uuid.NAMESPACE_DNS, key)
            entity = ResolvedEntityModel(
                entity_id=eid,
                entity_type=etype,
                canonical_name=name,
                alternative_names=json.dumps([]),
                identifiers=json.dumps({}),
                source_records=json.dumps([{"source": "test", "record_id": key}]),
                resolution_method="test",
                resolution_confidence=0.9,
                resolution_details=json.dumps({}),
                assurance_level="LEVEL_2",
                conflicts=json.dumps([]),
                needs_review=False,
                resolved_at=datetime.now(UTC),
            )
            session.add(entity)

            emb = await matcher.embed(name)
            emb_model = EntityEmbeddingModel(
                entity_id=eid,
                model_name="all-MiniLM-L6-v2",
                model_version="1.0.0",
                embedding=json.dumps(emb),
                created_at=datetime.now(UTC),
            )
            session.add(emb_model)

        await session.commit()

    async with factory() as session:
        yield session

    await engine.dispose()


class TestVectorSearch:
    """Tests for VectorSearchService."""

    async def test_find_similar_entities(self, async_session: AsyncSession) -> None:
        """Query returns neighbors ranked by cosine similarity."""
        from music_attribution.search.vector_search import VectorSearchService

        service = VectorSearchService()
        query_id = uuid.uuid5(uuid.NAMESPACE_DNS, "entity-a")
        results = await service.find_similar(query_id, limit=5, session=async_session)
        assert len(results) >= 1

    async def test_similarity_score_range(self, async_session: AsyncSession) -> None:
        """Similarity scores are between 0 and 1."""
        from music_attribution.search.vector_search import VectorSearchService

        service = VectorSearchService()
        query_id = uuid.uuid5(uuid.NAMESPACE_DNS, "entity-a")
        results = await service.find_similar(query_id, limit=5, session=async_session)
        for _, score in results:
            assert 0.0 <= score <= 1.0

    async def test_find_similar_excludes_self(self, async_session: AsyncSession) -> None:
        """Queried entity is not in results."""
        from music_attribution.search.vector_search import VectorSearchService

        service = VectorSearchService()
        query_id = uuid.uuid5(uuid.NAMESPACE_DNS, "entity-a")
        results = await service.find_similar(query_id, limit=5, session=async_session)
        result_ids = {eid for eid, _ in results}
        assert query_id not in result_ids

    async def test_find_similar_with_threshold(self, async_session: AsyncSession) -> None:
        """Filter by minimum similarity threshold."""
        from music_attribution.search.vector_search import VectorSearchService

        service = VectorSearchService()
        query_id = uuid.uuid5(uuid.NAMESPACE_DNS, "entity-a")
        results = await service.find_similar(
            query_id, limit=5, threshold=0.5, session=async_session,
        )
        for _, score in results:
            assert score >= 0.5

    async def test_find_similar_with_type_filter(self, async_session: AsyncSession) -> None:
        """Restrict results to same entity type."""
        from music_attribution.search.vector_search import VectorSearchService

        service = VectorSearchService()
        query_id = uuid.uuid5(uuid.NAMESPACE_DNS, "entity-a")
        results = await service.find_similar(
            query_id, limit=5, entity_type="ARTIST", session=async_session,
        )
        # Should only contain ARTIST-type entities, not WORK
        for eid, _ in results:
            assert eid != uuid.uuid5(uuid.NAMESPACE_DNS, "entity-c")
