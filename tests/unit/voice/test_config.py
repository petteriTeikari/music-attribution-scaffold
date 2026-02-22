"""Tests for voice agent configuration module."""

from __future__ import annotations

import pytest

from music_attribution.voice.config import (
    STTProvider,
    TransportType,
    TTSProvider,
    VoiceConfig,
)


class TestSTTProvider:
    """Tests for STT provider enum."""

    def test_whisper_is_default(self) -> None:
        """Whisper is the open-source default STT provider."""
        config = VoiceConfig()
        assert config.stt_provider == STTProvider.WHISPER

    def test_all_providers_defined(self) -> None:
        """All expected STT providers are available."""
        expected = {"whisper", "deepgram", "assemblyai"}
        actual = {p.value for p in STTProvider}
        assert expected == actual


class TestTTSProvider:
    """Tests for TTS provider enum."""

    def test_piper_is_default(self) -> None:
        """Piper is the open-source default TTS provider."""
        config = VoiceConfig()
        assert config.tts_provider == TTSProvider.PIPER

    def test_all_providers_defined(self) -> None:
        """All expected TTS providers are available."""
        expected = {"piper", "kokoro", "elevenlabs", "cartesia"}
        actual = {p.value for p in TTSProvider}
        assert expected == actual


class TestTransportType:
    """Tests for transport type enum."""

    def test_websocket_is_default(self) -> None:
        """WebSocket is the default dev transport."""
        config = VoiceConfig()
        assert config.transport == TransportType.WEBSOCKET

    def test_all_transports_defined(self) -> None:
        """All expected transports are available."""
        expected = {"websocket", "smallwebrtc", "daily"}
        actual = {t.value for t in TransportType}
        assert expected == actual


class TestVoiceConfig:
    """Tests for the VoiceConfig settings model."""

    def test_defaults_are_open_source(self) -> None:
        """Default config uses fully open-source stack."""
        config = VoiceConfig()
        assert config.stt_provider == STTProvider.WHISPER
        assert config.tts_provider == TTSProvider.PIPER
        assert config.transport == TransportType.WEBSOCKET
        assert config.persona_enabled is False
        assert config.drift_monitoring is False
        assert config.guardrails_enabled is False

    def test_whisper_model_default(self) -> None:
        """Default Whisper model is 'small' for balance of speed/quality."""
        config = VoiceConfig()
        assert config.whisper_model == "small"

    def test_api_keys_optional(self) -> None:
        """All commercial API keys are optional (None by default)."""
        config = VoiceConfig()
        assert config.deepgram_api_key is None
        assert config.elevenlabs_api_key is None
        assert config.cartesia_api_key is None
        assert config.daily_api_key is None

    def test_persona_settings_optional(self) -> None:
        """Persona management settings are optional."""
        config = VoiceConfig()
        assert config.letta_base_url is None
        assert config.mem0_api_key is None

    def test_commercial_provider_requires_api_key_validation(self) -> None:
        """Config can be created with commercial providers and API keys."""
        config = VoiceConfig(
            stt_provider="deepgram",
            deepgram_api_key="test-key",  # pragma: allowlist secret
        )
        assert config.stt_provider == STTProvider.DEEPGRAM
        assert config.deepgram_api_key == "test-key"  # pragma: allowlist secret

    def test_drift_monitoring_settings(self) -> None:
        """Drift monitoring has configurable thresholds."""
        config = VoiceConfig(drift_monitoring=True)
        assert config.drift_monitoring is True
        assert config.drift_sync_threshold == pytest.approx(0.85)
        assert config.drift_desync_threshold == pytest.approx(0.70)
        assert config.drift_ewma_alpha == pytest.approx(0.3)

    def test_persona_reinforcement_interval(self) -> None:
        """Persona reinforcement triggers every N turns."""
        config = VoiceConfig()
        assert config.persona_reinforcement_interval == 5

    def test_vad_params_have_defaults(self) -> None:
        """VAD parameters have sensible defaults."""
        config = VoiceConfig()
        assert config.vad_threshold > 0
        assert config.vad_min_speech_ms > 0
        assert config.vad_min_silence_ms > 0

    def test_from_env_prefix(self) -> None:
        """VoiceConfig uses VOICE_ prefix for env vars."""
        assert VoiceConfig.model_config.get("env_prefix") == "VOICE_"

    def test_voice_port_configurable(self) -> None:
        """Voice server port is configurable."""
        config = VoiceConfig(server_port=8001)
        assert config.server_port == 8001

    def test_voice_host_configurable(self) -> None:
        """Voice server host is configurable."""
        config = VoiceConfig(server_host="127.0.0.1")
        assert config.server_host == "127.0.0.1"
