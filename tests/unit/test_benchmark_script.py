"""Tests for the voice benchmark script structure and helpers.

Validates the benchmark script's AST structure, hardware detection,
test audio generation, and output schema without requiring ML dependencies.
"""

from __future__ import annotations

import ast
import io
import wave
from pathlib import Path


class TestBenchmarkScriptStructure:
    """AST-based structural checks for the benchmark script."""

    def _parse_script(self) -> ast.Module:
        """Parse the benchmark script into an AST."""
        script_path = Path("scripts/benchmark_voice.py")
        source = script_path.read_text(encoding="utf-8")
        return ast.parse(source)

    def test_script_has_argparse_import(self) -> None:
        """Script imports argparse for CLI argument handling."""
        tree = self._parse_script()
        has_argparse = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == "argparse":
                        has_argparse = True
            elif isinstance(node, ast.ImportFrom) and node.module == "argparse":
                has_argparse = True
        assert has_argparse, "Script must import argparse"

    def test_script_has_main_function(self) -> None:
        """Script defines a main() function."""
        tree = self._parse_script()
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        assert "main" in function_names, "Script must define main()"

    def test_script_has_detect_hardware_function(self) -> None:
        """Script defines a detect_hardware() function."""
        tree = self._parse_script()
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        assert "detect_hardware" in function_names, "Script must define detect_hardware()"


class TestBenchmarkHelpers:
    """Tests for benchmark helper functions."""

    def test_detect_hardware_returns_expected_keys(self) -> None:
        """detect_hardware() returns dict with required keys."""
        from scripts.benchmark_voice import detect_hardware

        hw = detect_hardware()
        assert isinstance(hw, dict)
        assert "cpu" in hw
        assert "gpu" in hw
        assert "vram_gb" in hw
        assert "cuda_available" in hw
        assert isinstance(hw["cuda_available"], bool)

    def test_generate_test_audio_produces_valid_wav(self) -> None:
        """generate_test_audio() produces valid 16kHz 16-bit mono WAV."""
        from scripts.benchmark_voice import generate_test_audio

        audio_bytes = generate_test_audio(duration_s=1.0, sample_rate=16000)
        assert len(audio_bytes) > 0

        buf = io.BytesIO(audio_bytes)
        with wave.open(buf, "rb") as wf:
            assert wf.getnchannels() == 1
            assert wf.getsampwidth() == 2
            assert wf.getframerate() == 16000
            assert wf.getnframes() == 16000  # 1 second at 16kHz
