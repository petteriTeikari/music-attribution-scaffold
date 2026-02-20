"""Voice agent demo script — try it in 30 seconds.

Usage::

    uv run python scripts/voice_demo.py
    uv run python scripts/voice_demo.py --stt whisper --tts piper
    uv run python scripts/voice_demo.py --stt deepgram --tts elevenlabs

This is the "Quick Start" entry point for readers of the SSRN paper.
It creates a voice pipeline with the selected providers and runs it
using the local microphone and speaker via Pipecat's WebSocket transport.

For fully local (zero API cost) mode::

    uv run python scripts/voice_demo.py --stt whisper --tts piper --whisper-model small

See Also
--------
docs/tutorials/voice-agent-implementation.md : Full implementation guide.
src/music_attribution/voice/config.py : All configuration options.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys

logger = logging.getLogger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for voice demo.

    Parameters
    ----------
    argv : list[str] | None
        Command-line arguments (defaults to sys.argv).

    Returns
    -------
    argparse.Namespace
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Music Attribution Voice Agent Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  uv run python scripts/voice_demo.py\n"
            "  uv run python scripts/voice_demo.py --stt deepgram --tts elevenlabs\n"
            "  uv run python scripts/voice_demo.py --whisper-model large\n"
        ),
    )
    parser.add_argument(
        "--stt",
        choices=["whisper", "deepgram", "assemblyai"],
        default="whisper",
        help="Speech-to-text provider (default: whisper)",
    )
    parser.add_argument(
        "--tts",
        choices=["piper", "kokoro", "elevenlabs", "cartesia"],
        default="piper",
        help="Text-to-speech provider (default: piper)",
    )
    parser.add_argument(
        "--transport",
        choices=["websocket", "smallwebrtc", "daily"],
        default="websocket",
        help="Audio transport type (default: websocket)",
    )
    parser.add_argument(
        "--whisper-model",
        choices=["tiny", "base", "small", "medium", "large"],
        default="small",
        help="Whisper model size (default: small)",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Server bind host (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8001,
        help="Server port (default: 8001)",
    )
    parser.add_argument(
        "--drift-monitoring",
        action="store_true",
        help="Enable persona drift monitoring",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )
    return parser.parse_args(argv)


async def main(argv: list[str] | None = None) -> None:
    """Run the voice agent demo.

    Parameters
    ----------
    argv : list[str] | None
        Command-line arguments (defaults to sys.argv).
    """
    args = parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    from music_attribution.voice.config import VoiceConfig

    config = VoiceConfig(
        stt_provider=args.stt,
        tts_provider=args.tts,
        transport=args.transport,
        whisper_model=args.whisper_model,
        server_host=args.host,
        server_port=args.port,
        drift_monitoring=args.drift_monitoring,
    )

    logger.info(
        "Starting voice agent demo: STT=%s, TTS=%s, transport=%s",
        config.stt_provider.value,
        config.tts_provider.value,
        config.transport.value,
    )

    from music_attribution.voice.pipeline import PIPECAT_AVAILABLE

    if not PIPECAT_AVAILABLE:
        logger.error("pipecat-ai is not installed. Install with: uv sync --group voice")
        sys.exit(1)

    # Create pipeline configuration
    from music_attribution.voice.pipeline import create_voice_pipeline

    pipeline_config = create_voice_pipeline(config)

    logger.info("Pipeline configured: %s", pipeline_config)
    logger.info(
        "Voice agent ready. Connect via WebSocket at ws://%s:%d/api/v1/voice/ws",
        config.server_host,
        config.server_port,
    )

    # Start FastAPI server with voice router
    import uvicorn
    from fastapi import FastAPI

    from music_attribution.voice.server import create_voice_router

    app = FastAPI(title="Music Attribution Voice Agent Demo")
    app.include_router(create_voice_router())

    server_config = uvicorn.Config(
        app,
        host=config.server_host,
        port=config.server_port,
        log_level="debug" if args.verbose else "info",
    )
    server = uvicorn.Server(server_config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
