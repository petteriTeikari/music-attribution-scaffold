"""Generate golden voice dataset: 20 commands × 5 presets = 100 FLAC fixtures.

Usage:
    uv run --group voice-gpl --group voice-test \
        python scripts/generate_golden_dataset.py

Requires Piper TTS (pipecat-ai[piper]) for synthesis and soxr for resampling.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from music_attribution.voice.config import (
    DEFAULT_PIPER_VOICE_ID,
    PIPELINE_SAMPLE_RATE,
)
from music_attribution.voice.piper_utils import (
    load_piper_voice,
    synthesize_speech,
)

if TYPE_CHECKING:
    from piper import PiperVoice

logger = logging.getLogger(__name__)

# Module-level voice instance, set in main() before generation loop
_voice: PiperVoice | None = None


def synthesize_command(
    text: str,
) -> tuple[np.ndarray, int]:
    """Synthesize a voice command and resample to pipeline sample rate.

    Args:
        text: Command text to synthesize.

    Returns:
        Tuple of (audio_float32, PIPELINE_SAMPLE_RATE).

    Raises:
        RuntimeError: If ``_voice`` has not been initialized via ``main()``.
    """
    import soxr

    if _voice is None:
        msg = "Piper voice not initialized — call main() or set _voice first"
        raise RuntimeError(msg)

    audio, sr = synthesize_speech(_voice, text)

    # Resample from Piper native rate to pipeline target rate
    if sr != PIPELINE_SAMPLE_RATE:
        audio = soxr.resample(audio, sr, PIPELINE_SAMPLE_RATE, quality="HQ")

    return audio.astype(np.float32), PIPELINE_SAMPLE_RATE


def generate_clean_fixtures(
    output_dir: Path,
) -> list[Path]:
    """Generate 20 clean FLAC fixtures from GOLDEN_COMMANDS.

    Requires ``_voice`` module-level variable to be initialized.

    Args:
        output_dir: Directory to write FLAC files to.

    Returns:
        List of created FLAC file paths.
    """
    from music_attribution.voice.degradation import write_audio
    from music_attribution.voice.golden_commands import GOLDEN_COMMANDS

    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for cmd in GOLDEN_COMMANDS:
        audio, sr = synthesize_command(cmd["text"])
        filename = f"{cmd['id']}_clean.flac"
        path = output_dir / filename
        write_audio(path, audio, sample_rate=sr)
        paths.append(path)
        logger.info("Generated %s (%d samples)", filename, len(audio))

    return paths


def generate_degraded_fixtures(
    clean_dir: Path,
    output_dir: Path,
    seed: int = 42,
) -> list[Path]:
    """Generate degraded FLAC fixtures from clean audio files.

    For each clean FLAC, applies 4 non-clean degradation presets
    (OFFICE, CODEC, NOISY_CAFE, EXTREME) to produce 80 degraded files.

    Args:
        clean_dir: Directory containing clean FLAC files.
        output_dir: Directory to write degraded files to.
        seed: Random seed for reproducibility.

    Returns:
        List of created degraded FLAC file paths.
    """
    from music_attribution.voice.degradation import (
        DegradationPreset,
        apply_degradation,
        read_audio,
        write_audio,
    )

    non_clean_presets = [
        DegradationPreset.OFFICE,
        DegradationPreset.CODEC,
        DegradationPreset.NOISY_CAFE,
        DegradationPreset.EXTREME,
    ]

    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    clean_files = sorted(clean_dir.glob("cmd_*_clean.flac"))
    for clean_path in clean_files:
        audio, sr = read_audio(clean_path)
        # Extract command ID: cmd_01_clean.flac -> cmd_01
        cmd_id = clean_path.stem.rsplit("_", maxsplit=1)[0]

        for preset in non_clean_presets:
            degraded = apply_degradation(audio.copy(), sr, preset, seed=seed)
            filename = f"{cmd_id}_{preset.value}.flac"
            out_path = output_dir / filename
            write_audio(out_path, degraded, sample_rate=sr)
            paths.append(out_path)
            logger.info("Generated %s (%d samples)", filename, len(degraded))

    return paths


def generate_manifest(
    output_dir: Path,
    paths: list[Path],
    seed: int = 42,
) -> dict:
    """Create manifest dict describing all generated fixture files.

    Args:
        output_dir: Directory containing FLAC files.
        paths: List of FLAC file paths to include.
        seed: Random seed used for generation.

    Returns:
        Manifest dict with version, seed, sample_rate, format, and files list.
    """
    from music_attribution.voice.degradation import read_audio
    from music_attribution.voice.golden_commands import GOLDEN_COMMANDS

    # Build command lookup
    cmd_lookup = {cmd["id"]: cmd for cmd in GOLDEN_COMMANDS}

    files = []
    for p in sorted(paths):
        stem = p.stem
        # Parse: cmd_01_clean -> cmd_id=cmd_01, preset=clean
        parts = stem.split("_")
        cmd_id = f"{parts[0]}_{parts[1]}"
        preset = "_".join(parts[2:])

        cmd_info = cmd_lookup.get(cmd_id, {})
        sha256 = hashlib.sha256(p.read_bytes()).hexdigest()

        audio, sr = read_audio(p)
        duration = len(audio) / sr

        files.append(
            {
                "filename": p.name,
                "command_id": cmd_id,
                "preset": preset,
                "text": cmd_info.get("text", ""),
                "domain_keywords": cmd_info.get("domain_keywords", []),
                "sha256": sha256,
                "duration_seconds": round(duration, 4),
            }
        )

    return {
        "version": "1.0",
        "seed": seed,
        "sample_rate": PIPELINE_SAMPLE_RATE,
        "format": "FLAC",
        "output_directory": str(output_dir),
        "files": files,
    }


def main(argv: list[str] | None = None) -> None:
    """CLI entry point for golden dataset generation.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).
    """
    global _voice  # noqa: PLW0603

    parser = argparse.ArgumentParser(
        description="Generate golden voice dataset fixtures.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tests/fixtures/voice/audio"),
        help="Directory to write fixture files to.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility.",
    )
    parser.add_argument(
        "--voice-id",
        default=DEFAULT_PIPER_VOICE_ID,
        help="Piper TTS voice model identifier.",
    )
    parser.add_argument(
        "--model-dir",
        type=Path,
        default=None,
        help="Explicit Piper model directory (auto-discovered if omitted).",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Initialize Piper voice once (downloads model if necessary)
    logger.info("Loading Piper voice '%s'...", args.voice_id)
    _voice = load_piper_voice(args.voice_id, model_dir=args.model_dir)
    logger.info("Piper voice loaded.")

    logger.info("Generating clean fixtures...")
    clean_paths = generate_clean_fixtures(args.output_dir)
    logger.info("Generated %d clean fixtures.", len(clean_paths))

    logger.info("Generating degraded fixtures...")
    degraded_paths = generate_degraded_fixtures(
        args.output_dir,
        args.output_dir,
        seed=args.seed,
    )
    logger.info("Generated %d degraded fixtures.", len(degraded_paths))

    all_paths = clean_paths + degraded_paths
    manifest = generate_manifest(args.output_dir, all_paths, seed=args.seed)

    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    logger.info("Wrote manifest to %s (%d files).", manifest_path, len(manifest["files"]))


if __name__ == "__main__":
    main()
