"""Tests for active learning priority queue."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest

from music_attribution.attribution.priority_queue import ReviewPriorityQueue
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ConformalSet,
    Credit,
)
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    CreditRoleEnum,
    SourceEnum,
)


def _make_attribution(
    confidence: float = 0.8,
    source_agreement: float = 0.9,
    needs_review: bool = False,
    version: int = 1,
    updated_at: datetime | None = None,
) -> AttributionRecord:
    """Create an AttributionRecord for testing."""
    now = updated_at or datetime.now(UTC)
    return AttributionRecord(
        work_entity_id=uuid.uuid4(),
        credits=[
            Credit(
                entity_id=uuid.uuid4(),
                role=CreditRoleEnum.PERFORMER,
                confidence=confidence,
                sources=[SourceEnum.MUSICBRAINZ],
                assurance_level=AssuranceLevelEnum.LEVEL_1,
            ),
        ],
        assurance_level=AssuranceLevelEnum.LEVEL_1,
        confidence_score=confidence,
        conformal_set=ConformalSet(
            coverage_level=0.9,
            marginal_coverage=0.9,
            calibration_error=0.02,
            calibration_method="APS",
            calibration_set_size=100,
        ),
        source_agreement=source_agreement,
        needs_review=needs_review,
        review_priority=0.5,
        created_at=now,
        updated_at=now,
        version=version,
    )


@pytest.fixture
def queue() -> ReviewPriorityQueue:
    """Create a ReviewPriorityQueue."""
    return ReviewPriorityQueue()


class TestReviewPriorityQueue:
    """Tests for active learning priority queue."""

    def test_low_confidence_gets_high_priority(self, queue) -> None:
        """Test that low-confidence records get higher priority."""
        low_conf = _make_attribution(confidence=0.3)
        high_conf = _make_attribution(confidence=0.95)
        p_low = queue.compute_priority(low_conf)
        p_high = queue.compute_priority(high_conf)
        assert p_low > p_high

    def test_source_disagreement_increases_priority(self, queue) -> None:
        """Test that low source agreement increases review priority."""
        low_agreement = _make_attribution(confidence=0.7, source_agreement=0.3)
        high_agreement = _make_attribution(confidence=0.7, source_agreement=0.95)
        p_low = queue.compute_priority(low_agreement)
        p_high = queue.compute_priority(high_agreement)
        assert p_low > p_high

    def test_never_reviewed_increases_priority(self, queue) -> None:
        """Test that never-reviewed records have higher priority."""
        never_reviewed = _make_attribution(confidence=0.7, version=1)
        reviewed = _make_attribution(confidence=0.7, version=3)
        p_never = queue.compute_priority(never_reviewed)
        p_reviewed = queue.compute_priority(reviewed)
        assert p_never >= p_reviewed

    def test_recently_reviewed_decreases_priority(self, queue) -> None:
        """Test that recently reviewed records get lower priority."""
        old_update = _make_attribution(
            confidence=0.7,
            updated_at=datetime.now(UTC) - timedelta(days=30),
        )
        recent_update = _make_attribution(
            confidence=0.7,
            updated_at=datetime.now(UTC),
        )
        p_old = queue.compute_priority(old_update)
        p_recent = queue.compute_priority(recent_update)
        assert p_old >= p_recent

    def test_priority_queue_ordering(self, queue) -> None:
        """Test that next_for_review returns items in priority order."""
        records = [
            _make_attribution(confidence=0.95),  # Low priority
            _make_attribution(confidence=0.3),  # High priority
            _make_attribution(confidence=0.6),  # Medium priority
        ]
        result = queue.next_for_review(records, limit=3)
        assert len(result) == 3
        # Should be ordered by priority descending (lowest confidence first)
        priorities = [queue.compute_priority(r) for r in result]
        assert priorities == sorted(priorities, reverse=True)
