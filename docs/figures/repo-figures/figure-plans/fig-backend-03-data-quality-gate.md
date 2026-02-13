# fig-backend-03: Data Quality Gate

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-03 |
| **Title** | DataQualityGate: Batch Validation Pipeline |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/etl/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure shows the three-check validation pipeline that every batch of NormalizedRecords must pass before entering the Entity Resolution pipeline. It answers "How does the system prevent bad data from propagating downstream?" for engineers implementing or extending the quality gate.

The key message is: "Every batch passes through three statistical checks -- identifier coverage, duplicate detection, and source distribution -- with pass/warn/fail outcomes that gate entry to the resolution pipeline."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DATA QUALITY GATE                                             |
|  ■ Batch Validation Before Entity Resolution                   |
+---------------------------------------------------------------+
|                                                                 |
|  NormalizedRecord[]  ──>  CHECK 1         CHECK 2         CHECK 3
|  (input batch)            ──────          ──────          ──────
|                           identifier      no_duplicates   source
|                           _coverage                       _distribution
|                           ┌─────────┐     ┌─────────┐    ┌─────────┐
|                           │ >= 50%  │     │ 0 dupes │    │ < 95%   │
|                           │ have ID │     │ by src+ │    │ single  │
|                           │         │     │ src_id  │    │ source  │
|                           └────┬────┘     └────┬────┘    └────┬────┘
|                                │               │              │
|                                ▼               ▼              ▼
|                           ┌────────────────────────────────────┐
|                           │        QualityReport               │
|                           │  overall_status: pass | warn | fail│
|                           │  records_in:  N                    │
|                           │  records_passed: M                 │
|                           └────────────────┬───────────────────┘
|                                            │
|                         ┌──────────────────┼──────────────────┐
|                         │                  │                  │
|                       PASS               WARN              FAIL
|                     (proceed)          (proceed           (raise
|                                       + log)           ValueError)
|                         │                  │
|                         ▼                  ▼
|                   ┌──────────────────────────┐
|                   │  enforce() removes dupes  │
|                   │  returns unique records    │
|                   └──────────────────────────┘
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DATA QUALITY GATE" in editorial caps |
| Input batch | `etl_extract` | NormalizedRecord[] input batch |
| Check 1: identifier_coverage | `processing_stage` | Checks >= 50% of records have at least one identifier |
| Check 2: no_duplicates | `processing_stage` | Checks for duplicate (source, source_id) combinations |
| Check 3: source_distribution | `processing_stage` | Checks no single source exceeds 95% of batch |
| QualityReport | `primary_outcome` | Aggregate report with overall_status and counts |
| Pass path | `confidence_high` | Proceed to Entity Resolution |
| Warn path | `confidence_medium` | Proceed with logging |
| Fail path | `confidence_low` | Raises ValueError, blocks pipeline |
| enforce() step | `processing_stage` | Deduplication step returning unique records |
| Threshold values | `data_mono` | "50%", "0 dupes", "95%" in monospace |
| Flow arrows | `data_flow` | Sequential flow through checks to outcome |

## Anti-Hallucination Rules

1. There are exactly 3 quality checks: identifier_coverage, no_duplicates, source_distribution. Not more, not fewer.
2. The default min_identifier_coverage threshold is 0.5 (50%), not 0.8 or any other value.
3. The default max_single_source_fraction threshold is 0.95 (95%), not 1.0 or any other value.
4. The QualityReport has exactly these fields: batch_id (UUID), checks, overall_status, records_in, records_passed, timestamp.
5. The overall_status logic is: fail if any check fails, warn if any check warns, else pass.
6. The enforce() method raises ValueError on fail, not a custom exception.
7. Duplicates are identified by (source, source_id) tuple, not by record_id.
8. The class is DataQualityGate, located in `music_attribution.etl.quality_gate`.

## Alt Text

Pipeline diagram showing three batch validation checks (identifier coverage, duplicate detection, source distribution) with pass, warn, and fail outcome paths before Entity Resolution.
