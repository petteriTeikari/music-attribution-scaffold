"""Audio degradation presets and pipeline for voice testing.

Provides reproducible audio degradation with 5 presets (CLEAN through EXTREME)
for generating golden dataset fixtures with controlled noise, reverb, frequency
shaping, and codec compression artifacts.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


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
