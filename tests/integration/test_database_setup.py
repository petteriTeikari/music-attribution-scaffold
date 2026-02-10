"""Tests for PostgreSQL + pgvector + Apache AGE Docker Compose setup.

These tests use testcontainers to spin up a PostgreSQL instance with
the required extensions. They are marked as integration tests and
skipped in CI by default.
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
    """Spin up a PostgreSQL container with pgvector.

    Note: Apache AGE is not available as a standard Docker extension,
    so we test pgvector only in the standard container. AGE will be
    tested with the custom Dockerfile.
    """
    with PostgresContainer(
        image="pgvector/pgvector:pg17",
        dbname="test_musicattr",
        username="test",
        password="test",
    ) as pg:
        yield pg


@pytest.fixture
def pg_connection(postgres_container):
    """Get a psycopg connection to the test database."""
    import psycopg

    conn_url = postgres_container.get_connection_url().replace("+psycopg2", "")
    with psycopg.connect(conn_url) as conn:
        yield conn


class TestDatabaseSetup:
    """Tests for database infrastructure."""

    def test_postgresql_connection(self, pg_connection) -> None:
        """Test that PostgreSQL accepts connections."""
        with pg_connection.cursor() as cur:
            cur.execute("SELECT 1")
            result = cur.fetchone()
            assert result[0] == 1

    def test_pgvector_extension_available(self, pg_connection) -> None:
        """Test that pgvector extension can be created."""
        with pg_connection.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            pg_connection.commit()
            cur.execute("SELECT extname FROM pg_extension WHERE extname = 'vector'")
            result = cur.fetchone()
            assert result is not None
            assert result[0] == "vector"

    def test_create_vector_index(self, pg_connection) -> None:
        """Test that vector indexes can be created."""
        with pg_connection.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute("CREATE TABLE IF NOT EXISTS test_embeddings (id serial PRIMARY KEY, embedding vector(384))")
            cur.execute(
                "CREATE INDEX IF NOT EXISTS test_embedding_idx ON test_embeddings USING hnsw (embedding vector_cosine_ops)"
            )
            pg_connection.commit()
            cur.execute("SELECT indexname FROM pg_indexes WHERE indexname = 'test_embedding_idx'")
            result = cur.fetchone()
            assert result is not None
