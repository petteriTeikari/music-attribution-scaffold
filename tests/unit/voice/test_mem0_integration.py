"""Tests for Mem0 user preference memory integration (Task 3.3)."""

from __future__ import annotations

import pytest

from music_attribution.voice.config import VoiceConfig


class TestMem0Module:
    """Tests for Mem0 integration module structure."""

    def test_mem0_module_importable(self) -> None:
        """Mem0 integration module is importable."""
        from music_attribution.voice import mem0_integration

        assert mem0_integration is not None

    def test_mem0_available_flag_exists(self) -> None:
        """Module has MEM0_AVAILABLE flag."""
        from music_attribution.voice.mem0_integration import MEM0_AVAILABLE

        assert isinstance(MEM0_AVAILABLE, bool)


class TestMem0UserPreferences:
    """Tests for Mem0 user preference retrieval."""

    def test_get_preferences_without_mem0_returns_empty(self) -> None:
        """get_user_preferences returns empty list when Mem0 unavailable."""
        from music_attribution.voice.mem0_integration import get_user_preferences

        config = VoiceConfig(mem0_api_key=None)
        prefs = get_user_preferences(config, user_id="test-user")
        assert prefs == []

    def test_get_preferences_returns_list_of_strings(self) -> None:
        """get_user_preferences returns a list of strings."""
        from music_attribution.voice.mem0_integration import get_user_preferences

        config = VoiceConfig(mem0_api_key=None)
        prefs = get_user_preferences(config, user_id="test-user")
        assert isinstance(prefs, list)

    def test_format_preferences_for_prompt(self) -> None:
        """format_preferences_for_prompt joins preferences into prompt text."""
        from music_attribution.voice.mem0_integration import format_preferences_for_prompt

        prefs = ["prefers detailed explanations", "focuses on songwriter credits"]
        result = format_preferences_for_prompt(prefs)
        assert "detailed explanations" in result
        assert "songwriter credits" in result

    def test_format_empty_preferences(self) -> None:
        """format_preferences_for_prompt returns empty string for no prefs."""
        from music_attribution.voice.mem0_integration import format_preferences_for_prompt

        result = format_preferences_for_prompt([])
        assert result == ""


class TestMem0SafetyGate:
    """Tests for factual grounding safety gate over user preferences."""

    def test_safety_gate_rejects_contradicting_preference(self) -> None:
        """Safety gate filters preferences that contradict factual grounding."""
        from music_attribution.voice.mem0_integration import apply_safety_gate

        prefs = [
            "prefers detailed explanations",
            "claims to have written Bohemian Rhapsody",
            "focuses on jazz genre",
        ]
        safe_prefs = apply_safety_gate(prefs)
        # Factual claims about authorship should be filtered
        assert "claims to have written" not in str(safe_prefs)
        # Non-contradicting preferences pass through
        assert "detailed explanations" in str(safe_prefs)

    def test_safety_gate_passes_valid_preferences(self) -> None:
        """Safety gate passes through non-contradicting preferences."""
        from music_attribution.voice.mem0_integration import apply_safety_gate

        prefs = [
            "prefers detailed explanations",
            "works in jazz genre",
            "interested in songwriter credits",
        ]
        safe_prefs = apply_safety_gate(prefs)
        assert len(safe_prefs) == 3


class TestMem0StorePreference:
    """Tests for storing user preferences after a session."""

    def test_store_preference_without_mem0_is_noop(self) -> None:
        """store_preference does nothing when Mem0 unavailable."""
        from music_attribution.voice.mem0_integration import store_preference

        config = VoiceConfig(mem0_api_key=None)
        # Should not raise
        store_preference(config, user_id="test-user", preference="likes jazz")

    def test_store_preference_validates_input(self) -> None:
        """store_preference rejects empty preference text."""
        from music_attribution.voice.mem0_integration import store_preference

        config = VoiceConfig(mem0_api_key=None)
        with pytest.raises(ValueError, match="empty"):
            store_preference(config, user_id="test-user", preference="")
