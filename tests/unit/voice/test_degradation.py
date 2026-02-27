"""Tests for voice audio degradation module."""

from __future__ import annotations

import math
from pathlib import Path

import pytest

from music_attribution.voice.degradation import (
    PRESETS,
    DegradationPreset,
)


class TestDegradationPreset:
    """Tests for DegradationPreset enum."""

    def test_degradation_preset_has_five_members(self) -> None:
        """DegradationPreset has exactly CLEAN, OFFICE, CODEC, NOISY_CAFE, EXTREME."""
        members = {m.name for m in DegradationPreset}
        assert members == {"CLEAN", "OFFICE", "CODEC", "NOISY_CAFE", "EXTREME"}

    def test_degradation_config_is_frozen(self) -> None:
        """DegradationConfig is a frozen dataclass."""
        config = PRESETS[DegradationPreset.CLEAN]
        with pytest.raises(AttributeError):
            config.snr_db = 10.0  # type: ignore[misc]

    def test_presets_dict_has_all_five(self) -> None:
        """PRESETS dict has one entry per DegradationPreset member."""
        assert set(PRESETS.keys()) == set(DegradationPreset)

    def test_clean_preset_values(self) -> None:
        """CLEAN preset: no noise, no reverb, no codec, full bandwidth."""
        c = PRESETS[DegradationPreset.CLEAN]
        assert c.snr_db == math.inf
        assert c.reverb_rt60 == 0.0
        assert c.mp3_bitrate_kbps is None
        assert c.low_cutoff_hz == 20.0
        assert c.high_cutoff_hz == 20000.0

    def test_office_preset_values(self) -> None:
        """OFFICE preset: mild noise, mild reverb, no codec."""
        c = PRESETS[DegradationPreset.OFFICE]
        assert c.snr_db == 25.0
        assert c.reverb_rt60 == 0.3
        assert c.mp3_bitrate_kbps is None
        assert c.low_cutoff_hz == 80.0
        assert c.high_cutoff_hz == 16000.0

    def test_codec_preset_values(self) -> None:
        """CODEC preset: no env noise, 32kbps mp3 compression."""
        c = PRESETS[DegradationPreset.CODEC]
        assert c.snr_db == math.inf
        assert c.reverb_rt60 == 0.0
        assert c.mp3_bitrate_kbps == 32
        assert c.low_cutoff_hz == 20.0
        assert c.high_cutoff_hz == 20000.0

    def test_noisy_cafe_preset_values(self) -> None:
        """NOISY_CAFE preset: heavy noise, reverb, 64kbps codec."""
        c = PRESETS[DegradationPreset.NOISY_CAFE]
        assert c.snr_db == 10.0
        assert c.reverb_rt60 == 0.6
        assert c.mp3_bitrate_kbps == 64
        assert c.low_cutoff_hz == 100.0
        assert c.high_cutoff_hz == 12000.0

    def test_extreme_preset_values(self) -> None:
        """EXTREME preset: maximum degradation."""
        c = PRESETS[DegradationPreset.EXTREME]
        assert c.snr_db == 5.0
        assert c.reverb_rt60 == 1.2
        assert c.mp3_bitrate_kbps == 16
        assert c.low_cutoff_hz == 200.0
        assert c.high_cutoff_hz == 8000.0

    def test_lossless_presets(self) -> None:
        """CLEAN and OFFICE have no mp3 compression (lossless pipeline)."""
        assert PRESETS[DegradationPreset.CLEAN].mp3_bitrate_kbps is None
        assert PRESETS[DegradationPreset.OFFICE].mp3_bitrate_kbps is None

    def test_lossy_presets(self) -> None:
        """CODEC, NOISY_CAFE, EXTREME have mp3 compression (lossy pipeline)."""
        assert PRESETS[DegradationPreset.CODEC].mp3_bitrate_kbps is not None
        assert PRESETS[DegradationPreset.NOISY_CAFE].mp3_bitrate_kbps is not None
        assert PRESETS[DegradationPreset.EXTREME].mp3_bitrate_kbps is not None


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
