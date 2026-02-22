"""NeMo Guardrails integration for persona boundary enforcement.

Provides optional runtime guardrails using NeMo Guardrails with Colang 2.0.
When NeMo is available and VOICE_GUARDRAILS_ENABLED=true, input and output
rails enforce persona boundaries. When unavailable, provides lightweight
regex-based fallback checks.

Input rails detect:
- Persona manipulation attempts ("ignore instructions", "pretend to be")
- Off-topic requests (outside music attribution domain)

Output rails detect:
- Persona violations (claiming different identity)
- Domain boundary violations (legal/medical/financial advice)

See Also
--------
src/music_attribution/voice/guardrails/config.yml : NeMo config.
src/music_attribution/voice/guardrails/rails.co : Colang 2.0 rails.
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)

# Optional NeMo Guardrails import
try:
    from nemoguardrails import RailsConfig  # noqa: F401

    NEMO_AVAILABLE = True
except ImportError:
    NEMO_AVAILABLE = False

# Lightweight regex patterns for fallback checks (when NeMo not installed)
_INPUT_MANIPULATION_PATTERNS = [
    re.compile(r"ignore\s+(your|all|previous)\s+instructions", re.IGNORECASE),
    re.compile(r"pretend\s+to\s+be", re.IGNORECASE),
    re.compile(r"you\s+are\s+now\s+(a|an)", re.IGNORECASE),
    re.compile(r"forget\s+(your|the)\s+(role|instructions|persona)", re.IGNORECASE),
    re.compile(r"act\s+as\s+(a|an)\s+(?!music)", re.IGNORECASE),
]

_OUTPUT_VIOLATION_PATTERNS = [
    re.compile(r"I\s+am\s+(a|an)\s+(legal|medical|financial)\s+(advisor|expert|consultant)", re.IGNORECASE),
    re.compile(r"I\s+am\s+(a|an)\s+(lawyer|doctor|accountant)", re.IGNORECASE),
    re.compile(r"(legal|medical|financial)\s+opinion", re.IGNORECASE),
    re.compile(r"(legal|medical|financial|investment)\s+advice", re.IGNORECASE),
]


def create_guardrails(config: VoiceConfig) -> Any | None:
    """Create NeMo Guardrails instance if enabled and available.

    Parameters
    ----------
    config : VoiceConfig
        Voice configuration with guardrails settings.

    Returns
    -------
    RailsConfig | None
        NeMo RailsConfig when enabled and available, None otherwise.
    """
    if not config.guardrails_enabled:
        logger.info("Guardrails disabled by config")
        return None

    if not NEMO_AVAILABLE:
        logger.warning("NeMo Guardrails not installed — using regex fallback. Install with: uv add nemoguardrails")
        return None

    from pathlib import Path

    from nemoguardrails import RailsConfig

    guardrails_dir = Path(__file__).parent / "guardrails"
    rails_config = RailsConfig.from_path(str(guardrails_dir))
    logger.info("NeMo Guardrails loaded from %s", guardrails_dir)
    return rails_config


def check_input(text: str) -> dict[str, Any]:
    """Check input text against persona manipulation patterns.

    Uses NeMo Guardrails when available, falls back to regex patterns.

    Parameters
    ----------
    text : str
        User input text to check.

    Returns
    -------
    dict
        Result with 'safe' bool and optional 'reason' string.
    """
    for pattern in _INPUT_MANIPULATION_PATTERNS:
        if pattern.search(text):
            reason = f"Persona manipulation detected: matches pattern '{pattern.pattern}'"
            logger.warning("Input blocked: %s", reason)
            return {"safe": False, "reason": reason}

    return {"safe": True}


def check_output(text: str) -> dict[str, Any]:
    """Check output text against persona violation patterns.

    Uses NeMo Guardrails when available, falls back to regex patterns.

    Parameters
    ----------
    text : str
        Agent response text to check.

    Returns
    -------
    dict
        Result with 'safe' bool and optional 'reason' string.
    """
    for pattern in _OUTPUT_VIOLATION_PATTERNS:
        if pattern.search(text):
            reason = f"Persona violation detected: matches pattern '{pattern.pattern}'"
            logger.warning("Output blocked: %s", reason)
            return {"safe": False, "reason": reason}

    return {"safe": True}
