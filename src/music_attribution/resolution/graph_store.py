"""Graph storage for ResolvedEntities.

Provides in-memory graph storage for development and testing, and defines
the interface for Apache AGE integration in production. Enables
relationship-based queries such as:

- "Find all entities that share an album with this artist."
- "What is the shortest path between two entities?"
- "Who are all performers on works by this composer?"

The graph is stored as an adjacency list of bidirectional edges with
typed relationships and arbitrary attributes. BFS traversal supports
depth-limited neighbor queries and shortest-path computation.

Notes
-----
In production, Apache AGE (PostgreSQL graph extension) provides the same
traversal semantics with persistent storage, ACID guarantees, and Cypher
query support. The ``AsyncEdgeRepository`` provides the PostgreSQL-backed
edge storage layer.

See Also
--------
music_attribution.resolution.graph_resolution : Graph-based entity resolution.
music_attribution.resolution.edge_repository : PostgreSQL edge persistence.
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

    The store maintains two data structures:

    - ``_entities``: UUID-keyed map of ``ResolvedEntity`` objects (nodes).
    - ``_edges``: Adjacency list of bidirectional edges with relationship
      type and arbitrary string attributes.

    Attributes
    ----------
    _entities : dict[uuid.UUID, ResolvedEntity]
        Entity node storage.
    _edges : dict[uuid.UUID, list[tuple[uuid.UUID, str, dict[str, str]]]]
        Adjacency list: ``entity_id -> [(neighbor_id, rel_type, attrs)]``.
    """

    def __init__(self) -> None:
        self._entities: dict[uuid.UUID, ResolvedEntity] = {}
        self._edges: dict[uuid.UUID, list[tuple[uuid.UUID, str, dict[str, str]]]] = defaultdict(list)

    async def add_entity(self, entity: ResolvedEntity) -> None:
        """Store a ResolvedEntity as a node in the graph.

        If an entity with the same ID already exists, it is overwritten.

        Parameters
        ----------
        entity : ResolvedEntity
            The resolved entity to store.
        """
        self._entities[entity.entity_id] = entity

    async def get_entity(self, entity_id: uuid.UUID) -> ResolvedEntity | None:
        """Retrieve a ResolvedEntity by its UUID.

        Parameters
        ----------
        entity_id : uuid.UUID
            The entity ID to look up.

        Returns
        -------
        ResolvedEntity | None
            The entity if found, ``None`` otherwise.
        """
        return self._entities.get(entity_id)

    async def add_relationship(
        self,
        from_id: uuid.UUID,
        to_id: uuid.UUID,
        rel_type: str,
        attrs: dict[str, str],
    ) -> None:
        """Add a bidirectional relationship between two entities.

        Both directions are stored to enable traversal from either endpoint.
        The entities referenced by ``from_id`` and ``to_id`` should already
        exist in the store (but this is not enforced).

        Parameters
        ----------
        from_id : uuid.UUID
            Source entity ID.
        to_id : uuid.UUID
            Target entity ID.
        rel_type : str
            Relationship type (e.g., ``"PERFORMED"``, ``"WROTE"``,
            ``"PRODUCED"``).
        attrs : dict[str, str]
            Additional relationship attributes (e.g., ``{"role": "lead vocalist"}``).
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

        Performs a breadth-first traversal following only edges of the
        specified type, up to the given depth. Each entity is visited
        at most once (cycle-safe).

        Parameters
        ----------
        entity_id : uuid.UUID
            Starting entity ID.
        rel_type : str
            Relationship type to follow (e.g., ``"PERFORMED"``).
        depth : int, optional
            Maximum traversal depth (number of hops). Default is 1.

        Returns
        -------
        list[ResolvedEntity]
            Related entities found within the traversal depth. Does
            not include the starting entity.
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
        """Find the shortest path between two entities using BFS.

        Traverses all relationship types to find the shortest path
        (fewest hops) between two entities. Useful for understanding
        how two entities are connected in the knowledge graph.

        Parameters
        ----------
        from_id : uuid.UUID
            Starting entity ID.
        to_id : uuid.UUID
            Target entity ID.

        Returns
        -------
        list[ResolvedEntity]
            Entities along the shortest path, inclusive of both endpoints.
            Returns a single-element list if ``from_id == to_id``.
            Returns an empty list if no path exists or either entity
            is not in the store.
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
