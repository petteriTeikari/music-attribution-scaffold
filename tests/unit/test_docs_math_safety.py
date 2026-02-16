"""Tests to prevent MathJax/arithmatex math overflow regressions.

Dollar signs in documentation content (e.g. $49/month, $2.3M) must not be
interpreted as LaTeX math delimiters. These tests verify:
1. mkdocs.yml arithmatex config restricts delimiters to \\(...\\) and \\[...\\]
2. MathJax config uses only backslash delimiters
3. If the config is ever loosened, paired $...$ patterns in docs would cause overflow
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = PROJECT_ROOT / "docs" / "site"
MKDOCS_YML = PROJECT_ROOT / "mkdocs.yml"


def _parse_arithmatex_config(content: str) -> dict[str, object]:
    """Extract arithmatex config from mkdocs.yml without full YAML parsing.

    Uses targeted text parsing to avoid !!python/name tag issues with safe_load.
    """
    lines = content.split("\n")
    config: dict[str, object] = {}
    in_arithmatex = False

    for line in lines:
        stripped = line.strip()

        if "pymdownx.arithmatex" in stripped:
            in_arithmatex = True
            continue

        if in_arithmatex:
            # End of arithmatex block — next extension or non-indented line
            if stripped.startswith("- ") and "pymdownx." in stripped:
                break
            if stripped and not line.startswith(" ") and not line.startswith("\t"):
                break

            if "generic:" in stripped:
                config["generic"] = "true" in stripped
            elif "smart_dollar:" in stripped:
                config["smart_dollar"] = "true" in stripped
            elif "inline_syntax:" in stripped:
                # Parse ['round'] or ['dollar', 'round'] etc.
                match = re.search(r"\[([^\]]*)\]", stripped)
                if match:
                    items = [s.strip().strip("'\"") for s in match.group(1).split(",")]
                    config["inline_syntax"] = [i for i in items if i]
            elif "block_syntax:" in stripped:
                match = re.search(r"\[([^\]]*)\]", stripped)
                if match:
                    items = [s.strip().strip("'\"") for s in match.group(1).split(",")]
                    config["block_syntax"] = [i for i in items if i]

    return config


def _arithmatex_allows_dollar(config: dict[str, object]) -> bool:
    """Check if the arithmatex config allows $ as a math delimiter."""
    inline = config.get("inline_syntax")
    if inline is None:
        # Default includes dollar — unsafe
        return True
    return isinstance(inline, list) and "dollar" in inline


class TestMkdocsArithmatexConfig:
    """Verify mkdocs.yml arithmatex config prevents dollar-sign math."""

    def test_mkdocs_yml_exists(self) -> None:
        """mkdocs.yml must exist at project root."""
        assert MKDOCS_YML.is_file(), f"Missing {MKDOCS_YML}"

    def test_arithmatex_uses_round_inline_only(self) -> None:
        """Arithmatex inline_syntax must be ['round'] — no dollar delimiters."""
        content = MKDOCS_YML.read_text(encoding="utf-8")
        config = _parse_arithmatex_config(content)
        assert config, "pymdownx.arithmatex config not found in mkdocs.yml"
        assert config.get("inline_syntax") == ["round"], (
            f"inline_syntax must be ['round'], got {config.get('inline_syntax')}"
        )

    def test_arithmatex_uses_square_block_only(self) -> None:
        """Arithmatex block_syntax must be ['square'] — no dollar delimiters."""
        content = MKDOCS_YML.read_text(encoding="utf-8")
        config = _parse_arithmatex_config(content)
        assert config, "pymdownx.arithmatex config not found in mkdocs.yml"
        assert config.get("block_syntax") == ["square"], (
            f"block_syntax must be ['square'], got {config.get('block_syntax')}"
        )

    def test_arithmatex_does_not_allow_dollar(self) -> None:
        """Arithmatex must not allow $ as a math delimiter."""
        content = MKDOCS_YML.read_text(encoding="utf-8")
        config = _parse_arithmatex_config(content)
        assert not _arithmatex_allows_dollar(config), (
            "arithmatex allows dollar-sign math delimiters — this will break pitch deck pages with monetary values"
        )

    def test_mathjax_js_uses_backslash_delimiters_only(self) -> None:
        """MathJax config must use \\(...\\) and \\[...\\] delimiters only."""
        mathjax_js = DOCS_DIR / "javascripts" / "mathjax.js"
        if not mathjax_js.is_file():
            pytest.skip("mathjax.js not found")

        content = mathjax_js.read_text(encoding="utf-8")
        assert '["$"' not in content, "mathjax.js must not use $ as inline delimiter"
        assert '["$$"' not in content, "mathjax.js must not use $$ as display delimiter"


# Pattern: two $ signs on the same line with content between them,
# outside of code blocks/inline code. Catches $49/month...$499/month.
_DOLLAR_MATH_PATTERN = re.compile(
    r"(?<!\\)\$"  # unescaped $
    r"[^$\n]{1,200}"  # content between (1-200 chars, no newline)
    r"(?<!\\)\$"  # closing unescaped $
)


def _is_in_code_context(line: str, match_start: int) -> bool:
    """Check if the match position is inside inline code."""
    prefix = line[:match_start]
    backtick_count = prefix.count("`")
    return backtick_count % 2 == 1


def _find_dollar_math_violations(filepath: Path) -> list[str]:
    """Find lines with paired $...$ that could be interpreted as math."""
    violations = []
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")
    in_code_block = False

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        for match in _DOLLAR_MATH_PATTERN.finditer(line):
            if not _is_in_code_context(line, match.start()):
                matched_text = match.group()
                # Skip legitimate LaTeX
                if any(cmd in matched_text for cmd in ["\\frac", "\\sum", "\\int", "\\alpha", "\\beta", "\\sigma"]):
                    continue
                violations.append(f"  L{line_num}: {matched_text}")

    return violations


class TestDocsNoDollarMath:
    """Verify docs dollar signs are protected by arithmatex config."""

    @pytest.fixture()
    def doc_files(self) -> list[Path]:
        """Collect all markdown files under docs/site/."""
        if not DOCS_DIR.is_dir():
            pytest.skip("docs/site/ directory not found")
        files = sorted(DOCS_DIR.rglob("*.md"))
        if not files:
            pytest.skip("No markdown files found in docs/site/")
        return files

    def test_dollar_signs_protected_by_config(self, doc_files: list[Path]) -> None:
        """If arithmatex allows dollar delimiters, paired $...$ patterns must not exist.

        With the current config (inline_syntax: ['round'], block_syntax: ['square']),
        dollar signs in monetary values are safe. This test fails only if someone
        loosens the config while dollar patterns exist in the docs.
        """
        content = MKDOCS_YML.read_text(encoding="utf-8")
        config = _parse_arithmatex_config(content)

        if not _arithmatex_allows_dollar(config):
            # Config is safe — dollar signs won't be interpreted as math
            return

        # Config allows dollar delimiters — check for dangerous patterns
        all_violations: dict[str, list[str]] = {}
        for filepath in doc_files:
            violations = _find_dollar_math_violations(filepath)
            if violations:
                rel_path = filepath.relative_to(PROJECT_ROOT)
                all_violations[str(rel_path)] = violations

        if all_violations:
            report_lines = [
                "arithmatex allows dollar-sign math AND docs contain paired $...$ patterns!",
                "This causes MathJax overflow. Fix one of:",
                "  1. Set inline_syntax: ['round'] in mkdocs.yml arithmatex config",
                "  2. Escape dollar signs as \\$ or wrap in inline code `$49`",
                "",
            ]
            for path, viols in sorted(all_violations.items()):
                report_lines.append(f"{path}:")
                report_lines.extend(viols)
                report_lines.append("")

            pytest.fail("\n".join(report_lines))
