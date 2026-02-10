"""String similarity matching for entity resolution.

Fast fuzzy matching for entity names using jellyfish and thefuzz.
Handles common music-domain variations: "The" prefix, accented characters,
abbreviations like "feat." / "featuring".
"""

from __future__ import annotations

import re
import unicodedata

import jellyfish
from thefuzz import fuzz

# Common music abbreviation expansions
_ABBREVIATIONS: dict[str, str] = {
    "feat.": "featuring",
    "ft.": "featuring",
    "feat": "featuring",
    "ft": "featuring",
    "vs.": "versus",
    "vs": "versus",
    "w/": "with",
    "prod.": "produced by",
    "prod": "produced by",
    "arr.": "arranged by",
    "orch.": "orchestra",
}


def _normalize_name(name: str) -> str:
    """Normalize a music entity name for comparison."""
    # Unicode normalization (NFD) and strip accents
    normalized = unicodedata.normalize("NFD", name)
    normalized = "".join(c for c in normalized if unicodedata.category(c) != "Mn")

    # Lowercase
    normalized = normalized.lower().strip()

    # Handle "The" prefix: "Beatles, The" → "the beatles"
    if normalized.endswith(", the"):
        normalized = "the " + normalized[:-5]

    # Expand abbreviations
    for abbrev, expansion in _ABBREVIATIONS.items():
        normalized = re.sub(
            r"\b" + re.escape(abbrev) + r"\b",
            expansion,
            normalized,
            flags=re.IGNORECASE,
        )

    # Normalize whitespace
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


class StringSimilarityMatcher:
    """String similarity matcher for music entity names.

    Combines Jaro-Winkler (good for short strings / typos) with
    token-sort ratio (good for word reordering) for robust matching.

    Args:
        threshold: Minimum similarity score (0.0-1.0) to consider a match.
    """

    def __init__(self, threshold: float = 0.85) -> None:
        self._threshold = threshold

    def score(self, name_a: str, name_b: str) -> float:
        """Compute similarity score between two names.

        Args:
            name_a: First name.
            name_b: Second name.

        Returns:
            Similarity score between 0.0 and 1.0.
        """
        norm_a = _normalize_name(name_a)
        norm_b = _normalize_name(name_b)

        if norm_a == norm_b:
            return 1.0

        # Jaro-Winkler: good for short strings and typos
        jw_score = jellyfish.jaro_winkler_similarity(norm_a, norm_b)

        # Token sort ratio: handles word reordering
        token_score = fuzz.token_sort_ratio(norm_a, norm_b) / 100.0

        # Take the max of both scores
        return float(max(jw_score, token_score))

    def find_candidates(
        self,
        name: str,
        corpus: list[str],
        threshold: float | None = None,
    ) -> list[tuple[str, float]]:
        """Find candidate matches from a corpus above the threshold.

        Args:
            name: Name to search for.
            corpus: List of candidate names to compare against.
            threshold: Override threshold (default: instance threshold).

        Returns:
            List of (candidate_name, score) tuples, sorted by score descending.
        """
        effective_threshold = threshold if threshold is not None else self._threshold
        candidates = []

        for candidate in corpus:
            s = self.score(name, candidate)
            if s >= effective_threshold:
                candidates.append((candidate, s))

        candidates.sort(key=lambda x: x[1], reverse=True)
        return candidates
