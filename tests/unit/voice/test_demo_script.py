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

    def test_has_argparse_or_click(self, tree: ast.Module) -> None:
        """Script imports argparse or click for CLI arguments (AST-verified)."""
        imports: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module)
        cli_libs = {"argparse", "click", "typer"}
        assert imports & cli_libs, f"Demo script should import a CLI lib, found imports: {imports & cli_libs}"

    def test_supports_stt_provider_arg(self, tree: ast.Module) -> None:
        """Script has string literal referencing 'stt' (AST-verified)."""
        string_values: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                string_values.append(node.value.lower())
        assert any("stt" in s for s in string_values), "Script should have 'stt' string literal for provider arg"

    def test_supports_tts_provider_arg(self, tree: ast.Module) -> None:
        """Script has string literal referencing 'tts' (AST-verified)."""
        string_values: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                string_values.append(node.value.lower())
        assert any("tts" in s for s in string_values), "Script should have 'tts' string literal for provider arg"

    def test_imports_voice_config(self, tree: ast.Module) -> None:
        """Script imports VoiceConfig (AST-verified)."""
        imported_names: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                imported_names.update(alias.name for alias in node.names)
        assert "VoiceConfig" in imported_names, f"Script should import VoiceConfig, found: {imported_names}"

    def test_has_docstring(self, tree: ast.Module) -> None:
        """Script has a module-level docstring."""
        assert ast.get_docstring(tree) is not None
