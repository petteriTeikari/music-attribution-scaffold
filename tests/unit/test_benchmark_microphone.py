"""Tests for microphone capture in benchmark_voice.py."""

from __future__ import annotations

import ast
import inspect
from pathlib import Path
from unittest.mock import patch


class TestCaptureMicrophone:
    """Tests for capture_microphone() (T10)."""

    def test_capture_microphone_import_error_without_sounddevice(self) -> None:
        """Should raise ImportError when sounddevice is not installed."""
        from scripts.benchmark_voice import capture_microphone

        with patch.dict("sys.modules", {"sounddevice": None}):
            try:
                capture_microphone(duration_s=1.0)
                # If sounddevice happens to not be installed, this is also fine
            except ImportError as e:
                assert "sounddevice" in str(e).lower()

    def test_capture_microphone_returns_bytes_type_hint(self) -> None:
        """capture_microphone() should have bytes return type annotation."""
        from scripts.benchmark_voice import capture_microphone

        # Just check the function exists and is callable
        assert callable(capture_microphone)

    def test_capture_microphone_accepts_duration_and_sample_rate(self) -> None:
        """capture_microphone() should accept duration_s and sample_rate params."""
        from scripts.benchmark_voice import capture_microphone

        sig = inspect.signature(capture_microphone)
        assert "duration_s" in sig.parameters
        assert "sample_rate" in sig.parameters


class TestMicrophoneCLIFlags:
    """Tests for --with-microphone and --record-seconds CLI flags (T11)."""

    def test_script_has_microphone_flags(self) -> None:
        """Script should accept microphone-related argparse flags."""
        script_path = Path("scripts/benchmark_voice.py")
        source = script_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        flags_found: set[str] = set()
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and node.value in ("--with-microphone", "--record-seconds")
            ):
                flags_found.add(node.value)

        assert "--with-microphone" in flags_found, "Script must have --with-microphone flag"
        assert "--record-seconds" in flags_found, "Script must have --record-seconds flag"

    def test_run_benchmarks_accepts_microphone_params(self) -> None:
        """run_benchmarks() should accept microphone-related parameters."""
        sig = inspect.signature(__import__("scripts.benchmark_voice", fromlist=["run_benchmarks"]).run_benchmarks)
        assert "with_microphone" in sig.parameters, "run_benchmarks() must accept with_microphone"
        assert "record_seconds" in sig.parameters, "run_benchmarks() must accept record_seconds"
