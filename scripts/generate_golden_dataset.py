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
) -> dict:
    """Create manifest dict describing all generated fixture files.

    Args:
        output_dir: Directory containing FLAC files.
        paths: List of FLAC file paths to include.

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
        "seed": 42,
        "sample_rate": TARGET_SR,
        "format": "FLAC",
        "output_directory": str(output_dir),
        "files": files,
    }


def main(argv: list[str] | None = None) -> None:
    """CLI entry point for golden dataset generation.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).
    """
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
        default="en_US-lessac-medium",
        help="Piper TTS voice model identifier.",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    logger.info("Generating clean fixtures...")
    clean_paths = generate_clean_fixtures(args.output_dir, args.voice_id)
    logger.info("Generated %d clean fixtures.", len(clean_paths))

    logger.info("Generating degraded fixtures...")
    degraded_paths = generate_degraded_fixtures(
        args.output_dir,
        args.output_dir,
        seed=args.seed,
    )
    logger.info("Generated %d degraded fixtures.", len(degraded_paths))

    all_paths = clean_paths + degraded_paths
    manifest = generate_manifest(args.output_dir, all_paths)
    manifest["seed"] = args.seed

    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    logger.info("Wrote manifest to %s (%d files).", manifest_path, len(manifest["files"]))


if __name__ == "__main__":
    main()
