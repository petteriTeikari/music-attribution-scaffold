"""Mem0 integration for cross-session user preference memory.

Provides optional integration with Mem0 for category-level user
preferences. These are abstract preferences ("prefers detailed
explanations", "focuses on songwriter credits") — NOT fine-grained
facts (PS-Bench: 244% attack surface increase for fact storage).

A safety gate ensures factual grounding overrides user preferences
when they contradict the database. If a user says "I wrote that song"
but the DB says otherwise, the DB wins.

See Also
--------
music_attribution.voice.letta_integration : Letta persona memory.
docs/prd/decisions/L3-implementation/user-modeling-strategy.decision.yaml
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)

# Optional Mem0 import
try:
    from mem0 import Memory  # noqa: F401

    MEM0_AVAILABLE = True
except ImportError:
    MEM0_AVAILABLE = False

# Patterns that indicate factual claims about authorship/ownership
# These should be filtered by the safety gate
_UNSAFE_PATTERNS = [
    re.compile(r"claims?\s+to\s+have\s+(written|composed|created|produced)", re.IGNORECASE),
    re.compile(r"(i|user)\s+(wrote|composed|created|own)", re.IGNORECASE),
    re.compile(r"says?\s+(they|he|she)\s+(wrote|own|created)", re.IGNORECASE),
]


def get_user_preferences(
    config: VoiceConfig,
    *,
    user_id: str,
) -> list[str]:
    """Retrieve user preferences from Mem0.

    Falls back to empty list if Mem0 is unavailable or not configured.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration with Mem0 settings.
    user_id : str
        User identifier for preference lookup.

    Returns
    -------
    list[str]
        List of user preference strings, or empty if unavailable.
    """
    if not config.mem0_api_key or not MEM0_AVAILABLE:
        logger.info(
            "Mem0 unavailable (api_key=%s, installed=%s) — no user preferences",
            "set" if config.mem0_api_key else "not set",
            MEM0_AVAILABLE,
        )
        return []

    try:
        from mem0 import MemoryClient

        client = MemoryClient(api_key=config.mem0_api_key)
        memories = client.search(
            query="user preferences",
            user_id=user_id,
            limit=10,
        )
        return [m.get("text", "") for m in memories if m.get("text")]
    except Exception:
        logger.exception("Mem0 preference retrieval failed for user %s", user_id)
        return []


def format_preferences_for_prompt(preferences: list[str]) -> str:
    """Format user preferences for injection into the system prompt.

    Parameters
    ----------
    preferences : list[str]
        List of user preference strings.

    Returns
    -------
    str
        Formatted preference text for system prompt, or empty string.
    """
    if not preferences:
        return ""

    prefs_text = "; ".join(preferences)
    return f"User preferences: {prefs_text}"


def apply_safety_gate(preferences: list[str]) -> list[str]:
    """Filter preferences that contradict factual grounding.

    The safety gate ensures that user preferences cannot override
    database facts. Preferences claiming authorship, ownership, or
    creation credits are filtered out.

    Parameters
    ----------
    preferences : list[str]
        Raw user preferences from Mem0.

    Returns
    -------
    list[str]
        Filtered preferences with factual claims removed.
    """
    safe = []
    for pref in preferences:
        is_unsafe = any(pattern.search(pref) for pattern in _UNSAFE_PATTERNS)
        if is_unsafe:
            logger.warning("Safety gate filtered preference: %s", pref)
        else:
            safe.append(pref)
    return safe


def store_preference(
    config: VoiceConfig,
    *,
    user_id: str,
    preference: str,
) -> None:
    """Store a user preference in Mem0.

    No-op if Mem0 is unavailable or not configured.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration with Mem0 settings.
    user_id : str
        User identifier.
    preference : str
        Preference text to store.

    Raises
    ------
    ValueError
        If preference text is empty.
    """
    if not preference.strip():
        msg = "Preference text cannot be empty"
        raise ValueError(msg)

    if not config.mem0_api_key or not MEM0_AVAILABLE:
        logger.info("Mem0 unavailable — preference not stored: %s", preference)
        return

    try:
        from mem0 import MemoryClient

        client = MemoryClient(api_key=config.mem0_api_key)
        client.add(
            messages=[{"role": "user", "content": preference}],
            user_id=user_id,
        )
        logger.info("Stored preference for user %s: %s", user_id, preference)
    except Exception:
        logger.exception("Failed to store preference for user %s", user_id)
