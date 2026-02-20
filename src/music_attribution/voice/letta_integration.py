"""Letta (MemGPT) integration for persistent persona memory.

Provides optional integration with Letta for memory-anchored persona.
When Letta is available and configured, the persona is stored as a
read-only memory block. When unavailable, falls back to prompt-only
approach (persona.py constants).

The Letta persona block is ALWAYS read-only — core identity cannot be
modified at runtime. Only the user context (human memory block) is
mutable, allowing the agent to remember user preferences across sessions.

See Also
--------
music_attribution.voice.persona : Prompt-only persona builder (fallback).
docs/prd/decisions/L3-implementation/voice-persona-management.decision.yaml
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)

# Optional Letta import
try:
    from letta_client import Letta  # noqa: F401

    LETTA_AVAILABLE = True
except ImportError:
    LETTA_AVAILABLE = False


def get_persona_block() -> str:
    """Return the immutable persona block text for Letta.

    This is the same core identity used in prompt-only mode,
    formatted for Letta's persona memory block.

    Returns
    -------
    str
        Persona block text including core identity and factual grounding.
    """
    from music_attribution.voice.persona import CORE_IDENTITY, FACTUAL_GROUNDING

    return f"{CORE_IDENTITY}\n\n{FACTUAL_GROUNDING}"


def create_letta_client(config: VoiceConfig) -> Any:
    """Create a Letta client connected to the configured server.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration with Letta settings.

    Returns
    -------
    Letta
        Connected Letta client.

    Raises
    ------
    ValueError
        If letta_base_url is not configured.
    ImportError
        If letta-client is not installed.
    """
    if not config.letta_base_url:
        msg = "letta_base_url must be configured for Letta integration"
        raise ValueError(msg)

    if not LETTA_AVAILABLE:
        msg = "letta-client is not installed. Install with: uv add letta-client"
        raise ImportError(msg)

    client = Letta(base_url=config.letta_base_url)
    logger.info("Letta client connected to %s", config.letta_base_url)
    return client


def get_user_context(
    config: VoiceConfig,
    *,
    user_id: str,
) -> str:
    """Retrieve user-specific context from Letta memory.

    Falls back to empty string if Letta is unavailable or not configured.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration.
    user_id : str
        User identifier for memory lookup.

    Returns
    -------
    str
        User context string, or empty if unavailable.
    """
    if not config.letta_base_url or not LETTA_AVAILABLE:
        logger.info(
            "Letta unavailable (base_url=%s, installed=%s) — using prompt-only persona",
            config.letta_base_url,
            LETTA_AVAILABLE,
        )
        return ""

    try:
        client = create_letta_client(config)
        # Search for user-specific memory
        agents = client.agents.list()
        for agent in agents:
            if hasattr(agent, "metadata") and agent.metadata.get("user_id") == user_id:
                # Found user's agent — retrieve human memory block
                memory = client.agents.get_memory(agent.id)
                if hasattr(memory, "human") and memory.human:
                    return str(memory.human)
        logger.info("No Letta agent found for user %s", user_id)
        return ""
    except Exception:
        logger.exception("Letta user context retrieval failed for user %s", user_id)
        return ""
