"""NormalizedRecord persistence layer.

Stores validated NormalizedRecords in PostgreSQL. Handles upsert logic
(same source + source_id = update, not duplicate). This is the handover
point from Data Engineering to Entity Resolution.
"""

from __future__ import annotations

import logging
import uuid

from sqlalchemy import create_engine, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from music_attribution.db.models import NormalizedRecordModel
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
    SourceMetadata,
)

logger = logging.getLogger(__name__)


class NormalizedRecordRepository:
    """Repository for NormalizedRecord persistence in PostgreSQL.

    Args:
        database_url: PostgreSQL connection string.
        engine: Optional pre-configured SQLAlchemy engine.
    """

    def __init__(
        self,
        database_url: str | None = None,
        engine: Engine | None = None,
    ) -> None:
        if engine is not None:
            self._engine = engine
        elif database_url is not None:
            self._engine = create_engine(database_url, echo=False)
        else:
            msg = "Either database_url or engine must be provided"
            raise ValueError(msg)

    def upsert(self, record: NormalizedRecord) -> uuid.UUID:
        """Insert or update a NormalizedRecord.

        If a record with the same source + source_id exists, it is updated.
        Otherwise, a new record is inserted.

        Args:
            record: NormalizedRecord to persist.

        Returns:
            UUID of the persisted record.
        """
        row = self._to_row(record)

        with Session(self._engine) as session:
            insert_stmt = pg_insert(NormalizedRecordModel).values(**row)
            upsert_stmt = insert_stmt.on_conflict_do_update(
                index_elements=["source", "source_id"],
                set_={
                    "canonical_name": insert_stmt.excluded.canonical_name,
                    "alternative_names": insert_stmt.excluded.alternative_names,
                    "identifiers": insert_stmt.excluded.identifiers,
                    "metadata": insert_stmt.excluded["metadata"],
                    "relationships": insert_stmt.excluded.relationships,
                    "fetch_timestamp": insert_stmt.excluded.fetch_timestamp,
                    "source_confidence": insert_stmt.excluded.source_confidence,
                    "raw_payload": insert_stmt.excluded.raw_payload,
                },
            ).returning(NormalizedRecordModel.record_id)

            result = session.execute(upsert_stmt)
            record_id: uuid.UUID = result.scalar_one()
            session.commit()
            return record_id

    def upsert_batch(self, records: list[NormalizedRecord]) -> list[uuid.UUID]:
        """Insert or update a batch of NormalizedRecords.

        Args:
            records: List of NormalizedRecords to persist.

        Returns:
            List of UUIDs of persisted records.
        """
        if not records:
            return []

        rows = [self._to_row(r) for r in records]
        record_ids: list[uuid.UUID] = []

        with Session(self._engine) as session:
            for row in rows:
                insert_stmt = pg_insert(NormalizedRecordModel).values(**row)
                upsert_stmt = insert_stmt.on_conflict_do_update(
                    index_elements=["source", "source_id"],
                    set_={
                        "canonical_name": insert_stmt.excluded.canonical_name,
                        "alternative_names": insert_stmt.excluded.alternative_names,
                        "identifiers": insert_stmt.excluded.identifiers,
                        "metadata": insert_stmt.excluded["metadata"],
                        "relationships": insert_stmt.excluded.relationships,
                        "fetch_timestamp": insert_stmt.excluded.fetch_timestamp,
                        "source_confidence": insert_stmt.excluded.source_confidence,
                        "raw_payload": insert_stmt.excluded.raw_payload,
                    },
                ).returning(NormalizedRecordModel.record_id)

                result = session.execute(upsert_stmt)
                rid: uuid.UUID = result.scalar_one()
                record_ids.append(rid)

            session.commit()

        return record_ids

    def find_by_source(self, source: SourceEnum) -> list[NormalizedRecord]:
        """Find all records from a specific source.

        Args:
            source: Source to filter by.

        Returns:
            List of matching NormalizedRecords.
        """
        with Session(self._engine) as session:
            stmt = select(NormalizedRecordModel).where(NormalizedRecordModel.source == source.value)
            results = session.execute(stmt).scalars().all()
            return [self._to_domain(r) for r in results]

    def find_by_entity_type(self, entity_type: EntityTypeEnum) -> list[NormalizedRecord]:
        """Find all records of a specific entity type.

        Args:
            entity_type: Entity type to filter by.

        Returns:
            List of matching NormalizedRecords.
        """
        with Session(self._engine) as session:
            stmt = select(NormalizedRecordModel).where(NormalizedRecordModel.entity_type == entity_type.value)
            results = session.execute(stmt).scalars().all()
            return [self._to_domain(r) for r in results]

    def find_by_identifier(self, **kwargs: str) -> list[NormalizedRecord]:
        """Find records matching any of the given identifiers.

        Args:
            **kwargs: Identifier key-value pairs (e.g., isrc="USRC...", mbid="abc-123").

        Returns:
            List of matching NormalizedRecords.
        """
        with Session(self._engine) as session:
            stmt = select(NormalizedRecordModel)

            # Build JSONB containment query for each identifier
            for key, value in kwargs.items():
                stmt = stmt.where(NormalizedRecordModel.identifiers[key].as_string() == value)

            results = session.execute(stmt).scalars().all()
            return [self._to_domain(r) for r in results]

    @staticmethod
    def _to_row(record: NormalizedRecord) -> dict:
        """Convert a NormalizedRecord to a database row dict."""
        return {
            "record_id": record.record_id,
            "schema_version": record.schema_version,
            "source": record.source.value,
            "source_id": record.source_id,
            "entity_type": record.entity_type.value,
            "canonical_name": record.canonical_name,
            "alternative_names": record.alternative_names,
            "identifiers": record.identifiers.model_dump(),
            "metadata_": record.metadata.model_dump() if record.metadata else {},
            "relationships": [r.model_dump(mode="json") for r in record.relationships],
            "fetch_timestamp": record.fetch_timestamp,
            "source_confidence": record.source_confidence,
            "raw_payload": record.raw_payload,
        }

    @staticmethod
    def _to_domain(model: NormalizedRecordModel) -> NormalizedRecord:
        """Convert a database model to a NormalizedRecord."""
        identifiers_data: dict = model.identifiers or {}
        metadata_data: dict = model.metadata_ or {}
        alt_names: list[str] = list(model.alternative_names) if model.alternative_names else []

        return NormalizedRecord(
            record_id=model.record_id,
            schema_version=model.schema_version,
            source=SourceEnum(model.source),
            source_id=model.source_id,
            entity_type=EntityTypeEnum(model.entity_type),
            canonical_name=model.canonical_name,
            alternative_names=alt_names,
            identifiers=IdentifierBundle(**identifiers_data),
            metadata=SourceMetadata(**metadata_data),
            relationships=[],
            fetch_timestamp=model.fetch_timestamp,  # type: ignore[arg-type]
            source_confidence=model.source_confidence,
            raw_payload=model.raw_payload,
        )
