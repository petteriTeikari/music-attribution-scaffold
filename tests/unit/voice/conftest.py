"""Shared fixtures for voice agent tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np
import pytest

from music_attribution.voice.config import VoiceConfig

if TYPE_CHECKING:
    pass


@pytest.fixture
def voice_config() -> VoiceConfig:
    """Return a VoiceConfig with all defaults (open-source stack)."""
    return VoiceConfig()


@pytest.fixture
def commercial_config() -> VoiceConfig:
    """Return a VoiceConfig simulating commercial provider selection."""
    return VoiceConfig(
        stt_provider="deepgram",
        tts_provider="elevenlabs",
        transport="daily",
        deepgram_api_key="test-key",  # pragma: allowlist secret
        elevenlabs_api_key="test-key",  # pragma: allowlist secret
        daily_api_key="test-key",  # pragma: allowlist secret
    )


# ─── Golden fixture helpers ────────────────────────────────────────────
# IMPORTANT: These are PLAIN PYTHON FUNCTIONS (not @pytest.fixture).
# They are called inside @pytest.mark.skipif() decorators, which are
# evaluated at MODULE COLLECTION TIME before any fixtures are resolved.

FIXTURES_DIR = Path(__file__).resolve().parent.parent.parent / "fixtures" / "voice" / "audio"


def golden_fixtures_available() -> bool:
    """Check if golden voice fixtures have been generated."""
    return (FIXTURES_DIR / "manifest.json").is_file()


def load_fixture(command_id: str, preset: str) -> tuple[np.ndarray, int]:
    """Load a golden fixture FLAC file as float32 audio.

    Args:
        command_id: Command identifier (e.g., "cmd_01").
        preset: Degradation preset name (e.g., "clean", "office").

    Returns:
        Tuple of (audio_array, sample_rate).
    """
    from music_attribution.voice.degradation import read_audio

    path = FIXTURES_DIR / f"{command_id}_{preset}.flac"
    return read_audio(path)


def load_manifest() -> dict:
    """Load the golden fixture manifest.

    Returns:
        Parsed manifest dict with version, seed, sample_rate, format, files.
    """
    return json.loads((FIXTURES_DIR / "manifest.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def whisper_model():
    """Session-scoped faster-whisper model for STT tests."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        pytest.skip("faster-whisper not installed")
    return WhisperModel("small", device="cpu", compute_type="int8")
