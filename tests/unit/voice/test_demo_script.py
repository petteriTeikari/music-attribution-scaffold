"""Tests for the voice agent demo script (Task 1.5)."""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

DEMO_SCRIPT = Path("scripts/voice_demo.py")


class TestDemoScriptExists:
    """Tests that the demo script exists and is valid Python."""

    def test_script_exists(self) -> None:
        """scripts/voice_demo.py exists."""
        assert DEMO_SCRIPT.exists(), f"Demo script not found at {DEMO_SCRIPT}"

    def test_script_is_valid_python(self) -> None:
        """Demo script is parseable Python."""
        source = DEMO_SCRIPT.read_text(encoding="utf-8")
        tree = ast.parse(source)
        assert tree is not None


class TestDemoScriptStructure:
    """Tests for demo script contents using AST analysis."""

    @pytest.fixture
    def tree(self) -> ast.Module:
        """Parse the demo script AST."""
        source = DEMO_SCRIPT.read_text(encoding="utf-8")
        return ast.parse(source)

    def test_has_main_function(self, tree: ast.Module) -> None:
        """Script defines a main() function."""
        func_names = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef)}
        assert "main" in func_names

    def test_has_argparse_or_click(self) -> None:
        """Script uses argparse or click for CLI arguments."""
        source = DEMO_SCRIPT.read_text(encoding="utf-8")
        has_argparse = "argparse" in source
        has_click = "click" in source
        has_typer = "typer" in source
        assert has_argparse or has_click or has_typer, "Demo script should have CLI argument parsing"

    def test_supports_stt_provider_arg(self) -> None:
        """Script supports --stt argument for STT provider selection."""
        source = DEMO_SCRIPT.read_text(encoding="utf-8")
        assert "stt" in source.lower(), "Script should support STT provider argument"

    def test_supports_tts_provider_arg(self) -> None:
        """Script supports --tts argument for TTS provider selection."""
        source = DEMO_SCRIPT.read_text(encoding="utf-8")
        assert "tts" in source.lower(), "Script should support TTS provider argument"

    def test_imports_voice_config(self) -> None:
        """Script imports VoiceConfig for configuration."""
        source = DEMO_SCRIPT.read_text(encoding="utf-8")
        assert "VoiceConfig" in source

    def test_has_docstring(self, tree: ast.Module) -> None:
        """Script has a module-level docstring."""
        assert ast.get_docstring(tree) is not None
