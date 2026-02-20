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


class TestPromptLayering:
    """Tests for the 5-dimension persona layering architecture."""

    def test_layers_are_separated_by_double_newlines(self) -> None:
        """Persona layers are joined by double newlines for clarity."""
        config = VoiceConfig()
        prompt = build_system_prompt(config)
        # Should have at least 2 section separators
        assert prompt.count("\n\n") >= 2

    def test_core_identity_mentions_transparency(self) -> None:
        """Core identity includes transparency commitment."""
        assert "transparent" in CORE_IDENTITY.lower()

    def test_core_identity_mentions_evidence(self) -> None:
        """Core identity mentions evidence-based answers."""
        assert "evidence" in CORE_IDENTITY.lower()

    def test_factual_grounding_mentions_isrc(self) -> None:
        """Factual grounding includes ISRC standard."""
        assert "ISRC" in FACTUAL_GROUNDING

    def test_factual_grounding_mentions_musicbrainz(self) -> None:
        """Factual grounding includes MusicBrainz as data source."""
        assert "MusicBrainz" in FACTUAL_GROUNDING

    def test_voice_style_mentions_30_seconds(self) -> None:
        """Voice style limits complex answers to 30 seconds."""
        assert "30 seconds" in VOICE_STYLE

    def test_voice_style_includes_confidence_language(self) -> None:
        """Voice style defines natural language for confidence levels."""
        assert "quite confident" in VOICE_STYLE
        assert "moderately confident" in VOICE_STYLE
        assert "uncertain" in VOICE_STYLE

    def test_reinforcement_is_concise(self) -> None:
        """Reinforcement reminder is under 200 chars for low context overhead."""
        assert len(REINFORCEMENT_REMINDER) < 300

    def test_prompt_with_all_layers_is_under_2000_chars(self) -> None:
        """Full prompt stays under 2000 chars for reasonable context usage."""
        config = VoiceConfig()
        prompt = build_system_prompt(
            config,
            user_context="Expert musicologist, prefers detailed explanations",
            turn_count=5,
        )
        # Should be substantial but not huge
        assert len(prompt) < 2000

    def test_user_context_comes_after_voice_style(self) -> None:
        """User context layer appears after voice style in prompt."""
        config = VoiceConfig()
        prompt = build_system_prompt(config, user_context="test context")
        style_pos = prompt.find(VOICE_STYLE)
        context_pos = prompt.find("test context")
        assert context_pos > style_pos


class TestPersonaImmutability:
    """Tests ensuring persona core dimensions are not modifiable."""

    def test_core_identity_is_constant(self) -> None:
        """CORE_IDENTITY is a module-level constant string."""
        assert isinstance(CORE_IDENTITY, str)
        assert len(CORE_IDENTITY) > 50

    def test_factual_grounding_is_constant(self) -> None:
        """FACTUAL_GROUNDING is a module-level constant string."""
        assert isinstance(FACTUAL_GROUNDING, str)
        assert len(FACTUAL_GROUNDING) > 50

    def test_voice_style_is_constant(self) -> None:
        """VOICE_STYLE is a module-level constant string."""
        assert isinstance(VOICE_STYLE, str)
        assert len(VOICE_STYLE) > 50

    def test_prompt_always_starts_with_core_identity(self) -> None:
        """System prompt always begins with core identity."""
        config = VoiceConfig()
        prompt = build_system_prompt(config, user_context="custom", turn_count=5)
        assert prompt.startswith(CORE_IDENTITY)
