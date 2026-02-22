"""Tests for Letta persona memory integration (Task 3.2)."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from music_attribution.voice.config import VoiceConfig


class TestLettaClientFactory:
    """Tests for Letta client creation and configuration."""

    def test_letta_module_importable(self) -> None:
        """Letta integration module is importable."""
        from music_attribution.voice import letta_integration

        assert letta_integration is not None

    def test_letta_available_flag_exists(self) -> None:
        """Module has LETTA_AVAILABLE flag."""
        from music_attribution.voice.letta_integration import LETTA_AVAILABLE

        assert isinstance(LETTA_AVAILABLE, bool)

    def test_create_letta_client_requires_base_url(self) -> None:
        """create_letta_client raises ValueError without base_url (when letta installed)."""
        from music_attribution.voice.letta_integration import LETTA_AVAILABLE, create_letta_client

        config = VoiceConfig(letta_base_url=None)
        if not LETTA_AVAILABLE:
            # Without letta-client, ImportError is raised before config check
            with pytest.raises(ImportError, match="letta-client"):
                create_letta_client(config)
        else:
            with pytest.raises(ValueError, match="letta_base_url"):
                create_letta_client(config)

    def test_create_letta_client_with_url(self) -> None:
        """create_letta_client returns a client dict/stub with URL set."""
        from music_attribution.voice.letta_integration import LETTA_AVAILABLE, create_letta_client

        if not LETTA_AVAILABLE:
            pytest.skip("Letta not installed")
        config = VoiceConfig(letta_base_url="http://localhost:8283")
        client = create_letta_client(config)
        assert client is not None


class TestLettaPersonaBlock:
    """Tests for Letta persona block management."""

    def test_get_persona_block_returns_string(self) -> None:
        """get_persona_block returns the immutable persona text."""
        from music_attribution.voice.letta_integration import get_persona_block

        block = get_persona_block()
        assert isinstance(block, str)
        assert "Music Attribution Assistant" in block

    def test_persona_block_contains_core_identity(self) -> None:
        """Persona block includes the immutable core identity."""
        from music_attribution.voice.letta_integration import get_persona_block

        block = get_persona_block()
        assert "transparent" in block.lower()
        assert "evidence" in block.lower()


class TestLettaFallback:
    """Tests for graceful fallback when Letta is unavailable."""

    def test_get_user_context_without_letta_returns_empty(self) -> None:
        """get_user_context returns empty string when Letta unavailable."""
        from music_attribution.voice.letta_integration import get_user_context

        config = VoiceConfig(persona_enabled=True, letta_base_url=None)
        context = get_user_context(config, user_id="test-user")
        assert context == ""

    def test_fallback_logged_when_letta_unavailable(self) -> None:
        """Fallback to prompt-only mode is logged."""
        from music_attribution.voice.letta_integration import get_user_context

        config = VoiceConfig(persona_enabled=True, letta_base_url=None)
        with patch("music_attribution.voice.letta_integration.logger") as mock_logger:
            get_user_context(config, user_id="test-user")
            mock_logger.info.assert_called()


class TestLettaPersonaPromptIntegration:
    """Tests for Letta integration with the persona prompt builder."""

    def test_build_prompt_with_letta_context(self) -> None:
        """build_system_prompt uses Letta context when available."""
        from music_attribution.voice.persona import build_system_prompt

        config = VoiceConfig(persona_enabled=True)
        prompt = build_system_prompt(config, user_context="prefers jazz analysis")
        assert "prefers jazz analysis" in prompt
