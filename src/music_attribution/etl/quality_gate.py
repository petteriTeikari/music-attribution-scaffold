"""Data quality gate for NormalizedRecord batches.

Validates batches of ``NormalizedRecord`` objects before they are passed
to the Entity Resolution pipeline.  Checks statistical properties beyond
what Pydantic field validators can cover, including:

* **Identifier coverage** — what fraction of records carry at least one
  standard identifier (ISRC, MBID, ISNI, etc.)
* **Duplicate detection** — same ``(source, source_id)`` appearing more
  than once in the batch
* **Source distribution** — whether the batch is dangerously skewed
  toward a single data source

These checks form a *quality firewall* between the ETL layer and the
downstream entity resolution layer, preventing garbage-in/garbage-out
propagation through the attribution pipeline.

Notes
-----
The gate operates in two modes:

1. **Reporting** (``validate_batch``) — produces a ``QualityReport``
   without modifying the input.
2. **Enforcement** (``enforce``) — raises ``ValueError`` on critical
   failures and removes duplicates on success.
"""

from __future__ import annotations

import logging
import uuid
from collections import Counter
from datetime import UTC, datetime
from typing import Literal

from pydantic import BaseModel, Field

from music_attribution.schemas.normalized import NormalizedRecord

logger = logging.getLogger(__name__)


class QualityCheckResult(BaseModel):
    """Result of a single quality check.

    Attributes
    ----------
    check_name : str
        Machine-readable name of the check (e.g.,
        ``"identifier_coverage"``).
    status : {'pass', 'warn', 'fail'}
        Outcome of the check.
    message : str
        Human-readable description of the result.
    metric_value : float or None
        Numeric metric associated with the check (e.g., coverage
        fraction), or ``None`` if not applicable.
    """

    check_name: str
    status: Literal["pass", "warn", "fail"]
    message: str
    metric_value: float | None = None


class QualityReport(BaseModel):
    """Aggregate quality report for a batch of NormalizedRecords.

    Attributes
    ----------
    batch_id : uuid.UUID
        Unique identifier for this quality report.
    checks : list[QualityCheckResult]
        Individual check results.
    overall_status : {'pass', 'warn', 'fail'}
        Worst status across all checks (``fail`` > ``warn`` > ``pass``).
    records_in : int
        Number of records in the input batch.
    records_passed : int
        Number of unique (non-duplicate) records.
    timestamp : datetime
        UTC timestamp when the report was generated.
    """

    batch_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    checks: list[QualityCheckResult] = Field(default_factory=list)
    overall_status: Literal["pass", "warn", "fail"] = "pass"
    records_in: int = 0
    records_passed: int = 0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class DataQualityGate:
    """Validates batches of NormalizedRecords before entity resolution.

    Runs a configurable series of quality checks and produces a
    ``QualityReport``.  The gate can operate in *report-only* mode
    (``validate_batch``) or *enforcement* mode (``enforce``) which
    raises on critical failures.

    Parameters
    ----------
    min_identifier_coverage : float, optional
        Minimum fraction of records that must have at least one
        standard identifier (ISRC, MBID, etc.), by default 0.5.
        Below this threshold the check emits a warning; zero coverage
        is a hard failure.
    max_single_source_fraction : float, optional
        Maximum fraction of records allowed from a single data source,
        by default 0.95.  If 100% of records come from one source, a
        warning is emitted (not a failure, since single-source batches
        are valid for targeted fetches).

    Examples
    --------
    >>> gate = DataQualityGate(min_identifier_coverage=0.6)
    >>> report = gate.validate_batch(records)
    >>> report.overall_status
    'pass'
    """

    def __init__(
        self,
        min_identifier_coverage: float = 0.5,
        max_single_source_fraction: float = 0.95,
    ) -> None:
        self._min_identifier_coverage = min_identifier_coverage
        self._max_single_source_fraction = max_single_source_fraction

    def validate_batch(self, records: list[NormalizedRecord]) -> QualityReport:
        """Validate a batch of NormalizedRecords (report-only mode).

        Runs all quality checks and returns a ``QualityReport`` without
        modifying the input batch.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Batch of NormalizedRecords to validate.

        Returns
        -------
        QualityReport
            Report containing individual check results, overall status,
            and record counts.
        """
        checks: list[QualityCheckResult] = []

        checks.append(self._check_identifier_coverage(records))
        checks.append(self._check_no_duplicates(records))
        checks.append(self._check_source_distribution(records))

        # Determine overall status
        statuses = [c.status for c in checks]
        overall: Literal["pass", "warn", "fail"]
        if "fail" in statuses:
            overall = "fail"
        elif "warn" in statuses:
            overall = "warn"
        else:
            overall = "pass"

        # Count records that would pass (all non-duplicate records with identifiers)
        seen = set()
        passed = 0
        for r in records:
            key = (r.source, r.source_id)
            if key not in seen:
                seen.add(key)
                passed += 1

        return QualityReport(
            checks=checks,
            overall_status=overall,
            records_in=len(records),
            records_passed=passed,
        )

    def enforce(self, records: list[NormalizedRecord]) -> list[NormalizedRecord]:
        """Validate and filter a batch, raising on critical failures.

        First runs ``validate_batch()``.  If the overall status is
        ``"fail"``, raises ``ValueError`` with details of the failing
        checks.  Otherwise, returns the deduplicated record list.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Batch of NormalizedRecords to validate and filter.

        Returns
        -------
        list[NormalizedRecord]
            Validated records with duplicates (same ``source`` +
            ``source_id``) removed, preserving first-seen order.

        Raises
        ------
        ValueError
            If any quality check has status ``"fail"`` (e.g., zero
            identifier coverage or duplicate records).
        """
        report = self.validate_batch(records)
        if report.overall_status == "fail":
            failures = [c for c in report.checks if c.status == "fail"]
            msg = "; ".join(f"{c.check_name}: {c.message}" for c in failures)
            raise ValueError(f"Batch failed quality gate: {msg}")

        # Remove duplicates
        seen: set[tuple] = set()
        unique: list[NormalizedRecord] = []
        for r in records:
            key = (r.source, r.source_id)
            if key not in seen:
                seen.add(key)
                unique.append(r)

        return unique

    def _check_identifier_coverage(
        self,
        records: list[NormalizedRecord],
    ) -> QualityCheckResult:
        """Check what fraction of records have at least one identifier.

        Uses ``IdentifierBundle.has_any()`` to test whether each record
        carries at least one standard identifier (ISRC, MBID, ISNI,
        Discogs ID, AcoustID).

        Parameters
        ----------
        records : list[NormalizedRecord]
            Batch of records to check.

        Returns
        -------
        QualityCheckResult
            ``"fail"`` if coverage is 0%, ``"warn"`` if below the
            configured minimum, ``"pass"`` otherwise.
        """
        if not records:
            return QualityCheckResult(
                check_name="identifier_coverage",
                status="warn",
                message="Empty batch",
                metric_value=0.0,
            )

        with_ids = sum(1 for r in records if r.identifiers.has_any())
        coverage = with_ids / len(records)

        if coverage == 0.0:
            return QualityCheckResult(
                check_name="identifier_coverage",
                status="fail",
                message=f"No records have identifiers (0/{len(records)})",
                metric_value=coverage,
            )
        if coverage < self._min_identifier_coverage:
            return QualityCheckResult(
                check_name="identifier_coverage",
                status="warn",
                message=f"Low identifier coverage: {coverage:.1%} ({with_ids}/{len(records)})",
                metric_value=coverage,
            )
        return QualityCheckResult(
            check_name="identifier_coverage",
            status="pass",
            message=f"Identifier coverage: {coverage:.1%} ({with_ids}/{len(records)})",
            metric_value=coverage,
        )

    def _check_no_duplicates(
        self,
        records: list[NormalizedRecord],
    ) -> QualityCheckResult:
        """Check for duplicate ``(source, source_id)`` combinations.

        Parameters
        ----------
        records : list[NormalizedRecord]
            Batch of records to check.

        Returns
        -------
        QualityCheckResult
            ``"fail"`` if any duplicates are found, ``"pass"`` otherwise.
            The ``metric_value`` is the total number of excess duplicate
            entries.
        """
        seen: Counter[tuple] = Counter()
        for r in records:
            seen[(r.source, r.source_id)] += 1

        duplicates = {k: v for k, v in seen.items() if v > 1}
        if duplicates:
            dup_count = sum(v - 1 for v in duplicates.values())
            return QualityCheckResult(
                check_name="no_duplicates",
                status="fail",
                message=f"Found {dup_count} duplicate records across {len(duplicates)} keys",
                metric_value=float(dup_count),
            )
        return QualityCheckResult(
            check_name="no_duplicates",
            status="pass",
            message="No duplicate source+source_id combinations",
            metric_value=0.0,
        )

    def _check_source_distribution(
        self,
        records: list[NormalizedRecord],
    ) -> QualityCheckResult:
        """Check that records are not all from a single data source.

        A batch consisting entirely of one source may indicate a
        pipeline misconfiguration (e.g., only MusicBrainz fetched,
        Discogs and AcoustID skipped).

        Parameters
        ----------
        records : list[NormalizedRecord]
            Batch of records to check.

        Returns
        -------
        QualityCheckResult
            ``"warn"`` if 100% of records come from a single source,
            ``"pass"`` otherwise.  The ``metric_value`` is the fraction
            of the most common source.
        """
        if not records:
            return QualityCheckResult(
                check_name="source_distribution",
                status="warn",
                message="Empty batch",
                metric_value=0.0,
            )

        source_counts = Counter(r.source for r in records)
        most_common_count = source_counts.most_common(1)[0][1]
        max_fraction = most_common_count / len(records)

        if max_fraction > self._max_single_source_fraction and len(source_counts) == 1:
            return QualityCheckResult(
                check_name="source_distribution",
                status="warn",
                message="All records from single source (100%)",
                metric_value=max_fraction,
            )
        return QualityCheckResult(
            check_name="source_distribution",
            status="pass",
            message=f"Sources: {dict(source_counts)}, max fraction: {max_fraction:.1%}",
            metric_value=max_fraction,
        )
