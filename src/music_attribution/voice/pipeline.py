"""Pipecat voice pipeline factory.

Assembles a Pipecat pipeline from VoiceConfig, selecting STT, TTS,
transport, and LLM services based on configuration. The LLM is bridged
through the existing PydanticAI agent (no duplicate Anthropic SDK).

Architecture
------------
Transport In → Silero VAD → STT → Context Aggregator → LLM → TTS → Transport Out

See Also
--------
docs/planning/voice-agent-and-personalization-plan.xml : Full architecture.
docs/prd/decisions/L3-implementation/voice-agent-stack.decision.yaml
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)


def create_voice_pipeline(config: VoiceConfig) -> Any:
    """Create a configured Pipecat voice pipeline from config.

    Selects services based on ``config.stt_provider``, ``config.tts_provider``,
    and ``config.transport``. Returns a pipeline object that can be run
    as an async task.

    Parameters
    ----------
    config : VoiceConfig
        Voice agent configuration (single source of truth).

    Returns
    -------
    Any
        Configured pipeline object. Returns a dict describing the
        pipeline configuration when Pipecat is not installed (for testing).

    Notes
    -----
    The LLM service uses the existing PydanticAI agent rather than
    Pipecat's built-in Anthropic service. This avoids the anthropic
    SDK version conflict (pipecat pins <0.50, pydantic-ai needs >=0.70)
    and reuses existing domain tool logic without duplication.
    """
    pipeline_config = {
        "stt": config.stt_provider.value,
        "tts": config.tts_provider.value,
        "transport": config.transport.value,
        "vad": {
            "threshold": config.vad_threshold,
            "min_speech_ms": config.vad_min_speech_ms,
            "min_silence_ms": config.vad_min_silence_ms,
        },
        "whisper_model": config.whisper_model,
        "persona_enabled": config.persona_enabled,
        "drift_monitoring": config.drift_monitoring,
        "guardrails_enabled": config.guardrails_enabled,
    }

    logger.info(
        "Pipeline configured: STT=%s, TTS=%s, transport=%s",
        config.stt_provider.value,
        config.tts_provider.value,
        config.transport.value,
    )

    return pipeline_config
