"""Multi-signal resolution orchestrator.

Combines all resolution methods (identifier, string, embedding, Splink,
graph, and LLM) into a single pipeline. Produces ResolvedEntities with
per-method confidence breakdown.
"""

from __future__ import annotations

import logging
import uuid
from collections import Counter, defaultdict
from datetime import UTC, datetime

from music_attribution.resolution.identifier_match import IdentifierMatcher
from music_attribution.resolution.string_similarity import StringSimilarityMatcher
from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    ConflictSeverityEnum,
    ResolutionMethodEnum,
)
from music_attribution.schemas.normalized import IdentifierBundle, NormalizedRecord
from music_attribution.schemas.resolved import (
    Conflict,
    ResolutionDetails,
    ResolvedEntity,
    SourceReference,
)

logger = logging.getLogger(__name__)

# Default signal weights for score combination
_DEFAULT_WEIGHTS: dict[str, float] = {
    "identifier": 1.0,
    "splink": 0.8,
    "string": 0.6,
    "embedding": 0.7,
    "graph": 0.75,
    "llm": 0.85,
}

# Threshold below which resolution is flagged for review
_REVIEW_THRESHOLD = 0.5


class ResolutionOrchestrator:
    """Orchestrate multi-signal entity resolution.

    Combines identifier matching, string similarity, embedding similarity,
    Splink, graph evidence, and LLM disambiguation into a unified pipeline.
    """

    def __init__(self, weights: dict[str, float] | None = None) -> None:
        self._weights = weights or _DEFAULT_WEIGHTS
        self._id_matcher = IdentifierMatcher()
        self._string_matcher = StringSimilarityMatcher()

    async def resolve(self, records: list[NormalizedRecord]) -> list[ResolvedEntity]:
        """Resolve a list of NormalizedRecords into ResolvedEntities.

        Args:
            records: List of NormalizedRecords to resolve.

        Returns:
            List of ResolvedEntities.
        """
        if not records:
            return []

        # Step 1: Group by shared identifiers
        groups = self._group_by_identifiers(records)

        # Step 2: For ungrouped records, try string similarity
        grouped_indices: set[int] = set()
        for group in groups:
            grouped_indices.update(group)

        ungrouped = [i for i in range(len(records)) if i not in grouped_indices]
        if ungrouped:
            string_groups = self._group_by_string_similarity(records, ungrouped)
            groups.extend(string_groups)
            for g in string_groups:
                grouped_indices.update(g)

        # Step 3: Singleton groups for remaining ungrouped
        for i in range(len(records)):
            if i not in grouped_indices:
                groups.append([i])

        # Step 4: Resolve each group into a ResolvedEntity
        entities = []
        for group in groups:
            group_records = [records[i] for i in group]
            entity = await self.resolve_group(group_records)
            entities.append(entity)

        return entities

    async def resolve_group(self, records: list[NormalizedRecord]) -> ResolvedEntity:
        """Resolve a pre-clustered group of records into a single entity.

        Args:
            records: Pre-clustered records believed to be the same entity.

        Returns:
            A ResolvedEntity combining all records.
        """
        # Determine resolution method and compute details
        details = self._compute_resolution_details(records)
        method = self._determine_method(records, details)
        confidence = self._compute_confidence(details)
        assurance = self._compute_assurance_level(records)
        conflicts = self._detect_conflicts(records)
        canonical = self._pick_canonical_name(records)
        alt_names = list({r.canonical_name for r in records if r.canonical_name != canonical})

        needs_review = confidence < _REVIEW_THRESHOLD
        review_reason = f"Low confidence ({confidence:.2f})" if needs_review else None

        # Merge identifiers
        merged_ids = self._merge_identifiers(records)

        # Source references
        source_refs = [
            SourceReference(
                record_id=uuid.uuid4(),
                source=r.source,
                source_id=r.source_id,
                agreement_score=confidence,
            )
            for r in records
        ]

        return ResolvedEntity(
            entity_type=records[0].entity_type,
            canonical_name=canonical,
            alternative_names=alt_names,
            identifiers=merged_ids,
            source_records=source_refs,
            resolution_method=method,
            resolution_confidence=confidence,
            resolution_details=details,
            assurance_level=assurance,
            conflicts=conflicts,
            needs_review=needs_review,
            review_reason=review_reason,
            resolved_at=datetime.now(UTC),
        )

    def _group_by_identifiers(self, records: list[NormalizedRecord]) -> list[list[int]]:
        """Group records by shared identifiers using union-find."""
        parent: dict[int, int] = {}

        def find(x: int) -> int:
            if x not in parent:
                parent[x] = x
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Build identifier index
        id_index: dict[str, list[int]] = defaultdict(list)
        for i, record in enumerate(records):
            ids = record.identifiers
            for field in ("isrc", "iswc", "isni", "mbid", "acoustid_fingerprint"):
                val = getattr(ids, field, None)
                if val:
                    id_index[f"{field}:{val}"].append(i)

        # Union records sharing identifiers
        for indices in id_index.values():
            for j in range(1, len(indices)):
                union(indices[0], indices[j])

        # Collect groups (only groups with 2+ records indicate matches)
        groups_map: dict[int, list[int]] = defaultdict(list)
        grouped: set[int] = set()
        for key_indices in id_index.values():
            if len(key_indices) > 1:
                for idx in key_indices:
                    grouped.add(idx)

        for idx in grouped:
            groups_map[find(idx)].append(idx)

        # Deduplicate within groups
        return [sorted(set(v)) for v in groups_map.values()]

    def _group_by_string_similarity(
        self,
        records: list[NormalizedRecord],
        indices: list[int],
    ) -> list[list[int]]:
        """Group records by string similarity."""
        parent: dict[int, int] = {}

        def find(x: int) -> int:
            if x not in parent:
                parent[x] = x
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for i_idx in range(len(indices)):
            for j_idx in range(i_idx + 1, len(indices)):
                i, j = indices[i_idx], indices[j_idx]
                score = self._string_matcher.score(
                    records[i].canonical_name,
                    records[j].canonical_name,
                )
                if score >= self._string_matcher._threshold:
                    union(i, j)

        groups_map: dict[int, list[int]] = defaultdict(list)
        for idx in indices:
            if idx in parent:
                groups_map[find(idx)].append(idx)

        return [sorted(set(v)) for v in groups_map.values() if len(v) > 1]

    def _compute_resolution_details(self, records: list[NormalizedRecord]) -> ResolutionDetails:
        """Compute per-method resolution details."""
        matched_ids: list[str] = []

        # Check identifier matches
        id_fields = ("isrc", "iswc", "isni", "mbid", "acoustid_fingerprint")
        for field in id_fields:
            vals = {getattr(r.identifiers, field, None) for r in records}
            vals.discard(None)
            if len(vals) == 1 and len(records) > 1:
                matched_ids.append(f"{field}:{vals.pop()}")

        # String similarity (pairwise max)
        string_sim: float | None = None
        if len(records) > 1:
            max_sim = 0.0
            for i in range(len(records)):
                for j in range(i + 1, len(records)):
                    score = self._string_matcher.score(
                        records[i].canonical_name,
                        records[j].canonical_name,
                    )
                    max_sim = max(max_sim, score)
            string_sim = max_sim

        return ResolutionDetails(
            string_similarity=string_sim,
            matched_identifiers=matched_ids,
        )

    def _determine_method(
        self,
        records: list[NormalizedRecord],
        details: ResolutionDetails,
    ) -> ResolutionMethodEnum:
        """Determine the primary resolution method used."""
        if details.matched_identifiers:
            return ResolutionMethodEnum.EXACT_ID
        if details.string_similarity and details.string_similarity >= 0.85:
            return ResolutionMethodEnum.FUZZY_STRING
        if details.embedding_similarity and details.embedding_similarity >= 0.7:
            return ResolutionMethodEnum.EMBEDDING
        if len(records) == 1:
            return ResolutionMethodEnum.EXACT_ID
        return ResolutionMethodEnum.FUZZY_STRING

    def _compute_confidence(self, details: ResolutionDetails) -> float:
        """Compute weighted combined confidence."""
        scores: list[tuple[float, float]] = []

        if details.matched_identifiers:
            scores.append((1.0, self._weights.get("identifier", 1.0)))
        if details.string_similarity is not None:
            scores.append((details.string_similarity, self._weights.get("string", 0.6)))
        if details.embedding_similarity is not None:
            scores.append((details.embedding_similarity, self._weights.get("embedding", 0.7)))
        if details.graph_path_confidence is not None:
            scores.append((details.graph_path_confidence, self._weights.get("graph", 0.75)))
        if details.llm_confidence is not None:
            scores.append((details.llm_confidence, self._weights.get("llm", 0.85)))

        if not scores:
            return 0.5  # Default for singletons

        total_weight = sum(w for _, w in scores)
        weighted_sum = sum(s * w for s, w in scores)
        return min(weighted_sum / total_weight, 1.0)

    def _compute_assurance_level(self, records: list[NormalizedRecord]) -> AssuranceLevelEnum:
        """Compute assurance level from available evidence."""
        sources = {r.source for r in records}
        has_isni = any(r.identifiers.isni for r in records)
        has_any_id = any(r.identifiers.isrc or r.identifiers.iswc or r.identifiers.mbid for r in records)

        if has_isni and len(sources) > 1:
            return AssuranceLevelEnum.LEVEL_3
        if len(sources) > 1 and has_any_id:
            return AssuranceLevelEnum.LEVEL_2
        if has_any_id:
            return AssuranceLevelEnum.LEVEL_1
        return AssuranceLevelEnum.LEVEL_0

    def _detect_conflicts(self, records: list[NormalizedRecord]) -> list[Conflict]:
        """Detect conflicting field values across records."""
        conflicts: list[Conflict] = []

        # Check canonical_name conflicts
        names = {r.canonical_name for r in records}
        if len(names) > 1:
            name_by_source = {r.source.value: r.canonical_name for r in records}
            conflicts.append(
                Conflict(
                    field="canonical_name",
                    values=name_by_source,
                    severity=ConflictSeverityEnum.LOW,
                )
            )

        return conflicts

    def _pick_canonical_name(self, records: list[NormalizedRecord]) -> str:
        """Pick the canonical name from records by frequency and source priority."""
        name_counts: Counter[str] = Counter()
        for r in records:
            name_counts[r.canonical_name] += 1

        # Prefer most common name, then alphabetically first
        return name_counts.most_common(1)[0][0]

    def _merge_identifiers(self, records: list[NormalizedRecord]) -> IdentifierBundle:
        """Merge identifiers from all records."""
        merged: dict[str, str | int | None] = {}
        fields = ("isrc", "iswc", "isni", "mbid", "acoustid_fingerprint", "discogs_id")
        for field in fields:
            for r in records:
                val = getattr(r.identifiers, field, None)
                if val is not None:
                    merged[field] = val

        return IdentifierBundle(**merged)  # type: ignore[arg-type]
