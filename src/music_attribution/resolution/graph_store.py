"""Graph storage for ResolvedEntities.

Provides in-memory graph storage for development/testing and the interface
for Apache AGE integration in production. Enables relationship-based queries
like "find all entities that share an album with this artist."
"""

from __future__ import annotations

import logging
import uuid
from collections import defaultdict, deque

from music_attribution.schemas.resolved import ResolvedEntity

logger = logging.getLogger(__name__)


class GraphStore:
    """Store and query ResolvedEntities as a graph.

    Uses in-memory storage by default. Production implementations
    would use Apache AGE (PostgreSQL graph extension).
    """

    def __init__(self) -> None:
        self._entities: dict[uuid.UUID, ResolvedEntity] = {}
        self._edges: dict[uuid.UUID, list[tuple[uuid.UUID, str, dict[str, str]]]] = defaultdict(list)

    async def add_entity(self, entity: ResolvedEntity) -> None:
        """Store a ResolvedEntity in the graph.

        Args:
            entity: The ResolvedEntity to store.
        """
        self._entities[entity.entity_id] = entity

    async def get_entity(self, entity_id: uuid.UUID) -> ResolvedEntity | None:
        """Retrieve a ResolvedEntity by ID.

        Args:
            entity_id: The entity ID to look up.

        Returns:
            The entity, or None if not found.
        """
        return self._entities.get(entity_id)

    async def add_relationship(
        self,
        from_id: uuid.UUID,
        to_id: uuid.UUID,
        rel_type: str,
        attrs: dict[str, str],
    ) -> None:
        """Add a directed relationship between two entities.

        Args:
            from_id: Source entity ID.
            to_id: Target entity ID.
            rel_type: Relationship type (e.g., PERFORMED, WROTE).
            attrs: Additional relationship attributes.
        """
        self._edges[from_id].append((to_id, rel_type, attrs))
        self._edges[to_id].append((from_id, rel_type, attrs))

    async def find_related(
        self,
        entity_id: uuid.UUID,
        rel_type: str,
        depth: int = 1,
    ) -> list[ResolvedEntity]:
        """Find entities related by a specific relationship type.

        Args:
            entity_id: Starting entity ID.
            rel_type: Relationship type to follow.
            depth: Maximum traversal depth.

        Returns:
            List of related ResolvedEntities.
        """
        visited: set[uuid.UUID] = {entity_id}
        current_level: set[uuid.UUID] = {entity_id}
        results: list[ResolvedEntity] = []

        for _ in range(depth):
            next_level: set[uuid.UUID] = set()
            for node in current_level:
                for target_id, edge_type, _ in self._edges.get(node, []):
                    if edge_type == rel_type and target_id not in visited:
                        visited.add(target_id)
                        next_level.add(target_id)
                        entity = self._entities.get(target_id)
                        if entity:
                            results.append(entity)
            current_level = next_level

        return results

    async def shortest_path(
        self,
        from_id: uuid.UUID,
        to_id: uuid.UUID,
    ) -> list[ResolvedEntity]:
        """Find the shortest path between two entities.

        Uses BFS to find the shortest path regardless of relationship type.

        Args:
            from_id: Starting entity ID.
            to_id: Target entity ID.

        Returns:
            List of entities along the path (inclusive of endpoints).
            Empty list if no path exists.
        """
        if from_id == to_id:
            entity = self._entities.get(from_id)
            return [entity] if entity else []

        # BFS
        queue: deque[list[uuid.UUID]] = deque([[from_id]])
        visited: set[uuid.UUID] = {from_id}

        while queue:
            path = queue.popleft()
            current = path[-1]

            for neighbor_id, _, _ in self._edges.get(current, []):
                if neighbor_id in visited:
                    continue
                new_path = [*path, neighbor_id]
                if neighbor_id == to_id:
                    # Convert IDs to entities
                    return [e for uid in new_path if (e := self._entities.get(uid)) is not None]
                visited.add(neighbor_id)
                queue.append(new_path)

        return []
