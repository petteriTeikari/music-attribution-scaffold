"""Tests for embedding generation service with database persistence."""

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

    # Override HALFVEC bind processor for SQLite: serialize as JSON string
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
    """Create an in-memory async SQLite database with required tables."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    from music_attribution.db.models import EntityEmbeddingModel, ResolvedEntityModel

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(ResolvedEntityModel.__table__.create)
        await conn.run_sync(EntityEmbeddingModel.__table__.create)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with factory() as session:
        yield session

    await engine.dispose()


def _seed_entity(session: AsyncSession, entity_id: uuid.UUID, name: str) -> None:
    """Insert a minimal resolved entity into the database."""
    import json
    from datetime import UTC, datetime

    from music_attribution.db.models import ResolvedEntityModel

    entity = ResolvedEntityModel(
        entity_id=entity_id,
        entity_type="ARTIST",
        canonical_name=name,
        alternative_names=json.dumps([]),
        identifiers=json.dumps({}),
        source_records=json.dumps([{"source": "test", "record_id": "r1"}]),
        resolution_method="test",
        resolution_confidence=0.9,
        resolution_details=json.dumps({}),
        assurance_level="LEVEL_2",
        conflicts=json.dumps([]),
        needs_review=False,
        resolved_at=datetime.now(UTC),
    )
    session.add(entity)


class TestEmbeddingService:
    """Tests for EmbeddingService database operations."""

    async def test_generate_embedding_returns_vector(self) -> None:
        """Generate embedding returns a 768-dimensional vector."""
        from music_attribution.resolution.embedding_service import EmbeddingService

        service = EmbeddingService()
        embedding = service.generate_embedding("Imogen Heap")
        # all-MiniLM-L6-v2 produces 384-dimensional vectors
        assert len(embedding) == 384
        assert all(isinstance(v, float) for v in embedding)

    async def test_embedding_text_format(self) -> None:
        """Entity text format includes name, type, and metadata."""
        from music_attribution.resolution.embedding_service import EmbeddingService

        service = EmbeddingService()
        text = service.format_entity_text(
            canonical_name="Imogen Heap",
            entity_type="ARTIST",
            alternative_names=["Imogen Jennifer Jane Heap"],
        )
        assert "Imogen Heap" in text
        assert "ARTIST" in text
        assert "Imogen Jennifer Jane Heap" in text

    async def test_store_embedding_in_db(self, async_session: AsyncSession) -> None:
        """Round-trip: store embedding in entity_embeddings, retrieve it."""
        from sqlalchemy import select

        from music_attribution.db.models import EntityEmbeddingModel
        from music_attribution.resolution.embedding_service import EmbeddingService

        entity_id = uuid.uuid4()
        _seed_entity(async_session, entity_id, "Test Artist")
        await async_session.flush()

        service = EmbeddingService()
        embedding = service.generate_embedding("Test Artist")

        await service.store_embedding(
            entity_id=entity_id,
            embedding=embedding,
            session=async_session,
        )
        await async_session.flush()

        result = await async_session.execute(
            select(EntityEmbeddingModel).where(
                EntityEmbeddingModel.entity_id == entity_id,
            )
        )
        model = result.scalar_one()
        assert model.model_name == "all-MiniLM-L6-v2"
        assert model.entity_id == entity_id

    async def test_model_name_and_version_stored(self, async_session: AsyncSession) -> None:
        """Model name and version are stored for reproducibility."""
        from sqlalchemy import select

        from music_attribution.db.models import EntityEmbeddingModel
        from music_attribution.resolution.embedding_service import EmbeddingService

        entity_id = uuid.uuid4()
        _seed_entity(async_session, entity_id, "Version Test")
        await async_session.flush()

        service = EmbeddingService()
        embedding = service.generate_embedding("Version Test")
        await service.store_embedding(entity_id, embedding, session=async_session)
        await async_session.flush()

        result = await async_session.execute(
            select(EntityEmbeddingModel).where(
                EntityEmbeddingModel.entity_id == entity_id,
            )
        )
        model = result.scalar_one()
        assert model.model_name == "all-MiniLM-L6-v2"
        assert model.model_version is not None
        assert len(model.model_version) > 0

    async def test_skip_existing_embeddings(self, async_session: AsyncSession) -> None:
        """Storing same entity twice doesn't create duplicates."""
        from sqlalchemy import func, select

        from music_attribution.db.models import EntityEmbeddingModel
        from music_attribution.resolution.embedding_service import EmbeddingService

        entity_id = uuid.uuid4()
        _seed_entity(async_session, entity_id, "Skip Test")
        await async_session.flush()

        service = EmbeddingService()
        embedding = service.generate_embedding("Skip Test")

        await service.store_embedding(entity_id, embedding, session=async_session)
        await async_session.flush()

        # Store again — should be idempotent
        await service.store_embedding(entity_id, embedding, session=async_session)
        await async_session.flush()

        result = await async_session.execute(
            select(func.count()).select_from(EntityEmbeddingModel).where(
                EntityEmbeddingModel.entity_id == entity_id,
            )
        )
        assert result.scalar() == 1
