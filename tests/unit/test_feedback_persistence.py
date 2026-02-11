"""Tests for async PostgreSQL feedback repository."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from music_attribution.db.models import FeedbackCardModel
from music_attribution.schemas.enums import EvidenceTypeEnum, ReviewerRoleEnum
from music_attribution.schemas.feedback import Correction, FeedbackCard


def _register_sqlite_type_compilers() -> None:
    """Register JSONB and HALFVEC compilation for SQLite dialect (test-only)."""
    from pgvector.sqlalchemy import HALFVEC
    from sqlalchemy.dialects.postgresql import JSONB
    from sqlalchemy.ext.compiler import compiles

    @compiles(JSONB, "sqlite")  # type: ignore[misc]
    def _compile_jsonb_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "JSON"

    @compiles(HALFVEC, "sqlite")  # type: ignore[misc]
    def _compile_halfvec_sqlite(type_, compiler, **kw):  # noqa: ARG001
        return "TEXT"


_register_sqlite_type_compilers()


def _make_card(
    *,
    attribution_id: uuid.UUID | None = None,
    overall_assessment: float = 0.8,
) -> FeedbackCard:
    """Create a minimal valid FeedbackCard for testing."""
    return FeedbackCard(
        attribution_id=attribution_id or uuid.uuid4(),
        reviewer_id="test-reviewer",
        reviewer_role=ReviewerRoleEnum.ARTIST,
        attribution_version=1,
        corrections=[
            Correction(
                field="role",
                current_value="performer",
                corrected_value="producer",
                confidence_in_correction=0.9,
            ),
        ],
        overall_assessment=overall_assessment,
        evidence_type=EvidenceTypeEnum.MEMORY,
        submitted_at=datetime.now(UTC),
    )


@pytest.fixture
async def async_session():
    """Create an in-memory async SQLite database with feedback table."""
    from sqlalchemy.ext.asyncio import async_sessionmaker

    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(FeedbackCardModel.__table__.create)

    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    await engine.dispose()


class TestAsyncFeedbackRepository:
    """Tests for AsyncFeedbackRepository."""

    async def test_store_and_retrieve(self, async_session: AsyncSession) -> None:
        """Round-trip: store → find_by_id returns equivalent card."""
        from music_attribution.feedback.persistence import AsyncFeedbackRepository

        repo = AsyncFeedbackRepository()
        card = _make_card()

        stored_id = await repo.store(card, async_session)
        assert stored_id == card.feedback_id

        found = await repo.find_by_id(card.feedback_id, async_session)
        assert found is not None
        assert found.feedback_id == card.feedback_id
        assert found.reviewer_id == "test-reviewer"

    async def test_find_by_attribution_id(self, async_session: AsyncSession) -> None:
        """Find all feedback for a specific attribution."""
        from music_attribution.feedback.persistence import AsyncFeedbackRepository

        repo = AsyncFeedbackRepository()
        attr_id = uuid.uuid4()

        c1 = _make_card(attribution_id=attr_id)
        c2 = _make_card(attribution_id=attr_id)
        c3 = _make_card()  # different attribution

        await repo.store(c1, async_session)
        await repo.store(c2, async_session)
        await repo.store(c3, async_session)

        results = await repo.find_by_attribution_id(attr_id, async_session)
        assert len(results) == 2

    async def test_center_bias_flag_auto_set(self, async_session: AsyncSession) -> None:
        """Center bias flag auto-set when assessment in [0.45, 0.55]."""
        from music_attribution.feedback.persistence import AsyncFeedbackRepository

        repo = AsyncFeedbackRepository()
        card = _make_card(overall_assessment=0.5)  # Should trigger center bias
        assert card.center_bias_flag is True

        await repo.store(card, async_session)
        found = await repo.find_by_id(card.feedback_id, async_session)
        assert found is not None
        assert found.center_bias_flag is True

    async def test_corrections_stored_as_jsonb(self, async_session: AsyncSession) -> None:
        """Corrections list preserved through round-trip."""
        from music_attribution.feedback.persistence import AsyncFeedbackRepository

        repo = AsyncFeedbackRepository()
        card = _make_card()

        await repo.store(card, async_session)
        found = await repo.find_by_id(card.feedback_id, async_session)
        assert found is not None
        assert len(found.corrections) == 1
        assert found.corrections[0].field == "role"
        assert found.corrections[0].corrected_value == "producer"
