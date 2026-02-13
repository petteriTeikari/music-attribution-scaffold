"""Graph-based entity resolution via relationship evidence.

Stage 5 of the resolution cascade. Uses relationship graph traversals to
resolve entities based on shared connections. Two artist records sharing
3+ album relationships are likely the same artist, even if their names
differ slightly.

The graph resolver computes confidence from two complementary signals:

- **Jaccard coefficient** of shared neighbor sets (structural similarity).
- **Absolute shared count** with diminishing returns (3+ shared neighbors
  is strong evidence regardless of total degree).

The in-memory adjacency graph is suitable for development and testing.
In production, Apache AGE (PostgreSQL graph extension) provides the same
traversal semantics with persistent storage and ACID guarantees.

Notes
-----
This module implements the graph-based resolution layer described in
Teikari (2026), Section 4.5. Graph evidence is particularly valuable
for resolving entities with common names (e.g., "John Smith") where
string similarity alone is insufficient.

See Also
--------
music_attribution.resolution.splink_linkage : Stage 4 (runs before this).
music_attribution.resolution.llm_disambiguation : Stage 6 (runs after this).
music_attribution.resolution.graph_store : Persistent graph storage.
"""

from __future__ import annotations

import logging
from collections import defaultdict

logger = logging.getLogger(__name__)


class GraphResolver:
    """Resolve entities using relationship graph evidence.

    Maintains an in-memory adjacency graph of entity relationships. Each
    entity is a node, and relationships (PERFORMED_ON, WROTE, PRODUCED,
    etc.) form bidirectional edges.

    In production, this would query Apache AGE or a similar graph database.
    The in-memory implementation provides the same API for testing and
    development.

    Attributes
    ----------
    _graph : dict[str, set[tuple[str, str]]]
        Adjacency list mapping entity IDs to sets of
        ``(neighbor_id, relationship_type)`` tuples.
    _test_ids : dict[str, str]
        Optional test-only ID mapping for deterministic tests.
    """

    def __init__(self) -> None:
        # Adjacency list: entity_id -> set of (neighbor_id, rel_type)
        self._graph: dict[str, set[tuple[str, str]]] = defaultdict(set)
        self._test_ids: dict[str, str] = {}

    def add_relationship(self, from_id: str, to_id: str, rel_type: str) -> None:
        """Add a bidirectional relationship to the graph.

        Both directions are stored so that neighbor lookups work
        regardless of edge direction.

        Parameters
        ----------
        from_id : str
            Source entity ID.
        to_id : str
            Target entity ID.
        rel_type : str
            Relationship type (e.g., ``"PERFORMED_ON"``, ``"WROTE"``).
        """
        self._graph[from_id].add((to_id, rel_type))
        self._graph[to_id].add((from_id, rel_type))

    async def find_candidate_matches(
        self,
        entity_id: str,
        min_shared: int = 2,
    ) -> list[tuple[str, float]]:
        """Find candidate entity matches based on shared neighbor relationships.

        Two entities that share many neighbors (e.g., both performed on the
        same albums) are likely the same entity or closely related. The
        confidence score combines the ratio of shared-to-total neighbors
        with an absolute shared-count bonus.

        Parameters
        ----------
        entity_id : str
            Entity ID to find matches for.
        min_shared : int, optional
            Minimum number of shared neighbors to qualify as a candidate.
            Default is 2.

        Returns
        -------
        list[tuple[str, float]]
            Candidate matches as ``(entity_id, confidence)`` tuples,
            sorted by confidence descending. Empty list if the entity
            has no graph relationships.
        """
        if entity_id not in self._graph:
            return []

        # Get this entity's neighbors
        my_neighbors = {n for n, _ in self._graph[entity_id]}

        # Find other entities that share neighbors
        shared_counts: dict[str, int] = defaultdict(int)
        for neighbor in my_neighbors:
            for other_entity, _ in self._graph[neighbor]:
                if other_entity != entity_id:
                    shared_counts[other_entity] += 1

        # Filter by minimum shared and score
        candidates: list[tuple[str, float]] = []
        for candidate_id, shared_count in shared_counts.items():
            if shared_count >= min_shared:
                score = self._compute_confidence(shared_count, len(my_neighbors))
                candidates.append((candidate_id, score))

        candidates.sort(key=lambda x: x[1], reverse=True)
        return candidates

    async def score_graph_evidence(self, entity_a: str, entity_b: str) -> float:
        """Score the graph evidence that two entities are the same.

        Combines two complementary signals:

        - **Jaccard coefficient**: ``|shared| / |union|`` of neighbor sets.
        - **Shared count bonus**: ``min(|shared| / 3, 1.0)`` (diminishing
          returns -- 3+ shared is strong evidence).

        The final score is the average of both signals, capped at 1.0.

        Parameters
        ----------
        entity_a : str
            First entity ID.
        entity_b : str
            Second entity ID.

        Returns
        -------
        float
            Confidence score in range [0.0, 1.0]. Returns 0.0 if either
            entity has no graph relationships or they share no neighbors.
        """
        if entity_a not in self._graph or entity_b not in self._graph:
            return 0.0

        neighbors_a = {n for n, _ in self._graph[entity_a]}
        neighbors_b = {n for n, _ in self._graph[entity_b]}

        shared = neighbors_a & neighbors_b
        if not shared:
            return 0.0

        total = neighbors_a | neighbors_b
        # Jaccard-like coefficient weighted by shared count
        jaccard = len(shared) / len(total)

        # Boost for more shared neighbors (diminishing returns)
        shared_boost = min(len(shared) / 3.0, 1.0)

        return min((jaccard + shared_boost) / 2.0, 1.0)

    @staticmethod
    def _compute_confidence(shared_count: int, total_neighbors: int) -> float:
        """Compute confidence from shared relationship count.

        Combines the shared-to-total ratio with an absolute count factor
        (3+ shared neighbors is treated as strong evidence).

        Parameters
        ----------
        shared_count : int
            Number of shared neighbors between query and candidate.
        total_neighbors : int
            Total neighbors of the query entity.

        Returns
        -------
        float
            Confidence score in range [0.0, 1.0].
        """
        if total_neighbors == 0:
            return 0.0
        ratio = shared_count / total_neighbors
        # Boost for absolute count (3+ shared is strong evidence)
        count_factor = min(shared_count / 3.0, 1.0)
        return min((ratio + count_factor) / 2.0, 1.0)
