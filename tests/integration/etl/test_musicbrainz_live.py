"""Integration tests for MusicBrainz ETL connector (live API).

These tests hit the real MusicBrainz API. They are marked as integration
tests and skipped by default in CI (deselected unless -m integration is passed).
"""

from __future__ import annotations

import asyncio

import pytest

from music_attribution.etl.musicbrainz import MusicBrainzConnector
from music_attribution.schemas.normalized import NormalizedRecord

pytestmark = pytest.mark.integration

# Known stable MusicBrainz IDs
BEATLES_ARTIST_MBID = "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"
COME_TOGETHER_RECORDING_MBID = "11145229-d3c1-44f2-bca8-476345b442e2"


@pytest.fixture
def live_connector() -> MusicBrainzConnector:
    """Create connector for live API testing."""
    return MusicBrainzConnector(
        user_agent="MusicAttributionTest/1.0 (https://github.com/petteriTeikari/music-attribution-scaffold)"
    )


class TestMusicBrainzLive:
    """Integration tests against live MusicBrainz API."""

    @pytest.mark.xfail(reason="Live MusicBrainz API — recording IDs may change or return 404", strict=False)
    def test_fetch_known_recording_abbey_road(self, live_connector) -> None:
        """Test fetching 'Come Together' from Abbey Road (known MBID)."""
        record = asyncio.run(live_connector.fetch_recording(COME_TOGETHER_RECORDING_MBID))
        assert isinstance(record, NormalizedRecord)
        assert record.source == "MUSICBRAINZ"
        assert "come together" in record.canonical_name.lower()

    def test_fetch_known_artist_beatles(self, live_connector) -> None:
        """Test fetching The Beatles (known MBID)."""
        record = asyncio.run(live_connector.fetch_artist(BEATLES_ARTIST_MBID))
        assert isinstance(record, NormalizedRecord)
        assert record.entity_type == "ARTIST"
