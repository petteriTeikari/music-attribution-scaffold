"""AttributionRecord persistence repository.

In-memory implementation for development/testing. Provides the same
interface that a PostgreSQL or other database-backed implementation
would use.
"""

from __future__ import annotations

import copy
import logging
import uuid
from datetime import UTC, datetime

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
