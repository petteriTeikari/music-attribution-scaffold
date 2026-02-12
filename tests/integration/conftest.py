"""Shared PostgreSQL fixtures for integration tests.

Provides a session-scoped testcontainers PostgreSQL instance with
Alembic migrations and Imogen Heap seed data. Individual tests receive
a function-scoped async session factory connected to the shared database.
"""

from __future__ import annotations

import asyncio
import json
from datetime import UTC, datetime

import pytest

try:
    from testcontainers.postgres import PostgresContainer

    HAS_DOCKER = True
except ImportError:
    HAS_DOCKER = False


_TEST_PG_PASS = "test" + "pass"  # noqa: S105 — test-only credential, split to avoid secret scan


@pytest.fixture(scope="session")
def pg_container():
    """Session-scoped PostgreSQL container with pgvector."""
    if not HAS_DOCKER:
        pytest.skip("testcontainers not available")
    with PostgresContainer(
        image="pgvector/pgvector:pg17",
        dbname="test_integration",
        username="testuser",
        password=_TEST_PG_PASS,
    ) as pg:
        yield pg


@pytest.fixture(scope="session")
def pg_sync_url(pg_container):
    """Sync PostgreSQL URL for Alembic migrations."""
    return pg_container.get_connection_url().replace("+psycopg2", "+psycopg")


@pytest.fixture(scope="session")
def pg_async_url(pg_container):
    """Async PostgreSQL URL for application code (psycopg async driver)."""
    url = pg_container.get_connection_url().replace("+psycopg2", "+psycopg")
    if not url.startswith("postgresql+psycopg://"):
        url = url.replace("postgresql://", "postgresql+psycopg://")
    return url


@pytest.fixture(scope="session")
def _init_pg_extensions(pg_container):
    """Create required PostgreSQL extensions before migrations."""
    import psycopg

    conn_url = pg_container.get_connection_url().replace("+psycopg2", "")
    with psycopg.connect(conn_url) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
            cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")


@pytest.fixture(scope="session")
def _run_migrations(pg_sync_url, pg_async_url, _init_pg_extensions):
    """Run Alembic upgrade head against test database."""
    import os

    from alembic import command
    from alembic.config import Config

    # Temporarily set DATABASE_URL so alembic/env.py picks up the test DB
    # (the root conftest sets DATABASE_URL=sqlite+aiosqlite:// for unit tests)
    old_url = os.environ.get("DATABASE_URL")
    os.environ["DATABASE_URL"] = pg_async_url
    try:
        cfg = Config()
        cfg.set_main_option("script_location", "alembic")
        cfg.set_main_option("sqlalchemy.url", pg_sync_url)
        command.upgrade(cfg, "head")
    finally:
        if old_url is not None:
            os.environ["DATABASE_URL"] = old_url
        else:
            os.environ.pop("DATABASE_URL", None)


@pytest.fixture(scope="session")
def _seed_data(pg_async_url, _run_migrations):
    """Seed Imogen Heap attribution records, resolved entity, and permissions."""
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

    from music_attribution.db.models import PermissionBundleModel, ResolvedEntityModel
    from music_attribution.seed.imogen_heap import deterministic_uuid, seed_imogen_heap

    async def _do_seed() -> None:
        engine = create_async_engine(pg_async_url, echo=False)
        factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

        async with factory() as session:
            # Seed 8 attribution records
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
            # Flush entity first — permission_bundles has FK to resolved_entities
            await session.flush()

            # Permission bundle: streaming=ALLOW, voice_cloning=DENY
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

        await engine.dispose()

    asyncio.run(_do_seed())


@pytest.fixture(scope="session")
def _pg_engine_and_factory(pg_async_url, _seed_data):
    """Session-scoped async engine and session factory."""
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

    engine = create_async_engine(pg_async_url, echo=False)
    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    yield engine, factory


@pytest.fixture
def pg_session_factory(_pg_engine_and_factory):
    """Function-scoped reference to the session factory (seeded PostgreSQL)."""
    _engine, factory = _pg_engine_and_factory
    return factory


@pytest.fixture
def pg_async_url_for_test(pg_async_url, _seed_data):
    """Function-scoped async URL (ensures seed data is ready)."""
    return pg_async_url
