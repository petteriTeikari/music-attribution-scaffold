"""Data quality gate for NormalizedRecord batches.

Validates batches of NormalizedRecords before they are passed to the
Entity Resolution pipeline. Checks statistical properties beyond what
Pydantic validators cover.
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
    """Result of a single quality check."""

    check_name: str
    status: Literal["pass", "warn", "fail"]
    message: str
    metric_value: float | None = None


class QualityReport(BaseModel):
    """Aggregate quality report for a batch of records."""

    batch_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    checks: list[QualityCheckResult] = Field(default_factory=list)
    overall_status: Literal["pass", "warn", "fail"] = "pass"
    records_in: int = 0
    records_passed: int = 0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class DataQualityGate:
    """Validates batches of NormalizedRecords.

    Runs a series of quality checks and produces a QualityReport.

    Args:
        min_identifier_coverage: Minimum fraction of records with at least one identifier.
        max_single_source_fraction: Maximum fraction of records from a single source.
    """

    def __init__(
        self,
        min_identifier_coverage: float = 0.5,
        max_single_source_fraction: float = 0.95,
    ) -> None:
        self._min_identifier_coverage = min_identifier_coverage
        self._max_single_source_fraction = max_single_source_fraction

    def validate_batch(self, records: list[NormalizedRecord]) -> QualityReport:
        """Validate a batch of NormalizedRecords.

        Args:
            records: Batch of NormalizedRecords to validate.

        Returns:
            QualityReport with results of all checks.
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

        Args:
            records: Batch of NormalizedRecords.

        Returns:
            Validated records (duplicates removed).

        Raises:
            ValueError: If batch fails critical quality checks.
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
        """Check what fraction of records have at least one identifier."""
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
        """Check for duplicate source+source_id combinations."""
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
        """Check that records aren't all from a single source."""
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
