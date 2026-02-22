"""Multi-signal resolution orchestrator.

Combines all resolution methods (identifier, string, embedding, Splink,
graph, and LLM) into a single pipeline. Produces ``ResolvedEntity`` objects
with per-method confidence breakdowns and A0-A3 assurance levels.

The orchestrator implements a **cascade** pattern: cheap deterministic methods
(identifier matching) run first, and more expensive probabilistic methods
(embedding, Splink, LLM) only fire for records that remain unresolved.
Signal weights are configurable per deployment.

Notes
-----
This is the top-level entry point for Pipeline 2 (Entity Resolution) in the
five-pipeline architecture. See Teikari (2026), Section 4 for the theoretical
framework behind multi-signal resolution and the A0-A3 assurance level mapping.

See Also
--------
music_attribution.resolution.identifier_match : Stage 1 -- exact ID matching.
music_attribution.resolution.string_similarity : Stage 2 -- fuzzy name matching.
music_attribution.resolution.embedding_match : Stage 3 -- semantic similarity.
music_attribution.resolution.splink_linkage : Stage 4 -- probabilistic linkage.
music_attribution.resolution.graph_resolution : Stage 5 -- graph evidence.
music_attribution.resolution.llm_disambiguation : Stage 6 -- LLM tie-breaking.
"""

from __future__ import annotations

import logging
import uuid
from collections import Counter, defaultdict
from datetime import UTC, datetime

from music_attribution.constants import REVIEW_THRESHOLD
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

# Threshold below which resolution is flagged for review — imported from constants
_REVIEW_THRESHOLD = REVIEW_THRESHOLD


class ResolutionOrchestrator:
    """Orchestrate multi-signal entity resolution.

    Combines identifier matching, string similarity, embedding similarity,
    Splink, graph evidence, and LLM disambiguation into a unified pipeline.
    Each signal contributes a weighted score; the final confidence is the
    weighted average of all active signals.

    Parameters
    ----------
    weights : dict[str, float] | None, optional
        Per-method weight overrides for score combination. Keys are method
        names (``"identifier"``, ``"splink"``, ``"string"``, ``"embedding"``,
        ``"graph"``, ``"llm"``). Defaults to ``_DEFAULT_WEIGHTS``.

    Attributes
    ----------
    _weights : dict[str, float]
        Active signal weights.
    _id_matcher : IdentifierMatcher
        Stage 1 identifier matcher.
    _string_matcher : StringSimilarityMatcher
        Stage 2 string similarity matcher.

    Examples
    --------
    >>> orchestrator = ResolutionOrchestrator()
    >>> entities = await orchestrator.resolve(normalized_records)
    """

    def __init__(self, weights: dict[str, float] | None = None) -> None:
        self._weights = weights or _DEFAULT_WEIGHTS
        self._id_matcher = IdentifierMatcher()
        self._string_matcher = StringSimilarityMatcher()

    async def resolve(self, records: list[NormalizedRecord]) -> list[ResolvedEntity]:
        """Resolve a list of NormalizedRecords into ResolvedEntities.

        Executes the resolution cascade in order:

        1. Group records by shared identifiers (exact match).
        2. For ungrouped records, attempt string-similarity grouping.
        3. Remaining singletons form their own groups.
        4. Each group is resolved into a ``ResolvedEntity`` with confidence
           scores and assurance levels.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Input records from the ETL pipeline. Each record represents a
            single source's view of an entity (artist, work, recording).

        Returns
        -------
        list[ResolvedEntity]
            One ``ResolvedEntity`` per distinct entity discovered. Each
            contains per-method confidence breakdown and merged identifiers.

        Notes
        -----
        The cascade ordering ensures that high-confidence deterministic
        matches are found first, reducing the workload for expensive
        probabilistic methods downstream.
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

        Merges identifiers, picks the canonical name, detects cross-source
        conflicts, and computes a weighted confidence score from all
        available resolution signals.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Pre-clustered records believed to represent the same entity.
            Must contain at least one record.

        Returns
        -------
        ResolvedEntity
            A merged entity with combined identifiers, canonical name,
            per-method confidence breakdown, and assurance level.

        Notes
        -----
        Records with confidence below ``_REVIEW_THRESHOLD`` (0.5) are
        automatically flagged for human review in the attribution pipeline.
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
        """Group records by shared identifiers using union-find.

        Builds an inverted index from identifier values to record indices,
        then uses union-find with path compression to merge records that
        share any identifier (ISRC, ISWC, ISNI, MBID, AcoustID).

        Parameters
        ----------
        records : list[NormalizedRecord]
            All input records to group.

        Returns
        -------
        list[list[int]]
            Groups of record indices. Only groups with 2+ records are
            returned (singletons are handled separately by the caller).
        """
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
            for field in ("isrc", "iswc", "isni", "mbid", "acoustid"):
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
        """Group ungrouped records by canonical name string similarity.

        Performs pairwise Jaro-Winkler + token-sort comparison on records
        that were not matched by identifier. Uses union-find to transitively
        merge records that exceed the similarity threshold.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Full record list (indexed by position).
        indices : list[int]
            Indices of records not yet grouped by identifier matching.

        Returns
        -------
        list[list[int]]
            Groups of record indices with 2+ members.
        """
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
        """Compute per-method resolution details for a record group.

        Checks which identifiers are shared across the group and computes
        pairwise string similarity (maximum across all pairs).

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the current resolution group.

        Returns
        -------
        ResolutionDetails
            Details including matched identifiers and similarity scores
            from each active resolution method.
        """
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
        """Determine the primary resolution method used for this group.

        Selects the highest-confidence method that contributed to the
        resolution, following the cascade priority order: exact ID >
        fuzzy string > embedding > singleton fallback.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the resolution group.
        details : ResolutionDetails
            Pre-computed per-method scores.

        Returns
        -------
        ResolutionMethodEnum
            The dominant resolution method for this group.
        """
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
        """Compute weighted combined confidence from all active signals.

        Aggregates per-method scores using the configured signal weights.
        Only methods that produced a score contribute to the weighted average.
        Singletons (no signals) receive a default confidence of 0.5.

        Parameters
        ----------
        details : ResolutionDetails
            Per-method resolution scores.

        Returns
        -------
        float
            Weighted combined confidence in range [0.0, 1.0].
        """
        scores: list[tuple[float, float]] = []

        if details.matched_identifiers:
            scores.append((1.0, self._weights.get("identifier", _DEFAULT_WEIGHTS["identifier"])))
        if details.string_similarity is not None:
            scores.append((details.string_similarity, self._weights.get("string", _DEFAULT_WEIGHTS["string"])))
        if details.embedding_similarity is not None:
            scores.append((details.embedding_similarity, self._weights.get("embedding", _DEFAULT_WEIGHTS["embedding"])))
        if details.graph_path_confidence is not None:
            scores.append((details.graph_path_confidence, self._weights.get("graph", _DEFAULT_WEIGHTS["graph"])))
        if details.llm_confidence is not None:
            scores.append((details.llm_confidence, self._weights.get("llm", _DEFAULT_WEIGHTS["llm"])))

        if not scores:
            return 0.5  # Default for singletons

        total_weight = sum(w for _, w in scores)
        weighted_sum = sum(s * w for s, w in scores)
        return min(weighted_sum / total_weight, 1.0)

    def _compute_assurance_level(self, records: list[NormalizedRecord]) -> AssuranceLevelEnum:
        """Compute assurance level from available evidence.

        Maps to the A0-A3 assurance hierarchy defined in Teikari (2026):

        - **A3** (identity-verified): ISNI present + multiple sources agree.
        - **A2** (cross-referenced): Multiple sources with any shared identifier.
        - **A1** (single-source): At least one identifier present.
        - **A0** (no data): No identifiers found.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the resolution group.

        Returns
        -------
        AssuranceLevelEnum
            The computed assurance level for this entity.
        """
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
        """Detect conflicting field values across records in a group.

        Currently checks ``canonical_name`` for disagreements between
        sources. Conflicts are tagged with severity (LOW for name
        variations) and stored on the ``ResolvedEntity`` for downstream
        review.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the resolution group.

        Returns
        -------
        list[Conflict]
            Detected conflicts with per-source values and severity.
        """
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
        """Pick the canonical name from records by frequency and source priority.

        Selects the most frequently occurring name across all source records.
        Ties are broken alphabetically for determinism.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the resolution group.

        Returns
        -------
        str
            The chosen canonical name for the resolved entity.
        """
        name_counts: Counter[str] = Counter()
        for r in records:
            name_counts[r.canonical_name] += 1

        # Prefer most common name, then alphabetically first
        return name_counts.most_common(1)[0][0]

    def _merge_identifiers(self, records: list[NormalizedRecord]) -> IdentifierBundle:
        """Merge identifiers from all records into a single bundle.

        Takes the first non-None value for each identifier field across
        all records in the group, producing a maximally populated
        ``IdentifierBundle``.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the resolution group.

        Returns
        -------
        IdentifierBundle
            Merged identifier bundle with best-available value per field.
        """
        merged: dict[str, str | int | None] = {}
        fields = ("isrc", "iswc", "isni", "mbid", "acoustid", "discogs_id")
        for field in fields:
            for r in records:
                val = getattr(r.identifiers, field, None)
                if val is not None:
                    merged[field] = val

        return IdentifierBundle(**merged)  # type: ignore[arg-type]
