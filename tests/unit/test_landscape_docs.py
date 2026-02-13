"""Tests for landscape documentation (Tasks B5, B6).

Validates MCP roadmap, multi-modal domain overlay, and
updated attribution company profiles.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RUNNING_IN_DOCKER = not (PROJECT_ROOT / "pyproject.toml").exists()
pytestmark = pytest.mark.skipif(RUNNING_IN_DOCKER, reason="Project root files not available in Docker")


class TestMcpRoadmap:
    """Tests for docs/api/mcp-roadmap.md (Task B5)."""

    def test_mcp_roadmap_exists(self) -> None:
        """Verify docs/api/mcp-roadmap.md exists."""
        assert (PROJECT_ROOT / "docs" / "api" / "mcp-roadmap.md").exists()

    def test_mcp_roadmap_mentions_tools(self) -> None:
        """Verify mentions query_training_influence, check_registry_status."""
        content = (PROJECT_ROOT / "docs" / "api" / "mcp-roadmap.md").read_text(encoding="utf-8")
        assert "query_training_influence" in content
        assert "check_registry_status" in content


class TestMultimodalOverlay:
    """Tests for docs/prd/domains/multimodal-attribution.yaml (Task B5)."""

    def test_multimodal_overlay_exists(self) -> None:
        """Verify docs/prd/domains/multimodal-attribution.yaml exists."""
        assert (PROJECT_ROOT / "docs" / "prd" / "domains" / "multimodal-attribution.yaml").exists()

    def test_multimodal_overlay_valid_yaml(self) -> None:
        """Verify it parses as valid YAML."""
        path = PROJECT_ROOT / "docs" / "prd" / "domains" / "multimodal-attribution.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert isinstance(data, dict), "multimodal-attribution.yaml should parse as YAML mapping"


class TestLandscapeDocs:
    """Tests for updated attribution company docs (Task B6)."""

    @pytest.fixture(scope="class")
    def content(self) -> str:
        """Load 01-attribution-companies.md."""
        path = PROJECT_ROOT / "docs" / "planning" / "music-tech-landscape" / "01-attribution-companies.md"
        return path.read_text(encoding="utf-8")

    def test_landscape_mentions_auracles(self, content: str) -> None:
        """Verify Auracles in 01-attribution-companies.md."""
        assert "Auracles" in content

    def test_landscape_mentions_musical_ai(self, content: str) -> None:
        """Verify Musical AI in 01-attribution-companies.md."""
        assert "Musical AI" in content

    def test_landscape_mentions_sureel(self, content: str) -> None:
        """Verify Sureel in 01-attribution-companies.md."""
        assert "Sureel" in content
