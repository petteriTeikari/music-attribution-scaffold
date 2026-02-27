"""Tests for golden dataset STT regression suite."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from music_attribution.voice.degradation import DegradationPreset

# ─── WER and keyword survival thresholds per preset ────────────────────

WER_THRESHOLDS: dict[DegradationPreset, float] = {
    DegradationPreset.CLEAN: 0.10,
    DegradationPreset.OFFICE: 0.15,
    DegradationPreset.CODEC: 0.15,
    DegradationPreset.NOISY_CAFE: 0.25,
    DegradationPreset.EXTREME: 0.50,
}

KEYWORD_THRESHOLDS: dict[DegradationPreset, float] = {
    DegradationPreset.CLEAN: 0.90,
    DegradationPreset.OFFICE: 0.85,
    DegradationPreset.CODEC: 0.85,
    DegradationPreset.NOISY_CAFE: 0.70,
    DegradationPreset.EXTREME: 0.50,
}


class TestThresholdDefinitions:
    """Tests for WER and keyword threshold constants."""

    def test_wer_thresholds_defined_for_all_presets(self) -> None:
        """WER_THRESHOLDS has entries for all 5 DegradationPreset values."""
        for preset in DegradationPreset:
            assert preset in WER_THRESHOLDS, f"Missing WER threshold for {preset}"

    def test_keyword_thresholds_defined_for_all_presets(self) -> None:
        """KEYWORD_THRESHOLDS has entries for all 5 DegradationPreset values."""
        for preset in DegradationPreset:
            assert preset in KEYWORD_THRESHOLDS, f"Missing keyword threshold for {preset}"

    def test_wer_thresholds_monotonically_ordered(self) -> None:
        """WER thresholds increase with degradation severity."""
        assert WER_THRESHOLDS[DegradationPreset.CLEAN] <= WER_THRESHOLDS[DegradationPreset.CODEC]
        assert WER_THRESHOLDS[DegradationPreset.CODEC] <= WER_THRESHOLDS[DegradationPreset.OFFICE]
        assert WER_THRESHOLDS[DegradationPreset.OFFICE] <= WER_THRESHOLDS[DegradationPreset.NOISY_CAFE]
        assert WER_THRESHOLDS[DegradationPreset.NOISY_CAFE] <= WER_THRESHOLDS[DegradationPreset.EXTREME]


class TestFixtureHelpers:
    """Tests for golden fixture loading helpers in conftest."""

    def test_golden_fixtures_available_returns_bool(self) -> None:
        """golden_fixtures_available() returns True or False without error."""
        from tests.unit.voice.conftest import golden_fixtures_available

        result = golden_fixtures_available()
        assert isinstance(result, bool)

    @pytest.mark.voice
    def test_load_fixture_audio_with_mock(self, tmp_path: Path) -> None:
        """load_fixture reads a FLAC file and returns (ndarray, sample_rate)."""
        pytest.importorskip("soundfile")
        import numpy as np

        from music_attribution.voice.degradation import write_audio
        from tests.unit.voice.conftest import load_fixture

        # Create a fake FLAC in tmp_path
        fake_audio = np.random.randn(16000).astype(np.float32) * 0.1
        write_audio(tmp_path / "cmd_01_clean.flac", fake_audio)

        with patch("tests.unit.voice.conftest.FIXTURES_DIR", tmp_path):
            audio, sr = load_fixture("cmd_01", "clean")

        assert isinstance(audio, np.ndarray)
        assert audio.dtype == np.float32
        assert sr == 16000

    def test_load_manifest_with_mock(self, tmp_path: Path) -> None:
        """load_manifest reads manifest.json and returns dict with 'files' key."""
        from tests.unit.voice.conftest import load_manifest

        manifest = {"version": "1.0", "files": [{"filename": "test.flac"}]}
        (tmp_path / "manifest.json").write_text(
            json.dumps(manifest),
            encoding="utf-8",
        )

        with patch("tests.unit.voice.conftest.FIXTURES_DIR", tmp_path):
            result = load_manifest()

        assert "files" in result
        assert len(result["files"]) == 1
