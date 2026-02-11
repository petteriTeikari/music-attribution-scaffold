"""Async PostgreSQL edge repository with recursive CTE graph traversal.

Tier 1 graph implementation: uses recursive CTEs for graph traversal
without Apache AGE dependency. Supports depth-limited neighbor queries,
relationship type filtering, and cycle prevention.
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
    """Lightweight result for edge queries."""

    edge_id: uuid.UUID
    from_entity_id: uuid.UUID
    to_entity_id: uuid.UUID
    relationship_type: str
    confidence: float


class AsyncEdgeRepository:
    """Async PostgreSQL repository for graph edges with recursive CTE traversal."""

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
        """Add a directed edge between two entities."""
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
        """Get all edges where entity is from_entity_id or to_entity_id."""
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
        """Get neighbors up to N hops away using recursive CTE.

        Uses an iterative approach with SQLAlchemy queries to traverse
        the graph, preventing cycles by tracking visited nodes.
        Compatible with both PostgreSQL and SQLite.

        Args:
            entity_id: Starting entity ID.
            depth: Maximum traversal depth.
            rel_type: Optional relationship type filter.
            session: Active async database session.

        Returns:
            List of EdgeResults for reachable edges.
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
