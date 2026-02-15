"""AttributionRecord persistence repositories.

Provides two repository implementations for ``AttributionRecord`` storage:

- ``AttributionRecordRepository``: In-memory storage for development and
  testing. No database required; data is lost on process exit.
- ``AsyncAttributionRepository``: Async PostgreSQL storage via SQLAlchemy
  ``AsyncSession``. Production-grade with ACID guarantees.

Both repositories expose the same async interface:

- ``store()`` -- persist a new attribution record.
- ``update()`` -- update an existing record (auto-increments version).
- ``find_by_id()`` -- lookup by attribution UUID.
- ``find_by_work_entity_id()`` -- lookup by work entity UUID.
- ``find_needs_review()`` -- fetch records flagged for human review.

Every update appends a ``ProvenanceEvent`` to the record's provenance
chain, creating an immutable audit trail.

Notes
-----
The provenance chain is a key component of the attribution-by-design
philosophy described in Teikari (2026), Section 5.3. Every change to
an attribution record is recorded with timestamp, agent, and details.

See Also
--------
music_attribution.schemas.attribution : Pydantic models for attribution.
music_attribution.db.models.AttributionRecordModel : SQLAlchemy ORM model.
"""

from __future__ import annotations

import copy
import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import AttributionRecordModel
from music_attribution.db.utils import ensure_utc, parse_jsonb
from music_attribution.schemas.attribution import (
    AttributionRecord,
    ProvenanceEvent,
    UpdateEventDetails,
)
from music_attribution.schemas.enums import ProvenanceEventTypeEnum

logger = logging.getLogger(__name__)


class AttributionRecordRepository:
    """In-memory repository for AttributionRecord persistence.

    Provides the same async interface as ``AsyncAttributionRepository``
    so that dev/test code can be written against the same API. Records
    are stored as deep copies to prevent mutation through references.

    Attributes
    ----------
    _records : dict[uuid.UUID, AttributionRecord]
        In-memory record storage keyed by ``attribution_id``.
    """

    def __init__(self) -> None:
        self._records: dict[uuid.UUID, AttributionRecord] = {}

    async def store(self, record: AttributionRecord) -> uuid.UUID:
        """Store an attribution record (deep copy).

        Parameters
        ----------
        record : AttributionRecord
            The attribution record to store.

        Returns
        -------
        uuid.UUID
            The ``attribution_id`` of the stored record.
        """
        self._records[record.attribution_id] = copy.deepcopy(record)
        return record.attribution_id

    async def update(self, record: AttributionRecord) -> uuid.UUID:
        """Update an existing attribution record with provenance tracking.

        Increments the version number, updates the timestamp, and appends
        an ``UPDATE`` provenance event to the record's provenance chain.

        Parameters
        ----------
        record : AttributionRecord
            The record to update.

        Returns
        -------
        uuid.UUID
            The ``attribution_id`` of the updated record.
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
        """Find an attribution record by its UUID.

        Parameters
        ----------
        attribution_id : uuid.UUID
            The attribution record UUID to look up.

        Returns
        -------
        AttributionRecord | None
            Deep copy of the record if found, ``None`` otherwise.
        """
        record = self._records.get(attribution_id)
        return copy.deepcopy(record) if record is not None else None

    async def find_by_work_entity_id(
        self,
        work_entity_id: uuid.UUID,
    ) -> AttributionRecord | None:
        """Find an attribution record by work entity ID.

        Parameters
        ----------
        work_entity_id : uuid.UUID
            The work entity UUID.

        Returns
        -------
        AttributionRecord | None
            Deep copy of the first matching record, or ``None``.
        """
        for record in self._records.values():
            if record.work_entity_id == work_entity_id:
                return copy.deepcopy(record)
        return None

    async def find_needs_review(self, limit: int = 50) -> list[AttributionRecord]:
        """Find records that need human review, sorted by priority descending.

        Parameters
        ----------
        limit : int, optional
            Maximum number of records to return. Default is 50.

        Returns
        -------
        list[AttributionRecord]
            Deep copies of records with ``needs_review=True``, sorted
            by ``review_priority`` descending (highest priority first).
        """
        needs_review = [copy.deepcopy(r) for r in self._records.values() if r.needs_review]
        needs_review.sort(key=lambda r: r.review_priority, reverse=True)
        return needs_review[:limit]


def _record_to_model(record: AttributionRecord) -> AttributionRecordModel:
    """Convert a Pydantic AttributionRecord to a SQLAlchemy ORM model.

    Serializes nested Pydantic models (credits, conformal_set,
    provenance_chain) to JSON-compatible dicts for JSONB storage.

    Parameters
    ----------
    record : AttributionRecord
        The Pydantic attribution record.

    Returns
    -------
    AttributionRecordModel
        SQLAlchemy ORM model ready for database insertion.
    """
    return AttributionRecordModel(
        attribution_id=record.attribution_id,
        schema_version=record.schema_version,
        work_entity_id=record.work_entity_id,
        work_title=record.work_title,
        artist_name=record.artist_name,
        credits=[c.model_dump(mode="json") for c in record.credits],
        assurance_level=record.assurance_level.value,
        confidence_score=record.confidence_score,
        conformal_set=record.conformal_set.model_dump(mode="json"),
        source_agreement=record.source_agreement,
        provenance_chain=[e.model_dump(mode="json") for e in record.provenance_chain],
        uncertainty_summary=(
            record.uncertainty_summary.model_dump(mode="json") if record.uncertainty_summary else None
        ),
        needs_review=record.needs_review,
        review_priority=record.review_priority,
        created_at=record.created_at,
        updated_at=record.updated_at,
        version=record.version,
    )


def _model_to_record(model: AttributionRecordModel) -> AttributionRecord:
    """Convert a SQLAlchemy ORM model to a Pydantic AttributionRecord.

    Pydantic validates and coerces the raw values from SQLAlchemy,
    so JSONB fields are passed through directly and Pydantic handles
    type conversion (including nested model reconstruction).

    Parameters
    ----------
    model : AttributionRecordModel
        SQLAlchemy ORM model from database query.

    Returns
    -------
    AttributionRecord
        Validated Pydantic attribution record.
    """
    return AttributionRecord(
        schema_version=model.schema_version,
        attribution_id=model.attribution_id,
        work_entity_id=model.work_entity_id,
        work_title=model.work_title,
        artist_name=model.artist_name,
        credits=parse_jsonb(model.credits),  # type: ignore[arg-type]
        assurance_level=model.assurance_level,  # type: ignore[arg-type]
        confidence_score=model.confidence_score,
        conformal_set=parse_jsonb(model.conformal_set),  # type: ignore[arg-type]
        source_agreement=model.source_agreement,
        provenance_chain=parse_jsonb(model.provenance_chain),  # type: ignore[arg-type]
        uncertainty_summary=(
            parse_jsonb(model.uncertainty_summary)  # type: ignore[arg-type]
            if model.uncertainty_summary is not None
            else None
        ),
        needs_review=model.needs_review,
        review_priority=model.review_priority,
        created_at=ensure_utc(model.created_at),
        updated_at=ensure_utc(model.updated_at),
        version=model.version,
    )


class AsyncAttributionRepository:
    """Async PostgreSQL repository for AttributionRecord persistence.

    Production-grade repository using SQLAlchemy ``AsyncSession`` for
    database access. All methods require an active session; the caller
    is responsible for transaction management (commit/rollback).

    Provides the same logical operations as ``AttributionRecordRepository``
    but backed by PostgreSQL with ACID guarantees and JSONB storage for
    nested Pydantic models.
    """

    async def store(self, record: AttributionRecord, session: AsyncSession) -> uuid.UUID:
        """Store an attribution record in PostgreSQL.

        Parameters
        ----------
        record : AttributionRecord
            The attribution record to store.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        uuid.UUID
            The ``attribution_id`` of the stored record.
        """
        model = _record_to_model(record)
        session.add(model)
        await session.flush()
        return record.attribution_id

    async def update(self, record: AttributionRecord, session: AsyncSession) -> uuid.UUID:
        """Update an existing attribution record with provenance tracking.

        Increments the version number, updates the timestamp, appends an
        ``UPDATE`` provenance event, and persists changes via
        ``session.flush()``.

        Parameters
        ----------
        record : AttributionRecord
            The record to update.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        uuid.UUID
            The ``attribution_id`` of the updated record.

        Raises
        ------
        sqlalchemy.exc.NoResultFound
            If no record with the given ``attribution_id`` exists.
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
        """Find an attribution record by its UUID.

        Parameters
        ----------
        attribution_id : uuid.UUID
            The attribution record UUID to look up.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        AttributionRecord | None
            The validated Pydantic record if found, ``None`` otherwise.
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
        """Find the most recent attribution record for a work entity.

        Returns the record with the highest version number if multiple
        versions exist for the same work entity.

        Parameters
        ----------
        work_entity_id : uuid.UUID
            The work entity UUID.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        AttributionRecord | None
            The most recent record for this work, or ``None``.
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
        """Find records that need human review, sorted by priority descending.

        Parameters
        ----------
        limit : int, optional
            Maximum number of records to return. Default is 50.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[AttributionRecord]
            Records with ``needs_review=True``, sorted by
            ``review_priority`` descending (highest priority first).
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

        Returns records ordered by ``created_at`` ascending (oldest first).

        Parameters
        ----------
        limit : int, optional
            Maximum number of records to return. Default is 50.
        offset : int, optional
            Number of records to skip for pagination. Default is 0.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[AttributionRecord]
            Paginated list of attribution records.
        """
        stmt = select(AttributionRecordModel).order_by(AttributionRecordModel.created_at).offset(offset).limit(limit)
        result = await session.execute(stmt)
        return [_model_to_record(m) for m in result.scalars().all()]
