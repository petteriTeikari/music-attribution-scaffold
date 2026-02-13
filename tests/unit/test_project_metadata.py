"""Tests for project metadata files (pyproject.toml, CITATION.cff, community files).

Validates that all SSRN-submission-required metadata files exist,
contain required content, and follow expected formats.
"""

from __future__ import annotations

import tomllib
from pathlib import Path

import pytest
import yaml

# Project root — tests/ is one level below root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Skip if running in Docker CI (these files may not be copied)
RUNNING_IN_DOCKER = not (PROJECT_ROOT / "pyproject.toml").exists()
pytestmark = pytest.mark.skipif(RUNNING_IN_DOCKER, reason="Project root files not available in Docker")


class TestPyprojectMetadata:
    """Tests for pyproject.toml metadata completeness (Task A1)."""

    @pytest.fixture(scope="class")
    def pyproject(self) -> dict:
        """Load pyproject.toml."""
        path = PROJECT_ROOT / "pyproject.toml"
        return tomllib.loads(path.read_text(encoding="utf-8"))

    def test_pyproject_has_keywords(self, pyproject: dict) -> None:
        """Verify keywords list exists in [project]."""
        keywords = pyproject["project"].get("keywords", [])
        assert len(keywords) >= 5, f"Expected at least 5 keywords, got {len(keywords)}"
        assert "music" in keywords
        assert "attribution" in keywords

    def test_pyproject_classifiers_include_science(self, pyproject: dict) -> None:
        """Verify Science/Research classifier is present."""
        classifiers = pyproject["project"].get("classifiers", [])
        assert any("Science/Research" in c for c in classifiers), (
            "Missing 'Intended Audience :: Science/Research' classifier"
        )

    def test_pyproject_classifiers_include_license(self, pyproject: dict) -> None:
        """Verify MIT license classifier is present."""
        classifiers = pyproject["project"].get("classifiers", [])
        assert any("MIT" in c for c in classifiers), "Missing MIT license classifier"

    def test_pyproject_urls_include_homepage(self, pyproject: dict) -> None:
        """Verify Homepage URL points to DOI."""
        urls = pyproject["project"].get("urls", {})
        homepage = urls.get("Homepage", "")
        assert "doi.org" in homepage or "ssrn" in homepage.lower(), (
            f"Homepage URL should point to DOI or SSRN, got: {homepage}"
        )

    def test_pyproject_urls_include_bug_tracker(self, pyproject: dict) -> None:
        """Verify Bug Tracker URL exists."""
        urls = pyproject["project"].get("urls", {})
        assert "Bug Tracker" in urls, "Missing 'Bug Tracker' in [project.urls]"
        assert "issues" in urls["Bug Tracker"], "Bug Tracker URL should point to /issues"


class TestCitationCff:
    """Tests for CITATION.cff (Task A2)."""

    def test_citation_cff_exists(self) -> None:
        """Verify CITATION.cff exists at repo root."""
        assert (PROJECT_ROOT / "CITATION.cff").exists(), "CITATION.cff not found at repo root"

    def test_citation_cff_valid_yaml(self) -> None:
        """Verify CITATION.cff parses as valid YAML."""
        path = PROJECT_ROOT / "CITATION.cff"
        content = path.read_text(encoding="utf-8")
        data = yaml.safe_load(content)
        assert isinstance(data, dict), "CITATION.cff should parse as a YAML mapping"

    def test_citation_cff_has_doi(self) -> None:
        """Verify doi field contains SSRN DOI."""
        path = PROJECT_ROOT / "CITATION.cff"
        content = path.read_text(encoding="utf-8")
        data = yaml.safe_load(content)
        # DOI can be in top-level or preferred-citation
        preferred = data.get("preferred-citation", {})
        doi = preferred.get("doi", data.get("doi", ""))
        assert "10.2139/ssrn.6109087" in doi, f"Expected SSRN DOI, got: {doi}"

    def test_citation_cff_has_author(self) -> None:
        """Verify Teikari appears in authors."""
        path = PROJECT_ROOT / "CITATION.cff"
        content = path.read_text(encoding="utf-8")
        data = yaml.safe_load(content)
        authors = data.get("authors", [])
        author_names = [a.get("family-names", "") for a in authors]
        assert "Teikari" in author_names, f"Expected 'Teikari' in authors, got: {author_names}"


class TestContributingMd:
    """Tests for CONTRIBUTING.md (Task A3)."""

    @pytest.fixture(scope="class")
    def content(self) -> str:
        """Load CONTRIBUTING.md."""
        return (PROJECT_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")

    def test_contributing_md_exists(self) -> None:
        """Verify CONTRIBUTING.md at repo root."""
        assert (PROJECT_ROOT / "CONTRIBUTING.md").exists()

    def test_contributing_mentions_uv(self, content: str) -> None:
        """Verify uv package manager is mentioned."""
        assert "uv" in content.lower(), "CONTRIBUTING.md should mention uv"

    def test_contributing_mentions_precommit(self, content: str) -> None:
        """Verify pre-commit hooks are mentioned."""
        assert "pre-commit" in content.lower(), "CONTRIBUTING.md should mention pre-commit"

    def test_contributing_mentions_tests(self, content: str) -> None:
        """Verify testing is mentioned."""
        assert "test" in content.lower(), "CONTRIBUTING.md should mention testing"


class TestSecurityMd:
    """Tests for SECURITY.md (Task A4)."""

    def test_security_md_exists(self) -> None:
        """Verify SECURITY.md at repo root."""
        assert (PROJECT_ROOT / "SECURITY.md").exists()

    def test_security_mentions_scope(self) -> None:
        """Verify research scaffold disclaimer."""
        content = (PROJECT_ROOT / "SECURITY.md").read_text(encoding="utf-8")
        assert "research scaffold" in content.lower() or "research" in content.lower(), (
            "SECURITY.md should mention research scope"
        )


class TestChangelogMd:
    """Tests for CHANGELOG.md (Task A5)."""

    @pytest.fixture(scope="class")
    def content(self) -> str:
        """Load CHANGELOG.md."""
        return (PROJECT_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

    def test_changelog_exists(self) -> None:
        """Verify CHANGELOG.md at repo root."""
        assert (PROJECT_ROOT / "CHANGELOG.md").exists()

    def test_changelog_has_unreleased(self, content: str) -> None:
        """Verify [Unreleased] section exists."""
        assert "Unreleased" in content, "CHANGELOG.md should have an [Unreleased] section"

    def test_changelog_mentions_version(self, content: str) -> None:
        """Verify at least one version entry."""
        assert "[0." in content, "CHANGELOG.md should have at least one [0.x.y] version entry"


class TestIssueTemplates:
    """Tests for .github/ISSUE_TEMPLATE/ (Task A6)."""

    TEMPLATE_DIR = PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE"

    def test_issue_templates_exist(self) -> None:
        """Verify all 3 template files exist."""
        assert (self.TEMPLATE_DIR / "bug_report.md").exists(), "Missing bug_report.md template"
        assert (self.TEMPLATE_DIR / "feature_request.md").exists(), "Missing feature_request.md template"
        assert (self.TEMPLATE_DIR / "research_question.md").exists(), "Missing research_question.md template"

    def test_issue_templates_have_frontmatter(self) -> None:
        """Verify YAML frontmatter with name/about fields."""
        for template_name in ["bug_report.md", "feature_request.md", "research_question.md"]:
            path = self.TEMPLATE_DIR / template_name
            content = path.read_text(encoding="utf-8")
            assert content.startswith("---"), f"{template_name} should start with YAML frontmatter '---'"
            # Extract frontmatter
            parts = content.split("---", 2)
            assert len(parts) >= 3, f"{template_name} should have complete YAML frontmatter"
            frontmatter = yaml.safe_load(parts[1])
            assert "name" in frontmatter, f"{template_name} frontmatter missing 'name'"
            assert "about" in frontmatter, f"{template_name} frontmatter missing 'about'"


class TestPrTemplate:
    """Tests for .github/PULL_REQUEST_TEMPLATE.md (Task A7)."""

    def test_pr_template_exists(self) -> None:
        """Verify PR template exists."""
        assert (PROJECT_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").exists()

    def test_pr_template_has_checklist(self) -> None:
        """Verify PR template contains checkbox markers."""
        content = (PROJECT_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")
        assert "- [ ]" in content, "PR template should contain checklist items '- [ ]'"
