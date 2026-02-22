"""Integration tests for the complete benchmark output schema."""

from __future__ import annotations

import json


class TestRunBenchmarksSchema:
    """Tests for the complete run_benchmarks() output (T12)."""

    def test_run_benchmarks_returns_complete_schema(self) -> None:
        """run_benchmarks() should return dict with hardware, timestamp, benchmarks."""
        from scripts.benchmark_voice import run_benchmarks

        # Use --skip-synthetic and --cpu-only for fast test
        result = run_benchmarks(
            models=["tiny"],
            cpu_only=True,
            skip_synthetic=True,
        )
        assert isinstance(result, dict)
        assert "hardware" in result
        assert "timestamp" in result
        assert "benchmarks" in result

        # Hardware keys
        hw = result["hardware"]
        assert "cpu" in hw
        assert "gpu" in hw
        assert "vram_gb" in hw
        assert "cuda_available" in hw

    def test_run_benchmarks_output_has_all_sections(self) -> None:
        """Benchmarks dict should have all section keys."""
        from scripts.benchmark_voice import run_benchmarks

        result = run_benchmarks(
            models=["tiny"],
            cpu_only=True,
            skip_synthetic=True,
        )
        benchmarks = result["benchmarks"]

        # All sections must exist (some may be None/empty)
        expected_sections = {"stt", "tts", "drift", "synthetic_stt", "end_to_end", "microphone"}
        assert expected_sections.issubset(benchmarks.keys()), (
            f"Missing sections: {expected_sections - benchmarks.keys()}"
        )

    def test_run_benchmarks_json_serializable(self) -> None:
        """Complete report should be JSON-serializable."""
        from scripts.benchmark_voice import run_benchmarks

        result = run_benchmarks(
            models=["tiny"],
            cpu_only=True,
            skip_synthetic=True,
        )
        # This should not raise
        json_str = json.dumps(result, indent=2)
        assert len(json_str) > 100

        # Round-trip
        parsed = json.loads(json_str)
        assert parsed["hardware"]["cpu"] == result["hardware"]["cpu"]

    def test_run_benchmarks_skip_synthetic_excludes_section(self) -> None:
        """When skip_synthetic=True, synthetic_stt and end_to_end should be None."""
        from scripts.benchmark_voice import run_benchmarks

        result = run_benchmarks(
            models=["tiny"],
            cpu_only=True,
            skip_synthetic=True,
        )
        assert result["benchmarks"]["synthetic_stt"] is None
        assert result["benchmarks"]["end_to_end"] is None

    def test_run_benchmarks_microphone_null_by_default(self) -> None:
        """Microphone section should be None when --with-microphone is not set."""
        from scripts.benchmark_voice import run_benchmarks

        result = run_benchmarks(
            models=["tiny"],
            cpu_only=True,
            skip_synthetic=True,
        )
        assert result["benchmarks"]["microphone"] is None
