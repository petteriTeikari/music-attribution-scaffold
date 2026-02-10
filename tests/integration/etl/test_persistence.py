"""Integration tests for NormalizedRecord persistence layer.

Uses Testcontainers to spin up a PostgreSQL instance for realistic testing.
"""

from __future__ import annotations

import time
import uuid
from datetime import UTC, datetime

import pytest

try:
    from testcontainers.postgres import PostgresContainer

    HAS_DOCKER = True
except ImportError:
    HAS_DOCKER = False

from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
    SourceMetadata,
)

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(not HAS_DOCKER, reason="testcontainers not available"),
]


def _make_record(
    source: SourceEnum = SourceEnum.MUSICBRAINZ,
    source_id: str | None = None,
    name: str = "Test Track",
    isrc: str | None = "USRC12345678",
    mbid: str | None = "test-mbid-123",
    entity_type: EntityTypeEnum = EntityTypeEnum.RECORDING,
) -> NormalizedRecord:
    """Helper to create a NormalizedRecord for testing."""
    return NormalizedRecord(
        source=source,
        source_id=source_id or str(uuid.uuid4()),
        entity_type=entity_type,
        canonical_name=name,
        identifiers=IdentifierBundle(isrc=isrc, mbid=mbid),
        metadata=SourceMetadata(roles=["The Beatles"], duration_ms=259000),
        fetch_timestamp=datetime.now(UTC),
        source_confidence=0.9,
    )


@pytest.fixture(scope="module")
def postgres_container():
    """Spin up a PostgreSQL container for persistence tests."""
    with PostgresContainer(
        image="pgvector/pgvector:pg17",
        dbname="test_persistence",
        username="test",
        password="test",
    ) as pg:
        yield pg


@pytest.fixture(scope="module")
def db_url(postgres_container):
    """Get database URL and create tables."""
    url = postgres_container.get_connection_url().replace("+psycopg2", "+psycopg")

    from sqlalchemy import create_engine

    from music_attribution.db.models import Base

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    engine.dispose()
    return url


@pytest.fixture
def repo(db_url):
    """Create a NormalizedRecordRepository connected to the test database."""
    from music_attribution.etl.persistence import NormalizedRecordRepository

    return NormalizedRecordRepository(database_url=db_url)


class TestNormalizedRecordPersistence:
    """Integration tests for NormalizedRecord persistence."""

    def test_insert_normalized_record(self, repo) -> None:
        """Test inserting a single NormalizedRecord."""
        record = _make_record(source_id="insert-test-1")
        record_id = repo.upsert(record)
        assert isinstance(record_id, uuid.UUID)

    def test_upsert_same_source_id_updates(self, repo) -> None:
        """Test that upserting with same source+source_id updates, not duplicates."""
        record1 = _make_record(source_id="upsert-test-1", name="Original Name")
        id1 = repo.upsert(record1)

        record2 = _make_record(source_id="upsert-test-1", name="Updated Name")
        id2 = repo.upsert(record2)

        # Should return the same record_id (updated, not new)
        assert id1 == id2

        # Verify the name was updated
        results = repo.find_by_source(SourceEnum.MUSICBRAINZ)
        updated = [r for r in results if r.source_id == "upsert-test-1"]
        assert len(updated) == 1
        assert updated[0].canonical_name == "Updated Name"

    def test_query_by_source(self, repo) -> None:
        """Test querying records by source."""
        # Insert records from different sources
        repo.upsert(_make_record(source=SourceEnum.MUSICBRAINZ, source_id="qbs-mb-1"))
        repo.upsert(
            _make_record(
                source=SourceEnum.DISCOGS,
                source_id="qbs-dg-1",
                mbid=None,
                isrc="USRC99999999",
            )
        )

        mb_records = repo.find_by_source(SourceEnum.MUSICBRAINZ)
        assert len(mb_records) >= 1
        assert all(r.source == SourceEnum.MUSICBRAINZ for r in mb_records)

    def test_query_by_entity_type(self, repo) -> None:
        """Test querying records by entity type."""
        repo.upsert(
            _make_record(
                source_id="qbet-recording",
                entity_type=EntityTypeEnum.RECORDING,
            )
        )
        repo.upsert(
            _make_record(
                source_id="qbet-artist",
                entity_type=EntityTypeEnum.ARTIST,
                isrc=None,
            )
        )

        recordings = repo.find_by_entity_type(EntityTypeEnum.RECORDING)
        assert len(recordings) >= 1
        assert all(r.entity_type == EntityTypeEnum.RECORDING for r in recordings)

    def test_query_by_identifier(self, repo) -> None:
        """Test querying records by identifier (ISRC, MBID, etc.)."""
        unique_isrc = f"USRC{uuid.uuid4().hex[:8].upper()}"
        repo.upsert(_make_record(source_id="qbi-1", isrc=unique_isrc, mbid="qbi-mbid-1"))

        results = repo.find_by_identifier(isrc=unique_isrc)
        assert len(results) >= 1
        assert results[0].identifiers.isrc == unique_isrc

    def test_batch_insert_performance(self, repo) -> None:
        """Test that batch insert of 1000 records completes in < 5s."""
        batch = [
            _make_record(
                source_id=f"batch-perf-{i}",
                isrc=f"USRC{i:08d}",
                mbid=f"batch-mbid-{i}",
            )
            for i in range(1000)
        ]

        start = time.monotonic()
        ids = repo.upsert_batch(batch)
        elapsed = time.monotonic() - start

        assert len(ids) == 1000
        assert elapsed < 5.0, f"Batch insert took {elapsed:.1f}s, expected < 5s"
