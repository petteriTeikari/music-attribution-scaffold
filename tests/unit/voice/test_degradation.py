"""Tests for voice audio degradation module."""

from __future__ import annotations

from pathlib import Path

import pytest


class TestVoiceTestDependencies:
    """Tests that voice-test dependency group is installable."""

    def test_voice_test_deps_importable(self) -> None:
        """All voice-test dependencies can be imported."""
        audiomentations = pytest.importorskip("audiomentations")
        soundfile = pytest.importorskip("soundfile")
        pyroomacoustics = pytest.importorskip("pyroomacoustics")
        soxr = pytest.importorskip("soxr")

        # Verify modules loaded
        assert audiomentations is not None
        assert soundfile is not None
        assert pyroomacoustics is not None
        assert soxr is not None


class TestFixtureDirectory:
    """Tests that the voice fixture directory exists."""

    def test_fixtures_directory_exists(self) -> None:
        """The tests/fixtures/voice/audio directory exists."""
        fixtures_dir = Path(__file__).resolve().parents[3] / "tests" / "fixtures" / "voice" / "audio"
        assert fixtures_dir.is_dir(), f"Fixture directory does not exist: {fixtures_dir}"
