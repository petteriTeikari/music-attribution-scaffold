"""Integration tests for MusicBrainz ETL connector (live API).

These tests hit the real MusicBrainz API. They are marked as integration
tests and skipped by default in CI.
"""

from __future__ import annotations

import asyncio

import pytest

from music_attribution.etl.musicbrainz import MusicBrainzConnector
from music_attribution.schemas.normalized import NormalizedRecord

pytestmark = pytest.mark.integration


@pytest.fixture
def live_connector() -> MusicBrainzConnector:
    """Create connector for live API testing."""
    return MusicBrainzConnector(
        user_agent="MusicAttributionTest/1.0 (https://github.com/petteriTeikari/music-attribution-scaffold)"
    )


class TestMusicBrainzLive:
    """Integration tests against live MusicBrainz API."""

    def test_fetch_known_recording_abbey_road(self, live_connector) -> None:
        """Test fetching 'Come Together' from Abbey Road (known MBID)."""
        record = asyncio.get_event_loop().run_until_complete(
            live_connector.fetch_recording("b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d")
        )
        assert isinstance(record, NormalizedRecord)
        assert record.source == "MUSICBRAINZ"
        assert "come together" in record.canonical_name.lower()

    def test_fetch_known_artist_beatles(self, live_connector) -> None:
        """Test fetching The Beatles (known MBID)."""
        record = asyncio.get_event_loop().run_until_complete(
            live_connector.fetch_artist("b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d")
        )
        assert isinstance(record, NormalizedRecord)
        assert record.entity_type == "ARTIST"
