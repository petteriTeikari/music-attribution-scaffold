"""Tests for voice pipeline factory."""

from __future__ import annotations

from music_attribution.voice.config import VoiceConfig
from music_attribution.voice.pipeline import create_voice_pipeline


class TestCreateVoicePipeline:
    """Tests for the pipeline factory function."""

    def test_returns_config_dict(self) -> None:
        """Pipeline factory returns a configuration dict."""
        config = VoiceConfig()
        result = create_voice_pipeline(config)
        assert isinstance(result, dict)

    def test_default_stt_is_whisper(self) -> None:
        """Default pipeline uses Whisper STT."""
        config = VoiceConfig()
        result = create_voice_pipeline(config)
        assert result["stt"] == "whisper"

    def test_default_tts_is_piper(self) -> None:
        """Default pipeline uses Piper TTS."""
        config = VoiceConfig()
        result = create_voice_pipeline(config)
        assert result["tts"] == "piper"

    def test_default_transport_is_websocket(self) -> None:
        """Default pipeline uses WebSocket transport."""
        config = VoiceConfig()
        result = create_voice_pipeline(config)
        assert result["transport"] == "websocket"

    def test_vad_params_present(self) -> None:
        """Pipeline config includes VAD parameters."""
        config = VoiceConfig()
        result = create_voice_pipeline(config)
        assert "vad" in result
        assert "threshold" in result["vad"]
        assert "min_speech_ms" in result["vad"]
        assert "min_silence_ms" in result["vad"]

    def test_commercial_provider_selection(self) -> None:
        """Pipeline reflects commercial provider config."""
        config = VoiceConfig(
            stt_provider="deepgram",
            tts_provider="elevenlabs",
            transport="daily",
        )
        result = create_voice_pipeline(config)
        assert result["stt"] == "deepgram"
        assert result["tts"] == "elevenlabs"
        assert result["transport"] == "daily"

    def test_optional_features_reflected(self) -> None:
        """Pipeline config includes optional feature flags."""
        config = VoiceConfig(
            persona_enabled=True,
            drift_monitoring=True,
            guardrails_enabled=True,
        )
        result = create_voice_pipeline(config)
        assert result["persona_enabled"] is True
        assert result["drift_monitoring"] is True
        assert result["guardrails_enabled"] is True

    def test_whisper_model_in_config(self) -> None:
        """Pipeline config includes the Whisper model size."""
        config = VoiceConfig(whisper_model="large")
        result = create_voice_pipeline(config)
        assert result["whisper_model"] == "large"
