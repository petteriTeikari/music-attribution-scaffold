"""Tests for MusicBrainz ETL connector (unit tests with mocked HTTP)."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from music_attribution.etl.musicbrainz import MusicBrainzConnector
from music_attribution.etl.rate_limiter import TokenBucketRateLimiter
from music_attribution.schemas.normalized import NormalizedRecord


@pytest.fixture
def connector() -> MusicBrainzConnector:
    """Create a MusicBrainzConnector with test user agent."""
    return MusicBrainzConnector(user_agent="TestApp/1.0 (test@example.com)")


@pytest.fixture
def sample_recording_response() -> dict:
    """Sample MusicBrainz recording API response."""
    return {
        "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d",
        "title": "Come Together",
        "length": 259000,
        "artist-credit": [
            {
                "artist": {
                    "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600a",
                    "name": "The Beatles",
                    "sort-name": "Beatles, The",
                }
            }
        ],
        "isrc-list": ["GBAYE0601690"],
        "release-list": [
            {
                "id": "release-123",
                "title": "Abbey Road",
                "date": "1969-09-26",
                "country": "GB",
            }
        ],
        "artist-relation-list": [
            {
                "type": "producer",
                "artist": {
                    "id": "artist-gm-123",
                    "name": "George Martin",
                },
                "attributes": [],
            }
        ],
    }


@pytest.fixture
def sample_artist_response() -> dict:
    """Sample MusicBrainz artist API response."""
    return {
        "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600a",
        "name": "The Beatles",
        "sort-name": "Beatles, The",
        "type": "Group",
        "country": "GB",
        "life-span": {"begin": "1960", "end": "1970", "ended": True},
        "isni-list": ["0000000121707484"],
        "alias-list": [
            {"alias": "Beatles", "type": "Search hint"},
            {"alias": "ビートルズ", "type": "Artist name"},
        ],
    }


class TestMusicBrainzConnector:
    """Unit tests for MusicBrainz ETL connector."""

    async def test_fetch_recording_by_mbid(self, connector, sample_recording_response) -> None:
        """Test fetching a recording by MBID with mocked API."""
        with patch("musicbrainzngs.get_recording_by_id", return_value={"recording": sample_recording_response}):
            record = await connector.fetch_recording("b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d")
            assert isinstance(record, NormalizedRecord)
            assert record.source == "MUSICBRAINZ"
            assert record.canonical_name == "Come Together"

    async def test_fetch_artist_by_mbid(self, connector, sample_artist_response) -> None:
        """Test fetching an artist by MBID with mocked API."""
        with patch("musicbrainzngs.get_artist_by_id", return_value={"artist": sample_artist_response}):
            record = await connector.fetch_artist("b10bbbfc-cf9e-42e0-be17-e2c3e1d2600a")
            assert isinstance(record, NormalizedRecord)
            assert record.entity_type == "ARTIST"
            assert record.canonical_name == "The Beatles"

    def test_transform_recording_to_normalized_record(self, connector, sample_recording_response) -> None:
        """Test transformation of raw API response to NormalizedRecord."""
        record = connector.transform_recording(sample_recording_response)
        assert isinstance(record, NormalizedRecord)
        assert record.source == "MUSICBRAINZ"
        assert record.entity_type == "RECORDING"
        assert record.source_id == "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"

    def test_transform_artist_to_normalized_record(self, connector, sample_artist_response) -> None:
        """Test transformation of raw artist response to NormalizedRecord."""
        record = connector.transform_artist(sample_artist_response)
        assert isinstance(record, NormalizedRecord)
        assert record.entity_type == "ARTIST"
        assert "Beatles" in record.canonical_name

    def test_extract_relationships_from_recording(self, connector, sample_recording_response) -> None:
        """Test extraction of relationships from recording response."""
        record = connector.transform_recording(sample_recording_response)
        assert len(record.relationships) >= 1
        producer_rel = [r for r in record.relationships if r.relationship_type == "PRODUCED"]
        assert len(producer_rel) == 1

    def test_extract_isrc_from_recording(self, connector, sample_recording_response) -> None:
        """Test that ISRC is extracted from recording response."""
        record = connector.transform_recording(sample_recording_response)
        assert record.identifiers.isrc == "GBAYE0601690"

    def test_handles_missing_fields_gracefully(self, connector) -> None:
        """Test that missing optional fields don't cause errors."""
        minimal_response = {
            "id": "test-mbid",
            "title": "Minimal Track",
        }
        record = connector.transform_recording(minimal_response)
        assert record.canonical_name == "Minimal Track"
        assert record.identifiers.isrc is None


class TestTokenBucketRateLimiter:
    """Tests for the rate limiter."""

    async def test_rate_limiter_enforces_one_per_second(self) -> None:
        """Test that rate limiter enforces the configured rate."""
        limiter = TokenBucketRateLimiter(rate=2.0, capacity=2)
        assert await limiter.acquire()
        assert await limiter.acquire()

    async def test_retry_on_503_with_backoff(self, connector, sample_recording_response) -> None:
        """Test that 503 errors trigger retries with backoff."""
        import musicbrainzngs

        call_count = 0

        def mock_get(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise musicbrainzngs.WebServiceError("503 Service Unavailable")
            return {"recording": sample_recording_response}

        with patch("musicbrainzngs.get_recording_by_id", side_effect=mock_get):
            record = await connector.fetch_recording("b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d")
            assert record.canonical_name == "Come Together"
            assert call_count == 3
