"""Embedding-based persona drift detector.

Monitors agent response fidelity by comparing response embeddings to a
reference persona embedding using cosine similarity + EWMA smoothing.

Three states:
- **Sync** (score > 0.85): Agent is on-persona
- **Drift** (0.70-0.85): Warning — inject reinforcement prompt
- **Desync** (< 0.70): Alert — full context recalibration needed

The 8-turn drift cliff (Guo et al., 2025) motivates continuous monitoring
rather than periodic sampling.

Also provides ``DriftMonitorProcessor``, a Pipecat FrameProcessor that
sits in the pipeline after the LLM and monitors output text for drift.

See Also
--------
docs/planning/voice-agent-research/persona-coherence/drift-detection-methods.md
docs/prd/decisions/L5-operations/persona-drift-monitoring.decision.yaml
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from music_attribution.voice.config import VoiceConfig

logger = logging.getLogger(__name__)

# Conditional Pipecat imports for the FrameProcessor
try:
    from pipecat.frames.frames import Frame, LLMTextFrame
    from pipecat.processors.frame_processor import FrameDirection, FrameProcessor

    PIPECAT_AVAILABLE = True
except ImportError:
    PIPECAT_AVAILABLE = False


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
        # Try sentence-transformers first
        try:
            return self._compute_embedding_similarity(response_text)
        except ImportError:
            pass

        # Lightweight fallback: Jaccard token similarity
        ref_tokens = set(self._reference_text.lower().split())
        resp_tokens = set(response_text.lower().split())
        if not ref_tokens or not resp_tokens:
            return 0.0
        intersection = ref_tokens & resp_tokens
        union = ref_tokens | resp_tokens
        return len(intersection) / len(union) if union else 0.0

    def _compute_embedding_similarity(self, response_text: str) -> float:
        """Compute cosine similarity using sentence-transformers.

        Parameters
        ----------
        response_text : str
            Text to compare against persona reference.

        Returns
        -------
        float
            Cosine similarity (0.0-1.0).

        Raises
        ------
        ImportError
            If sentence-transformers is not installed.
        """
        from sentence_transformers import SentenceTransformer

        # Cache the model on the instance
        if not hasattr(self, "_model"):
            self._model = SentenceTransformer("all-MiniLM-L6-v2")
        if not hasattr(self, "_ref_embedding"):
            self._ref_embedding = self._model.encode(self._reference_text)

        resp_embedding = self._model.encode(response_text)

        # Cosine similarity
        import numpy as np

        ref = self._ref_embedding
        dot_product = float(np.dot(ref, resp_embedding))
        norm_product = float(np.linalg.norm(ref) * np.linalg.norm(resp_embedding))
        if norm_product == 0:
            return 0.0
        return max(0.0, min(1.0, dot_product / norm_product))


if PIPECAT_AVAILABLE:

    class DriftMonitorProcessor(FrameProcessor):
        """Pipecat FrameProcessor that monitors LLM output for persona drift.

        Sits in the pipeline after the LLM service. Accumulates text tokens
        from ``LLMTextFrame`` and scores each complete response for drift.
        Passes all frames through without modification (monitoring only).

        Parameters
        ----------
        config : VoiceConfig
            Voice configuration with drift thresholds.
        reference_text : str
            Persona definition text for drift comparison.
        """

        def __init__(self, config: VoiceConfig, reference_text: str, **kwargs: Any) -> None:
            super().__init__(**kwargs)
            self._detector = DriftDetector(config, reference_text)
            self._current_response = ""

        async def process_frame(self, frame: Frame, direction: FrameDirection) -> None:
            """Process a frame, monitoring LLM text output for drift.

            Accumulates ``LLMTextFrame`` tokens. On ``LLMFullResponseEndFrame``,
            scores the complete response and logs drift state.

            All frames are passed through — this processor never blocks.

            Parameters
            ----------
            frame : Frame
                Incoming pipeline frame.
            direction : FrameDirection
                Frame flow direction (usually downstream).
            """
            # Accumulate LLM text tokens
            if isinstance(frame, LLMTextFrame):
                self._current_response += frame.text

            # Check for response completion
            from pipecat.frames.frames import LLMFullResponseEndFrame

            if isinstance(frame, LLMFullResponseEndFrame) and self._current_response:
                score = self._detector.score(self._current_response)
                state = self._detector.state()

                if state == "drift":
                    logger.warning(
                        "Persona drift detected (EWMA=%.3f, state=%s). Consider injecting reinforcement.",
                        score,
                        state,
                    )
                elif state == "desync":
                    logger.error(
                        "Persona DESYNC detected (EWMA=%.3f). Full context recalibration recommended.",
                        score,
                    )
                else:
                    logger.debug("Drift check: EWMA=%.3f, state=%s", score, state)

                self._current_response = ""

            # Always pass frames through — never block the pipeline
            await self.push_frame(frame, direction)

        @property
        def detector(self) -> DriftDetector:
            """Access the underlying DriftDetector for state queries."""
            return self._detector
