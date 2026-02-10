"""LLM-assisted disambiguation for entity resolution.

For complex disambiguation cases (e.g., "John Williams the composer vs the
guitarist"), uses PydanticAI with structured output to make a reasoned decision.
LLM is ONLY called when other signals are ambiguous (cost control).
"""

from __future__ import annotations

import hashlib
import logging

from pydantic import BaseModel

from music_attribution.schemas.normalized import NormalizedRecord
from music_attribution.schemas.resolved import ResolutionDetails

logger = logging.getLogger(__name__)

# Ambiguity range — LLM only invoked when max signal is in this range
_AMBIGUITY_LOW = 0.4
_AMBIGUITY_HIGH = 0.7


class DisambiguationResult(BaseModel):
    """Structured output from LLM disambiguation."""

    chosen_index: int | None  # Index in candidates list, None if uncertain
    confidence: float  # LLM's self-reported confidence 0.0-1.0
    reasoning: str  # LLM's explanation
    alternatives_considered: int
    cached: bool = False  # Whether result came from cache


class LLMDisambiguator:
    """LLM-assisted entity disambiguation.

    Only invoked when other resolution methods produce ambiguous results
    (confidence in the 0.4-0.7 range). Uses caching to reduce LLM costs.
    """

    def __init__(self) -> None:
        self._cache: dict[str, DisambiguationResult] = {}

    async def disambiguate(
        self,
        candidates: list[NormalizedRecord],
        context: str,
    ) -> DisambiguationResult:
        """Disambiguate between candidate entities using LLM.

        Args:
            candidates: List of candidate NormalizedRecords.
            context: Additional context for disambiguation.

        Returns:
            DisambiguationResult with chosen candidate and reasoning.
        """
        cache_key = self._cache_key(candidates, context)

        # Check cache
        if cache_key in self._cache:
            cached = self._cache[cache_key]
            return DisambiguationResult(
                chosen_index=cached.chosen_index,
                confidence=cached.confidence,
                reasoning=cached.reasoning,
                alternatives_considered=cached.alternatives_considered,
                cached=True,
            )

        # Call LLM
        try:
            result = await self._call_llm(candidates, context)
            self._cache[cache_key] = result
            return result
        except (TimeoutError, Exception) as e:
            logger.warning("LLM disambiguation failed: %s", e)
            return DisambiguationResult(
                chosen_index=None,
                confidence=0.0,
                reasoning=f"LLM error: {e}",
                alternatives_considered=len(candidates),
            )

    async def should_invoke(self, existing_scores: ResolutionDetails) -> bool:
        """Determine if LLM disambiguation is needed.

        LLM is only invoked when the best signal from other methods
        falls in the ambiguous range (0.4-0.7).

        Args:
            existing_scores: Resolution scores from other methods.

        Returns:
            True if LLM should be invoked.
        """
        scores = [
            s for s in [
                existing_scores.string_similarity,
                existing_scores.embedding_similarity,
                existing_scores.graph_path_confidence,
            ]
            if s is not None
        ]

        if not scores:
            return True  # No other signals — invoke LLM

        max_score = max(scores)
        return _AMBIGUITY_LOW <= max_score <= _AMBIGUITY_HIGH

    async def _call_llm(
        self,
        candidates: list[NormalizedRecord],
        context: str,
    ) -> DisambiguationResult:
        """Call the LLM for disambiguation.

        This method is designed to be overridden or mocked in tests.
        In production, it would use PydanticAI Agent with structured output.

        Args:
            candidates: Candidate records.
            context: Additional context.

        Returns:
            DisambiguationResult from LLM.
        """
        # Production implementation would use:
        # from pydantic_ai import Agent
        # agent = Agent('openai:gpt-4o', result_type=DisambiguationResult)
        # result = await agent.run(prompt)
        raise NotImplementedError("LLM call not configured — mock in tests")

    @staticmethod
    def _cache_key(candidates: list[NormalizedRecord], context: str) -> str:
        """Generate a deterministic cache key for a disambiguation request."""
        parts = sorted(f"{c.source}:{c.source_id}:{c.canonical_name}" for c in candidates)
        raw = "|".join(parts) + "|" + context
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
