"""Tests for WER computation and domain keyword checking in benchmark_voice.py."""

from __future__ import annotations

from scripts.benchmark_voice import check_domain_keywords, compute_wer


class TestComputeWER:
    """Tests for compute_wer() — Word Error Rate via Levenshtein on words."""

    def test_wer_identical_strings_returns_zero(self) -> None:
        """Identical reference and hypothesis should have WER 0.0."""
        assert compute_wer("hello world", "hello world") == 0.0

    def test_wer_completely_different_returns_one(self) -> None:
        """Completely different strings should have WER 1.0."""
        assert compute_wer("hello world", "foo bar") == 1.0

    def test_wer_single_substitution(self) -> None:
        """One substitution in a 4-word sentence => WER 0.25."""
        result = compute_wer("the cat sat down", "the dog sat down")
        assert abs(result - 0.25) < 0.01

    def test_wer_insertion_and_deletion(self) -> None:
        """WER handles insertions and deletions correctly."""
        # Reference has 3 words, hypothesis has 4 (one insertion)
        result = compute_wer("a b c", "a b x c")
        assert 0.0 < result <= 1.0
        # 1 insertion / 3 reference words = 0.333...
        assert abs(result - 1.0 / 3.0) < 0.01

    def test_wer_case_insensitive(self) -> None:
        """WER should be case-insensitive (normalized)."""
        assert compute_wer("Hello World", "hello world") == 0.0

    def test_wer_strips_punctuation(self) -> None:
        """WER should strip punctuation before comparison."""
        assert compute_wer("Hello, world!", "hello world") == 0.0

    def test_wer_empty_reference_returns_one(self) -> None:
        """Empty reference with non-empty hypothesis should return 1.0."""
        assert compute_wer("", "hello") == 1.0

    def test_wer_empty_hypothesis_returns_one(self) -> None:
        """Non-empty reference with empty hypothesis should return 1.0."""
        assert compute_wer("hello", "") == 1.0

    def test_wer_both_empty_returns_zero(self) -> None:
        """Both empty should return 0.0 (vacuously correct)."""
        assert compute_wer("", "") == 0.0


class TestCheckDomainKeywords:
    """Tests for check_domain_keywords() — domain term survival checking."""

    def test_domain_keywords_all_found(self) -> None:
        """All keywords present in text should be in found list."""
        found, missed = check_domain_keywords(
            "The confidence score for this track is high",
            ["confidence", "score", "track"],
        )
        assert found == ["confidence", "score", "track"]
        assert missed == []

    def test_domain_keywords_some_missing(self) -> None:
        """Missing keywords should appear in missed list."""
        found, missed = check_domain_keywords(
            "The confidence for this is high",
            ["confidence", "attribution", "score"],
        )
        assert "confidence" in found
        assert "attribution" in missed
        assert "score" in missed

    def test_domain_keywords_case_insensitive(self) -> None:
        """Keyword matching should be case-insensitive."""
        found, missed = check_domain_keywords(
            "Hide and Seek by Imogen Heap",
            ["hide", "seek", "imogen"],
        )
        assert found == ["hide", "seek", "imogen"]
        assert missed == []

    def test_domain_keywords_empty_text(self) -> None:
        """Empty text should miss all keywords."""
        found, missed = check_domain_keywords("", ["confidence", "score"])
        assert found == []
        assert missed == ["confidence", "score"]

    def test_domain_keywords_empty_keywords_list(self) -> None:
        """Empty keywords list should return empty lists."""
        found, missed = check_domain_keywords("some text here", [])
        assert found == []
        assert missed == []
