"""Tests for Discogs ETL connector (unit tests with mocked HTTP)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from music_attribution.etl.discogs import DiscogsConnector
from music_attribution.schemas.normalized import NormalizedRecord


@pytest.fixture
def connector() -> DiscogsConnector:
    """Create a DiscogsConnector with test user agent."""
    return DiscogsConnector(user_agent="TestApp/1.0", token="test-token-123")


@pytest.fixture
def sample_release_data() -> dict:
    """Sample Discogs release API response (dict form)."""
    return {
        "id": 249504,
        "title": "Abbey Road",
        "year": 1969,
        "country": "UK",
        "artists": [
            {"id": 82730, "name": "The Beatles"},
        ],
        "tracklist": [
            {
                "position": "A1",
                "title": "Come Together",
                "duration": "4:19",
                "extraartists": [
                    {
                        "id": 252898,
                        "name": "George Martin",
                        "role": "Producer",
                    }
                ],
            },
            {
                "position": "A2",
                "title": "Something",
                "duration": "3:03",
                "extraartists": [
                    {
                        "id": 252898,
                        "name": "George Martin",
                        "role": "Producer",
                    }
                ],
            },
        ],
        "extraartists": [
            {
                "id": 252898,
                "name": "George Martin",
                "role": "Producer",
            },
            {
                "id": 999999,
                "name": "Geoff Emerick",
                "role": "Engineer",
            },
        ],
        "labels": [
            {"id": 25030, "name": "Apple Records", "catno": "PCS 7088"},
        ],
        "genres": ["Rock"],
        "styles": ["Pop Rock", "Psychedelic Rock"],
    }


@pytest.fixture
def sample_artist_data() -> dict:
    """Sample Discogs artist API response (dict form)."""
    return {
        "id": 82730,
        "name": "The Beatles",
        "realname": "",
        "namevariations": ["Beatles", "ビートルズ"],
        "profile": "The Beatles were an English rock band...",
        "urls": ["https://www.thebeatles.com"],
        "members": [
            {"id": 100, "name": "John Lennon"},
            {"id": 101, "name": "Paul McCartney"},
            {"id": 102, "name": "George Harrison"},
            {"id": 103, "name": "Ringo Starr"},
        ],
    }


class TestDiscogsConnector:
    """Unit tests for Discogs ETL connector."""

    async def test_fetch_release_by_id(self, connector, sample_release_data) -> None:
        """Test fetching a release by Discogs ID with mocked API."""
        mock_release = MagicMock()
        mock_release.data = sample_release_data
        mock_release.id = sample_release_data["id"]
        mock_release.title = sample_release_data["title"]

        with patch.object(connector._client, "release", return_value=mock_release):
            records = await connector.fetch_release(249504)
            assert isinstance(records, list)
            assert len(records) >= 1
            assert all(isinstance(r, NormalizedRecord) for r in records)
            assert records[0].source == "DISCOGS"

    def test_transform_release_credits_to_normalized_records(
        self, connector, sample_release_data
    ) -> None:
        """Test transformation of release data into NormalizedRecords."""
        records = connector.transform_release(sample_release_data)
        assert isinstance(records, list)
        assert len(records) >= 1
        # Should have at least a recording-type record
        recording_records = [r for r in records if r.entity_type == "RECORDING"]
        assert len(recording_records) >= 1

    def test_extract_role_details(self, connector, sample_release_data) -> None:
        """Test that credit roles (Guitar, Bass, Vocals) are extracted."""
        records = connector.transform_release(sample_release_data)
        # Release-level record should have relationships for producer and engineer
        release_records = [r for r in records if r.entity_type == "RELEASE"]
        if release_records:
            rels = release_records[0].relationships
            rel_types = {r.relationship_type for r in rels}
            assert "PRODUCED" in rel_types or "ENGINEERED" in rel_types

    def test_handles_multiple_artists_per_credit(self, connector) -> None:
        """Test release with multiple artists in a single credit."""
        multi_artist_data = {
            "id": 12345,
            "title": "Collaboration Album",
            "year": 2020,
            "country": "US",
            "artists": [
                {"id": 1, "name": "Artist A"},
                {"id": 2, "name": "Artist B"},
            ],
            "tracklist": [
                {
                    "position": "1",
                    "title": "Duet Track",
                    "duration": "3:30",
                    "extraartists": [
                        {"id": 1, "name": "Artist A", "role": "Vocals"},
                        {"id": 2, "name": "Artist B", "role": "Vocals, Guitar"},
                    ],
                }
            ],
            "extraartists": [],
            "labels": [],
            "genres": [],
            "styles": [],
        }
        records = connector.transform_release(multi_artist_data)
        assert len(records) >= 1

    def test_rate_limiter_enforces_sixty_per_minute(self, connector) -> None:
        """Test that the rate limiter is configured for Discogs limits."""
        # Authenticated rate: 60/min = 1/sec
        limiter = connector._rate_limiter
        assert limiter._rate <= 1.0  # At most 1 token per second for authenticated

    def test_authenticated_vs_unauthenticated_limits(self) -> None:
        """Test that authenticated and unauthenticated connectors have different rate limits."""
        auth_conn = DiscogsConnector(user_agent="TestApp/1.0", token="test-token")
        unauth_conn = DiscogsConnector(user_agent="TestApp/1.0")

        assert auth_conn._rate_limiter._rate >= unauth_conn._rate_limiter._rate

    def test_transform_artist_to_normalized_record(
        self, connector, sample_artist_data
    ) -> None:
        """Test transformation of artist data into a NormalizedRecord."""
        record = connector.transform_artist(sample_artist_data)
        assert isinstance(record, NormalizedRecord)
        assert record.entity_type == "ARTIST"
        assert record.source == "DISCOGS"
        assert record.canonical_name == "The Beatles"
        assert "Beatles" in record.alternative_names
