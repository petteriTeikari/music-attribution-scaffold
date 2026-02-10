"""Graph-based entity resolution via relationship evidence.

Uses relationship graph traversals to resolve entities based on shared
connections. Two artist records sharing 3+ album relationships are likely
the same artist, even if names differ slightly.
"""

from __future__ import annotations

import logging
from collections import defaultdict

logger = logging.getLogger(__name__)


class GraphResolver:
    """Resolve entities using relationship graph evidence.

    Maintains an in-memory adjacency graph of entity relationships.
    In production, this would query Apache AGE or similar graph database.
    """

    def __init__(self) -> None:
        # Adjacency list: entity_id -> set of (neighbor_id, rel_type)
        self._graph: dict[str, set[tuple[str, str]]] = defaultdict(set)
        self._test_ids: dict[str, str] = {}

    def add_relationship(self, from_id: str, to_id: str, rel_type: str) -> None:
        """Add a relationship to the graph.

        Args:
            from_id: Source entity ID.
            to_id: Target entity ID.
            rel_type: Relationship type (e.g., PERFORMED_ON, WROTE).
        """
        self._graph[from_id].add((to_id, rel_type))
        self._graph[to_id].add((from_id, rel_type))

    async def find_candidate_matches(
        self,
        entity_id: str,
        min_shared: int = 2,
    ) -> list[tuple[str, float]]:
        """Find candidate entity matches based on shared relationships.

        Two entities that share many neighbors (e.g., albums) are likely
        the same entity or closely related.

        Args:
            entity_id: Entity to find matches for.
            min_shared: Minimum shared neighbors to qualify as candidate.

        Returns:
            List of (candidate_id, confidence) tuples, sorted descending.
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

        Args:
            entity_a: First entity ID.
            entity_b: Second entity ID.

        Returns:
            Confidence score between 0.0 and 1.0.
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

        Args:
            shared_count: Number of shared neighbors.
            total_neighbors: Total neighbors of the query entity.

        Returns:
            Confidence score between 0.0 and 1.0.
        """
        if total_neighbors == 0:
            return 0.0
        ratio = shared_count / total_neighbors
        # Boost for absolute count (3+ shared is strong evidence)
        count_factor = min(shared_count / 3.0, 1.0)
        return min((ratio + count_factor) / 2.0, 1.0)
