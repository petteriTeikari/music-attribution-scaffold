"""Voice agent configuration — single source of truth.

All voice pipeline settings are defined here as a Pydantic Settings model.
Environment variables use the ``VOICE_`` prefix. Every setting has a
sensible default for the open-source stack so the voice agent runs
without any API keys.

Provider Swapping
-----------------
Changing a provider is a one-line config change::

    # Open-source default
    VOICE_STT_PROVIDER = whisper
    VOICE_TTS_PROVIDER = piper

    # Commercial swap
    VOICE_STT_PROVIDER = deepgram
    VOICE_DEEPGRAM_API_KEY = your - key
    VOICE_TTS_PROVIDER = elevenlabs
    VOICE_ELEVENLABS_API_KEY = your - key

See Also
--------
docs/tutorials/voice-agent-implementation.md : Full provider comparison.
docs/prd/decisions/L3-implementation/voice-agent-stack.decision.yaml : PRD node.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Final

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# ── Pipeline constants — single source of truth for sample rates and defaults ──
PIPELINE_SAMPLE_RATE: Final[int] = 16_000
"""Whisper/STT target sample rate (Hz)."""

PIPER_NATIVE_SAMPLE_RATE: Final[int] = 22_050
"""Piper TTS native output sample rate (Hz)."""

DEFAULT_PIPER_VOICE_ID: Final[str] = "en_US-lessac-medium"
"""Default Piper TTS voice model identifier."""


class STTProvider(str, Enum):
    """Speech-to-text provider selection.

    Each value maps to a Pipecat service class in ``pipeline.py``.
    """

    WHISPER = "whisper"
    DEEPGRAM = "deepgram"
    ASSEMBLYAI = "assemblyai"


class TTSProvider(str, Enum):
    """Text-to-speech provider selection.

    Each value maps to a Pipecat service class in ``pipeline.py``.
    """

    PIPER = "piper"
    KOKORO = "kokoro"
    ELEVENLABS = "elevenlabs"
    CARTESIA = "cartesia"


class TransportType(str, Enum):
    """Audio transport layer selection.

    WebSocket is the simplest for development. SmallWebRTC provides
    peer-to-peer audio (non-commercial license). Daily WebRTC is the
    production option via Pipecat Cloud.
    """

    WEBSOCKET = "websocket"
    SMALLWEBRTC = "smallwebrtc"
    DAILY = "daily"


class VoiceConfig(BaseSettings):
    """Voice agent configuration loaded from environment variables.

    All settings have open-source defaults. Commercial API keys are
    optional — only needed when switching to commercial providers.

    Attributes
    ----------
    stt_provider : STTProvider
        Speech-to-text engine (default: whisper).
    tts_provider : TTSProvider
        Text-to-speech engine (default: piper).
    transport : TransportType
        Audio transport (default: websocket).
    whisper_model : str
        Whisper model size (default: small).
    persona_enabled : bool
        Enable Letta/Mem0 persona management (default: false).
    drift_monitoring : bool
        Enable embedding-based drift detection (default: false).
    guardrails_enabled : bool
        Enable NeMo Guardrails persona boundary rails (default: false).
    """

    model_config = SettingsConfigDict(
        env_prefix="VOICE_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Provider Selection ──────────────────────────────────────────
    stt_provider: STTProvider = Field(
        default=STTProvider.WHISPER,
        description="Speech-to-text provider",
    )
    tts_provider: TTSProvider = Field(
        default=TTSProvider.PIPER,
        description="Text-to-speech provider",
    )
    transport: TransportType = Field(
        default=TransportType.WEBSOCKET,
        description="Audio transport type",
    )

    # ── STT Settings ────────────────────────────────────────────────
    whisper_model: str = Field(
        default="small",
        description="Whisper model size: tiny, base, small, medium, large",
    )

    # ── Server Settings ─────────────────────────────────────────────
    server_host: str = Field(
        default="0.0.0.0",
        description="Voice server bind host",
    )
    server_port: int = Field(
        default=8001,
        description="Voice server port",
    )

    # ── VAD Settings ────────────────────────────────────────────────
    vad_threshold: float = Field(
        default=0.5,
        description="Silero VAD speech probability threshold",
    )
    vad_min_speech_ms: int = Field(
        default=250,
        description="Minimum speech duration in ms to trigger STT",
    )
    vad_min_silence_ms: int = Field(
        default=300,
        description="Minimum silence duration in ms to end utterance",
    )

    # ── Persona Settings ────────────────────────────────────────────
    persona_enabled: bool = Field(
        default=False,
        description="Enable Letta/Mem0 persona management",
    )
    persona_reinforcement_interval: int = Field(
        default=5,
        description="Inject persona reminder every N turns",
    )
    letta_base_url: str | None = Field(
        default=None,
        description="Letta server URL (e.g. http://localhost:8283)",
    )
    mem0_api_key: str | None = Field(
        default=None,
        description="Mem0 API key (for mem0.ai platform)",
    )

    # ── Drift Detection ─────────────────────────────────────────────
    drift_monitoring: bool = Field(
        default=False,
        description="Enable embedding-based persona drift detection",
    )
    drift_sync_threshold: float = Field(
        default=0.85,
        description="Cosine similarity above which agent is 'in sync'",
    )
    drift_desync_threshold: float = Field(
        default=0.70,
        description="Cosine similarity below which agent is 'desynced'",
    )
    drift_ewma_alpha: float = Field(
        default=0.3,
        description="EWMA smoothing factor for drift scores",
    )

    # ── Guardrails ──────────────────────────────────────────────────
    guardrails_enabled: bool = Field(
        default=False,
        description="Enable NeMo Guardrails persona boundary rails",
    )

    # ── LLM Settings ──────────────────────────────────────────────────
    llm_api_key: str | None = Field(
        default=None,
        description="API key for the voice pipeline LLM (OpenAI-compatible)",
    )
    llm_model: str = Field(
        default="gpt-4o-mini",
        description="LLM model name for voice pipeline (OpenAI-compatible)",
    )

    # ── TTS Voice IDs ──────────────────────────────────────────────
    piper_voice_id: str = Field(
        default=DEFAULT_PIPER_VOICE_ID,
        description="Piper voice model name (auto-downloaded on first use)",
    )
    piper_model_dir: Path | None = Field(
        default=None,
        description="Explicit directory for Piper ONNX models (auto-discovered if None)",
    )
    elevenlabs_voice_id: str = Field(
        default="21m00Tcm4TlvDq8ikWAM",
        description="ElevenLabs voice ID (default: Rachel)",
    )
    cartesia_voice_id: str = Field(
        default="a0e99841-438c-4a64-b679-ae501e7d6091",
        description="Cartesia voice ID (default: Barbershop Man)",
    )

    # ── Commercial API Keys (all optional) ──────────────────────────
    deepgram_api_key: str | None = Field(
        default=None,
        description="Deepgram API key (for STT)",
    )
    elevenlabs_api_key: str | None = Field(
        default=None,
        description="ElevenLabs API key (for TTS)",
    )
    cartesia_api_key: str | None = Field(
        default=None,
        description="Cartesia API key (for TTS)",
    )
    daily_api_key: str | None = Field(
        default=None,
        description="Daily API key (for WebRTC transport)",
    )
    assemblyai_api_key: str | None = Field(
        default=None,
        description="AssemblyAI API key (for STT)",
    )
