"""LLM-assisted disambiguation for entity resolution.

Stage 6 (final) of the resolution cascade. For complex disambiguation cases
(e.g., "John Williams the composer vs the guitarist"), uses PydanticAI with
structured output to make a reasoned decision. The LLM is **only** called
when other signals produce ambiguous results (confidence in the 0.4-0.7
range), providing strict cost control.

Key design decisions:

- **Cost gating**: LLM invocation is guarded by ``should_invoke()``, which
  checks that the best existing signal falls in the ambiguity range.
- **Deterministic caching**: A SHA-256 cache key prevents duplicate LLM
  calls for the same candidate set and context.
- **Structured output**: The LLM returns a ``DisambiguationResult`` with
  chosen index, confidence, and reasoning (not free text).

Notes
-----
This module implements the LLM disambiguation layer described in
Teikari (2026), Section 4.6. The Oracle Problem (digital systems cannot
fully verify physical reality) means LLM confidence is treated as one
signal among many, not as ground truth.

See Also
--------
music_attribution.resolution.graph_resolution : Stage 5 (runs before this).
music_attribution.resolution.orchestrator : Cascade coordinator.
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
    """Structured output from LLM disambiguation.

    Represents the LLM's reasoned decision about which candidate entity
    (if any) matches the query, along with self-reported confidence
    and a natural-language explanation.

    Attributes
    ----------
    chosen_index : int | None
        Index into the candidates list identifying the chosen entity.
        ``None`` if the LLM is uncertain and cannot make a selection.
    confidence : float
        LLM's self-reported confidence in range [0.0, 1.0]. This is
        one signal among many and should not be taken at face value.
    reasoning : str
        Natural-language explanation of the LLM's decision.
    alternatives_considered : int
        Number of candidate entities the LLM evaluated.
    cached : bool
        Whether this result was served from the in-memory cache.
    """

    chosen_index: int | None  # Index in candidates list, None if uncertain
    confidence: float  # LLM's self-reported confidence 0.0-1.0
    reasoning: str  # LLM's explanation
    alternatives_considered: int
    cached: bool = False  # Whether result came from cache


class LLMDisambiguator:
    """LLM-assisted entity disambiguation.

    Only invoked when other resolution methods produce ambiguous results
    (confidence in the 0.4-0.7 range). Uses SHA-256 content-based
    caching to reduce LLM costs.

    The ``_call_llm`` method is designed to be overridden in subclasses
    or mocked in tests. In production, it would use a PydanticAI Agent
    with structured ``DisambiguationResult`` output.

    Attributes
    ----------
    _cache : dict[str, DisambiguationResult]
        In-memory cache keyed by SHA-256 hash of candidate + context.

    Notes
    -----
    The ambiguity range constants (``_AMBIGUITY_LOW=0.4``,
    ``_AMBIGUITY_HIGH=0.7``) define when the LLM is invoked. Scores
    above 0.7 are confident enough to not need LLM; scores below 0.4
    are too uncertain for LLM to add value.
    """

    def __init__(self) -> None:
        self._cache: dict[str, DisambiguationResult] = {}

    async def disambiguate(
        self,
        candidates: list[NormalizedRecord],
        context: str,
    ) -> DisambiguationResult:
        """Disambiguate between candidate entities using LLM.

        Checks the content-addressed cache first. On cache miss, calls
        ``_call_llm()`` and caches the result. On LLM failure, returns
        a safe fallback with ``chosen_index=None`` and ``confidence=0.0``.

        Parameters
        ----------
        candidates : list[NormalizedRecord]
            List of candidate records that could not be resolved by
            earlier cascade stages.
        context : str
            Additional context for disambiguation (e.g., album name,
            genre, release year).

        Returns
        -------
        DisambiguationResult
            The LLM's structured decision, or a safe fallback on error.
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
        except TimeoutError as e:
            logger.warning("LLM disambiguation timed out: %s", e)
            return DisambiguationResult(
                chosen_index=None,
                confidence=0.0,
                reasoning=f"LLM timeout: {e}",
                alternatives_considered=len(candidates),
            )
        except Exception as e:  # noqa: BLE001
            logger.warning("LLM disambiguation failed: %s", e)
            return DisambiguationResult(
                chosen_index=None,
                confidence=0.0,
                reasoning=f"LLM error: {e}",
                alternatives_considered=len(candidates),
            )

    async def should_invoke(self, existing_scores: ResolutionDetails) -> bool:
        """Determine if LLM disambiguation is needed based on existing signals.

        The LLM is only invoked when the best signal from other methods
        falls in the ambiguity range [0.4, 0.7]. If no other signals
        exist at all, the LLM is invoked as a last resort.

        Parameters
        ----------
        existing_scores : ResolutionDetails
            Resolution scores from earlier cascade stages (string
            similarity, embedding similarity, graph path confidence).

        Returns
        -------
        bool
            ``True`` if LLM should be invoked (ambiguous or missing signals).
        """
        scores = [
            s
            for s in [
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
        """Call the LLM for disambiguation (abstract / override point).

        This method is designed to be overridden in subclasses or mocked
        in tests. In production, it would use a PydanticAI Agent with
        ``DisambiguationResult`` as the structured result type.

        Parameters
        ----------
        candidates : list[NormalizedRecord]
            Candidate records to disambiguate.
        context : str
            Additional context (album, genre, year, etc.).

        Returns
        -------
        DisambiguationResult
            Structured decision from the LLM.

        Raises
        ------
        NotImplementedError
            Always raised in the base implementation. Subclass or mock
            this method for actual LLM calls.
        """
        # Production implementation would use:
        # from pydantic_ai import Agent
        # agent = Agent('openai:gpt-4o', result_type=DisambiguationResult)
        # result = await agent.run(prompt)
        raise NotImplementedError("LLM call not configured — mock in tests")

    @staticmethod
    def _cache_key(candidates: list[NormalizedRecord], context: str) -> str:
        """Generate a deterministic cache key for a disambiguation request.

        Produces a SHA-256 hash from the sorted ``source:source_id:name``
        of each candidate plus the context string. Sorting ensures that
        candidate order does not affect the cache key.

        Parameters
        ----------
        candidates : list[NormalizedRecord]
            Candidate records.
        context : str
            Additional context string.

        Returns
        -------
        str
            64-character hex SHA-256 digest.
        """
        parts = sorted(f"{c.source}:{c.source_id}:{c.canonical_name}" for c in candidates)
        raw = "|".join(parts) + "|" + context
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
