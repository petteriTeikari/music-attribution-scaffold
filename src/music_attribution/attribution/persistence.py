"""AttributionRecord persistence repositories.

Two implementations:
  - AttributionRecordRepository: In-memory for dev/testing (no database needed).
  - AsyncAttributionRepository: Async PostgreSQL via SQLAlchemy AsyncSession.
"""

from __future__ import annotations

import copy
import json
import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import AttributionRecordModel
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ProvenanceEvent,
    UpdateEventDetails,
)
from music_attribution.schemas.enums import ProvenanceEventTypeEnum

logger = logging.getLogger(__name__)


class AttributionRecordRepository:
    """In-memory repository for AttributionRecord persistence.

    Provides async interface matching what a database-backed
    implementation would expose.
    """

    def __init__(self) -> None:
        self._records: dict[uuid.UUID, AttributionRecord] = {}

    async def store(self, record: AttributionRecord) -> uuid.UUID:
        """Store an attribution record.

        Args:
            record: The attribution record to store.

        Returns:
            The attribution_id of the stored record.
        """
        self._records[record.attribution_id] = copy.deepcopy(record)
        return record.attribution_id

    async def update(self, record: AttributionRecord) -> uuid.UUID:
        """Update an existing attribution record.

        Increments the version, updates the timestamp, and appends
        a provenance event.

        Args:
            record: The record to update.

        Returns:
            The attribution_id of the updated record.
        """
        now = datetime.now(UTC)
        old_version = record.version

        updated = record.model_copy(
            update={
                "version": old_version + 1,
                "updated_at": now,
                "provenance_chain": [
                    *record.provenance_chain,
                    ProvenanceEvent(
                        event_type=ProvenanceEventTypeEnum.UPDATE,
                        timestamp=now,
                        agent="system",
                        details=UpdateEventDetails(
                            previous_version=old_version,
                            new_version=old_version + 1,
                            fields_changed=["version", "updated_at"],
                            trigger="repository_update",
                        ),
                    ),
                ],
            },
        )

        self._records[updated.attribution_id] = updated
        return updated.attribution_id

    async def find_by_id(self, attribution_id: uuid.UUID) -> AttributionRecord | None:
        """Find an attribution record by its ID.

        Args:
            attribution_id: The attribution record UUID.

        Returns:
            The record if found, None otherwise.
        """
        record = self._records.get(attribution_id)
        return copy.deepcopy(record) if record is not None else None

    async def find_by_work_entity_id(
        self,
        work_entity_id: uuid.UUID,
    ) -> AttributionRecord | None:
        """Find an attribution record by work entity ID.

        Args:
            work_entity_id: The work entity UUID.

        Returns:
            The most recent record for this work, or None.
        """
        for record in self._records.values():
            if record.work_entity_id == work_entity_id:
                return copy.deepcopy(record)
        return None

    async def find_needs_review(self, limit: int = 50) -> list[AttributionRecord]:
        """Find records that need review, sorted by priority descending.

        Args:
            limit: Maximum number of records to return.

        Returns:
            List of records needing review, highest priority first.
        """
        needs_review = [copy.deepcopy(r) for r in self._records.values() if r.needs_review]
        needs_review.sort(key=lambda r: r.review_priority, reverse=True)
        return needs_review[:limit]


def _record_to_model(record: AttributionRecord) -> AttributionRecordModel:
    """Convert a Pydantic AttributionRecord to an ORM model."""
    return AttributionRecordModel(
        attribution_id=record.attribution_id,
        schema_version=record.schema_version,
        work_entity_id=record.work_entity_id,
        credits=[c.model_dump(mode="json") for c in record.credits],
        assurance_level=record.assurance_level.value,
        confidence_score=record.confidence_score,
        conformal_set=record.conformal_set.model_dump(mode="json"),
        source_agreement=record.source_agreement,
        provenance_chain=[e.model_dump(mode="json") for e in record.provenance_chain],
        needs_review=record.needs_review,
        review_priority=record.review_priority,
        created_at=record.created_at,
        updated_at=record.updated_at,
        version=record.version,
    )


def _ensure_utc(dt: datetime | str) -> datetime:
    """Ensure a datetime has UTC timezone (SQLite strips tzinfo).

    ORM models annotate DateTime columns as Mapped[str] but the actual
    runtime value is a datetime object. Accept both to satisfy mypy.
    """
    if isinstance(dt, str):
        parsed = datetime.fromisoformat(dt)
        return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt


def _parse_jsonb(value: dict | list | str) -> dict | list:  # noqa: E501
    """Parse JSONB value — str from SQLite, native dict/list from PostgreSQL."""
    if isinstance(value, str):
        return json.loads(value)  # type: ignore[no-any-return]
    return value


def _model_to_record(model: AttributionRecordModel) -> AttributionRecord:
    """Convert an ORM model to a Pydantic AttributionRecord.

    Pydantic validates and coerces the raw values from SQLAlchemy,
    so we pass through directly and let Pydantic handle type conversion.
    """
    return AttributionRecord(
        schema_version=model.schema_version,
        attribution_id=model.attribution_id,
        work_entity_id=model.work_entity_id,
        credits=_parse_jsonb(model.credits),  # type: ignore[arg-type]
        assurance_level=model.assurance_level,  # type: ignore[arg-type]
        confidence_score=model.confidence_score,
        conformal_set=_parse_jsonb(model.conformal_set),  # type: ignore[arg-type]
        source_agreement=model.source_agreement,
        provenance_chain=_parse_jsonb(model.provenance_chain),  # type: ignore[arg-type]
        needs_review=model.needs_review,
        review_priority=model.review_priority,
        created_at=_ensure_utc(model.created_at),
        updated_at=_ensure_utc(model.updated_at),
        version=model.version,
    )


class AsyncAttributionRepository:
    """Async PostgreSQL repository for AttributionRecord persistence."""

    async def store(self, record: AttributionRecord, session: AsyncSession) -> uuid.UUID:
        """Store an attribution record.

        Args:
            record: The attribution record to store.
            session: Active async database session.

        Returns:
            The attribution_id of the stored record.
        """
        model = _record_to_model(record)
        session.add(model)
        await session.flush()
        return record.attribution_id

    async def update(self, record: AttributionRecord, session: AsyncSession) -> uuid.UUID:
        """Update an existing attribution record.

        Increments version, updates timestamp, appends provenance event.

        Args:
            record: The record to update.
            session: Active async database session.

        Returns:
            The attribution_id of the updated record.
        """
        now = datetime.now(UTC)
        old_version = record.version

        updated = record.model_copy(
            update={
                "version": old_version + 1,
                "updated_at": now,
                "provenance_chain": [
                    *record.provenance_chain,
                    ProvenanceEvent(
                        event_type=ProvenanceEventTypeEnum.UPDATE,
                        timestamp=now,
                        agent="system",
                        details=UpdateEventDetails(
                            previous_version=old_version,
                            new_version=old_version + 1,
                            fields_changed=["version", "updated_at"],
                            trigger="repository_update",
                        ),
                    ),
                ],
            },
        )

        stmt = select(AttributionRecordModel).where(
            AttributionRecordModel.attribution_id == record.attribution_id,
        )
        result = await session.execute(stmt)
        existing = result.scalar_one()

        existing.version = updated.version
        existing.updated_at = updated.updated_at  # type: ignore[assignment]
        existing.provenance_chain = [e.model_dump(mode="json") for e in updated.provenance_chain]  # type: ignore[assignment]
        existing.confidence_score = updated.confidence_score
        existing.needs_review = updated.needs_review
        existing.review_priority = updated.review_priority
        existing.credits = [c.model_dump(mode="json") for c in updated.credits]  # type: ignore[assignment]

        await session.flush()
        return updated.attribution_id

    async def find_by_id(
        self,
        attribution_id: uuid.UUID,
        session: AsyncSession,
    ) -> AttributionRecord | None:
        """Find an attribution record by its ID.

        Args:
            attribution_id: The attribution record UUID.
            session: Active async database session.

        Returns:
            The record if found, None otherwise.
        """
        stmt = select(AttributionRecordModel).where(
            AttributionRecordModel.attribution_id == attribution_id,
        )
        result = await session.execute(stmt)
        model = result.scalar_one_or_none()
        return _model_to_record(model) if model is not None else None

    async def find_by_work_entity_id(
        self,
        work_entity_id: uuid.UUID,
        session: AsyncSession,
    ) -> AttributionRecord | None:
        """Find an attribution record by work entity ID.

        Args:
            work_entity_id: The work entity UUID.
            session: Active async database session.

        Returns:
            The most recent record for this work, or None.
        """
        stmt = (
            select(AttributionRecordModel)
            .where(AttributionRecordModel.work_entity_id == work_entity_id)
            .order_by(AttributionRecordModel.version.desc())
            .limit(1)
        )
        result = await session.execute(stmt)
        model = result.scalar_one_or_none()
        return _model_to_record(model) if model is not None else None

    async def find_needs_review(
        self,
        limit: int = 50,
        *,
        session: AsyncSession,
    ) -> list[AttributionRecord]:
        """Find records that need review, sorted by priority descending.

        Args:
            limit: Maximum number of records to return.
            session: Active async database session.

        Returns:
            List of records needing review, highest priority first.
        """
        stmt = (
            select(AttributionRecordModel)
            .where(AttributionRecordModel.needs_review.is_(True))
            .order_by(AttributionRecordModel.review_priority.desc())
            .limit(limit)
        )
        result = await session.execute(stmt)
        return [_model_to_record(m) for m in result.scalars().all()]

    async def list_all(
        self,
        limit: int = 50,
        offset: int = 0,
        *,
        session: AsyncSession,
    ) -> list[AttributionRecord]:
        """List all attribution records with pagination.

        Args:
            limit: Maximum number of records to return.
            offset: Number of records to skip.
            session: Active async database session.

        Returns:
            List of attribution records.
        """
        stmt = (
            select(AttributionRecordModel)
            .order_by(AttributionRecordModel.created_at)
            .offset(offset)
            .limit(limit)
        )
        result = await session.execute(stmt)
        return [_model_to_record(m) for m in result.scalars().all()]
