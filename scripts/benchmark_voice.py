"""Voice pipeline benchmark: CPU vs GPU latency for STT, TTS, and drift.

Measures hardware capabilities and inference latency for each stage of the
voice pipeline. Generates a JSON report suitable for CI regression tracking.

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
    """Benchmark Whisper STT inference.

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
        Benchmark results per model × device combination.
    """
    results: list[dict[str, Any]] = []

    try:
        import whisper
    except ImportError:
        logger.warning("whisper not installed — skipping STT benchmarks")
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

            # Cold start: model load time
            t0 = time.perf_counter()
            try:
                model = whisper.load_model(model_name, device=device)
            except Exception:
                logger.exception("Failed to load whisper %s on %s", model_name, device)
                continue
            load_ms = (time.perf_counter() - t0) * 1000

            # Warm inference: multiple iterations, take median
            latencies: list[float] = []
            for _ in range(_BENCHMARK_ITERATIONS):
                t0 = time.perf_counter()
                model.transcribe(str(audio_path), fp16=(device == "cuda"))
                latencies.append((time.perf_counter() - t0) * 1000)

            latencies.sort()
            median_ms = latencies[len(latencies) // 2]

            results.append(
                {
                    "model": model_name,
                    "device": device,
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


def benchmark_tts() -> list[dict[str, Any]]:
    """Benchmark Piper TTS synthesis.

    Returns
    -------
    list[dict[str, Any]]
        Benchmark results for TTS providers.
    """
    results: list[dict[str, Any]] = []

    try:
        from piper import PiperVoice
    except ImportError:
        logger.warning("piper-tts not installed — skipping TTS benchmarks")
        return results

    try:
        # Use default model if available
        voice = PiperVoice.load(str(Path.home() / ".local/share/piper/en_US-lessac-medium.onnx"))
        test_text = "This is a benchmark test for the voice synthesis pipeline."

        latencies: list[float] = []
        for _ in range(_BENCHMARK_ITERATIONS):
            buf = io.BytesIO()
            with wave.open(buf, "wb") as wf:
                voice.synthesize(test_text, wf)
            latencies.append(0.0)  # placeholder — timed below

        # Re-run with actual timing
        latencies = []
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
                "synthesis_ms": round(latencies[len(latencies) // 2], 1),
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
                "score_ms": round(latencies[len(latencies) // 2], 1),
            }
        )
    except Exception:
        logger.exception("Drift benchmark failed")

    return results


def run_benchmarks(
    models: list[str],
    cpu_only: bool = False,
    output_path: Path | None = None,
) -> dict[str, Any]:
    """Run all voice pipeline benchmarks.

    Parameters
    ----------
    models : list[str]
        Whisper model sizes to benchmark.
    cpu_only : bool
        If True, skip GPU benchmarks.
    output_path : Path | None
        If provided, write JSON results to this path.

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
        tts_results = benchmark_tts()
        drift_results = benchmark_drift()
    finally:
        audio_path.unlink(missing_ok=True)

    report = {
        "hardware": hw,
        "timestamp": datetime.now(UTC).isoformat(),
        "benchmarks": {
            "stt": stt_results,
            "tts": tts_results,
            "drift": drift_results,
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
        print("STT (Whisper):")
        print(f"  {'Model':<10} {'Device':<8} {'Load (ms)':<12} {'Inference (ms)':<16} {'RSS (MB)':<10}")
        for r in stt_results:
            print(
                f"  {r['model']:<10} {r['device']:<8} {r['load_ms']:<12.1f} {r['inference_ms']:<16.1f} {r['rss_mb']:<10.1f}"
            )
        print()

    if tts_results:
        print("TTS:")
        for r in tts_results:
            print(f"  {r['provider']}: {r['synthesis_ms']:.1f} ms")
        print()

    if drift_results:
        print("Drift Detection:")
        for r in drift_results:
            print(f"  {r['method']}: {r['score_ms']:.1f} ms")
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
        "--output",
        type=str,
        default=None,
        help="Path to write JSON results file",
    )

    args = parser.parse_args()
    models = [m.strip() for m in args.models.split(",")]
    output_path = Path(args.output) if args.output else None

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_benchmarks(models=models, cpu_only=args.cpu_only, output_path=output_path)


if __name__ == "__main__":
    main()
