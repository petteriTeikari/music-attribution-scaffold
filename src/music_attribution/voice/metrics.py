"""Voice STT metrics: WER computation and domain keyword checking.

Standalone module with no external dependencies (stdlib re only).
"""

from __future__ import annotations

import re


def _normalize_text(text: str) -> list[str]:
    """Normalize text for WER: lowercase, strip punctuation, split to words.

    Args:
        text: Raw text to normalize.

    Returns:
        List of lowercase words with punctuation removed.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def compute_wer(reference: str, hypothesis: str) -> float:
    """Compute Word Error Rate between reference and hypothesis.

    Uses Levenshtein distance on word sequences after normalization
    (lowercase, strip punctuation).

    Args:
        reference: Ground truth text.
        hypothesis: Transcribed text to evaluate.

    Returns:
        WER in range [0.0, 1.0]. 0.0 = perfect, 1.0 = completely wrong.
    """
    ref_words = _normalize_text(reference)
    hyp_words = _normalize_text(hypothesis)

    if not ref_words and not hyp_words:
        return 0.0
    if not ref_words or not hyp_words:
        return 1.0

    n = len(ref_words)
    m = len(hyp_words)

    # Levenshtein distance on word sequences
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            if ref_words[i - 1] == hyp_words[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = temp

    return min(dp[m] / n, 1.0)


def check_domain_keywords(
    text: str,
    keywords: list[str],
) -> tuple[list[str], list[str]]:
    """Check which domain keywords appear in transcribed text.

    Args:
        text: Transcribed text to check.
        keywords: Domain keywords to look for.

    Returns:
        Tuple of (found, missed) keyword lists.
    """
    text_lower = text.lower()
    found = []
    missed = []
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
        else:
            missed.append(kw)
    return found, missed
