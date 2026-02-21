"""Tests for PydanticAI-to-Pipecat tool schema bridge."""

from __future__ import annotations

import pytest

from music_attribution.voice.tools import (
    get_function_schemas,
    get_tool_schemas,
)


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


class TestGetFunctionSchemas:
    """Tests for Pipecat FunctionSchema wrapper."""

    def test_returns_four_schemas(self) -> None:
        """get_function_schemas returns 4 items."""
        schemas = get_function_schemas()
        assert len(schemas) == 4

    def test_schemas_are_dicts_without_pipecat(self) -> None:
        """Without pipecat, falls back to dict format."""
        from music_attribution.voice.tools import PIPECAT_AVAILABLE

        schemas = get_function_schemas()
        if not PIPECAT_AVAILABLE:
            assert all(isinstance(s, dict) for s in schemas)


class TestSessionFactory:
    """Tests for database session factory management."""

    def test_session_factory_initially_none(self) -> None:
        """Module-level session factory starts as None."""
        # Import fresh to check initial state
        import music_attribution.voice.tools as tools_mod

        # It may have been set by other tests, so just check the function exists
        assert callable(tools_mod.set_session_factory)

    def test_set_session_factory_sets_value(self) -> None:
        """set_session_factory updates the module-level factory."""
        import music_attribution.voice.tools as tools_mod

        sentinel = object()
        old = tools_mod._session_factory
        try:
            tools_mod.set_session_factory(sentinel)  # type: ignore[arg-type]
            assert tools_mod._session_factory is sentinel
        finally:
            tools_mod._session_factory = old  # type: ignore[assignment]


class TestToolHandlers:
    """Tests for individual tool handler functions."""

    @pytest.mark.anyio
    async def test_explain_confidence_no_db(self) -> None:
        """explain_confidence returns error when no DB session."""
        import music_attribution.voice.tools as tools_mod

        old = tools_mod._session_factory
        tools_mod._session_factory = None

        results: list[dict] = []

        class MockParams:
            arguments = {"work_id": "00000000-0000-0000-0000-000000000001"}

            async def result_callback(self, result: dict) -> None:
                results.append(result)

        try:
            await tools_mod._handle_explain_confidence(MockParams())
            assert len(results) == 1
            assert "Database not available" in results[0]["explanation"]
        finally:
            tools_mod._session_factory = old  # type: ignore[assignment]

    @pytest.mark.anyio
    async def test_search_attributions_no_db(self) -> None:
        """search_attributions returns error when no DB session."""
        import music_attribution.voice.tools as tools_mod

        old = tools_mod._session_factory
        tools_mod._session_factory = None

        results: list[dict] = []

        class MockParams:
            arguments = {"query": "test search"}

            async def result_callback(self, result: dict) -> None:
                results.append(result)

        try:
            await tools_mod._handle_search_attributions(MockParams())
            assert len(results) == 1
            assert "Database not available" in results[0]["results"]
        finally:
            tools_mod._session_factory = old  # type: ignore[assignment]

    @pytest.mark.anyio
    async def test_suggest_correction_returns_preview(self) -> None:
        """suggest_correction formats correction preview."""
        import music_attribution.voice.tools as tools_mod

        results: list[dict] = []

        class MockParams:
            arguments = {
                "work_id": "00000000-0000-0000-0000-000000000002",
                "field": "artist_name",
                "current_value": "Imogene Heap",
                "suggested_value": "Imogen Heap",
                "reason": "Typo in artist name",
            }

            async def result_callback(self, result: dict) -> None:
                results.append(result)

        await tools_mod._handle_suggest_correction(MockParams())
        assert len(results) == 1
        assert "Imogen Heap" in results[0]["result"]
        assert "Typo" in results[0]["result"]

    @pytest.mark.anyio
    async def test_submit_feedback_no_db(self) -> None:
        """submit_feedback returns error when no DB session."""
        import music_attribution.voice.tools as tools_mod

        old = tools_mod._session_factory
        tools_mod._session_factory = None

        results: list[dict] = []

        class MockParams:
            arguments = {"work_id": "00000000-0000-0000-0000-000000000003", "overall_assessment": 0.8}

            async def result_callback(self, result: dict) -> None:
                results.append(result)

        try:
            await tools_mod._handle_submit_feedback(MockParams())
            assert len(results) == 1
            assert "Database not available" in results[0]["result"]
        finally:
            tools_mod._session_factory = old  # type: ignore[assignment]
