"""Audio degradation presets and pipeline for voice testing.

Provides reproducible audio degradation with 5 presets (CLEAN through EXTREME)
for generating golden dataset fixtures with controlled noise, reverb, frequency
shaping, and codec compression artifacts.
"""

from __future__ import annotations

import logging
import math
import random
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import numpy as np

from music_attribution.voice.config import PIPELINE_SAMPLE_RATE

logger = logging.getLogger(__name__)


class DegradationPreset(Enum):
    """Audio degradation preset levels."""

    CLEAN = "clean"
    OFFICE = "office"
    CODEC = "codec"
    NOISY_CAFE = "noisy_cafe"
    EXTREME = "extreme"


@dataclass(frozen=True)
class DegradationConfig:
    """Configuration for a single degradation preset.

    Attributes:
        snr_db: Signal-to-noise ratio in dB (inf = no noise).
        reverb_rt60: Reverberation time in seconds (0.0 = no reverb).
        low_cutoff_hz: High-pass filter cutoff frequency.
        high_cutoff_hz: Low-pass filter cutoff frequency.
        mp3_bitrate_kbps: Mp3 compression bitrate (None = lossless).
    """

    snr_db: float
    reverb_rt60: float
    low_cutoff_hz: float
    high_cutoff_hz: float
    mp3_bitrate_kbps: int | None


PRESETS: dict[DegradationPreset, DegradationConfig] = {
    DegradationPreset.CLEAN: DegradationConfig(
        snr_db=math.inf,
        reverb_rt60=0.0,
        low_cutoff_hz=20.0,
        high_cutoff_hz=20000.0,
        mp3_bitrate_kbps=None,
    ),
    DegradationPreset.OFFICE: DegradationConfig(
        snr_db=25.0,
        reverb_rt60=0.3,
        low_cutoff_hz=80.0,
        high_cutoff_hz=16000.0,
        mp3_bitrate_kbps=None,
    ),
    DegradationPreset.CODEC: DegradationConfig(
        snr_db=math.inf,
        reverb_rt60=0.0,
        low_cutoff_hz=20.0,
        high_cutoff_hz=20000.0,
        mp3_bitrate_kbps=32,
    ),
    DegradationPreset.NOISY_CAFE: DegradationConfig(
        snr_db=10.0,
        reverb_rt60=0.6,
        low_cutoff_hz=100.0,
        high_cutoff_hz=12000.0,
        mp3_bitrate_kbps=64,
    ),
    DegradationPreset.EXTREME: DegradationConfig(
        snr_db=5.0,
        reverb_rt60=1.2,
        low_cutoff_hz=200.0,
        high_cutoff_hz=8000.0,
        mp3_bitrate_kbps=16,
    ),
}


def apply_degradation(
    audio: np.ndarray,
    sample_rate: int,
    preset: DegradationPreset,
    seed: int = 42,
) -> np.ndarray:
    """Apply audio degradation pipeline for a given preset.

    Pipeline order: noise → filters → reverb → DC offset → clip → codec → clip.

    Args:
        audio: Input audio as float32 numpy array.
        sample_rate: Audio sample rate in Hz.
        preset: Degradation preset to apply.
        seed: Random seed for reproducibility.

    Returns:
        Degraded audio as float32 numpy array, clipped to [-1.0, 1.0].
    """
    config = PRESETS[preset]

    # Seed BOTH random sources for full determinism.
    # audiomentations reads from global random + numpy.random internally.
    random.seed(seed)
    np.random.seed(seed)

    # Step 1: Build audiomentations pipeline
    transforms: list = []

    # Additive noise — use AddGaussianSNR (NOT AddGaussianNoise!)
    if config.snr_db != float("inf"):
        from audiomentations import AddGaussianSNR

        transforms.append(
            AddGaussianSNR(
                min_snr_db=config.snr_db,
                max_snr_db=config.snr_db,
                p=1.0,
            )
        )

    # Frequency shaping — HighPassFilter + LowPassFilter combo
    if config.low_cutoff_hz > 20.0:
        from audiomentations import HighPassFilter

        transforms.append(
            HighPassFilter(
                min_cutoff_freq=config.low_cutoff_hz,
                max_cutoff_freq=config.low_cutoff_hz,
                p=1.0,
            )
        )
    if config.high_cutoff_hz < 20000.0:
        from audiomentations import LowPassFilter

        transforms.append(
            LowPassFilter(
                min_cutoff_freq=config.high_cutoff_hz,
                max_cutoff_freq=config.high_cutoff_hz,
                p=1.0,
            )
        )

    # Step 2: Apply audiomentations pipeline
    if transforms:
        from audiomentations import Compose

        pipeline = Compose(transforms)
        degraded = pipeline(samples=audio, sample_rate=sample_rate)
    else:
        degraded = audio.copy()

    # Step 3: Room reverb via pyroomacoustics (if RT60 > 0)
    if config.reverb_rt60 > 0:
        import pyroomacoustics as pra

        room_dim = [8.0, 6.0, 3.0]
        e_absorption, max_order = pra.inverse_sabine(config.reverb_rt60, room_dim)
        mat = pra.Material(e_absorption)
        room = pra.ShoeBox(
            room_dim,
            fs=sample_rate,
            materials=mat,
            max_order=max_order,
        )
        room.add_source([2.0, 3.0, 1.7], signal=degraded)
        room.add_microphone([5.0, 3.0, 1.5])
        room.simulate()
        # Output is LONGER than input due to reverb tail — keep it
        mic_signals = room.mic_array.signals  # type: ignore[union-attr]
        degraded = mic_signals[0].astype(np.float32)

    # Step 4: Remove DC offset
    degraded -= np.mean(degraded)

    # Step 5: Clip to [-1.0, 1.0]
    degraded = np.clip(degraded, -1.0, 1.0)

    # Step 6: Codec compression (if configured)
    if config.mp3_bitrate_kbps is not None:
        from audiomentations import Mp3Compression

        codec = Mp3Compression(
            min_bitrate=config.mp3_bitrate_kbps,
            max_bitrate=config.mp3_bitrate_kbps,
            p=1.0,
            backend="fast-mp3-augment",
        )
        degraded = codec(samples=degraded, sample_rate=sample_rate)

    # Step 7: Final clip + dtype
    result: np.ndarray = np.clip(degraded, -1.0, 1.0).astype(np.float32)
    return result


def write_audio(path: Path, audio: np.ndarray, sample_rate: int = PIPELINE_SAMPLE_RATE) -> None:
    """Write float32 audio to FLAC file with int16 subtype.

    Args:
        path: Output file path (parent dirs created automatically).
        audio: Audio data as float32 numpy array.
        sample_rate: Sample rate in Hz.
    """
    import soundfile as sf

    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(path), audio, sample_rate, subtype="PCM_16", format="FLAC")


def read_audio(path: Path) -> tuple[np.ndarray, int]:
    """Read audio from a FLAC file as float32.

    Args:
        path: Path to FLAC file.

    Returns:
        Tuple of (audio_array, sample_rate).
    """
    import soundfile as sf

    audio, sample_rate = sf.read(str(path), dtype="float32")
    return audio, sample_rate
