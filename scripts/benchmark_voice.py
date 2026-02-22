"""Voice pipeline benchmark: CPU vs GPU latency for STT, TTS, and drift.

Measures hardware capabilities and inference latency for each stage of the
voice pipeline. Generates a JSON report suitable for CI regression tracking.

Uses faster-whisper (CTranslate2) for STT and Piper for TTS — the same
libraries used by the production Pipecat pipeline.

Test audio is a synthetic 440 Hz sine wave (16 kHz, 16-bit, 10 s) created
in memory — no external audio files required.

Usage
-----
::

    uv run python scripts/benchmark_voice.py --models tiny,small --cpu-only
    uv run python scripts/benchmark_voice.py --output benchmark-results.json

See Also
--------
src/music_attribution/observability/voice_metrics.py : Prometheus metrics.
docs/prd/decisions/L5-operations/voice-pipeline-benchmarking.decision.yaml
docs/planning/voice-agent-benchmarking-plan.md : Full benchmarking plan.
"""

from __future__ import annotations

import argparse
import io
import json
import logging
import math
import resource
import struct
import time
import wave
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def _normalize_text(text: str) -> list[str]:
    """Normalize text for WER: lowercase, strip punctuation, split to words."""
    import re

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def compute_wer(reference: str, hypothesis: str) -> float:
    """Compute Word Error Rate between reference and hypothesis.

    Uses Levenshtein distance on word sequences after normalization
    (lowercase, strip punctuation).

    Parameters
    ----------
    reference : str
        Ground truth text.
    hypothesis : str
        Transcribed text to evaluate.

    Returns
    -------
    float
        WER in range [0.0, 1.0]. 0.0 = perfect, 1.0 = completely wrong.
    """
    ref_words = _normalize_text(reference)
    hyp_words = _normalize_text(hypothesis)

    if not ref_words and not hyp_words:
        return 0.0
    if not ref_words or not hyp_words:
        return 1.0

    n = len(ref_words)
    m = len(hyp_words)

    # Levenshtein distance on word sequences
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            if ref_words[i - 1] == hyp_words[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = temp

    return min(dp[m] / n, 1.0)


def check_domain_keywords(
    text: str,
    keywords: list[str],
) -> tuple[list[str], list[str]]:
    """Check which domain keywords appear in transcribed text.

    Parameters
    ----------
    text : str
        Transcribed text to check.
    keywords : list[str]
        Domain keywords to look for.

    Returns
    -------
    tuple[list[str], list[str]]
        (found, missed) keyword lists.
    """
    text_lower = text.lower()
    found = []
    missed = []
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
        else:
            missed.append(kw)
    return found, missed


# Models safe for GPUs with limited VRAM
_VRAM_THRESHOLDS: dict[str, float] = {
    "tiny": 1.0,
    "base": 1.5,
    "small": 3.0,
    "medium": 6.0,
    "large": 10.0,
}

_DEFAULT_MODELS = ["tiny", "base", "small", "medium"]
_BENCHMARK_ITERATIONS = 3

# ── Synthetic Voice Command Corpus ──────────────────────────────────
# Domain-specific utterances for TTS->STT round-trip accuracy testing.
# Categories: A = simple queries, B = action commands.
SYNTHETIC_COMMANDS: list[dict[str, Any]] = [
    {
        "id": "A1",
        "text": "What is the confidence score for Hide and Seek?",
        "category": "A",
        "domain_keywords": ["confidence", "score", "hide", "seek"],
    },
    {
        "id": "A2",
        "text": "Search for tracks by Imogen Heap",
        "category": "A",
        "domain_keywords": ["search", "tracks", "imogen", "heap"],
    },
    {
        "id": "A3",
        "text": "Show me low confidence attributions",
        "category": "A",
        "domain_keywords": ["confidence", "attributions"],
    },
    {
        "id": "A4",
        "text": "What does assurance level A2 mean?",
        "category": "A",
        "domain_keywords": ["assurance", "level"],
    },
    {
        "id": "B1",
        "text": "The songwriter for Headlock should be Imogen Heap, not unknown",
        "category": "B",
        "domain_keywords": ["songwriter", "headlock", "imogen", "heap"],
    },
    {
        "id": "B2",
        "text": "I rate this attribution a nine out of ten",
        "category": "B",
        "domain_keywords": ["rate", "attribution", "nine", "ten"],
    },
    {
        "id": "B3",
        "text": "Correct the artist name to Frou Frou",
        "category": "B",
        "domain_keywords": ["correct", "artist", "frou"],
    },
]


def detect_hardware() -> dict[str, Any]:
    """Detect CPU, GPU, VRAM, and CUDA availability.

    Returns
    -------
    dict[str, Any]
        Hardware information including cpu, gpu, vram_gb, cuda_available,
        and torch_version.
    """
    import platform

    hw: dict[str, Any] = {
        "cpu": platform.processor() or platform.machine(),
        "gpu": None,
        "vram_gb": 0,
        "cuda_available": False,
        "torch_version": None,
    }

    try:
        import torch

        hw["torch_version"] = torch.__version__
        hw["cuda_available"] = torch.cuda.is_available()
        if torch.cuda.is_available():
            props = torch.cuda.get_device_properties(0)
            hw["gpu"] = props.name
            hw["vram_gb"] = round(props.total_memory / (1024**3), 1)
    except ImportError:
        pass

    return hw


def generate_test_audio(duration_s: float = 10.0, sample_rate: int = 16000) -> bytes:
    """Generate a 440 Hz sine wave as 16-bit PCM WAV bytes.

    Parameters
    ----------
    duration_s : float
        Duration in seconds.
    sample_rate : int
        Sample rate in Hz.

    Returns
    -------
    bytes
        In-memory WAV file content.
    """
    n_samples = int(duration_s * sample_rate)
    samples = []
    for i in range(n_samples):
        t = i / sample_rate
        value = int(32767 * 0.5 * math.sin(2 * math.pi * 440 * t))
        samples.append(struct.pack("<h", value))

    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(samples))
    return buf.getvalue()


def _get_rss_mb() -> float:
    """Get current RSS in megabytes."""
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def _get_vram_mb() -> float:
    """Get peak VRAM allocated in megabytes (0 if no CUDA)."""
    try:
        import torch

        if torch.cuda.is_available():
            return torch.cuda.max_memory_allocated() / (1024**2)
    except ImportError:
        pass
    return 0.0


def _should_skip_model(model: str, device: str, vram_gb: float) -> bool:
    """Check if a model should be skipped based on VRAM constraints."""
    if device == "cpu":
        return False
    threshold = _VRAM_THRESHOLDS.get(model, 10.0)
    return vram_gb < threshold


def benchmark_stt(
    audio_path: Path,
    models: list[str],
    devices: list[str],
    vram_gb: float,
) -> list[dict[str, Any]]:
    """Benchmark faster-whisper STT inference.

    Uses CTranslate2 via faster-whisper — the same backend as the
    production Pipecat WhisperSTTService.

    Parameters
    ----------
    audio_path : Path
        Path to the test WAV file.
    models : list[str]
        Whisper model sizes to benchmark.
    devices : list[str]
        Devices to benchmark on (e.g., ["cpu", "cuda"]).
    vram_gb : float
        Available GPU VRAM in GB.

    Returns
    -------
    list[dict[str, Any]]
        Benchmark results per model x device combination.
    """
    results: list[dict[str, Any]] = []

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        logger.warning("faster-whisper not installed — skipping STT benchmarks")
        return results

    for model_name in models:
        for device in devices:
            if _should_skip_model(model_name, device, vram_gb):
                logger.info(
                    "Skipping %s on %s (VRAM %.1f GB < %.1f GB)",
                    model_name,
                    device,
                    vram_gb,
                    _VRAM_THRESHOLDS[model_name],
                )
                continue

            compute_type = "float16" if device == "cuda" else "int8"

            # Cold start: model load time
            t0 = time.perf_counter()
            try:
                model = WhisperModel(model_name, device=device, compute_type=compute_type)
            except Exception:
                logger.exception("Failed to load faster-whisper %s on %s", model_name, device)
                continue
            load_ms = (time.perf_counter() - t0) * 1000

            # Warm inference: multiple iterations, take median
            # Must consume the segments generator to measure full decode time
            latencies: list[float] = []
            for _ in range(_BENCHMARK_ITERATIONS):
                t0 = time.perf_counter()
                segments, _info = model.transcribe(str(audio_path))
                for _ in segments:
                    pass  # Force full decode — generator is lazy
                latencies.append((time.perf_counter() - t0) * 1000)

            latencies.sort()
            median_ms = latencies[len(latencies) // 2]

            results.append(
                {
                    "model": model_name,
                    "device": device,
                    "compute_type": compute_type,
                    "load_ms": round(load_ms, 1),
                    "inference_ms": round(median_ms, 1),
                    "rss_mb": round(_get_rss_mb(), 1),
                    "vram_mb": round(_get_vram_mb(), 1) if device == "cuda" else 0,
                }
            )

            # Free GPU memory between models
            del model
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except ImportError:
                pass

    return results


def benchmark_tts(piper_model: str | None = None) -> list[dict[str, Any]]:
    """Benchmark Piper TTS synthesis.

    Uses piper-tts directly — the same backend that Pipecat's
    PiperTTSService wraps.

    Parameters
    ----------
    piper_model : str | None
        Path to Piper ONNX model file. If None, uses Pipecat's
        PiperTTSService default model auto-download.

    Returns
    -------
    list[dict[str, Any]]
        Benchmark results for TTS providers.
    """
    results: list[dict[str, Any]] = []

    try:
        from piper import PiperVoice
    except ImportError:
        logger.warning("piper-tts not installed — skipping TTS benchmarks (install with: uv sync --group voice-gpl)")
        return results

    model_path = piper_model

    # Auto-discover model from Pipecat's default download location
    if model_path is None:
        search_dirs = [
            Path.home() / ".local/share/piper",
            Path.home() / ".cache/piper",
            Path("/tmp/piper"),  # noqa: S108
        ]
        for d in search_dirs:
            if d.exists():
                onnx_files = list(d.glob("**/*.onnx"))
                if onnx_files:
                    model_path = str(onnx_files[0])
                    logger.info("Found Piper model: %s", model_path)
                    break

    if model_path is None:
        logger.warning(
            "No Piper model found. Run the voice server once to auto-download, "
            "or pass --piper-model /path/to/model.onnx"
        )
        return results

    try:
        voice = PiperVoice.load(model_path)
        test_text = "This is a benchmark test for the voice synthesis pipeline."

        latencies: list[float] = []
        for _ in range(_BENCHMARK_ITERATIONS):
            buf = io.BytesIO()
            t0 = time.perf_counter()
            with wave.open(buf, "wb") as wf:
                voice.synthesize(test_text, wf)
            latencies.append((time.perf_counter() - t0) * 1000)

        latencies.sort()
        results.append(
            {
                "provider": "piper",
                "model": Path(model_path).stem,
                "synthesis_ms": round(latencies[len(latencies) // 2], 1),
                "text_length": len(test_text),
            }
        )
    except Exception:
        logger.exception("Piper TTS benchmark failed")

    return results


def benchmark_drift() -> list[dict[str, Any]]:
    """Benchmark drift detection (embedding encode + cosine).

    Returns
    -------
    list[dict[str, Any]]
        Benchmark results for drift scoring.
    """
    results: list[dict[str, Any]] = []

    try:
        from music_attribution.voice.config import VoiceConfig
        from music_attribution.voice.drift import DriftDetector

        config = VoiceConfig()
        reference = "I am a helpful music attribution assistant."
        detector = DriftDetector(config, reference)

        test_responses = [
            "Let me help you with that attribution query.",
            "The confidence score for this track is 0.87.",
            "I can see three sources agree on this songwriter credit.",
        ]

        latencies: list[float] = []
        for text in test_responses:
            t0 = time.perf_counter()
            detector.score(text)
            latencies.append((time.perf_counter() - t0) * 1000)

        latencies.sort()
        results.append(
            {
                "method": "embedding",
                "model": "all-MiniLM-L6-v2",
                "score_ms": round(latencies[len(latencies) // 2], 1),
            }
        )
    except Exception:
        logger.exception("Drift benchmark failed")

    return results


def generate_command_wavs(
    piper_model_path: str | None = None,
) -> dict[str, tuple[bytes, float]]:
    """Pre-synthesize all SYNTHETIC_COMMANDS to WAV using Piper TTS.

    Parameters
    ----------
    piper_model_path : str | None
        Path to Piper ONNX model. Auto-discovers if None.

    Returns
    -------
    dict[str, tuple[bytes, float]]
        Mapping of command_id -> (wav_bytes, duration_ms).
        Empty dict if Piper is not available.
    """
    result: dict[str, tuple[bytes, float]] = {}

    try:
        from piper import PiperVoice
    except ImportError:
        logger.warning("piper-tts not installed — skipping synthetic WAV generation")
        return result

    # Auto-discover model path
    model_path = piper_model_path
    if model_path is None:
        search_dirs = [
            Path.home() / ".local/share/piper",
            Path.home() / ".cache/piper",
            Path("/tmp/piper"),  # noqa: S108
        ]
        for d in search_dirs:
            if d.exists():
                onnx_files = list(d.glob("**/*.onnx"))
                if onnx_files:
                    model_path = str(onnx_files[0])
                    break

    if model_path is None:
        logger.warning("No Piper model found — skipping synthetic WAV generation")
        return result

    try:
        voice = PiperVoice.load(model_path)
        for cmd in SYNTHETIC_COMMANDS:
            buf = io.BytesIO()
            with wave.open(buf, "wb") as wf:
                voice.synthesize(cmd["text"], wf)
            wav_bytes = buf.getvalue()

            # Calculate duration from WAV header
            buf.seek(0)
            with wave.open(buf, "rb") as wf:
                frames = wf.getnframes()
                rate = wf.getframerate()
                duration_ms = (frames / rate) * 1000

            result[cmd["id"]] = (wav_bytes, duration_ms)

        logger.info("Synthesized %d command WAVs", len(result))
    except Exception:
        logger.exception("Failed to generate synthetic command WAVs")

    return result


def benchmark_synthetic_stt(
    model: str = "tiny",
    device: str = "cpu",
    command_wavs: dict[str, tuple[bytes, float]] | None = None,
    piper_model_path: str | None = None,
) -> list[dict[str, Any]]:
    """Benchmark STT accuracy on synthetic voice commands.

    Feeds pre-generated TTS WAVs through faster-whisper and measures
    Word Error Rate + domain keyword survival per command.

    Parameters
    ----------
    model : str
        Whisper model size.
    device : str
        Device to run STT on.
    command_wavs : dict | None
        Pre-generated WAVs. If None, generates them.
    piper_model_path : str | None
        Piper model path for WAV generation.

    Returns
    -------
    list[dict[str, Any]]
        Per-command accuracy results.
    """
    results: list[dict[str, Any]] = []

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        logger.warning("faster-whisper not installed — skipping synthetic STT benchmark")
        return results

    # Get or generate command WAVs
    if command_wavs is None:
        command_wavs = generate_command_wavs(piper_model_path)

    if not command_wavs:
        logger.warning("No synthetic command WAVs available — skipping synthetic STT benchmark")
        return results

    compute_type = "float16" if device == "cuda" else "int8"
    try:
        whisper_model = WhisperModel(model, device=device, compute_type=compute_type)
    except Exception:
        logger.exception("Failed to load faster-whisper %s on %s", model, device)
        return results

    import tempfile

    for cmd in SYNTHETIC_COMMANDS:
        if cmd["id"] not in command_wavs:
            continue

        wav_bytes, _duration_ms = command_wavs[cmd["id"]]

        # Write WAV to temp file for Whisper
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(wav_bytes)
            tmp_path = Path(f.name)

        try:
            t0 = time.perf_counter()
            segments, _info = whisper_model.transcribe(str(tmp_path))
            transcribed = " ".join(seg.text.strip() for seg in segments)
            stt_ms = (time.perf_counter() - t0) * 1000
        finally:
            tmp_path.unlink(missing_ok=True)

        wer = compute_wer(cmd["text"], transcribed)
        found, missed = check_domain_keywords(transcribed, cmd["domain_keywords"])

        results.append(
            {
                "command_id": cmd["id"],
                "original_text": cmd["text"],
                "transcribed_text": transcribed,
                "wer": round(wer, 3),
                "domain_keywords_found": found,
                "domain_keywords_missed": missed,
                "stt_ms": round(stt_ms, 1),
                "model": model,
                "device": device,
            }
        )

    # Free model
    del whisper_model
    try:
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except ImportError:
        pass

    return results


def capture_microphone(
    duration_s: float = 5.0,
    sample_rate: int = 16000,
) -> bytes:
    """Record audio from the default microphone.

    Parameters
    ----------
    duration_s : float
        Recording duration in seconds.
    sample_rate : int
        Sample rate in Hz.

    Returns
    -------
    bytes
        WAV file content.

    Raises
    ------
    ImportError
        If sounddevice is not installed.
    RuntimeError
        If no audio input device is found.
    """
    try:
        import sounddevice as sd
    except ImportError:
        msg = "sounddevice is not installed — required for microphone capture. Install with: uv add sounddevice"
        raise ImportError(msg) from None

    logger.info("Recording %s seconds from microphone at %d Hz...", duration_s, sample_rate)
    try:
        audio = sd.rec(
            int(duration_s * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
        )
        sd.wait()
    except Exception as e:
        msg = f"Microphone recording failed: {e}"
        raise RuntimeError(msg) from e

    # Convert to WAV bytes
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())
    return buf.getvalue()


class MockLLM:
    """Mock LLM with configurable delay for benchmarking without API keys.

    Parameters
    ----------
    delay_ms : int
        Simulated response delay in milliseconds.
    """

    def __init__(self, delay_ms: int = 500) -> None:
        self.delay_ms = delay_ms

    def respond(self, text: str) -> str:  # noqa: ARG002
        """Return a canned response after sleeping for the configured delay.

        Parameters
        ----------
        text : str
            Input text (ignored — response is fixed).

        Returns
        -------
        str
            Canned response string.
        """
        time.sleep(self.delay_ms / 1000)
        return (
            "I can help you with that music attribution query. "
            "The confidence score indicates how reliable the attribution data is."
        )


def benchmark_end_to_end(
    model: str = "tiny",
    device: str = "cpu",
    live_llm: bool = False,
    llm_delay_ms: int = 500,
    command_wavs: dict[str, tuple[bytes, float]] | None = None,
    piper_model_path: str | None = None,
) -> list[dict[str, Any]]:
    """Benchmark end-to-end voice pipeline: STT -> LLM -> TTS.

    Parameters
    ----------
    model : str
        Whisper model size for STT.
    device : str
        Device for STT inference.
    live_llm : bool
        If True, use real PydanticAI agent (requires API key).
    llm_delay_ms : int
        Mock LLM delay in milliseconds.
    command_wavs : dict | None
        Pre-generated WAVs. If None, generates them.
    piper_model_path : str | None
        Piper model path for WAV generation.

    Returns
    -------
    list[dict[str, Any]]
        Per-command latency breakdown results.
    """
    results: list[dict[str, Any]] = []

    # Check STT dependency
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        logger.warning("faster-whisper not installed — skipping end-to-end benchmark")
        return results

    # Get or generate command WAVs
    if command_wavs is None:
        command_wavs = generate_command_wavs(piper_model_path)

    if not command_wavs:
        logger.warning("No synthetic command WAVs — skipping end-to-end benchmark")
        return results

    # Check TTS dependency
    try:
        from piper import PiperVoice
    except ImportError:
        logger.warning("piper-tts not installed — skipping end-to-end TTS stage")
        PiperVoice = None  # type: ignore[assignment, misc]

    compute_type = "float16" if device == "cuda" else "int8"
    try:
        whisper_model = WhisperModel(model, device=device, compute_type=compute_type)
    except Exception:
        logger.exception("Failed to load faster-whisper %s on %s", model, device)
        return results

    # Initialize LLM
    llm = MockLLM(delay_ms=llm_delay_ms)
    llm_mode = "mock"
    if live_llm:
        logger.info("Live LLM mode requested — using PydanticAI agent")
        llm_mode = "live"
        # TODO: Wire PydanticAI agent when --live-llm is used

    # Load TTS voice if available
    tts_voice = None
    if PiperVoice is not None:
        model_path = piper_model_path
        if model_path is None:
            for d in [Path.home() / ".local/share/piper", Path.home() / ".cache/piper", Path("/tmp/piper")]:  # noqa: S108
                if d.exists():
                    onnx_files = list(d.glob("**/*.onnx"))
                    if onnx_files:
                        model_path = str(onnx_files[0])
                        break
        if model_path:
            try:
                tts_voice = PiperVoice.load(model_path)
            except Exception:
                logger.exception("Failed to load Piper voice for end-to-end TTS")

    import tempfile

    for cmd in SYNTHETIC_COMMANDS:
        if cmd["id"] not in command_wavs:
            continue

        wav_bytes, input_duration_ms = command_wavs[cmd["id"]]

        total_t0 = time.perf_counter()

        # Stage 1: STT
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(wav_bytes)
            tmp_path = Path(f.name)

        try:
            stt_t0 = time.perf_counter()
            segments, _info = whisper_model.transcribe(str(tmp_path))
            transcribed = " ".join(seg.text.strip() for seg in segments)
            stt_ms = (time.perf_counter() - stt_t0) * 1000
        finally:
            tmp_path.unlink(missing_ok=True)

        # Stage 2: LLM
        llm_t0 = time.perf_counter()
        _response = llm.respond(transcribed)
        llm_ms = (time.perf_counter() - llm_t0) * 1000

        # Stage 3: TTS
        tts_ms = 0.0
        if tts_voice is not None:
            tts_t0 = time.perf_counter()
            buf = io.BytesIO()
            try:
                with wave.open(buf, "wb") as wf:
                    tts_voice.synthesize(_response, wf)
                tts_ms = (time.perf_counter() - tts_t0) * 1000
            except Exception:
                logger.exception("TTS synthesis failed for command %s", cmd["id"])

        total_ms = (time.perf_counter() - total_t0) * 1000
        overhead_ms = total_ms - (stt_ms + llm_ms + tts_ms)
        rtf = total_ms / input_duration_ms if input_duration_ms > 0 else 0

        results.append(
            {
                "command_id": cmd["id"],
                "stt_ms": round(stt_ms, 1),
                "llm_ms": round(llm_ms, 1),
                "llm_mode": llm_mode,
                "tts_ms": round(tts_ms, 1),
                "total_ms": round(total_ms, 1),
                "overhead_ms": round(overhead_ms, 1),
                "input_audio_duration_ms": round(input_duration_ms, 1),
                "rtf": round(rtf, 3),
            }
        )

    # Clean up
    del whisper_model
    try:
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except ImportError:
        pass

    return results


def run_benchmarks(
    models: list[str],
    cpu_only: bool = False,
    piper_model: str | None = None,
    output_path: Path | None = None,
    skip_synthetic: bool = False,
    live_llm: bool = False,
    llm_delay_ms: int = 500,
    with_microphone: bool = False,
    record_seconds: float = 5.0,
) -> dict[str, Any]:
    """Run all voice pipeline benchmarks.

    Parameters
    ----------
    models : list[str]
        Whisper model sizes to benchmark.
    cpu_only : bool
        If True, skip GPU benchmarks.
    piper_model : str | None
        Path to Piper ONNX model file.
    output_path : Path | None
        If provided, write JSON results to this path.
    skip_synthetic : bool
        If True, skip synthetic voice command benchmarks.
    live_llm : bool
        If True, use real PydanticAI agent for end-to-end (requires API key).
    llm_delay_ms : int
        Mock LLM response delay in milliseconds.
    with_microphone : bool
        If True, capture audio from microphone.
    record_seconds : float
        Microphone recording duration in seconds.

    Returns
    -------
    dict[str, Any]
        Complete benchmark results.
    """
    hw = detect_hardware()

    devices = ["cpu"]
    if not cpu_only and hw["cuda_available"]:
        devices.append("cuda")

    # Write test audio to a temp file for Whisper
    import tempfile

    audio_bytes = generate_test_audio()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(audio_bytes)
        audio_path = Path(f.name)

    try:
        stt_results = benchmark_stt(audio_path, models, devices, hw.get("vram_gb", 0))
        tts_results = benchmark_tts(piper_model=piper_model)
        drift_results = benchmark_drift()

        # Synthetic voice command benchmarks
        synthetic_results: list[dict[str, Any]] | None = None
        e2e_results: list[dict[str, Any]] | None = None
        syn_device = "cuda" if "cuda" in devices else "cpu"
        syn_model = models[0] if models else "tiny"

        if not skip_synthetic:
            # Generate command WAVs once, reuse for synthetic + e2e
            command_wavs = generate_command_wavs(piper_model)
            synthetic_results = benchmark_synthetic_stt(
                model=syn_model,
                device=syn_device,
                command_wavs=command_wavs,
                piper_model_path=piper_model,
            )
            e2e_results = benchmark_end_to_end(
                model=syn_model,
                device=syn_device,
                live_llm=live_llm,
                llm_delay_ms=llm_delay_ms,
                command_wavs=command_wavs,
                piper_model_path=piper_model,
            )
    finally:
        audio_path.unlink(missing_ok=True)

    # Microphone capture (optional)
    mic_results: dict[str, Any] | None = None
    if with_microphone:
        try:
            mic_wav = capture_microphone(
                duration_s=record_seconds,
                sample_rate=16000,
            )
            mic_results = {
                "duration_s": record_seconds,
                "wav_bytes": len(mic_wav),
                "transcriptions": [],
            }

            # Transcribe with first model
            try:
                from faster_whisper import WhisperModel

                mic_model_name = models[0] if models else "tiny"
                mic_device = "cuda" if "cuda" in devices else "cpu"
                compute_type = "float16" if mic_device == "cuda" else "int8"
                mic_whisper = WhisperModel(mic_model_name, device=mic_device, compute_type=compute_type)

                import tempfile

                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    f.write(mic_wav)
                    mic_path = Path(f.name)

                try:
                    t0 = time.perf_counter()
                    segments, _info = mic_whisper.transcribe(str(mic_path))
                    transcribed = " ".join(seg.text.strip() for seg in segments)
                    mic_stt_ms = (time.perf_counter() - t0) * 1000
                    mic_results["transcriptions"].append(
                        {
                            "model": mic_model_name,
                            "device": mic_device,
                            "text": transcribed,
                            "stt_ms": round(mic_stt_ms, 1),
                        }
                    )
                finally:
                    mic_path.unlink(missing_ok=True)

                del mic_whisper
            except ImportError:
                logger.warning("faster-whisper not installed — skipping mic transcription")
        except (ImportError, RuntimeError):
            logger.exception("Microphone capture failed")

    report = {
        "hardware": hw,
        "timestamp": datetime.now(UTC).isoformat(),
        "benchmarks": {
            "stt": stt_results,
            "tts": tts_results,
            "drift": drift_results,
            "synthetic_stt": synthetic_results,
            "end_to_end": e2e_results,
            "microphone": mic_results,
        },
    }

    # Print summary table
    print("\n=== Voice Pipeline Benchmark ===")
    print(f"CPU: {hw['cpu']}")
    if hw["gpu"]:
        print(f"GPU: {hw['gpu']} ({hw['vram_gb']} GB VRAM)")
    print(f"CUDA: {hw['cuda_available']}")
    print()

    if stt_results:
        print("STT (faster-whisper):")
        print(
            f"  {'Model':<10} {'Device':<8} {'Compute':<10} {'Load (ms)':<12} {'Inference (ms)':<16} {'RSS (MB)':<10}"
        )
        for r in stt_results:
            print(
                f"  {r['model']:<10} {r['device']:<8} {r['compute_type']:<10} "
                f"{r['load_ms']:<12.1f} {r['inference_ms']:<16.1f} {r['rss_mb']:<10.1f}"
            )
        print()

    if tts_results:
        print("TTS (Piper):")
        for r in tts_results:
            print(f"  {r['provider']} ({r['model']}): {r['synthesis_ms']:.1f} ms")
        print()

    if drift_results:
        print("Drift Detection:")
        for r in drift_results:
            print(f"  {r['method']} ({r['model']}): {r['score_ms']:.1f} ms")
        print()

    if synthetic_results:
        print("Synthetic STT (TTS->STT round-trip):")
        print(f"  {'ID':<5} {'WER':<8} {'STT (ms)':<10} {'Keywords':<20} {'Transcription':<50}")
        for r in synthetic_results:
            kw_str = f"{len(r['domain_keywords_found'])}/{len(r['domain_keywords_found']) + len(r['domain_keywords_missed'])}"
            trans = r["transcribed_text"][:47] + "..." if len(r["transcribed_text"]) > 50 else r["transcribed_text"]
            print(f"  {r['command_id']:<5} {r['wer']:<8.3f} {r['stt_ms']:<10.1f} {kw_str:<20} {trans:<50}")
        print()

    if e2e_results:
        print("End-to-End Pipeline (STT -> LLM -> TTS):")
        print(
            f"  {'ID':<5} {'STT (ms)':<10} {'LLM (ms)':<10} {'TTS (ms)':<10} {'Total (ms)':<12} {'RTF':<8} {'Mode':<6}"
        )
        for r in e2e_results:
            print(
                f"  {r['command_id']:<5} {r['stt_ms']:<10.1f} {r['llm_ms']:<10.1f} "
                f"{r['tts_ms']:<10.1f} {r['total_ms']:<12.1f} {r['rtf']:<8.3f} {r['llm_mode']:<6}"
            )
        print()

    if mic_results:
        print("Microphone Capture:")
        print(f"  Duration: {mic_results['duration_s']}s, Size: {mic_results['wav_bytes']} bytes")
        for t in mic_results.get("transcriptions", []):
            print(f'  [{t["model"]}/{t["device"]}] {t["stt_ms"]:.1f} ms: "{t["text"]}"')
        print()

    if output_path:
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Results written to {output_path}")

    return report


def main() -> None:
    """CLI entry point for the voice benchmark."""
    parser = argparse.ArgumentParser(
        description="Voice pipeline benchmark (CPU vs GPU latency)",
    )
    parser.add_argument(
        "--models",
        type=str,
        default=",".join(_DEFAULT_MODELS),
        help="Comma-separated Whisper model sizes (default: tiny,base,small,medium)",
    )
    parser.add_argument(
        "--cpu-only",
        action="store_true",
        help="Skip GPU benchmarks even if CUDA is available",
    )
    parser.add_argument(
        "--piper-model",
        type=str,
        default=None,
        help="Path to Piper ONNX model file (auto-discovers if not set)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Path to write JSON results file",
    )
    parser.add_argument(
        "--skip-synthetic",
        action="store_true",
        help="Skip synthetic voice command benchmarks",
    )
    parser.add_argument(
        "--mock-llm",
        action="store_true",
        default=True,
        help="Use mock LLM for end-to-end (default: true)",
    )
    parser.add_argument(
        "--live-llm",
        action="store_true",
        help="Use real PydanticAI agent for end-to-end (requires API key)",
    )
    parser.add_argument(
        "--llm-delay-ms",
        type=int,
        default=500,
        help="Mock LLM response delay in milliseconds (default: 500)",
    )
    parser.add_argument(
        "--with-microphone",
        action="store_true",
        help="Enable microphone capture for live audio benchmarking",
    )
    parser.add_argument(
        "--record-seconds",
        type=float,
        default=5.0,
        help="Microphone recording duration in seconds (default: 5)",
    )

    args = parser.parse_args()
    models = [m.strip() for m in args.models.split(",")]
    output_path = Path(args.output) if args.output else None

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_benchmarks(
        models=models,
        cpu_only=args.cpu_only,
        piper_model=args.piper_model,
        output_path=output_path,
        skip_synthetic=args.skip_synthetic,
        live_llm=args.live_llm,
        llm_delay_ms=args.llm_delay_ms,
        with_microphone=args.with_microphone,
        record_seconds=args.record_seconds,
    )


if __name__ == "__main__":
    main()
