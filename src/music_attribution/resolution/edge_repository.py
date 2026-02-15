"""Async PostgreSQL edge repository with iterative graph traversal.

Tier 1 graph implementation: uses iterative SQLAlchemy queries for graph
traversal without Apache AGE dependency. Supports depth-limited neighbor
queries, relationship type filtering, and cycle prevention via visited-set
tracking.

This is the production-grade persistence layer for graph edges, replacing
the in-memory ``GraphStore`` for deployed environments. Compatible with
both PostgreSQL and SQLite backends.

Notes
-----
The original design called for recursive CTEs, but the current
implementation uses an iterative frontier-expansion approach for broader
database compatibility. The traversal semantics are identical.

See Also
--------
music_attribution.resolution.graph_store : In-memory graph for dev/testing.
music_attribution.resolution.graph_resolution : Graph-based entity resolution.
music_attribution.db.models.EdgeModel : SQLAlchemy ORM model for edges.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime
from typing import NamedTuple

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from music_attribution.db.models import EdgeModel

logger = logging.getLogger(__name__)


class EdgeResult(NamedTuple):
    """Lightweight result for edge queries.

    Attributes
    ----------
    edge_id : uuid.UUID
        Unique identifier for the edge.
    from_entity_id : uuid.UUID
        Source entity ID.
    to_entity_id : uuid.UUID
        Target entity ID.
    relationship_type : str
        Relationship type (e.g., ``"PERFORMED"``, ``"WROTE"``).
    confidence : float
        Confidence score for this edge in range [0.0, 1.0].
    """

    edge_id: uuid.UUID
    from_entity_id: uuid.UUID
    to_entity_id: uuid.UUID
    relationship_type: str
    confidence: float


class AsyncEdgeRepository:
    """Async PostgreSQL repository for graph edges with iterative traversal.

    Provides CRUD operations for directed edges between entities and
    depth-limited graph traversal via iterative frontier expansion.
    All methods require an ``AsyncSession`` for database access.
    """

    async def add_edge(
        self,
        from_entity_id: uuid.UUID,
        to_entity_id: uuid.UUID,
        relationship_type: str,
        confidence: float,
        *,
        metadata: dict[str, object] | None = None,
        session: AsyncSession,
    ) -> uuid.UUID:
        """Add a directed edge between two entities.

        Creates a new edge record in the database. The caller is
        responsible for committing the transaction.

        Parameters
        ----------
        from_entity_id : uuid.UUID
            Source entity ID.
        to_entity_id : uuid.UUID
            Target entity ID.
        relationship_type : str
            Edge type (e.g., ``"PERFORMED"``, ``"WROTE"``).
        confidence : float
            Confidence score for this relationship in [0.0, 1.0].
        metadata : dict[str, object] | None, optional
            Additional edge metadata stored as JSONB.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        uuid.UUID
            The auto-generated edge UUID.
        """
        edge = EdgeModel(
            from_entity_id=from_entity_id,
            to_entity_id=to_entity_id,
            relationship_type=relationship_type,
            confidence=confidence,
            metadata_=metadata or {},
            created_at=datetime.now(UTC),
        )
        session.add(edge)
        await session.flush()
        return edge.edge_id

    async def get_edges(
        self,
        entity_id: uuid.UUID,
        *,
        session: AsyncSession,
    ) -> list[EdgeResult]:
        """Get all edges where the entity appears as source or target.

        Returns both outgoing and incoming edges for the given entity,
        enabling bidirectional graph traversal.

        Parameters
        ----------
        entity_id : uuid.UUID
            Entity ID to query edges for.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[EdgeResult]
            All edges involving this entity.
        """
        stmt = select(EdgeModel).where(
            or_(
                EdgeModel.from_entity_id == entity_id,
                EdgeModel.to_entity_id == entity_id,
            ),
        )
        result = await session.execute(stmt)
        return [
            EdgeResult(
                edge_id=m.edge_id,
                from_entity_id=m.from_entity_id,
                to_entity_id=m.to_entity_id,
                relationship_type=m.relationship_type,
                confidence=m.confidence,
            )
            for m in result.scalars().all()
        ]

    async def get_neighbors(
        self,
        entity_id: uuid.UUID,
        depth: int = 1,
        *,
        rel_type: str | None = None,
        session: AsyncSession,
    ) -> list[EdgeResult]:
        """Get neighbors up to N hops away using iterative frontier expansion.

        Traverses the graph from ``entity_id`` outward, following directed
        edges up to ``depth`` hops. Prevents cycles by tracking visited
        entity IDs. Compatible with both PostgreSQL and SQLite.

        Parameters
        ----------
        entity_id : uuid.UUID
            Starting entity ID.
        depth : int, optional
            Maximum traversal depth (number of hops). Default is 1.
        rel_type : str | None, optional
            If specified, only follow edges of this relationship type.
        session : AsyncSession
            Active async database session.

        Returns
        -------
        list[EdgeResult]
            All edges discovered during traversal. The starting entity's
            direct edges at depth 1, plus transitive edges at deeper levels.
        """
        visited: set[uuid.UUID] = {entity_id}
        current_frontier: set[uuid.UUID] = {entity_id}
        all_results: list[EdgeResult] = []

        for _ in range(depth):
            if not current_frontier:
                break

            # Build query for edges from current frontier
            stmt = select(EdgeModel).where(
                EdgeModel.from_entity_id.in_(current_frontier),
            )
            if rel_type is not None:
                stmt = stmt.where(EdgeModel.relationship_type == rel_type)

            result = await session.execute(stmt)
            edges = result.scalars().all()

            next_frontier: set[uuid.UUID] = set()
            for edge in edges:
                if edge.to_entity_id not in visited:
                    visited.add(edge.to_entity_id)
                    next_frontier.add(edge.to_entity_id)
                    all_results.append(
                        EdgeResult(
                            edge_id=edge.edge_id,
                            from_entity_id=edge.from_entity_id,
                            to_entity_id=edge.to_entity_id,
                            relationship_type=edge.relationship_type,
                            confidence=edge.confidence,
                        )
                    )

            current_frontier = next_frontier

        return all_results
