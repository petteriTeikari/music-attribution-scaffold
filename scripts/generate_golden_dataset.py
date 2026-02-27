"""Generate golden voice dataset: 20 commands × 5 presets = 100 FLAC fixtures.

Usage:
    uv run --group voice-gpl --group voice-test \
        python scripts/generate_golden_dataset.py

Requires Piper TTS (pipecat-ai[piper]) for synthesis and soxr for resampling.
"""

from __future__ import annotations

import logging
import subprocess
import tempfile
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

# Target sample rate for all fixtures
TARGET_SR = 16000

# Piper native output rate
PIPER_SR = 22050


def _call_piper_tts(
    text: str,
    voice_id: str = "en_US-lessac-medium",
) -> tuple[np.ndarray, int]:
    """Call Piper TTS via subprocess to synthesize speech.

    Args:
        text: Text to synthesize.
        voice_id: Piper voice model identifier.

    Returns:
        Tuple of (audio_array_float32, sample_rate).
    """
    import soundfile as sf

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        cmd = [
            "piper",
            "--model",
            voice_id,
            "--output_file",
            str(tmp_path),
        ]
        subprocess.run(
            cmd,
            input=text.encode("utf-8"),
            check=True,
            capture_output=True,
        )
        audio, sr = sf.read(str(tmp_path), dtype="float32")
        return audio, sr
    finally:
        tmp_path.unlink(missing_ok=True)


def synthesize_command(
    text: str,
    voice_id: str = "en_US-lessac-medium",
) -> tuple[np.ndarray, int]:
    """Synthesize a voice command and resample to 16kHz.

    Args:
        text: Command text to synthesize.
        voice_id: Piper voice model identifier.

    Returns:
        Tuple of (audio_float32_16kHz, 16000).
    """
    import soxr

    audio, sr = _call_piper_tts(text, voice_id)

    # Resample from Piper native rate to target rate
    if sr != TARGET_SR:
        audio = soxr.resample(audio, sr, TARGET_SR, quality="HQ")

    return audio.astype(np.float32), TARGET_SR


def generate_clean_fixtures(
    output_dir: Path,
    voice_id: str = "en_US-lessac-medium",
) -> list[Path]:
    """Generate 20 clean FLAC fixtures from GOLDEN_COMMANDS.

    Args:
        output_dir: Directory to write FLAC files to.
        voice_id: Piper voice model identifier.

    Returns:
        List of created FLAC file paths.
    """
    from music_attribution.voice.degradation import write_audio
    from music_attribution.voice.golden_commands import GOLDEN_COMMANDS

    paths: list[Path] = []
    for cmd in GOLDEN_COMMANDS:
        audio, sr = synthesize_command(cmd["text"], voice_id)
        filename = f"{cmd['id']}_clean.flac"
        path = output_dir / filename
        write_audio(path, audio, sample_rate=sr)
        paths.append(path)
        logger.info("Generated %s (%d samples)", filename, len(audio))

    return paths
