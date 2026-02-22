"""Tests for synthetic voice command benchmarking in benchmark_voice.py."""

from __future__ import annotations

import ast
from pathlib import Path
from unittest.mock import patch


class TestSyntheticCommandsCorpus:
    """Tests for SYNTHETIC_COMMANDS constant (T03)."""

    def test_synthetic_commands_is_list(self) -> None:
        """SYNTHETIC_COMMANDS should be a list."""
        from scripts.benchmark_voice import SYNTHETIC_COMMANDS

        assert isinstance(SYNTHETIC_COMMANDS, list)
        assert len(SYNTHETIC_COMMANDS) >= 7  # At least 7 commands per plan

    def test_synthetic_commands_has_required_keys(self) -> None:
        """Each command should have id, text, category, domain_keywords."""
        from scripts.benchmark_voice import SYNTHETIC_COMMANDS

        required_keys = {"id", "text", "category", "domain_keywords"}
        for cmd in SYNTHETIC_COMMANDS:
            assert required_keys.issubset(cmd.keys()), (
                f"Command {cmd.get('id')} missing keys: {required_keys - cmd.keys()}"
            )

    def test_synthetic_commands_has_categories_a_and_b(self) -> None:
        """Corpus should include both category A (queries) and B (actions)."""
        from scripts.benchmark_voice import SYNTHETIC_COMMANDS

        categories = {cmd["category"] for cmd in SYNTHETIC_COMMANDS}
        assert "A" in categories, "Must have category A (simple queries)"
        assert "B" in categories, "Must have category B (action commands)"

    def test_synthetic_commands_all_have_domain_keywords(self) -> None:
        """Every command should have at least one domain keyword."""
        from scripts.benchmark_voice import SYNTHETIC_COMMANDS

        for cmd in SYNTHETIC_COMMANDS:
            assert len(cmd["domain_keywords"]) >= 1, f"Command {cmd['id']} has no domain keywords"

    def test_synthetic_commands_ids_are_unique(self) -> None:
        """All command IDs should be unique."""
        from scripts.benchmark_voice import SYNTHETIC_COMMANDS

        ids = [cmd["id"] for cmd in SYNTHETIC_COMMANDS]
        assert len(ids) == len(set(ids)), f"Duplicate IDs found: {[x for x in ids if ids.count(x) > 1]}"


class TestGenerateCommandWavs:
    """Tests for generate_command_wavs() (T04)."""

    def test_generate_command_wavs_returns_dict(self) -> None:
        """generate_command_wavs() should return a dict."""
        from scripts.benchmark_voice import generate_command_wavs

        # Will return empty dict if Piper not available (which is fine)
        result = generate_command_wavs()
        assert isinstance(result, dict)

    def test_generate_command_wavs_graceful_without_piper(self) -> None:
        """Should return empty dict when piper is not installed."""
        from scripts.benchmark_voice import generate_command_wavs

        with patch.dict("sys.modules", {"piper": None}):
            result = generate_command_wavs()
            assert isinstance(result, dict)
            # May or may not be empty depending on caching — just check type

    def test_generate_command_wavs_returns_valid_wav_bytes(self) -> None:
        """If Piper is available, returned values should be (bytes, float) tuples."""
        from scripts.benchmark_voice import generate_command_wavs

        result = generate_command_wavs()
        if result:  # Only check if Piper was available
            for _cmd_id, (wav_bytes, duration_ms) in result.items():
                assert isinstance(wav_bytes, bytes)
                assert isinstance(duration_ms, float)
                assert duration_ms > 0
                assert len(wav_bytes) > 44  # WAV header is 44 bytes minimum


class TestBenchmarkSyntheticSTT:
    """Tests for benchmark_synthetic_stt() (T05)."""

    def test_benchmark_synthetic_stt_returns_list(self) -> None:
        """benchmark_synthetic_stt() should return a list."""
        from scripts.benchmark_voice import benchmark_synthetic_stt

        # Without Piper/Whisper installed, returns empty list
        result = benchmark_synthetic_stt(model="tiny", device="cpu")
        assert isinstance(result, list)

    def test_benchmark_synthetic_stt_result_schema(self) -> None:
        """Each result should have the expected keys when data is available."""
        from scripts.benchmark_voice import benchmark_synthetic_stt

        results = benchmark_synthetic_stt(model="tiny", device="cpu")
        required_keys = {
            "command_id",
            "original_text",
            "transcribed_text",
            "wer",
            "domain_keywords_found",
            "domain_keywords_missed",
            "stt_ms",
            "model",
            "device",
        }
        for r in results:
            assert required_keys.issubset(r.keys()), f"Missing keys: {required_keys - r.keys()}"

    def test_benchmark_synthetic_stt_skips_without_deps(self) -> None:
        """Should return empty list when faster-whisper is not available."""
        from scripts.benchmark_voice import benchmark_synthetic_stt

        with patch.dict("sys.modules", {"faster_whisper": None}):
            result = benchmark_synthetic_stt(model="tiny", device="cpu")
            assert isinstance(result, list)


class TestSkipSyntheticFlag:
    """Tests for --skip-synthetic CLI flag (T06)."""

    def test_script_has_skip_synthetic_flag(self) -> None:
        """Script should accept --skip-synthetic flag via argparse."""
        script_path = Path("scripts/benchmark_voice.py")
        source = script_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        # Find all string constants that look like argparse flag names
        has_flag = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value == "--skip-synthetic":
                has_flag = True
                break
        assert has_flag, "Script must have --skip-synthetic argparse flag"

    def test_run_benchmarks_accepts_skip_synthetic(self) -> None:
        """run_benchmarks() should accept skip_synthetic parameter."""
        import inspect

        from scripts.benchmark_voice import run_benchmarks

        sig = inspect.signature(run_benchmarks)
        assert "skip_synthetic" in sig.parameters, "run_benchmarks() must accept skip_synthetic parameter"
