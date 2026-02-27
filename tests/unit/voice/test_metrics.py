"""Tests for voice metrics module (WER and keyword checking)."""

from __future__ import annotations

from music_attribution.voice.metrics import check_domain_keywords, compute_wer


class TestComputeWer:
    """Tests for compute_wer()."""

    def test_compute_wer_identical(self) -> None:
        """Identical strings have 0.0 WER."""
        assert compute_wer("hello world", "hello world") == 0.0

    def test_compute_wer_completely_wrong(self) -> None:
        """Completely different strings have WER >= 1.0."""
        wer = compute_wer("hello world", "foo bar baz")
        assert wer >= 1.0

    def test_compute_wer_partial(self) -> None:
        """Partially matching strings have WER between 0.0 and 1.0."""
        wer = compute_wer("one two three", "one two four")
        assert 0.0 < wer < 1.0

    def test_compute_wer_empty_both(self) -> None:
        """Empty strings have 0.0 WER."""
        assert compute_wer("", "") == 0.0

    def test_compute_wer_case_insensitive(self) -> None:
        """WER is case-insensitive."""
        assert compute_wer("Hello World", "hello world") == 0.0

    def test_compute_wer_strips_punctuation(self) -> None:
        """WER strips punctuation before comparing."""
        assert compute_wer("Hello, world!", "hello world") == 0.0


class TestCheckDomainKeywords:
    """Tests for check_domain_keywords()."""

    def test_check_domain_keywords_all_found(self) -> None:
        """All keywords found returns them in found list, empty missed."""
        found, missed = check_domain_keywords("attribution saved for headlock", ["attribution", "saved"])
        assert found == ["attribution", "saved"]
        assert missed == []

    def test_check_domain_keywords_some_missed(self) -> None:
        """Missing keywords appear in missed list."""
        found, missed = check_domain_keywords("attribution updated", ["attribution", "saved"])
        assert found == ["attribution"]
        assert missed == ["saved"]

    def test_check_domain_keywords_case_insensitive(self) -> None:
        """Keyword checking is case-insensitive."""
        found, missed = check_domain_keywords("Attribution SAVED", ["attribution", "saved"])
        assert found == ["attribution", "saved"]
        assert missed == []
