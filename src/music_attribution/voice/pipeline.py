"""Pipecat voice pipeline factory.

Assembles a Pipecat pipeline from VoiceConfig, selecting STT, TTS,
transport, and LLM services based on configuration. The LLM is bridged
through the existing PydanticAI agent (no duplicate Anthropic SDK).

Architecture
------------
Transport In → Silero VAD → STT → Context Aggregator → LLM → TTS → Transport Out

When Pipecat is not installed (base package without ``[voice]`` extras),
returns a configuration dict for testing. When installed, returns a real
``Pipeline`` object ready to be wrapped in ``PipelineTask``.

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

# Conditional Pipecat imports — the voice extras are optional.
try:
    from pipecat.adapters.schemas.tools_schema import ToolsSchema
    from pipecat.audio.vad.silero import SileroVADAnalyzer
    from pipecat.pipeline.pipeline import Pipeline
    from pipecat.pipeline.task import PipelineParams, PipelineTask
    from pipecat.processors.aggregators.llm_context import LLMContext
    from pipecat.processors.aggregators.llm_response_universal import (
        LLMContextAggregatorPair,
        LLMUserAggregatorParams,
    )

    PIPECAT_AVAILABLE = True
except ImportError:
    PIPECAT_AVAILABLE = False


def get_pipeline_config(config: VoiceConfig) -> dict[str, Any]:
    """Return a pipeline configuration dict for inspection and testing.

    This is a lightweight function that summarizes the pipeline config
    without creating any Pipecat objects. Useful for health checks,
    logging, and testing without Pipecat installed.

    Parameters
    ----------
    config : VoiceConfig
        Voice agent configuration (single source of truth).

    Returns
    -------
    dict
        Configuration dict describing the pipeline settings.
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


def create_stt_service(config: VoiceConfig) -> Any:
    """Create an STT service based on config.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration with STT provider selection.

    Returns
    -------
    Any
        A Pipecat STT service instance.

    Raises
    ------
    ImportError
        If Pipecat is not installed.
    ValueError
        If the STT provider is not recognized.
    """
    if not PIPECAT_AVAILABLE:
        msg = "pipecat-ai is not installed. Install with: uv sync --group voice"
        raise ImportError(msg)

    from music_attribution.voice.config import STTProvider

    if config.stt_provider == STTProvider.WHISPER:
        from pipecat.services.whisper.stt import WhisperSTTService

        return WhisperSTTService(model=config.whisper_model)

    if config.stt_provider == STTProvider.DEEPGRAM:
        from pipecat.services.deepgram.stt import DeepgramSTTService

        if not config.deepgram_api_key:
            msg = "VOICE_DEEPGRAM_API_KEY required for Deepgram STT"
            raise ValueError(msg)
        return DeepgramSTTService(api_key=config.deepgram_api_key)

    if config.stt_provider == STTProvider.ASSEMBLYAI:
        from pipecat.services.assemblyai.stt import AssemblyAISTTService

        if not config.assemblyai_api_key:
            msg = "VOICE_ASSEMBLYAI_API_KEY required for AssemblyAI STT"
            raise ValueError(msg)
        return AssemblyAISTTService(api_key=config.assemblyai_api_key)

    msg = f"Unknown STT provider: {config.stt_provider}"
    raise ValueError(msg)


def create_tts_service(config: VoiceConfig) -> Any:
    """Create a TTS service based on config.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration with TTS provider selection.

    Returns
    -------
    Any
        A Pipecat TTS service instance.

    Raises
    ------
    ImportError
        If Pipecat is not installed.
    ValueError
        If the TTS provider is not recognized or API key is missing.
    """
    if not PIPECAT_AVAILABLE:
        msg = "pipecat-ai is not installed. Install with: uv sync --group voice"
        raise ImportError(msg)

    from music_attribution.voice.config import TTSProvider

    if config.tts_provider == TTSProvider.PIPER:
        from pipecat.services.piper.tts import PiperTTSService

        return PiperTTSService()

    if config.tts_provider == TTSProvider.ELEVENLABS:
        from pipecat.services.elevenlabs.tts import ElevenLabsTTSService

        if not config.elevenlabs_api_key:
            msg = "VOICE_ELEVENLABS_API_KEY required for ElevenLabs TTS"
            raise ValueError(msg)
        return ElevenLabsTTSService(api_key=config.elevenlabs_api_key)

    if config.tts_provider == TTSProvider.CARTESIA:
        from pipecat.services.cartesia.tts import CartesiaTTSService

        if not config.cartesia_api_key:
            msg = "VOICE_CARTESIA_API_KEY required for Cartesia TTS"
            raise ValueError(msg)
        return CartesiaTTSService(api_key=config.cartesia_api_key)

    if config.tts_provider == TTSProvider.KOKORO:
        # Kokoro is not yet a Pipecat extra — use Piper as fallback
        logger.warning("Kokoro TTS not yet available in Pipecat; falling back to Piper")
        from pipecat.services.piper.tts import PiperTTSService

        return PiperTTSService()

    msg = f"Unknown TTS provider: {config.tts_provider}"
    raise ValueError(msg)


def create_llm_service(config: VoiceConfig) -> Any:
    """Create an LLM service for the voice pipeline.

    Uses OpenAI-compatible API to avoid the anthropic SDK version conflict
    between pipecat-ai (<0.50) and pydantic-ai-slim (>=0.70).

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration.

    Returns
    -------
    Any
        A Pipecat LLM service instance with domain tools registered.

    Raises
    ------
    ImportError
        If Pipecat is not installed.
    """
    if not PIPECAT_AVAILABLE:
        msg = "pipecat-ai is not installed. Install with: uv sync --group voice"
        raise ImportError(msg)

    from pipecat.services.openai.llm import OpenAILLMService

    from music_attribution.voice.tools import register_domain_tools

    if not config.llm_api_key:
        msg = "VOICE_LLM_API_KEY must be set for voice pipeline LLM. Set it in .env or environment variables."
        raise ValueError(msg)

    logger.info("Creating LLM service (model=%s, transport=%s)", config.llm_model, config.transport.value)

    llm = OpenAILLMService(
        api_key=config.llm_api_key,
        model=config.llm_model,
    )

    # Register domain tools as function handlers
    register_domain_tools(llm)

    return llm


def build_pipecat_pipeline(
    config: VoiceConfig,
    *,
    transport: Any | None = None,
) -> Any:
    """Build a real Pipecat pipeline with all services.

    This is the production pipeline factory. Call it with a transport
    (WebSocket, SmallWebRTC, or Daily) to get a running pipeline.

    Parameters
    ----------
    config : VoiceConfig
        Voice agent configuration.
    transport : Any | None
        Pre-created transport. If None, creates based on config.

    Returns
    -------
    tuple[Pipeline, PipelineTask]
        The assembled pipeline and its task wrapper.

    Raises
    ------
    ImportError
        If Pipecat is not installed.
    """
    if not PIPECAT_AVAILABLE:
        msg = "pipecat-ai is not installed. Install with: uv sync --group voice"
        raise ImportError(msg)

    from music_attribution.voice.persona import build_system_prompt
    from music_attribution.voice.tools import get_function_schemas

    # Create services
    stt = create_stt_service(config)
    tts = create_tts_service(config)
    llm = create_llm_service(config)

    # Build system prompt
    system_prompt = build_system_prompt(config)

    # Build tools schema
    tool_schemas = get_function_schemas()
    tools = ToolsSchema(standard_tools=tool_schemas)

    # Context setup
    messages = [{"role": "system", "content": system_prompt}]
    context = LLMContext(messages, tools)

    user_aggregator, assistant_aggregator = LLMContextAggregatorPair(
        context,
        user_params=LLMUserAggregatorParams(vad_analyzer=SileroVADAnalyzer()),
    )

    # Build pipeline processors list
    processors: list[Any] = []
    if transport is not None:
        processors.append(transport.input())
    processors.extend([stt, user_aggregator, llm, tts])
    if transport is not None:
        processors.append(transport.output())
    processors.append(assistant_aggregator)

    # Optional: add drift monitor
    if config.drift_monitoring:
        from music_attribution.voice.drift import DriftMonitorProcessor

        drift_monitor = DriftMonitorProcessor(config, system_prompt)
        # Insert after LLM, before TTS
        llm_idx = processors.index(llm)
        processors.insert(llm_idx + 1, drift_monitor)

    pipeline = Pipeline(processors)
    task = PipelineTask(
        pipeline,
        params=PipelineParams(
            enable_metrics=True,
            enable_usage_metrics=True,
        ),
    )

    logger.info(
        "Pipecat pipeline built: %d processors, STT=%s, TTS=%s",
        len(processors),
        config.stt_provider.value,
        config.tts_provider.value,
    )

    return pipeline, task
