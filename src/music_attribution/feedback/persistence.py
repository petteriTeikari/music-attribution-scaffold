"""Async PostgreSQL feedback repository."""

from __future__ import annotations

import json
import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import FeedbackCardModel
from music_attribution.schemas.feedback import FeedbackCard

logger = logging.getLogger(__name__)


def _ensure_utc(dt: datetime | str) -> datetime:
    """Ensure a datetime has UTC timezone (SQLite strips tzinfo)."""
    if isinstance(dt, str):
        parsed = datetime.fromisoformat(dt)
        return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt


def _parse_jsonb(value: dict | list | str) -> dict | list:
    """Parse JSONB value — str from SQLite, native dict/list from PostgreSQL."""
    if isinstance(value, str):
        return json.loads(value)  # type: ignore[no-any-return]
    return value


def _card_to_model(card: FeedbackCard) -> FeedbackCardModel:
    """Convert a Pydantic FeedbackCard to an ORM model."""
    return FeedbackCardModel(
        feedback_id=card.feedback_id,
        attribution_id=card.attribution_id,
        reviewer_id=card.reviewer_id,
        reviewer_role=card.reviewer_role.value,
        attribution_version=card.attribution_version,
        corrections=[c.model_dump(mode="json") for c in card.corrections],
        overall_assessment=card.overall_assessment,
        center_bias_flag=card.center_bias_flag,
        free_text=card.free_text,
        evidence_type=card.evidence_type.value,
        submitted_at=card.submitted_at,
    )


def _model_to_card(model: FeedbackCardModel) -> FeedbackCard:
    """Convert an ORM model to a Pydantic FeedbackCard."""
    return FeedbackCard(
        feedback_id=model.feedback_id,
        attribution_id=model.attribution_id,
        reviewer_id=model.reviewer_id,
        reviewer_role=model.reviewer_role,  # type: ignore[arg-type]
        attribution_version=model.attribution_version,
        corrections=_parse_jsonb(model.corrections),  # type: ignore[arg-type]
        overall_assessment=model.overall_assessment,
        center_bias_flag=model.center_bias_flag,
        free_text=model.free_text,
        evidence_type=model.evidence_type,  # type: ignore[arg-type]
        submitted_at=_ensure_utc(model.submitted_at),
    )


class AsyncFeedbackRepository:
    """Async PostgreSQL repository for FeedbackCard persistence."""

    async def store(self, card: FeedbackCard, session: AsyncSession) -> uuid.UUID:
        """Store a feedback card."""
        model = _card_to_model(card)
        session.add(model)
        await session.flush()
        return card.feedback_id

    async def find_by_id(
        self,
        feedback_id: uuid.UUID,
        session: AsyncSession,
    ) -> FeedbackCard | None:
        """Find a feedback card by its ID."""
        stmt = select(FeedbackCardModel).where(
            FeedbackCardModel.feedback_id == feedback_id,
        )
        result = await session.execute(stmt)
        model = result.scalar_one_or_none()
        return _model_to_card(model) if model is not None else None

    async def find_by_attribution_id(
        self,
        attribution_id: uuid.UUID,
        session: AsyncSession,
    ) -> list[FeedbackCard]:
        """Find all feedback for a specific attribution."""
        stmt = (
            select(FeedbackCardModel)
            .where(FeedbackCardModel.attribution_id == attribution_id)
            .order_by(FeedbackCardModel.submitted_at.desc())
        )
        result = await session.execute(stmt)
        return [_model_to_card(m) for m in result.scalars().all()]
