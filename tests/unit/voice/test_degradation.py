"""Tests for voice audio degradation module."""

from __future__ import annotations

import math
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from music_attribution.voice.degradation import (
    PRESETS,
    DegradationPreset,
)

if TYPE_CHECKING:
    import numpy as np


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


class TestApplyDegradation:
    """Tests for apply_degradation() function."""

    @staticmethod
    def _sine_wave(freq: float = 440.0, duration: float = 1.0, sr: int = 16000) -> np.ndarray:
        """Generate a sine wave for testing."""
        import numpy as np

        t = np.arange(int(sr * duration), dtype=np.float32) / sr
        return (0.5 * np.sin(2 * np.pi * freq * t)).astype(np.float32)

    @pytest.mark.voice
    def test_apply_clean_is_passthrough(self) -> None:
        """CLEAN preset returns audio unchanged (no noise/reverb/codec)."""
        np = pytest.importorskip("audiomentations")  # noqa: F841
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        output = apply_degradation(audio, 16000, DegradationPreset.CLEAN, seed=42)
        assert np_mod.allclose(output, audio, atol=1e-5)

    @pytest.mark.voice
    def test_apply_office_changes_audio(self) -> None:
        """OFFICE preset modifies audio (noise + reverb applied)."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        output = apply_degradation(audio, 16000, DegradationPreset.OFFICE, seed=42)
        assert not np_mod.allclose(output[: len(audio)], audio)

    @pytest.mark.voice
    def test_apply_codec_has_compression_artifacts(self) -> None:
        """CODEC preset introduces mp3 artifacts but preserves structure."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        output = apply_degradation(audio, 16000, DegradationPreset.CODEC, seed=42)
        # Should differ (codec artifacts)
        assert not np_mod.array_equal(output, audio)
        # But high correlation (structure preserved)
        corr = np_mod.corrcoef(output[: len(audio)], audio)[0, 1]
        assert corr > 0.8

    @pytest.mark.voice
    def test_apply_noisy_cafe_has_codec_and_noise(self) -> None:
        """NOISY_CAFE preset applies both env degradation and codec."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        output = apply_degradation(audio, 16000, DegradationPreset.NOISY_CAFE, seed=42)
        assert not np_mod.allclose(output[: len(audio)], audio)

    @pytest.mark.voice
    def test_apply_extreme_changes_audio(self) -> None:
        """EXTREME preset modifies audio significantly."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        output = apply_degradation(audio, 16000, DegradationPreset.EXTREME, seed=42)
        assert not np_mod.allclose(output[: len(audio)], audio)

    @pytest.mark.voice
    def test_apply_degradation_deterministic(self) -> None:
        """Same preset + same seed = identical output."""
        pytest.importorskip("audiomentations")
        import random

        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()

        random.seed(42)
        np_mod.random.seed(42)
        out1 = apply_degradation(audio, 16000, DegradationPreset.OFFICE, seed=42)

        random.seed(42)
        np_mod.random.seed(42)
        out2 = apply_degradation(audio, 16000, DegradationPreset.OFFICE, seed=42)

        assert np_mod.array_equal(out1, out2)

    @pytest.mark.voice
    def test_apply_degradation_different_seeds_differ(self) -> None:
        """Different seeds produce different output."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        out1 = apply_degradation(audio, 16000, DegradationPreset.OFFICE, seed=42)
        out2 = apply_degradation(audio, 16000, DegradationPreset.OFFICE, seed=99)
        assert not np_mod.array_equal(out1, out2)

    @pytest.mark.voice
    def test_codec_deterministic(self) -> None:
        """CODEC preset is deterministic (Mp3Compression has no random component)."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        out1 = apply_degradation(audio, 16000, DegradationPreset.CODEC, seed=42)
        out2 = apply_degradation(audio, 16000, DegradationPreset.CODEC, seed=42)
        assert np_mod.array_equal(out1, out2)

    @pytest.mark.voice
    def test_output_dtype_is_float32(self) -> None:
        """Output dtype is float32 for all presets."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        for preset in DegradationPreset:
            output = apply_degradation(audio, 16000, preset, seed=42)
            assert output.dtype == np_mod.float32, f"Wrong dtype for {preset.name}"

    @pytest.mark.voice
    def test_output_amplitude_bounded(self) -> None:
        """Output amplitude is within [-1.0, 1.0] for all presets."""
        pytest.importorskip("audiomentations")
        import numpy as np_mod

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        for preset in DegradationPreset:
            output = apply_degradation(audio, 16000, preset, seed=42)
            assert np_mod.all(np_mod.abs(output) <= 1.0), f"Amplitude exceeded for {preset.name}"

    @pytest.mark.voice
    def test_reverb_output_length(self) -> None:
        """Reverb tail extends signal — output >= input length."""
        pytest.importorskip("audiomentations")

        from music_attribution.voice.degradation import apply_degradation

        audio = self._sine_wave()
        output = apply_degradation(audio, 16000, DegradationPreset.OFFICE, seed=42)
        assert len(output) >= len(audio)


class TestFlacIO:
    """Tests for read_audio() and write_audio() FLAC I/O helpers."""

    @staticmethod
    def _sine_wave(freq: float = 440.0, duration: float = 1.0, sr: int = 16000) -> np.ndarray:
        """Generate a sine wave for testing."""
        import numpy as np_mod

        t = np_mod.arange(int(sr * duration), dtype=np_mod.float32) / sr
        return (0.5 * np_mod.sin(2 * np_mod.pi * freq * t)).astype(np_mod.float32)

    @pytest.mark.voice
    def test_write_then_read_flac_roundtrip(self, tmp_path: Path) -> None:
        """Write float32 to FLAC, read back — within int16 quantization tolerance."""
        pytest.importorskip("soundfile")
        import numpy as np_mod

        from music_attribution.voice.degradation import read_audio, write_audio

        audio = self._sine_wave()
        flac_path = tmp_path / "test.flac"
        write_audio(flac_path, audio, sample_rate=16000)
        recovered, sr = read_audio(flac_path)
        assert sr == 16000
        assert np_mod.allclose(audio, recovered, atol=1 / 32768)

    @pytest.mark.voice
    def test_read_audio_returns_float32(self, tmp_path: Path) -> None:
        """read_audio() returns float32 numpy array."""
        pytest.importorskip("soundfile")
        import numpy as np_mod

        from music_attribution.voice.degradation import read_audio, write_audio

        audio = self._sine_wave()
        flac_path = tmp_path / "test.flac"
        write_audio(flac_path, audio)
        recovered, _ = read_audio(flac_path)
        assert recovered.dtype == np_mod.float32

    @pytest.mark.voice
    def test_read_audio_returns_correct_sample_rate(self, tmp_path: Path) -> None:
        """read_audio() returns the correct sample rate."""
        pytest.importorskip("soundfile")

        from music_attribution.voice.degradation import read_audio, write_audio

        audio = self._sine_wave()
        flac_path = tmp_path / "test.flac"
        write_audio(flac_path, audio, sample_rate=16000)
        _, sr = read_audio(flac_path)
        assert sr == 16000

    @pytest.mark.voice
    def test_write_audio_creates_flac_file(self, tmp_path: Path) -> None:
        """write_audio() creates a .flac file."""
        pytest.importorskip("soundfile")

        from music_attribution.voice.degradation import write_audio

        audio = self._sine_wave()
        flac_path = tmp_path / "test.flac"
        write_audio(flac_path, audio)
        assert flac_path.exists()
        assert flac_path.suffix == ".flac"

    @pytest.mark.voice
    def test_write_audio_creates_parent_dirs(self, tmp_path: Path) -> None:
        """write_audio() creates parent directories if needed."""
        pytest.importorskip("soundfile")

        from music_attribution.voice.degradation import write_audio

        audio = self._sine_wave()
        flac_path = tmp_path / "a" / "b" / "test.flac"
        write_audio(flac_path, audio)
        assert flac_path.exists()

    @pytest.mark.voice
    def test_write_audio_file_size_reasonable(self, tmp_path: Path) -> None:
        """3s audio FLAC is between 1KB and 100KB."""
        pytest.importorskip("soundfile")

        from music_attribution.voice.degradation import write_audio

        audio = self._sine_wave(duration=3.0)
        flac_path = tmp_path / "test.flac"
        write_audio(flac_path, audio)
        size = flac_path.stat().st_size
        assert 1000 < size < 100_000


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
