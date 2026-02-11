"""Verify Alembic migrations against real PostgreSQL (Task 0.1).

Tests that migrations run cleanly on pgvector/pgvector:pg17,
extensions are enabled, all tables exist, and seed data inserts
correctly. Uses testcontainers for Docker-managed PostgreSQL.
"""

from __future__ import annotations

import pytest

try:
    from testcontainers.postgres import PostgresContainer

    HAS_DOCKER = True
except ImportError:
    HAS_DOCKER = False

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(not HAS_DOCKER, reason="testcontainers not available"),
]


@pytest.fixture(scope="module")
def postgres_container():
    """Spin up PostgreSQL with pgvector for migration testing."""
    with PostgresContainer(
        image="pgvector/pgvector:pg17",
        dbname="test_migration_verify",
        username="testuser",
        password="testpass",
    ) as pg:
        yield pg


@pytest.fixture(scope="module")
def _init_extensions(postgres_container):
    """Create required PostgreSQL extensions before migrations."""
    import psycopg

    conn_url = postgres_container.get_connection_url().replace("+psycopg2", "")
    with psycopg.connect(conn_url) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
            cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")


@pytest.fixture
def alembic_cfg(postgres_container, _init_extensions):
    """Create Alembic config pointing to test database."""
    from alembic.config import Config

    conn_url = postgres_container.get_connection_url().replace("+psycopg2", "+psycopg")
    cfg = Config()
    cfg.set_main_option("script_location", "alembic")
    cfg.set_main_option("sqlalchemy.url", conn_url)
    return cfg


class TestMigrationsRealPG:
    """Verify Alembic migrations on real PostgreSQL with pgvector."""

    def test_alembic_upgrade_head_succeeds(self, alembic_cfg) -> None:
        """alembic upgrade head completes without error on real PostgreSQL."""
        from alembic import command

        command.upgrade(alembic_cfg, "head")

    def test_all_tables_created(self, alembic_cfg, postgres_container) -> None:
        """All expected tables exist after migration."""
        import psycopg
        from alembic import command

        command.upgrade(alembic_cfg, "head")

        conn_url = postgres_container.get_connection_url().replace("+psycopg2", "")
        with psycopg.connect(conn_url) as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT table_name FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name NOT LIKE 'alembic_%'
                ORDER BY table_name
            """)
            tables = {row[0] for row in cur.fetchall()}

        expected = {
            "attribution_records",
            "resolved_entities",
            "entity_embeddings",
            "edges",
            "permission_bundles",
            "feedback_cards",
            "audit_log",
            "normalized_records",
        }
        for table in expected:
            assert table in tables, f"Missing table: {table}"

    def test_pgvector_extension_enabled(self, alembic_cfg, postgres_container) -> None:
        """pgvector extension is available on the PostgreSQL instance."""
        import psycopg
        from alembic import command

        command.upgrade(alembic_cfg, "head")

        conn_url = postgres_container.get_connection_url().replace("+psycopg2", "")
        with psycopg.connect(conn_url) as conn, conn.cursor() as cur:
            cur.execute("SELECT extname FROM pg_extension WHERE extname = 'vector'")
            row = cur.fetchone()
        assert row is not None, "pgvector extension not enabled"
        assert row[0] == "vector"

    def test_seed_data_insertable(self, alembic_cfg, postgres_container) -> None:
        """Imogen Heap seed data inserts successfully into real PostgreSQL."""
        import asyncio

        from alembic import command
        from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

        from music_attribution.seed.imogen_heap import seed_imogen_heap

        command.upgrade(alembic_cfg, "head")

        async_url = (
            postgres_container.get_connection_url()
            .replace("+psycopg2", "+psycopg")
            .replace("postgresql://", "postgresql+psycopg://")
        )
        # Ensure async driver prefix
        if not async_url.startswith("postgresql+psycopg://"):
            async_url = async_url.replace("postgresql://", "postgresql+psycopg://")

        async def _seed_and_verify() -> int:
            engine = create_async_engine(async_url, echo=False)
            factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
            async with factory() as session:
                await seed_imogen_heap(session)
                await session.commit()
            # Verify records exist
            async with factory() as session:
                from sqlalchemy import text

                result = await session.execute(text("SELECT COUNT(*) FROM attribution_records"))
                count = result.scalar_one()
            await engine.dispose()
            return count

        count = asyncio.run(_seed_and_verify())
        assert count == 8, f"Expected 8 seed records, got {count}"

    def test_alembic_downgrade_succeeds(self, alembic_cfg) -> None:
        """alembic downgrade base completes without error."""
        from alembic import command

        command.upgrade(alembic_cfg, "head")
        command.downgrade(alembic_cfg, "base")
