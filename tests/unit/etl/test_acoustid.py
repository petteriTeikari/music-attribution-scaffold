"""Tests for AcoustID fingerprint connector (unit tests with mocked HTTP)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from music_attribution.etl.acoustid import AcoustIDConnector
from music_attribution.schemas.normalized import NormalizedRecord


@pytest.fixture
def connector() -> AcoustIDConnector:
    """Create an AcoustIDConnector with test API key."""
    return AcoustIDConnector(api_key="test-api-key-123")


@pytest.fixture
def sample_lookup_response() -> dict:
    """Sample AcoustID lookup API response."""
    return {
        "status": "ok",
        "results": [
            {
                "id": "acoustid-result-1",
                "score": 0.98,
                "recordings": [
                    {
                        "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d",
                        "title": "Come Together",
                        "duration": 259,
                        "artists": [
                            {
                                "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600a",
                                "name": "The Beatles",
                            }
                        ],
                    }
                ],
            },
            {
                "id": "acoustid-result-2",
                "score": 0.72,
                "recordings": [
                    {
                        "id": "another-recording-mbid",
                        "title": "Come Together (Remastered)",
                        "duration": 260,
                        "artists": [
                            {
                                "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600a",
                                "name": "The Beatles",
                            }
                        ],
                    }
                ],
            },
        ],
    }


class TestAcoustIDConnector:
    """Unit tests for AcoustID fingerprint connector."""

    async def test_generate_fingerprint_from_audio_file(self, connector) -> None:
        """Test fingerprint generation from an audio file."""
        mock_fingerprint = (259, "AQAA...")  # (duration, fingerprint) — matches acoustid API

        with patch("acoustid.fingerprint_file", return_value=mock_fingerprint):
            fp, duration = await connector.fingerprint_file(Path("/tmp/test.mp3"))
            assert isinstance(fp, str)
            assert fp == "AQAA..."
            assert duration == 259

    async def test_lookup_fingerprint_returns_mbids(
        self, connector, sample_lookup_response
    ) -> None:
        """Test that fingerprint lookup returns MusicBrainz IDs as NormalizedRecords."""
        with patch("acoustid.lookup", return_value=sample_lookup_response):
            records = await connector.lookup("AQAA...", 259)
            assert isinstance(records, list)
            assert len(records) >= 1
            assert all(isinstance(r, NormalizedRecord) for r in records)
            # First result should have highest score
            assert records[0].source_confidence >= records[-1].source_confidence

    async def test_handles_no_match_gracefully(self, connector) -> None:
        """Test that no-match response returns empty list."""
        empty_response = {"status": "ok", "results": []}

        with patch("acoustid.lookup", return_value=empty_response):
            records = await connector.lookup("AQAA...", 259)
            assert isinstance(records, list)
            assert len(records) == 0

    def test_rate_limiter_three_per_second(self, connector) -> None:
        """Test that the rate limiter is configured for AcoustID limits."""
        limiter = connector._rate_limiter
        assert limiter._rate == 3.0

    def test_transform_lookup_result_to_normalized_record(
        self, connector, sample_lookup_response
    ) -> None:
        """Test transformation of lookup results to NormalizedRecords."""
        records = connector.transform_lookup_results(sample_lookup_response)
        assert len(records) >= 1
        first = records[0]
        assert first.source == "ACOUSTID"
        assert first.entity_type == "RECORDING"
        assert first.identifiers.mbid == "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"
        assert first.identifiers.acoustid == "acoustid-result-1"
