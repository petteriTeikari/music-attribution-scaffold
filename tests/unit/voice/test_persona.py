"""Tests for voice persona prompt builder."""

from __future__ import annotations

from music_attribution.voice.config import VoiceConfig
from music_attribution.voice.persona import (
    CORE_IDENTITY,
    FACTUAL_GROUNDING,
    REINFORCEMENT_REMINDER,
    VOICE_STYLE,
    build_system_prompt,
    get_reinforcement_reminder,
)


class TestBuildSystemPrompt:
    """Tests for the multi-dimensional persona prompt builder."""

    def test_includes_core_identity(self) -> None:
        """System prompt always includes the immutable core identity."""
        config = VoiceConfig()
        prompt = build_system_prompt(config)
        assert "Music Attribution Assistant" in prompt

    def test_includes_factual_grounding(self) -> None:
        """System prompt includes A0-A3 factual grounding."""
        config = VoiceConfig()
        prompt = build_system_prompt(config)
        assert "A0-A3" in prompt
        assert "Oracle Problem" in prompt

    def test_includes_voice_style(self) -> None:
        """System prompt includes voice communication style."""
        config = VoiceConfig()
        prompt = build_system_prompt(config)
        assert "speaking aloud" in prompt
        assert "concise" in prompt

    def test_all_five_dimensions_present(self) -> None:
        """All five persona dimensions are represented."""
        config = VoiceConfig()
        prompt = build_system_prompt(config)
        # Core Identity
        assert CORE_IDENTITY in prompt
        # Factual Grounding
        assert FACTUAL_GROUNDING in prompt
        # Communication Style
        assert VOICE_STYLE in prompt

    def test_user_context_injected_when_provided(self) -> None:
        """User context layer is added when provided."""
        config = VoiceConfig()
        prompt = build_system_prompt(config, user_context="prefers detailed explanations")
        assert "prefers detailed explanations" in prompt

    def test_user_context_absent_when_empty(self) -> None:
        """User context is not injected when empty string."""
        config = VoiceConfig()
        prompt = build_system_prompt(config, user_context="")
        assert "User context:" not in prompt

    def test_reinforcement_at_interval(self) -> None:
        """Persona reinforcement is injected at the configured interval."""
        config = VoiceConfig(persona_reinforcement_interval=5)
        # At turn 5, should get reinforcement
        prompt = build_system_prompt(config, turn_count=5)
        assert REINFORCEMENT_REMINDER in prompt

    def test_no_reinforcement_at_turn_zero(self) -> None:
        """No reinforcement at turn 0 (start of conversation)."""
        config = VoiceConfig(persona_reinforcement_interval=5)
        prompt = build_system_prompt(config, turn_count=0)
        assert REINFORCEMENT_REMINDER not in prompt

    def test_no_reinforcement_between_intervals(self) -> None:
        """No reinforcement at turns between intervals."""
        config = VoiceConfig(persona_reinforcement_interval=5)
        for turn in [1, 2, 3, 4, 6, 7, 8, 9]:
            prompt = build_system_prompt(config, turn_count=turn)
            assert REINFORCEMENT_REMINDER not in prompt, f"Unexpected reinforcement at turn {turn}"

    def test_reinforcement_at_multiple_intervals(self) -> None:
        """Reinforcement triggers at every interval (5, 10, 15, ...)."""
        config = VoiceConfig(persona_reinforcement_interval=5)
        for turn in [5, 10, 15, 20]:
            prompt = build_system_prompt(config, turn_count=turn)
            assert REINFORCEMENT_REMINDER in prompt, f"Missing reinforcement at turn {turn}"

    def test_custom_reinforcement_interval(self) -> None:
        """Reinforcement interval is configurable."""
        config = VoiceConfig(persona_reinforcement_interval=3)
        assert REINFORCEMENT_REMINDER in build_system_prompt(config, turn_count=3)
        assert REINFORCEMENT_REMINDER in build_system_prompt(config, turn_count=6)
        assert REINFORCEMENT_REMINDER not in build_system_prompt(config, turn_count=4)


class TestGetReinforcementReminder:
    """Tests for the reinforcement reminder getter."""

    def test_returns_non_empty_string(self) -> None:
        """Reinforcement reminder is a non-empty string."""
        reminder = get_reinforcement_reminder()
        assert isinstance(reminder, str)
        assert len(reminder) > 0

    def test_contains_persona_identity(self) -> None:
        """Reinforcement reminder references the persona identity."""
        reminder = get_reinforcement_reminder()
        assert "Music Attribution Assistant" in reminder
