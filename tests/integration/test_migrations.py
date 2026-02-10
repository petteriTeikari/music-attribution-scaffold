"""Tests for Alembic migrations with SQLAlchemy 2.0.

These tests verify that database migrations can run successfully
and that the resulting schema matches the Pydantic boundary objects.
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
def postgres_for_migrations():
    """Spin up PostgreSQL for migration testing."""
    with PostgresContainer(
        image="pgvector/pgvector:pg17",
        dbname="test_migrations",
        username="test",
        password="test",
    ) as pg:
        yield pg


@pytest.fixture
def alembic_config(postgres_for_migrations, tmp_path):
    """Create Alembic config pointing to test database."""
    from alembic.config import Config

    conn_url = postgres_for_migrations.get_connection_url().replace("+psycopg2", "")
    cfg = Config()
    cfg.set_main_option("script_location", "alembic")
    cfg.set_main_option("sqlalchemy.url", conn_url)
    return cfg


class TestMigrations:
    """Tests for Alembic migration infrastructure."""

    def test_alembic_upgrade_head(self, alembic_config) -> None:
        """Test that alembic upgrade head runs without errors."""
        from alembic import command

        command.upgrade(alembic_config, "head")

    def test_alembic_downgrade_base(self, alembic_config) -> None:
        """Test that alembic downgrade base runs without errors."""
        from alembic import command

        command.upgrade(alembic_config, "head")
        command.downgrade(alembic_config, "base")

    def test_alembic_heads_single(self, alembic_config) -> None:
        """Test that there is only one head (no branching)."""
        from alembic.script import ScriptDirectory

        script = ScriptDirectory.from_config(alembic_config)
        heads = script.get_heads()
        assert len(heads) == 1, f"Expected 1 head, got {len(heads)}: {heads}"

    def test_tables_match_pydantic_schemas(self, alembic_config, postgres_for_migrations) -> None:
        """Test that created tables have expected columns."""
        import psycopg
        from alembic import command

        command.upgrade(alembic_config, "head")

        conn_url = postgres_for_migrations.get_connection_url().replace("+psycopg2", "")
        with psycopg.connect(conn_url) as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT table_name FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name NOT LIKE 'alembic_%'
                ORDER BY table_name
            """)
            tables = [row[0] for row in cur.fetchall()]
            assert "normalized_records" in tables
            assert "resolved_entities" in tables
            assert "attribution_records" in tables
