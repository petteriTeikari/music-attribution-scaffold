"""Identifier-based exact matching for entity resolution.

Stage 1 of the resolution cascade. The simplest and highest-confidence
resolution method: if two records share the same ISRC, ISWC, ISNI, or MBID,
they refer to the same entity with confidence approaching 1.0.

Standardized identifiers provide the strongest resolution signal because they
are globally unique by design:

- **ISRC** (International Standard Recording Code) -- identifies recordings
- **ISWC** (International Standard Musical Work Code) -- identifies compositions
- **ISNI** (International Standard Name Identifier) -- identifies contributors
- **MBID** (MusicBrainz Identifier) -- MusicBrainz-specific stable UUID
- **AcoustID** -- acoustic fingerprint identifier

Notes
-----
This module implements the deterministic resolution layer described in
Teikari (2026), Section 4.1. Because standardized identifiers are globally
unique, matches found here bypass all downstream probabilistic methods and
receive A1+ assurance levels automatically.

See Also
--------
music_attribution.resolution.orchestrator : Cascade coordinator that calls this first.
music_attribution.resolution.string_similarity : Fallback for records without identifiers.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from datetime import UTC, datetime

from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    ConflictSeverityEnum,
    ResolutionMethodEnum,
    SourceEnum,
)
from music_attribution.schemas.normalized import NormalizedRecord
from music_attribution.schemas.resolved import (
    Conflict,
    ResolutionDetails,
    ResolvedEntity,
    SourceReference,
)

logger = logging.getLogger(__name__)

# Identifier fields that participate in matching, in priority order
_IDENTIFIER_FIELDS = ("isrc", "iswc", "isni", "mbid", "acoustid")


class IdentifierMatcher:
    """Resolve entities by exact identifier matching.

    Two ``NormalizedRecord`` objects sharing any standard identifier (ISRC,
    ISWC, ISNI, MBID, AcoustID) are considered the same entity. This is the
    highest-confidence resolution strategy because standardized identifiers
    are globally unique by design.

    The matcher uses a union-find data structure with path compression to
    efficiently cluster records that share identifiers, even transitively
    (e.g., record A shares ISRC with B, and B shares MBID with C, so
    A, B, C are all the same entity).

    Notes
    -----
    This is Stage 1 of the resolution cascade. Records matched here bypass
    all downstream probabilistic methods. See Teikari (2026), Section 4.1.

    See Also
    --------
    music_attribution.resolution.orchestrator : Cascade coordinator.
    music_attribution.resolution.string_similarity : Stage 2 fallback.
    """

    def match(self, records: list[NormalizedRecord]) -> list[ResolvedEntity]:
        """Match records by shared identifiers and produce ResolvedEntities.

        Groups records using union-find on shared identifier values, then
        builds a ``ResolvedEntity`` for each group with merged identifiers,
        conflict detection, and assurance level computation.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Input records to match. Records without any identifiers will
            form singleton groups.

        Returns
        -------
        list[ResolvedEntity]
            One entity per distinct group found. Multi-record groups have
            resolution method ``EXACT_ID`` and confidence >= 0.7.
        """
        if not records:
            return []

        # Build groups using union-find by shared identifiers
        groups = self._group_by_identifiers(records)

        entities: list[ResolvedEntity] = []
        for group in groups:
            entity = self._build_entity(group)
            entities.append(entity)

        return entities

    def _group_by_identifiers(
        self,
        records: list[NormalizedRecord],
    ) -> list[list[NormalizedRecord]]:
        """Group records that share any identifier using union-find.

        Builds an inverted index from ``field:value`` keys to record indices,
        then uses union-find with path compression to merge all records
        sharing any identifier into the same group.

        Parameters
        ----------
        records : list[NormalizedRecord]
            All input records to group.

        Returns
        -------
        list[list[NormalizedRecord]]
            Groups of records. Every input record appears in exactly one
            group (singletons included).
        """
        # Map each identifier value to the set of record indices that have it
        id_to_indices: dict[str, set[int]] = defaultdict(set)

        for i, record in enumerate(records):
            for field in _IDENTIFIER_FIELDS:
                value = getattr(record.identifiers, field, None)
                if value is not None:
                    key = f"{field}:{value}"
                    id_to_indices[key].add(i)

        # Union-find to group records
        parent = list(range(len(records)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Union records that share any identifier
        for indices in id_to_indices.values():
            idx_list = list(indices)
            for j in range(1, len(idx_list)):
                union(idx_list[0], idx_list[j])

        # Collect groups
        group_map: dict[int, list[int]] = defaultdict(list)
        for i in range(len(records)):
            group_map[find(i)].append(i)

        return [[records[i] for i in group] for group in group_map.values()]

    def _build_entity(self, records: list[NormalizedRecord]) -> ResolvedEntity:
        """Build a ResolvedEntity from a group of identifier-matched records.

        Selects the canonical name from the highest-confidence source record,
        merges identifiers, detects name conflicts, and computes the
        assurance level based on identifier coverage and source diversity.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the matched group (1 or more).

        Returns
        -------
        ResolvedEntity
            Fully constructed entity with ``resolution_method=EXACT_ID``.
        """
        # Choose canonical name from highest-confidence record
        records_sorted = sorted(records, key=lambda r: r.source_confidence, reverse=True)
        canonical = records_sorted[0]

        # Collect all identifiers
        merged_ids = self._merge_identifiers(records)
        matched_ids = self._find_matched_identifiers(records)

        # Compute assurance level
        sources = {r.source for r in records}
        assurance = self._compute_assurance(records, sources, matched_ids)

        # Detect conflicts
        conflicts = self._detect_conflicts(records)

        # Build source references
        source_refs = [
            SourceReference(
                record_id=r.record_id,
                source=r.source,
                source_id=r.source_id,
                agreement_score=1.0 if not conflicts else 0.8,
            )
            for r in records
        ]

        # Resolution confidence based on number of sources and identifier matches
        confidence = min(1.0, 0.7 + 0.1 * len(sources) + 0.05 * len(matched_ids))

        return ResolvedEntity(
            entity_type=canonical.entity_type,
            canonical_name=canonical.canonical_name,
            alternative_names=self._collect_alt_names(records, canonical.canonical_name),
            identifiers=merged_ids,
            source_records=source_refs,
            resolution_method=ResolutionMethodEnum.EXACT_ID,
            resolution_confidence=confidence,
            resolution_details=ResolutionDetails(matched_identifiers=matched_ids),
            assurance_level=assurance,
            conflicts=conflicts,
            resolved_at=datetime.now(UTC),
        )

    @staticmethod
    def _merge_identifiers(records: list[NormalizedRecord]):
        """Merge identifiers from all records, preferring non-None values.

        Iterates through identifier fields in priority order and takes the
        first non-None value found across all records for each field.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records to merge identifiers from.

        Returns
        -------
        IdentifierBundle
            Maximally populated identifier bundle.
        """
        from music_attribution.schemas.normalized import IdentifierBundle

        merged = {}
        for field in _IDENTIFIER_FIELDS + ("ipi",):
            for r in records:
                val = getattr(r.identifiers, field, None)
                if val is not None:
                    merged[field] = val
                    break
        return IdentifierBundle(**merged)

    @staticmethod
    def _find_matched_identifiers(records: list[NormalizedRecord]) -> list[str]:
        """Find which identifier fields are shared across multiple records.

        An identifier field is "matched" when two or more records have the
        same non-None value for that field.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records to check for shared identifiers.

        Returns
        -------
        list[str]
            Field names (e.g., ``"isrc"``, ``"iswc"``) with shared values.
        """
        matched = []
        for field in _IDENTIFIER_FIELDS:
            values = set()
            for r in records:
                val = getattr(r.identifiers, field, None)
                if val is not None:
                    values.add(val)
            # If multiple records share the same value for this field
            if len(values) == 1 and sum(1 for r in records if getattr(r.identifiers, field, None) is not None) > 1:
                matched.append(field)
        return matched

    @staticmethod
    def _compute_assurance(
        records: list[NormalizedRecord],
        sources: set[SourceEnum],
        matched_ids: list[str],
    ) -> AssuranceLevelEnum:
        """Compute assurance level based on verification depth.

        Maps the combination of identifier presence and source diversity
        to the A0-A3 assurance hierarchy:

        - **A3**: ISNI confirmed + cross-registry agreement (identity-verified).
        - **A2**: Same identifier in multiple sources (cross-referenced).
        - **A1**: At least one identifier present (single-source verified).
        - **A0**: No identifiers found.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records in the matched group.
        sources : set[SourceEnum]
            Distinct data sources represented in the group.
        matched_ids : list[str]
            Identifier field names shared across multiple records.

        Returns
        -------
        AssuranceLevelEnum
            The computed assurance level.

        Notes
        -----
        See Teikari (2026), Section 4.1 for the A0-A3 assurance level
        definitions and their mapping to ISRC/ISWC/ISNI identifiers.
        """
        has_isni = any(r.identifiers.isni is not None for r in records)
        multi_source = len(sources) > 1

        if has_isni and multi_source:
            # ISNI confirmed + cross-registry = identity-verified
            return AssuranceLevelEnum.LEVEL_3
        if multi_source and matched_ids:
            # Same identifier in multiple sources = cross-referenced
            return AssuranceLevelEnum.LEVEL_2
        if matched_ids or any(r.identifiers.has_any() for r in records):
            # Single source with identifier = single-source verified
            return AssuranceLevelEnum.LEVEL_1
        return AssuranceLevelEnum.LEVEL_0

    @staticmethod
    def _detect_conflicts(records: list[NormalizedRecord]) -> list[Conflict]:
        """Detect conflicts in non-identifier fields between records.

        Checks for disagreements in ``canonical_name`` across sources.
        Name conflicts (e.g., "Beatles" vs "The Beatles") receive LOW
        severity and are recorded for downstream review.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records to check for conflicts.

        Returns
        -------
        list[Conflict]
            Detected conflicts with per-source values and severity level.
        """
        conflicts = []
        names = {r.source.value: r.canonical_name for r in records}
        unique_names = set(names.values())

        if len(unique_names) > 1:
            conflicts.append(
                Conflict(
                    field="canonical_name",
                    values=names,
                    severity=ConflictSeverityEnum.LOW,
                )
            )
        return conflicts

    @staticmethod
    def _collect_alt_names(records: list[NormalizedRecord], canonical: str) -> list[str]:
        """Collect alternative names from all records.

        Gathers all names that differ from the chosen canonical name,
        including each record's own alternative names list. Returns a
        sorted, deduplicated list.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Records to collect names from.
        canonical : str
            The chosen canonical name (excluded from results).

        Returns
        -------
        list[str]
            Sorted list of unique alternative names.
        """
        alt_names: set[str] = set()
        for r in records:
            if r.canonical_name != canonical:
                alt_names.add(r.canonical_name)
            alt_names.update(r.alternative_names)
        return sorted(alt_names)
