"""Tests for golden dataset STT regression suite."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from music_attribution.voice.degradation import DegradationPreset
from music_attribution.voice.golden_commands import GOLDEN_COMMANDS
from tests.unit.voice.conftest import (
    FIXTURES_DIR,
    golden_fixtures_available,
    load_fixture,
    load_manifest,
)

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


# ─── Whisper domain prompt for improved recognition ────────────────────

_WHISPER_INITIAL_PROMPT = (
    "Music attribution, confidence score, assurance level, MusicBrainz, Discogs, Imogen Heap, Frou Frou"
)


def _transcribe_fixture(
    whisper_model: object,
    command_id: str,
    preset: str,
) -> str:
    """Transcribe a golden fixture and return the text.

    Args:
        whisper_model: faster-whisper WhisperModel instance.
        command_id: Command ID (e.g., "cmd_01").
        preset: Preset name (e.g., "clean").

    Returns:
        Transcribed text string.
    """
    audio, _sr = load_fixture(command_id, preset)
    segments, _ = whisper_model.transcribe(  # type: ignore[union-attr]
        audio,
        vad_filter=True,
        initial_prompt=_WHISPER_INITIAL_PROMPT,
    )
    return " ".join(seg.text.strip() for seg in segments)


# ─── STT accuracy tests (require golden fixtures + faster-whisper) ─────


@pytest.mark.slow
@pytest.mark.voice
@pytest.mark.skipif(
    not golden_fixtures_available(),
    reason="Golden fixtures not generated",
)
class TestSTTAccuracy:
    """Parametrized STT accuracy tests across presets."""

    @pytest.mark.parametrize("preset", list(DegradationPreset))
    def test_stt_wer_per_preset_aggregate(
        self,
        whisper_model: object,
        preset: DegradationPreset,
    ) -> None:
        """Mean WER across 20 commands is below threshold for each preset."""
        from music_attribution.voice.metrics import compute_wer

        wer_values = []
        for cmd in GOLDEN_COMMANDS:
            transcript = _transcribe_fixture(whisper_model, cmd["id"], preset.value)
            wer = compute_wer(cmd["text"], transcript)
            wer_values.append(wer)

        mean_wer = sum(wer_values) / len(wer_values)
        threshold = WER_THRESHOLDS[preset]
        assert mean_wer < threshold, f"{preset.value}: mean WER {mean_wer:.3f} >= threshold {threshold}"

    @pytest.mark.parametrize("preset", list(DegradationPreset))
    def test_stt_keyword_survival_per_preset(
        self,
        whisper_model: object,
        preset: DegradationPreset,
    ) -> None:
        """Keyword survival rate across 20 commands meets threshold."""
        from music_attribution.voice.metrics import check_domain_keywords

        total_keywords = 0
        total_found = 0
        for cmd in GOLDEN_COMMANDS:
            transcript = _transcribe_fixture(whisper_model, cmd["id"], preset.value)
            found, missed = check_domain_keywords(transcript, cmd["domain_keywords"])
            total_found += len(found)
            total_keywords += len(found) + len(missed)

        survival_rate = total_found / total_keywords if total_keywords > 0 else 0.0
        threshold = KEYWORD_THRESHOLDS[preset]
        assert survival_rate >= threshold, (
            f"{preset.value}: keyword survival {survival_rate:.3f} < threshold {threshold}"
        )

    @pytest.mark.parametrize(
        "cmd",
        GOLDEN_COMMANDS,
        ids=[c["id"] for c in GOLDEN_COMMANDS],
    )
    def test_stt_clean_individual_commands(
        self,
        whisper_model: object,
        cmd: dict,
    ) -> None:
        """Each individual clean command has WER < 0.20."""
        from music_attribution.voice.metrics import compute_wer

        transcript = _transcribe_fixture(whisper_model, cmd["id"], "clean")
        wer = compute_wer(cmd["text"], transcript)
        assert wer < 0.20, f"{cmd['id']}: WER {wer:.3f} >= 0.20 (ref={cmd['text']!r}, hyp={transcript!r})"


# ─── Fixture integrity tests (no STT, fast) ───────────────────────────


@pytest.mark.voice
@pytest.mark.skipif(
    not golden_fixtures_available(),
    reason="Golden fixtures not generated",
)
class TestFixtureIntegrity:
    """Validate committed FLAC fixtures match manifest checksums."""

    def test_fixture_checksums_match_manifest(self) -> None:
        """SHA256 of each FLAC matches the value recorded in manifest.json."""
        manifest = load_manifest()
        for entry in manifest["files"]:
            path = FIXTURES_DIR / entry["filename"]
            actual_sha = hashlib.sha256(path.read_bytes()).hexdigest()
            assert actual_sha == entry["sha256"], f"Checksum mismatch for {entry['filename']}"

    def test_fixture_count_matches_manifest(self) -> None:
        """Number of FLAC files equals manifest entry count (100)."""
        manifest = load_manifest()
        flac_files = list(FIXTURES_DIR.glob("*.flac"))
        assert len(flac_files) == len(manifest["files"])

    def test_all_presets_represented(self) -> None:
        """All 5 presets exist for cmd_01."""
        for preset in DegradationPreset:
            path = FIXTURES_DIR / f"cmd_01_{preset.value}.flac"
            assert path.exists(), f"Missing fixture: {path.name}"
