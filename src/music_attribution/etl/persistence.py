"""NormalizedRecord persistence layer.

Stores validated ``NormalizedRecord`` objects in PostgreSQL using
SQLAlchemy.  Handles upsert logic so that records with the same
``(source, source_id)`` pair are updated rather than duplicated.

This module represents the *handover point* from the Data Engineering
(ETL) layer to the Entity Resolution layer.  Once records are persisted
here, the entity resolution pipeline can query them by source, entity
type, or identifier to build resolved entity clusters.

Notes
-----
The upsert uses PostgreSQL's ``INSERT ... ON CONFLICT DO UPDATE`` via
``sqlalchemy.dialects.postgresql.insert``.  The conflict target is the
unique index on ``(source, source_id)``.
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

    Provides CRUD operations for ``NormalizedRecord`` objects, with
    upsert semantics to prevent duplicates.

    Parameters
    ----------
    database_url : str or None, optional
        PostgreSQL connection string (e.g.,
        ``"postgresql://…@host/db"``).  Creates a new engine.
    engine : Engine or None, optional
        Pre-configured SQLAlchemy engine.  Takes precedence over
        ``database_url`` if both are provided.

    Raises
    ------
    ValueError
        If neither ``database_url`` nor ``engine`` is provided.

    Examples
    --------
    >>> repo = NormalizedRecordRepository(database_url="postgresql://localhost/music_attribution")
    >>> record_id = repo.upsert(some_normalized_record)
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
        """Insert or update a single NormalizedRecord.

        If a record with the same ``(source, source_id)`` already exists
        in the database, its mutable fields are updated.  Otherwise, a
        new row is inserted.

        Parameters
        ----------
        record : NormalizedRecord
            The record to persist.

        Returns
        -------
        uuid.UUID
            Primary key (``record_id``) of the persisted row.
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

        Each record is upserted individually within a single
        transaction.  If any upsert fails, the entire batch is rolled
        back.

        Parameters
        ----------
        records : list[NormalizedRecord]
            List of NormalizedRecords to persist.

        Returns
        -------
        list[uuid.UUID]
            List of ``record_id`` UUIDs in the same order as the input.
            Returns an empty list if ``records`` is empty.
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
        """Find all records from a specific data source.

        Parameters
        ----------
        source : SourceEnum
            Data source to filter by (e.g., ``SourceEnum.MUSICBRAINZ``).

        Returns
        -------
        list[NormalizedRecord]
            All records originating from the specified source.
        """
        with Session(self._engine) as session:
            stmt = select(NormalizedRecordModel).where(NormalizedRecordModel.source == source.value)
            results = session.execute(stmt).scalars().all()
            return [self._to_domain(r) for r in results]

    def find_by_entity_type(self, entity_type: EntityTypeEnum) -> list[NormalizedRecord]:
        """Find all records of a specific entity type.

        Parameters
        ----------
        entity_type : EntityTypeEnum
            Entity type to filter by (e.g.,
            ``EntityTypeEnum.RECORDING``).

        Returns
        -------
        list[NormalizedRecord]
            All records with the specified entity type.
        """
        with Session(self._engine) as session:
            stmt = select(NormalizedRecordModel).where(NormalizedRecordModel.entity_type == entity_type.value)
            results = session.execute(stmt).scalars().all()
            return [self._to_domain(r) for r in results]

    def find_by_identifier(self, **kwargs: str) -> list[NormalizedRecord]:
        """Find records matching the given identifier key-value pairs.

        Queries the JSONB ``identifiers`` column using containment
        operators.  All specified key-value pairs must match (AND
        semantics).

        Parameters
        ----------
        **kwargs : str
            Identifier key-value pairs, e.g.,
            ``isrc="GBAYE0200774"`` or ``mbid="b10bbbfc-..."``).
            Keys correspond to fields in ``IdentifierBundle``.

        Returns
        -------
        list[NormalizedRecord]
            Records whose ``identifiers`` JSONB column contains all
            specified key-value pairs.

        Examples
        --------
        >>> records = repo.find_by_identifier(isrc="GBAYE0200774")
        >>> len(records)
        1
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
        """Convert a NormalizedRecord to a database row dictionary.

        Parameters
        ----------
        record : NormalizedRecord
            Domain object to serialise.

        Returns
        -------
        dict
            Column-name to value mapping suitable for
            ``NormalizedRecordModel`` insertion.
        """
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
        """Convert a database model row to a NormalizedRecord domain object.

        Parameters
        ----------
        model : NormalizedRecordModel
            SQLAlchemy ORM model instance.

        Returns
        -------
        NormalizedRecord
            Reconstituted domain object.  Note that ``relationships``
            are not round-tripped (set to empty list) because the JSONB
            serialisation format may differ from the Pydantic model.
        """
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
