"""Tests for LLM-assisted disambiguation."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

import pytest

from music_attribution.resolution.llm_disambiguation import (
    DisambiguationResult,
    LLMDisambiguator,
)
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
)
from music_attribution.schemas.resolved import ResolutionDetails


def _make_record(name: str, source_id: str | None = None) -> NormalizedRecord:
    """Create a NormalizedRecord for testing."""
    return NormalizedRecord(
        source=SourceEnum.MUSICBRAINZ,
        source_id=source_id or str(uuid.uuid4()),
        entity_type=EntityTypeEnum.ARTIST,
        canonical_name=name,
        identifiers=IdentifierBundle(mbid=str(uuid.uuid4())),
        fetch_timestamp=datetime.now(UTC),
        source_confidence=0.9,
    )


@pytest.fixture
def disambiguator() -> LLMDisambiguator:
    """Create an LLMDisambiguator."""
    return LLMDisambiguator()


class TestLLMDisambiguation:
    """Tests for LLM-assisted disambiguation."""

    async def test_llm_disambiguation_john_williams(self, disambiguator) -> None:
        """Test disambiguation of 'John Williams' (composer vs guitarist)."""
        candidates = [
            _make_record("John Williams"),  # The composer
            _make_record("John Williams"),  # The guitarist
        ]
        mock_result = DisambiguationResult(
            chosen_index=0,
            confidence=0.85,
            reasoning="John Williams the film composer is more commonly referenced.",
            alternatives_considered=2,
        )

        with patch.object(disambiguator, "_call_llm", new_callable=AsyncMock, return_value=mock_result):
            result = await disambiguator.disambiguate(
                candidates, context="Film music attribution"
            )
            assert isinstance(result, DisambiguationResult)
            assert result.chosen_index == 0
            assert result.confidence >= 0.5

    async def test_llm_only_called_when_other_signals_ambiguous(
        self, disambiguator
    ) -> None:
        """Test that LLM is only invoked when other scores are ambiguous."""
        # High confidence — LLM should NOT be needed
        high_confidence = ResolutionDetails(
            string_similarity=0.95,
            embedding_similarity=0.92,
        )
        assert not await disambiguator.should_invoke(high_confidence)

        # Low confidence — LLM should be needed
        ambiguous = ResolutionDetails(
            string_similarity=0.55,
            embedding_similarity=0.50,
        )
        assert await disambiguator.should_invoke(ambiguous)

    async def test_llm_structured_output_via_pydanticai(self, disambiguator) -> None:
        """Test that LLM returns structured DisambiguationResult."""
        candidates = [_make_record("Test Artist A"), _make_record("Test Artist B")]
        mock_result = DisambiguationResult(
            chosen_index=1,
            confidence=0.75,
            reasoning="Based on context, Artist B is the better match.",
            alternatives_considered=2,
        )

        with patch.object(disambiguator, "_call_llm", new_callable=AsyncMock, return_value=mock_result):
            result = await disambiguator.disambiguate(candidates, context="test")
            assert isinstance(result, DisambiguationResult)
            assert result.reasoning != ""

    async def test_llm_response_cached_to_reduce_cost(self, disambiguator) -> None:
        """Test that identical disambiguation requests use cache."""
        candidates = [_make_record("Cache Test", source_id="fixed-1")]
        mock_result = DisambiguationResult(
            chosen_index=0,
            confidence=0.9,
            reasoning="Only one candidate.",
            alternatives_considered=1,
        )

        call_count = 0
        original_result = mock_result

        async def mock_call(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            return original_result

        with patch.object(disambiguator, "_call_llm", side_effect=mock_call):
            result1 = await disambiguator.disambiguate(candidates, context="test")
            result2 = await disambiguator.disambiguate(candidates, context="test")
            assert result1.confidence == result2.confidence
            # Second call should hit cache
            assert call_count == 1
            assert result2.cached

    async def test_llm_timeout_returns_uncertain_not_error(
        self, disambiguator
    ) -> None:
        """Test that LLM timeout returns uncertain result, not error."""
        candidates = [_make_record("Timeout Test A"), _make_record("Timeout Test B")]

        async def mock_timeout(*args, **kwargs):
            raise TimeoutError("LLM timed out")

        with patch.object(disambiguator, "_call_llm", side_effect=mock_timeout):
            result = await disambiguator.disambiguate(candidates, context="test")
            assert isinstance(result, DisambiguationResult)
            assert result.chosen_index is None
            assert result.confidence == 0.0
            assert "timeout" in result.reasoning.lower() or "error" in result.reasoning.lower()
