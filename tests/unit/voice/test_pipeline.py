"""Tests for voice pipeline factory."""

from __future__ import annotations

import pytest

from music_attribution.voice.config import STTProvider, TransportType, TTSProvider, VoiceConfig
from music_attribution.voice.pipeline import (
    PIPECAT_AVAILABLE,
    create_stt_service,
    create_tts_service,
    get_pipeline_config,
)


class TestGetPipelineConfig:
    """Tests for the pipeline config function."""

    def test_returns_config_dict(self) -> None:
        """Pipeline factory returns a configuration dict."""
        config = VoiceConfig()
        result = get_pipeline_config(config)
        assert isinstance(result, dict)

    def test_default_stt_is_whisper(self) -> None:
        """Default pipeline uses Whisper STT."""
        config = VoiceConfig()
        result = get_pipeline_config(config)
        assert result["stt"] == "whisper"

    def test_default_tts_is_piper(self) -> None:
        """Default pipeline uses Piper TTS."""
        config = VoiceConfig()
        result = get_pipeline_config(config)
        assert result["tts"] == "piper"

    def test_default_transport_is_websocket(self) -> None:
        """Default pipeline uses WebSocket transport."""
        config = VoiceConfig()
        result = get_pipeline_config(config)
        assert result["transport"] == "websocket"

    def test_vad_params_present(self) -> None:
        """Pipeline config includes VAD parameters."""
        config = VoiceConfig()
        result = get_pipeline_config(config)
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
        result = get_pipeline_config(config)
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
        result = get_pipeline_config(config)
        assert result["persona_enabled"] is True
        assert result["drift_monitoring"] is True
        assert result["guardrails_enabled"] is True

    def test_whisper_model_in_config(self) -> None:
        """Pipeline config includes the Whisper model size."""
        config = VoiceConfig(whisper_model="large")
        result = get_pipeline_config(config)
        assert result["whisper_model"] == "large"


class TestPipecatAvailability:
    """Tests for conditional Pipecat import handling."""

    def test_pipecat_available_is_bool(self) -> None:
        """PIPECAT_AVAILABLE is a boolean flag."""
        assert isinstance(PIPECAT_AVAILABLE, bool)

    @pytest.mark.skipif(PIPECAT_AVAILABLE, reason="Only test when pipecat NOT installed")
    def test_create_stt_raises_without_pipecat(self) -> None:
        """create_stt_service raises ImportError without pipecat."""
        config = VoiceConfig()
        with pytest.raises(ImportError, match="pipecat-ai is not installed"):
            create_stt_service(config)

    @pytest.mark.skipif(PIPECAT_AVAILABLE, reason="Only test when pipecat NOT installed")
    def test_create_tts_raises_without_pipecat(self) -> None:
        """create_tts_service raises ImportError without pipecat."""
        config = VoiceConfig()
        with pytest.raises(ImportError, match="pipecat-ai is not installed"):
            create_tts_service(config)


class TestProviderServiceFactory:
    """Tests for provider-specific service creation logic."""

    def test_stt_provider_enum_values(self) -> None:
        """All STT providers have expected string values."""
        assert STTProvider.WHISPER.value == "whisper"
        assert STTProvider.DEEPGRAM.value == "deepgram"
        assert STTProvider.ASSEMBLYAI.value == "assemblyai"

    def test_tts_provider_enum_values(self) -> None:
        """All TTS providers have expected string values."""
        assert TTSProvider.PIPER.value == "piper"
        assert TTSProvider.KOKORO.value == "kokoro"
        assert TTSProvider.ELEVENLABS.value == "elevenlabs"
        assert TTSProvider.CARTESIA.value == "cartesia"

    def test_transport_enum_values(self) -> None:
        """All transport types have expected string values."""
        assert TransportType.WEBSOCKET.value == "websocket"
        assert TransportType.SMALLWEBRTC.value == "smallwebrtc"
        assert TransportType.DAILY.value == "daily"

    def test_pipeline_config_all_providers(self) -> None:
        """Pipeline config works with all provider combinations."""
        for stt in STTProvider:
            for tts in TTSProvider:
                config = VoiceConfig(stt_provider=stt, tts_provider=tts)
                result = get_pipeline_config(config)
                assert result["stt"] == stt.value
                assert result["tts"] == tts.value
