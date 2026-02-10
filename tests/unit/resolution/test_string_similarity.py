"""Tests for string similarity matching."""

from __future__ import annotations

import pytest

from music_attribution.resolution.string_similarity import StringSimilarityMatcher


@pytest.fixture
def matcher() -> StringSimilarityMatcher:
    """Create a StringSimilarityMatcher with default threshold."""
    return StringSimilarityMatcher()


class TestStringSimilarityMatcher:
    """Tests for string similarity matching."""

    def test_exact_match_score_1_0(self, matcher) -> None:
        """Test that identical strings score 1.0."""
        score = matcher.score("The Beatles", "The Beatles")
        assert score == 1.0

    def test_the_prefix_handling(self, matcher) -> None:
        """Test handling of 'The' prefix in band names."""
        score = matcher.score("The Beatles", "Beatles, The")
        assert score >= 0.85

    def test_unicode_normalization(self, matcher) -> None:
        """Test handling of accented characters."""
        score = matcher.score("Björk", "Bjork")
        assert score >= 0.85

    def test_abbreviation_handling(self, matcher) -> None:
        """Test handling of common abbreviations."""
        score = matcher.score("feat. John Smith", "featuring John Smith")
        assert score >= 0.85

    def test_low_similarity_below_threshold_rejected(self, matcher) -> None:
        """Test that dissimilar strings are below threshold."""
        candidates = matcher.find_candidates("The Beatles", ["Mozart", "Bach"], threshold=0.85)
        assert len(candidates) == 0

    def test_configurable_threshold(self) -> None:
        """Test that threshold is configurable."""
        strict = StringSimilarityMatcher(threshold=0.95)
        lenient = StringSimilarityMatcher(threshold=0.5)

        # "Beatles" vs "The Beatles" — strict may reject, lenient should accept
        strict_candidates = strict.find_candidates("Beatles", ["The Beatles"])
        lenient_candidates = lenient.find_candidates("Beatles", ["The Beatles"])

        assert len(lenient_candidates) >= len(strict_candidates)
