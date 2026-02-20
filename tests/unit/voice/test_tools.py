"""Tests for PydanticAI-to-Pipecat tool schema bridge."""

from __future__ import annotations

from music_attribution.voice.tools import get_tool_schemas


class TestGetToolSchemas:
    """Tests for tool schema generation."""

    def test_returns_four_schemas(self) -> None:
        """Four domain tools are registered."""
        schemas = get_tool_schemas()
        assert len(schemas) == 4

    def test_schema_format(self) -> None:
        """Each schema has the expected structure."""
        schemas = get_tool_schemas()
        for schema in schemas:
            assert schema["type"] == "function"
            assert "function" in schema
            assert "name" in schema["function"]
            assert "description" in schema["function"]
            assert "parameters" in schema["function"]

    def test_tool_names(self) -> None:
        """All four domain tools are registered by name."""
        schemas = get_tool_schemas()
        names = {s["function"]["name"] for s in schemas}
        assert names == {
            "explain_confidence",
            "search_attributions",
            "suggest_correction",
            "submit_feedback",
        }

    def test_explain_confidence_params(self) -> None:
        """explain_confidence requires work_id parameter."""
        schemas = get_tool_schemas()
        schema = next(s for s in schemas if s["function"]["name"] == "explain_confidence")
        params = schema["function"]["parameters"]
        assert "work_id" in params["properties"]
        assert "work_id" in params["required"]

    def test_search_attributions_params(self) -> None:
        """search_attributions requires query parameter."""
        schemas = get_tool_schemas()
        schema = next(s for s in schemas if s["function"]["name"] == "search_attributions")
        params = schema["function"]["parameters"]
        assert "query" in params["properties"]
        assert "query" in params["required"]

    def test_suggest_correction_has_five_params(self) -> None:
        """suggest_correction has all five required parameters."""
        schemas = get_tool_schemas()
        schema = next(s for s in schemas if s["function"]["name"] == "suggest_correction")
        params = schema["function"]["parameters"]
        required = set(params["required"])
        assert required == {"work_id", "field", "current_value", "suggested_value", "reason"}

    def test_submit_feedback_params(self) -> None:
        """submit_feedback requires work_id and overall_assessment."""
        schemas = get_tool_schemas()
        schema = next(s for s in schemas if s["function"]["name"] == "submit_feedback")
        params = schema["function"]["parameters"]
        assert "work_id" in params["required"]
        assert "overall_assessment" in params["required"]
