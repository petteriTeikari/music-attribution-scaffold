"""String similarity matching for entity resolution.

Stage 2 of the resolution cascade. Fast fuzzy matching for entity names
using Jaro-Winkler distance (via ``jellyfish``) and token-sort ratio
(via ``thefuzz``). Handles common music-domain variations:

- ``"The"`` prefix reordering (``"Beatles, The"`` -> ``"the beatles"``)
- Accented character normalization (``"Bjork"`` matches ``"Bjork"``)
- Abbreviation expansion (``"feat."`` -> ``"featuring"``, ``"ft."`` -> ``"featuring"``)
- Whitespace normalization

The two similarity algorithms are complementary:

- **Jaro-Winkler** excels at short strings and character-level typos.
- **Token-sort ratio** handles word reordering (``"John Elton"`` matches ``"Elton John"``).

Notes
-----
This module implements the fuzzy string matching layer described in
Teikari (2026), Section 4.2. It fires only for records that were not
matched by exact identifiers in Stage 1.

See Also
--------
music_attribution.resolution.identifier_match : Stage 1 (runs before this).
music_attribution.resolution.embedding_match : Stage 3 (semantic similarity).
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
    """Normalize a music entity name for comparison.

    Applies a sequence of normalization steps to reduce surface-level
    variation between equivalent names:

    1. Unicode NFD normalization and accent stripping.
    2. Lowercasing.
    3. ``"The"`` prefix reordering (``"Beatles, The"`` -> ``"the beatles"``).
    4. Abbreviation expansion (``"feat."`` -> ``"featuring"``).
    5. Whitespace normalization.

    Parameters
    ----------
    name : str
        Raw entity name from any source.

    Returns
    -------
    str
        Normalized name suitable for similarity comparison.

    Examples
    --------
    >>> _normalize_name("Bjork")
    'bjork'
    >>> _normalize_name("Beatles, The")
    'the beatles'
    >>> _normalize_name("Jay-Z feat. Kanye West")
    'jay-z featuring kanye west'
    """
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

    Combines Jaro-Winkler similarity (good for short strings and typos)
    with token-sort ratio (good for word reordering) for robust matching.
    Takes the maximum of both scores for each comparison.

    Parameters
    ----------
    threshold : float, optional
        Minimum similarity score (0.0-1.0) to consider a match.
        Default is 0.85, which balances precision and recall for
        typical music entity names.

    Attributes
    ----------
    _threshold : float
        Active similarity threshold.

    See Also
    --------
    music_attribution.resolution.orchestrator.ResolutionOrchestrator : Uses this as Stage 2.
    """

    def __init__(self, threshold: float = 0.85) -> None:
        self._threshold = threshold

    def score(self, name_a: str, name_b: str) -> float:
        """Compute similarity score between two entity names.

        Both names are normalized (accent stripping, abbreviation expansion,
        lowercase) before comparison. The score is the maximum of
        Jaro-Winkler similarity and token-sort ratio.

        Parameters
        ----------
        name_a : str
            First entity name (raw, unnormalized).
        name_b : str
            Second entity name (raw, unnormalized).

        Returns
        -------
        float
            Similarity score in range [0.0, 1.0]. Returns 1.0 for
            exact matches after normalization.
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
        """Find candidate matches from a corpus above the similarity threshold.

        Compares ``name`` against every entry in ``corpus`` and returns
        those exceeding the threshold, sorted by descending score.

        Parameters
        ----------
        name : str
            Query name to search for.
        corpus : list[str]
            List of candidate names to compare against.
        threshold : float | None, optional
            Override the instance threshold for this query. If ``None``,
            uses the threshold set at construction time.

        Returns
        -------
        list[tuple[str, float]]
            Candidate matches as ``(name, score)`` tuples, sorted by
            score descending. Empty list if no matches exceed threshold.
        """
        effective_threshold = threshold if threshold is not None else self._threshold
        candidates = []

        for candidate in corpus:
            s = self.score(name, candidate)
            if s >= effective_threshold:
                candidates.append((candidate, s))

        candidates.sort(key=lambda x: x[1], reverse=True)
        return candidates
