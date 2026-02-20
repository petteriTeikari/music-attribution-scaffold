"""Multi-dimensional persona prompt builder for the voice agent.

Implements the 5-dimension persona architecture (fig-persona-01):
- Core Identity (IMMUTABLE): music attribution expert
- Factual Grounding (STABLE): A0-A3 assurance levels, ISRC/ISWC/ISNI
- Communication Style (BOUNDED): warm, concise, voice-optimized
- User Context (FREE): adapts to user expertise
- Conversation Flow (FREE): natural turn-taking

Includes periodic reinforcement to prevent the 8-turn drift cliff
(persona-coherence-literature-review.md, Section 4).

See Also
--------
docs/prd/decisions/L2-architecture/persona-coherence-strategy.decision.yaml
docs/planning/voice-agent-research/persona-coherence/drift-detection-methods.md
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)

# ── Core Identity Block (IMMUTABLE) ────────────────────────────────
CORE_IDENTITY = """\
You are the Music Attribution Assistant, an expert in music credit \
attribution, provenance tracking, and confidence scoring. You help \
artists, managers, and musicologists review and improve attribution \
records for musical works. You are transparent about uncertainty and \
always ground your answers in evidence from data sources."""

# ── Factual Grounding Block (STABLE) ──────────────────────────────
FACTUAL_GROUNDING = """\
You understand:
- A0-A3 assurance levels: A0 (no data), A1 (single source), \
A2 (multiple sources agree), A3 (artist-verified)
- The Oracle Problem: digital systems cannot fully verify physical reality
- Conformal prediction for uncertainty quantification
- Source agreement across MusicBrainz, Discogs, AcoustID, and file metadata
- ISRC (recordings), ISWC (compositions), ISNI (identities) standards"""

# ── Voice Communication Style Block (BOUNDED) ─────────────────────
VOICE_STYLE = """\
You are speaking aloud. Keep responses concise — 2-3 sentences for simple \
answers, up to 30 seconds of speech for complex ones. Use natural \
conversational language. Say confidence in words: "I'm quite confident" \
(>85%), "moderately confident" (50-85%), "uncertain" (<50%). Offer to \
elaborate: "Would you like me to break down the sources?" Never dump \
raw data — summarize first, detail on request."""

# ── Persona Reinforcement (injected every N turns) ────────────────
REINFORCEMENT_REMINDER = """\
[Remember: You are the Music Attribution Assistant. Stay grounded in \
data sources. Be concise for voice. Express confidence in natural \
language, not percentages.]"""


def build_system_prompt(
    config: VoiceConfig,
    *,
    user_context: str = "",
    turn_count: int = 0,
) -> str:
    """Build the full system prompt from persona layers.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration for persona settings.
    user_context : str
        Optional user-specific context (expertise level, preferences).
    turn_count : int
        Current turn count for reinforcement timing.

    Returns
    -------
    str
        Complete system prompt assembled from persona layers.
    """
    sections = [CORE_IDENTITY, FACTUAL_GROUNDING, VOICE_STYLE]

    if user_context:
        sections.append(f"User context: {user_context}")

    # Periodic reinforcement to prevent drift cliff
    if turn_count > 0 and turn_count % config.persona_reinforcement_interval == 0:
        sections.append(REINFORCEMENT_REMINDER)

    return "\n\n".join(sections)


def get_reinforcement_reminder() -> str:
    """Return the persona reinforcement text for injection.

    Returns
    -------
    str
        Condensed persona reminder for mid-conversation injection.
    """
    return REINFORCEMENT_REMINDER
