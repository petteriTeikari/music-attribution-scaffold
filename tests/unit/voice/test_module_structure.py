"""Tests for voice module structure and public API."""

from __future__ import annotations

import importlib


class TestVoiceModuleExports:
    """Verify voice module has expected public API."""

    def test_voice_package_importable(self) -> None:
        """Voice package can be imported."""
        mod = importlib.import_module("music_attribution.voice")
        assert mod is not None

    def test_config_importable(self) -> None:
        """VoiceConfig is importable from config module."""
        from music_attribution.voice.config import VoiceConfig

        assert VoiceConfig is not None

    def test_persona_importable(self) -> None:
        """Persona module is importable."""
        mod = importlib.import_module("music_attribution.voice.persona")
        assert hasattr(mod, "build_system_prompt")

    def test_pipeline_importable(self) -> None:
        """Pipeline module is importable."""
        mod = importlib.import_module("music_attribution.voice.pipeline")
        assert hasattr(mod, "create_voice_pipeline")

    def test_tools_importable(self) -> None:
        """Tools module is importable."""
        mod = importlib.import_module("music_attribution.voice.tools")
        assert hasattr(mod, "get_tool_schemas")

    def test_server_importable(self) -> None:
        """Server module is importable."""
        mod = importlib.import_module("music_attribution.voice.server")
        assert hasattr(mod, "create_voice_router")

    def test_drift_importable(self) -> None:
        """Drift detection module is importable."""
        mod = importlib.import_module("music_attribution.voice.drift")
        assert hasattr(mod, "DriftDetector")

    def test_protocols_importable(self) -> None:
        """Protocol interfaces are importable."""
        from music_attribution.voice.protocols import (
            STTServiceProtocol,
            TTSServiceProtocol,
        )

        assert STTServiceProtocol is not None
        assert TTSServiceProtocol is not None
