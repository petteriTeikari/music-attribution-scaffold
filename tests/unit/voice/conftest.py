"""Shared fixtures for voice agent tests."""

from __future__ import annotations

import pytest

from music_attribution.voice.config import VoiceConfig


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
