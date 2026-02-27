"""Shared Piper TTS model utilities.

Provides functions for finding, downloading, loading, and using Piper TTS
models via the Python API (no subprocess calls). Used by both
``scripts/generate_golden_dataset.py`` and ``scripts/benchmark_voice.py``.

See Also
--------
piper.download_voices : Upstream download utility (HuggingFace).
"""

from __future__ import annotations

import io
import logging
import wave
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from music_attribution.voice.config import DEFAULT_PIPER_VOICE_ID

if TYPE_CHECKING:
    from piper import PiperVoice

logger = logging.getLogger(__name__)

# Standard search directories for cached Piper ONNX models
_MODEL_SEARCH_DIRS: list[Path] = [
    Path.home() / ".local" / "share" / "piper",
    Path.home() / ".cache" / "piper",
    Path("/tmp") / "piper",  # noqa: S108
]


def find_piper_model(
    voice_id: str = DEFAULT_PIPER_VOICE_ID,
    model_dir: Path | None = None,
) -> Path | None:
    """Search common locations for an existing Piper ONNX model.

    Args:
        voice_id: Piper voice model identifier (e.g., "en_US-lessac-medium").
        model_dir: Optional explicit directory to search first.

    Returns:
        Path to the ``.onnx`` file, or ``None`` if not found.
    """
    onnx_filename = f"{voice_id}.onnx"

    search_dirs = list(_MODEL_SEARCH_DIRS)
    if model_dir is not None:
        search_dirs.insert(0, model_dir)

    for d in search_dirs:
        candidate = d / onnx_filename
        if candidate.is_file():
            logger.info("Found Piper model: %s", candidate)
            return candidate
        # Also check for models in subdirectories
        if d.exists():
            matches = list(d.glob(f"**/{onnx_filename}"))
            if matches:
                logger.info("Found Piper model: %s", matches[0])
                return matches[0]

    return None


def download_piper_model(
    voice_id: str = DEFAULT_PIPER_VOICE_ID,
    download_dir: Path | None = None,
) -> Path:
    """Download a Piper voice model from HuggingFace.

    Uses ``piper.download_voices.download_voice`` to fetch the ONNX model
    and its JSON config.

    Args:
        voice_id: Piper voice model identifier (e.g., "en_US-lessac-medium").
        download_dir: Target directory for downloaded files. Defaults to
            ``~/.local/share/piper/``.

    Returns:
        Path to the downloaded ``.onnx`` file.

    Raises:
        ImportError: If ``piper`` is not installed.
        ValueError: If the voice_id doesn't match the expected pattern.
    """
    from piper.download_voices import download_voice

    if download_dir is None:
        download_dir = Path.home() / ".local" / "share" / "piper"

    download_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Downloading Piper model '%s' to %s ...", voice_id, download_dir)
    download_voice(voice_id, download_dir)

    model_path = download_dir / f"{voice_id}.onnx"
    if not model_path.is_file():
        msg = f"Download completed but model file not found: {model_path}"
        raise FileNotFoundError(msg)

    logger.info("Downloaded Piper model: %s", model_path)
    return model_path


def ensure_piper_model(
    voice_id: str = DEFAULT_PIPER_VOICE_ID,
    model_dir: Path | None = None,
) -> Path:
    """Find an existing Piper model or download it.

    Args:
        voice_id: Piper voice model identifier.
        model_dir: Optional explicit directory to search/download to.

    Returns:
        Path to the ``.onnx`` model file.
    """
    existing = find_piper_model(voice_id, model_dir)
    if existing is not None:
        return existing

    return download_piper_model(voice_id, download_dir=model_dir)


def load_piper_voice(
    voice_id: str = DEFAULT_PIPER_VOICE_ID,
    model_dir: Path | None = None,
) -> PiperVoice:
    """Load a Piper voice model, downloading if necessary.

    Args:
        voice_id: Piper voice model identifier.
        model_dir: Optional explicit directory for model files.

    Returns:
        Loaded ``PiperVoice`` instance ready for synthesis.

    Raises:
        ImportError: If ``piper`` package is not installed.
        FileNotFoundError: If model cannot be found or downloaded.
    """
    from piper import PiperVoice

    model_path = ensure_piper_model(voice_id, model_dir)
    logger.info("Loading Piper voice from %s", model_path)
    return PiperVoice.load(str(model_path))


def synthesize_speech(
    voice: PiperVoice,
    text: str,
) -> tuple[np.ndarray, int]:
    """Synthesize text to a float32 audio array using a loaded Piper voice.

    Uses ``voice.synthesize_wav()`` which handles WAV format setup
    automatically. The raw audio is then extracted as a float32 numpy array
    normalized to [-1.0, 1.0].

    Args:
        voice: Loaded ``PiperVoice`` instance.
        text: Text to synthesize.

    Returns:
        Tuple of (audio_float32_array, sample_rate).
    """
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        voice.synthesize_wav(text, wf)

    buf.seek(0)
    with wave.open(buf, "rb") as wf:
        sample_rate = wf.getframerate()
        n_frames = wf.getnframes()
        sample_width = wf.getsampwidth()
        raw_bytes = wf.readframes(n_frames)

    # Convert raw PCM bytes to float32 array
    if sample_width == 2:  # noqa: PLR2004
        audio_int = np.frombuffer(raw_bytes, dtype=np.int16)
        audio = audio_int.astype(np.float32) / 32768.0
    elif sample_width == 4:  # noqa: PLR2004
        audio_int = np.frombuffer(raw_bytes, dtype=np.int32)
        audio = audio_int.astype(np.float32) / 2147483648.0
    else:
        msg = f"Unsupported sample width: {sample_width}"
        raise ValueError(msg)

    return audio, sample_rate
