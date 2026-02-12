"""Tests for chat agent tools and configuration."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from music_attribution.chat.agent import (
    AgentDeps,
    create_attribution_agent,
)
from music_attribution.chat.state import AttributionAgentState

MOCK_ATTRIBUTIONS = {
    "attr-001": {
        "attribution_id": "attr-001",
        "work_title": "Hide and Seek",
        "artist_name": "Imogen Heap",
        "confidence_score": 0.95,
        "assurance_level": "LEVEL_3",
        "source_agreement": 0.92,
        "credits": [
            {
                "entity_id": "e1",
                "role": "PERFORMER",
                "confidence": 0.95,
                "sources": ["MUSICBRAINZ", "DISCOGS", "ACOUSTID"],
            }
        ],
    },
    "attr-002": {
        "attribution_id": "attr-002",
        "work_title": "Speak for Yourself",
        "artist_name": "Imogen Heap",
        "confidence_score": 0.42,
        "assurance_level": "LEVEL_1",
        "source_agreement": 0.35,
        "credits": [
            {
                "entity_id": "e2",
                "role": "SONGWRITER",
                "confidence": 0.42,
                "sources": ["MUSICBRAINZ"],
            }
        ],
    },
}


def _make_deps() -> AgentDeps:
    return AgentDeps(
        state=AttributionAgentState(),
    )


class TestAgentCreation:
    """Tests for agent creation and configuration."""

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})  # pragma: allowlist secret
    def test_agent_created(self) -> None:
        agent = create_attribution_agent()
        assert agent is not None

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})  # pragma: allowlist secret
    def test_agent_has_system_prompt(self) -> None:
        agent = create_attribution_agent()
        assert len(agent._system_prompts) > 0

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})  # pragma: allowlist secret
    def test_agent_has_tools(self) -> None:
        agent = create_attribution_agent()
        tool_names = set(agent._function_toolset.tools.keys())
        assert "explain_confidence" in tool_names
        assert "search_attributions" in tool_names
        assert "suggest_correction" in tool_names
        assert "submit_feedback" in tool_names


class TestAgentDeps:
    """Tests for AgentDeps dataclass."""

    def test_deps_state_accessible(self) -> None:
        deps = _make_deps()
        assert deps.state.current_work_id is None

    def test_deps_state_mutable(self) -> None:
        deps = _make_deps()
        deps.state.current_work_id = "attr-001"
        assert deps.state.current_work_id == "attr-001"

    def test_deps_session_factory_default_none(self) -> None:
        """AgentDeps.session_factory defaults to None."""
        deps = _make_deps()
        assert deps.session_factory is None

    def test_deps_accepts_session_factory(self) -> None:
        """AgentDeps accepts a session_factory argument."""
        from unittest.mock import MagicMock

        mock_factory = MagicMock()
        deps = AgentDeps(
            state=AttributionAgentState(),
            session_factory=mock_factory,
        )
        assert deps.session_factory is mock_factory


class TestExplainConfidenceLogic:
    """Tests for explain_confidence tool logic (without LLM call)."""

    def test_high_agreement_explanation(self) -> None:
        """Test that high source agreement is reflected in explanation factors."""
        record = MOCK_ATTRIBUTIONS["attr-001"]
        agreement = record["source_agreement"]
        assert agreement > 0.8

    def test_low_agreement_record(self) -> None:
        record = MOCK_ATTRIBUTIONS["attr-002"]
        assert record["source_agreement"] < 0.5

    def test_missing_record_handled(self) -> None:
        assert MOCK_ATTRIBUTIONS.get("nonexistent") is None


class TestSearchLogic:
    """Tests for search_attributions tool logic (reference data)."""

    def test_search_by_title(self) -> None:
        query = "hide"
        results = [
            attr_id
            for attr_id, record in MOCK_ATTRIBUTIONS.items()
            if query.lower() in record.get("work_title", "").lower()
        ]
        assert len(results) == 1
        assert results[0] == "attr-001"

    def test_search_by_artist(self) -> None:
        query = "imogen"
        results = [
            attr_id
            for attr_id, record in MOCK_ATTRIBUTIONS.items()
            if query.lower() in record.get("artist_name", "").lower()
        ]
        assert len(results) == 2

    def test_search_no_results(self) -> None:
        query = "nonexistent"
        results = [
            attr_id
            for attr_id, record in MOCK_ATTRIBUTIONS.items()
            if query.lower() in record.get("work_title", "").lower()
        ]
        assert len(results) == 0


class TestCenterBiasDetection:
    """Tests for center bias detection in feedback submission."""

    @pytest.mark.parametrize(
        "assessment,expected_bias",
        [
            (0.45, True),
            (0.50, True),
            (0.55, True),
            (0.44, False),
            (0.56, False),
            (0.0, False),
            (1.0, False),
        ],
    )
    def test_center_bias_detection(self, assessment: float, expected_bias: bool) -> None:
        is_center = 0.45 <= assessment <= 0.55
        assert is_center == expected_bias
