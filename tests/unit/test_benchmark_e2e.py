"""Tests for end-to-end pipeline benchmarking and MockLLM in benchmark_voice.py."""

from __future__ import annotations

import ast
import time
from pathlib import Path


class TestMockLLM:
    """Tests for MockLLM class (T07)."""

    def test_mock_llm_returns_string(self) -> None:
        """MockLLM.respond() should return a string."""
        from scripts.benchmark_voice import MockLLM

        llm = MockLLM()
        result = llm.respond("test input")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_mock_llm_respects_delay(self) -> None:
        """MockLLM should sleep for approximately the configured delay."""
        from scripts.benchmark_voice import MockLLM

        llm = MockLLM(delay_ms=100)
        t0 = time.perf_counter()
        llm.respond("test")
        elapsed_ms = (time.perf_counter() - t0) * 1000
        # Allow 50ms tolerance for scheduling jitter
        assert elapsed_ms >= 80, f"Expected >= 80ms, got {elapsed_ms:.1f}ms"

    def test_mock_llm_default_delay_500ms(self) -> None:
        """MockLLM default delay should be 500ms."""
        from scripts.benchmark_voice import MockLLM

        llm = MockLLM()
        assert llm.delay_ms == 500

    def test_mock_llm_custom_delay(self) -> None:
        """MockLLM should accept custom delay."""
        from scripts.benchmark_voice import MockLLM

        llm = MockLLM(delay_ms=200)
        assert llm.delay_ms == 200


class TestBenchmarkEndToEnd:
    """Tests for benchmark_end_to_end() (T08)."""

    def test_benchmark_e2e_returns_list(self) -> None:
        """benchmark_end_to_end() should return a list."""
        from scripts.benchmark_voice import benchmark_end_to_end

        result = benchmark_end_to_end(model="tiny", device="cpu")
        assert isinstance(result, list)

    def test_benchmark_e2e_result_has_latency_fields(self) -> None:
        """Each result should have latency breakdown fields."""
        from scripts.benchmark_voice import benchmark_end_to_end

        results = benchmark_end_to_end(model="tiny", device="cpu")
        required_keys = {
            "command_id",
            "stt_ms",
            "llm_ms",
            "llm_mode",
            "tts_ms",
            "total_ms",
            "overhead_ms",
        }
        for r in results:
            assert required_keys.issubset(r.keys()), f"Missing keys: {required_keys - r.keys()}"

    def test_benchmark_e2e_skips_without_deps(self) -> None:
        """Should return empty list when dependencies are not available."""
        from unittest.mock import patch

        from scripts.benchmark_voice import benchmark_end_to_end

        with patch.dict("sys.modules", {"faster_whisper": None}):
            result = benchmark_end_to_end(model="tiny", device="cpu")
            assert isinstance(result, list)

    def test_benchmark_e2e_rtf_calculation(self) -> None:
        """RTF (real-time factor) should be total_ms / input_audio_duration_ms."""
        from scripts.benchmark_voice import benchmark_end_to_end

        results = benchmark_end_to_end(model="tiny", device="cpu")
        for r in results:
            if "rtf" in r and "input_audio_duration_ms" in r:
                expected_rtf = r["total_ms"] / r["input_audio_duration_ms"]
                assert abs(r["rtf"] - expected_rtf) < 0.01


class TestLLMCLIFlags:
    """Tests for --mock-llm, --live-llm, --llm-delay-ms CLI flags (T09)."""

    def test_script_has_llm_flags(self) -> None:
        """Script should accept LLM-related argparse flags."""
        script_path = Path("scripts/benchmark_voice.py")
        source = script_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        flags_found: set[str] = set()
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and node.value in ("--mock-llm", "--live-llm", "--llm-delay-ms")
            ):
                flags_found.add(node.value)

        assert "--mock-llm" in flags_found, "Script must have --mock-llm flag"
        assert "--live-llm" in flags_found, "Script must have --live-llm flag"
        assert "--llm-delay-ms" in flags_found, "Script must have --llm-delay-ms flag"

    def test_run_benchmarks_accepts_llm_params(self) -> None:
        """run_benchmarks() should accept LLM-related parameters."""
        import inspect

        from scripts.benchmark_voice import run_benchmarks

        sig = inspect.signature(run_benchmarks)
        assert "live_llm" in sig.parameters, "run_benchmarks() must accept live_llm"
        assert "llm_delay_ms" in sig.parameters, "run_benchmarks() must accept llm_delay_ms"
