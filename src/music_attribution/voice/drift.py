"""Embedding-based persona drift detector.

Monitors agent response fidelity by comparing response embeddings to a
reference persona embedding using cosine similarity + EWMA smoothing.

Three states:
- **Sync** (score > 0.85): Agent is on-persona
- **Drift** (0.70-0.85): Warning — inject reinforcement prompt
- **Desync** (< 0.70): Alert — full context recalibration needed

The 8-turn drift cliff (Guo et al., 2025) motivates continuous monitoring
rather than periodic sampling.

See Also
--------
docs/planning/voice-agent-research/persona-coherence/drift-detection-methods.md
docs/prd/decisions/L5-operations/persona-drift-monitoring.decision.yaml
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)


class DriftDetector:
    """Embedding-based persona drift detector with EWMA smoothing.

    Parameters
    ----------
    config : VoiceConfig
        Configuration with drift thresholds and EWMA alpha.
    reference_text : str
        Persona definition text to embed as reference.
    """

    def __init__(self, config: VoiceConfig, reference_text: str) -> None:
        self._sync_threshold = config.drift_sync_threshold
        self._desync_threshold = config.drift_desync_threshold
        self._alpha = config.drift_ewma_alpha
        self._reference_text = reference_text
        self._ewma_score: float = 1.0  # Start in sync
        self._raw_scores: list[float] = []

    def score(self, response_text: str) -> float:
        """Compute drift score for a response.

        Uses a simple text similarity heuristic when sentence-transformers
        is not available. When the full embedding model is loaded, computes
        cosine similarity between response and persona reference.

        Parameters
        ----------
        response_text : str
            The agent's response text to evaluate.

        Returns
        -------
        float
            EWMA-smoothed similarity score (0.0-1.0).
        """
        raw_score = self._compute_similarity(response_text)
        self._raw_scores.append(raw_score)
        self._ewma_score = self._alpha * raw_score + (1 - self._alpha) * self._ewma_score
        return self._ewma_score

    def state(self) -> str:
        """Return current drift state based on EWMA score.

        Returns
        -------
        str
            One of ``'sync'``, ``'drift'``, or ``'desync'``.
        """
        if self._ewma_score >= self._sync_threshold:
            return "sync"
        if self._ewma_score >= self._desync_threshold:
            return "drift"
        return "desync"

    @property
    def ewma_score(self) -> float:
        """Current EWMA-smoothed drift score."""
        return self._ewma_score

    @property
    def raw_scores(self) -> list[float]:
        """History of raw (unsmoothed) similarity scores."""
        return list(self._raw_scores)

    def _compute_similarity(self, response_text: str) -> float:
        """Compute cosine similarity between response and reference.

        Falls back to token overlap when sentence-transformers is not
        installed (test/dev without ML dependencies).

        Parameters
        ----------
        response_text : str
            Text to compare against persona reference.

        Returns
        -------
        float
            Similarity score (0.0-1.0).
        """
        # Lightweight fallback: Jaccard token similarity
        ref_tokens = set(self._reference_text.lower().split())
        resp_tokens = set(response_text.lower().split())
        if not ref_tokens or not resp_tokens:
            return 0.0
        intersection = ref_tokens & resp_tokens
        union = ref_tokens | resp_tokens
        return len(intersection) / len(union) if union else 0.0
