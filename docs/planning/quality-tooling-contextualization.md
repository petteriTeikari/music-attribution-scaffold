# Quality Tooling Contextualization for the Probabilistic PRD

**Date**: 2026-02-10
**Status**: Research complete, not yet implemented
**Branch for implementation**: Future branches (not `feat/expansion-of-probabilistic-prd`)
**Related decision nodes**: [`data_quality_strategy`](../prd/decisions/L3-implementation/data-quality-strategy.decision.yaml), [`schema_governance`](../prd/decisions/L5-operations/schema-governance.decision.yaml)

---

## Executive Summary

The 27-task TDD execution revealed that **well-typed Pydantic boundary objects are the single strongest predictor of first-pass code correctness** (~70% ALL_GREEN on iteration 1). This document analyzes what stacks on top of Pydantic to amplify that effect, contextualized to the probabilistic PRD's decision network, with conditional probability estimates for when each tool justifies its adoption cost.

This project serves dual purposes (research companion + portfolio/learning), so the adoption threshold is lower than a pure MVP — demonstrating comprehensive quality engineering has value even when a simpler approach would suffice for functionality alone.

---

## The Validation Spectrum

```
Design-Time (IDE)      Build-Time (CI)              Runtime (Production)
────────────────────────────────────────────────────────────────────────
mypy/pyright           Hypothesis (property-based)   Pydantic (every request)
ruff                   Schemathesis (API fuzz)       Pandera (batch stats)
                       Pact contracts                Great Expectations (drift)
                       Pandera (in-test assertions)  pydantic-logfire (observability)
                                                     OpenLineage/Marquez (lineage)
```

Each layer catches a different class of defects. The question is not "which one?" but "how many layers does the project justify?"

---

## Tool-by-Tool Analysis with Conditional Probabilities

### Tier 1: Add Now (Already in deps or zero-config)

#### Pandera (Statistical DataFrame Validation)

**Current status**: In `pyproject.toml` (`pandera>=0.22`), used in Task 1.5 (data quality gate)
**What it catches that Pydantic alone misses**: Aggregate/statistical validation — "confidence scores collapsed to mean=0.98", "source distribution changed", "batch completeness below 80%"

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| Processing batch data from 2+ sources | **0.90** | Pandera's core value prop — batch-level statistical assertions |
| Single-source pipeline | 0.40 | Still useful for regression detection on distributions |
| Research/portfolio project (this project) | **0.95** | Already installed; demonstrates statistical quality gates |

**Concrete next steps for this project**:
- Custom Pandera checks for the NormalizedRecord batch pipeline:
  - `check_source_distribution(df)`: No single source > 70% of batch
  - `check_confidence_spread(df)`: `std(source_confidence) > 0.05` (not collapsed)
  - `check_identifier_coverage(df)`: At least 1 identifier per record for machine sources
- Integration with `BatchEnvelope` drift detection (Task X.1)

#### Hypothesis (Property-Based Testing)

**Current status**: In dependencies, underutilized
**What it catches that Pydantic alone misses**: Edge cases humans don't write fixtures for — "any valid AttributionRecord survives JSON roundtrip", "conformal set coverage is monotonically related to calibration data size"

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| Pydantic models with numeric fields | **0.85** | Boundary conditions on floats are where bugs hide |
| Serialization/deserialization paths | **0.90** | Property: `model == Model.model_validate_json(model.model_dump_json())` |
| Research/portfolio project (this project) | **0.95** | Demonstrates sophisticated testing; Pydantic v2 strategies work well |

**Concrete next steps for this project**:
```python
from hypothesis import given, strategies as st

@given(st.builds(AttributionRecord,
    confidence_score=st.floats(min_value=0.0, max_value=1.0),
    version=st.integers(min_value=1, max_value=1000),
))
def test_attribution_record_roundtrip(record: AttributionRecord):
    """Any valid AttributionRecord survives JSON serialization."""
    json_bytes = record.model_dump_json()
    restored = AttributionRecord.model_validate_json(json_bytes)
    assert restored == record
```

#### Schemathesis (API Fuzzing from OpenAPI)

**Current status**: Not installed
**What it catches**: API-level edge cases — "empty string passes Pydantic but violates DB constraint", "extremely long entity names cause 500 errors"

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| FastAPI with OpenAPI spec (this project) | **0.80** | Zero-config: `schemathesis.openapi.from_asgi("/openapi.json", app)` |
| API consumed by external clients | **0.90** | Adversarial input testing is essential |
| Internal-only API | 0.50 | Nice-to-have, not critical |

**Concrete next steps**:
```python
import schemathesis
schema = schemathesis.openapi.from_asgi("/openapi.json", app)

@schema.parametrize()
def test_api(case):
    case.call_and_validate()
```

#### pydantic-settings (Configuration Validation)

**Current status**: Already using
**What it catches**: "DATABASE_URL is empty string, not unset", "ATTRIBUTION_SEED is negative"

Already integrated. No further action needed.

---

### Tier 2: Add for Production Readiness (Medium Effort)

#### pydantic-logfire (Validation Observability)

**What it adds**: Production monitoring — which Pydantic fields fail validation most, trend analysis, OpenTelemetry traces through validation paths

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| Production deployment handling real traffic | **0.75** | Validation failure trends reveal data quality issues |
| Dev/staging only | 0.20 | Test suites provide this feedback |
| Research/portfolio project | 0.50 | Demonstrates observability integration with Pydantic |

**Conditional on observability_stack decision**:
- P(adopt | langfuse_plus_platform) = 0.60 — complements Langfuse tracing
- P(adopt | grafana_stack) = 0.40 — competes with Grafana for dashboard attention
- P(adopt | minimal_logging) = 0.70 — biggest bang for the buck when no other observability

#### pydantic-ai (Structured LLM Outputs)

**What it adds**: Validates LLM responses against Pydantic schemas, automatic retries on validation failure, type-safe prompt engineering

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| LLM disambiguation pipeline (Task 2.3d) | **0.75** | LLM output validation with retry is the exact use case |
| No LLM usage | 0.00 | Not relevant |
| Research/portfolio project | 0.70 | Demonstrates structured AI output validation |

**Conditional on ai_framework_strategy**:
- P(adopt | direct_api_pydantic) = **0.80** — pydantic-ai IS the "Direct API + Pydantic" strategy
- P(adopt | lightweight_sdk) = 0.30 — overlaps with instructor/mirascope
- P(adopt | orchestration_framework) = 0.10 — framework handles this

#### OpenLineage + Marquez (Pipeline Lineage)

**What it adds**: Infrastructure-level provenance — tracks which pipeline produced which data, when, with what inputs. Complements the record-level `provenance_chain` field on `AttributionRecord`.

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| 3+ pipeline stages in production | **0.60** | Pipeline-level lineage becomes valuable |
| Single pipeline | 0.15 | Git log sufficient |
| Regulatory/compliance needs | **0.80** | Audit trail requirement |
| Research/portfolio project | 0.45 | Demonstrates infrastructure-level provenance |

**Relationship to existing provenance_chain**:
- `provenance_chain` (BO-3 AttributionRecord): **Record-level** — "this attribution was created by pipeline X, updated by feedback Y"
- OpenLineage: **Pipeline-level** — "pipeline run #123 consumed 500 NormalizedRecords, produced 200 ResolvedEntities, took 45s"
- Complementary, not duplicative

---

### Tier 3: Add Only If Needed (High Effort, Conditional)

#### Great Expectations

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| 3+ external sources with distribution drift | **0.65** | GX excels at drift monitoring |
| < 3 sources, no drift risk | 0.10 | Pandera is sufficient |
| Stakeholders need data quality reports | **0.70** | GX data docs are unmatched |
| Research/portfolio project | 0.30 | 107+ deps is heavy for a scaffold |

**Key differentiator from Pandera**: GX provides **data docs** (shareable HTML reports) and **checkpoint-based pipeline integration**. If you don't need these, Pandera does the same statistical checks with 10x fewer dependencies.

#### DVC (Data Artifact Versioning)

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| Embedding models or calibration datasets > 100MB | **0.80** | Git can't handle large binaries |
| Reproducibility requirement for experiments | **0.75** | `dvc repro SEED=42` |
| All data fits in git | 0.20 | Over-engineering |
| Research/portfolio project | 0.65 | Demonstrates ML ops maturity |

**Concrete value for this project**:
- Version entity resolution embedding models (sentence-transformers)
- Version conformal prediction calibration datasets
- `dvc.yaml` pipeline DAG for reproducible training→calibration→evaluation
- `dvc push/pull` to S3/GCS for team sharing

#### OpenMetadata (Metadata Catalog)

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| Multi-team, > 3 engineers | **0.65** | Self-service schema discovery |
| Solo/small team | 0.10 | Git search is sufficient |
| Regulatory data governance | **0.70** | EU AI Act lineage requirements |
| Research/portfolio project | 0.35 | Impressive but overkill for solo |

#### Pact (Consumer-Driven Contracts)

| Condition | P(adopt) | Rationale |
|-----------|----------|-----------|
| Independently deployed services (microservices) | **0.70** | Prevents deployment-time schema breaks |
| Modular monolith (this project) | 0.15 | Pydantic schemas at boundaries suffice |
| MCP server consumed by external agents | 0.50 | MCP protocol changes could break consumers |

---

## Probabilistic Schema Concept: `uq.*` Extension Properties

### The Idea

Every confidence-bearing field in the Pydantic boundary objects could carry **uncertainty quantification (UQ) metadata** as JSON Schema extension properties. This makes uncertainty first-class in the schema, not just an application-layer concern.

### Current State (What We Have)

```python
class AttributionRecord(BaseModel):
    confidence_score: float = Field(ge=0.0, le=1.0)
    conformal_set: ConformalSet  # has coverage_level, calibration_error
```

### Proposed Extension (Future Work)

```python
class AttributionRecord(BaseModel):
    confidence_score: float = Field(
        ge=0.0, le=1.0,
        json_schema_extra={
            "uq.type": "conformal_prediction",
            "uq.coverage": 0.90,
            "uq.calibration_method": "APS",
            "uq.calibration_error_target": 0.05,
            "uq.interpretation": "probability that true attribution is in prediction set",
        }
    )
```

### What This Enables

1. **Schema-level uncertainty documentation**: Consumers can inspect the JSON Schema to understand what each confidence field means, without reading Python code
2. **Automated uncertainty-aware analytics**: Tools can discover all `uq.*` fields and generate appropriate visualizations (calibration curves, reliability diagrams)
3. **OpenMetadata integration**: Push JSON Schemas with `uq.*` properties as custom schema definitions — enables schema search by uncertainty type
4. **Cross-domain portability**: The DPP traceability domain can use the same `uq.*` convention for supply chain confidence scores

### Conditional Probability for Implementation

| Condition | P(implement) | Rationale |
|-----------|-------------|-----------|
| Confidence scores exposed to external consumers | **0.75** | Consumers need to know what "0.85 confidence" means |
| Internal-only confidence scores | 0.30 | Docstrings sufficient |
| Academic/research context (this project) | **0.80** | Demonstrates uncertainty-aware schema design |
| Integration with OpenMetadata | **0.85** | Schema registry benefits from structured UQ metadata |

### Implementation Priority

This is a **schema annotation** task — no behavioral changes, just adding `json_schema_extra` to existing Pydantic fields. Low risk, high discoverability value. Good candidate for a focused future PR.

---

## Label Noise Detection

### The Problem

When multiple sources disagree on attribution credits, some of those disagreements are **noise** (data errors) and some are **genuine conflicts** (e.g., ghostwriting, uncredited contributions). Distinguishing these is critical for calibration.

### Research Context

Recent work on LLM-powered label noise detection:
- **Confident Learning** (cleanlab): Identifies label errors by finding examples where model confidence disagrees with label — applicable to attribution confidence scores
- **Data-Centric AI**: Systematic approaches to finding and fixing data quality issues rather than model issues
- **Agentic quality scoring**: Using LLMs to assess data quality of individual records (e.g., "does this MusicBrainz record look internally consistent?")

### Where This Fits in the Architecture

```
NormalizedRecord                    ResolvedEntity
    │                                    │
    ├─ source_confidence (per-source)    ├─ resolution_confidence (merged)
    ├─ QualityReport (Pandera batch)     ├─ assurance_level (A0-A3)
    │                                    ├─ conflicts (typed)
    └─ Label noise detection ◄──────────►└─ needs_review flag
       (identifies suspicious records)      (surfaces to priority queue)
```

### Conditional Probability for Implementation

| Condition | P(implement) | Rationale |
|-----------|-------------|-----------|
| 3+ sources with conflicting attributions | **0.70** | Label noise detection most valuable with disagreement |
| Single authoritative source | 0.15 | No disagreement to analyze |
| Active learning pipeline exists (Task 3.3) | **0.75** | Priority queue can surface noise candidates |
| Research/portfolio project | 0.60 | Demonstrates data-centric AI approach |

### Concrete Approach for This Project

1. **Phase 1**: Use inter-source agreement as a proxy for label quality (already in resolution orchestrator via conflict detection)
2. **Phase 2**: Apply cleanlab's `find_label_issues()` on the attribution confidence scores vs. human feedback corrections
3. **Phase 3**: LLM-powered record-level quality assessment ("given these 3 sources for the same recording, which attribution credits are likely errors?")

---

## Adoption Roadmap: Conditional on Project Phase

### Phase 0 (Current — Scaffold Complete)

**Already have**: Pydantic v2, Pandera (installed), Hypothesis (installed), pytest, mypy, ruff

**Recommended additions for immediate value**:
- Hypothesis property-based tests for all 5 boundary objects (P=0.95)
- Schemathesis API fuzzing for FastAPI endpoints (P=0.80)

**Estimated effort**: 1-2 tasks (< 1 session)

### Phase 1 (Production Readiness — When Deploying)

**Trigger**: First deployment to staging/production

**Recommended additions**:
- pydantic-ai for LLM disambiguation pipeline (P=0.75)
- pydantic-logfire for validation observability (P=0.60)
- `uq.*` JSON Schema extensions on confidence fields (P=0.80)

**Estimated effort**: 3-4 tasks (1 session)

### Phase 2 (Data Scale — When Processing Real Data)

**Trigger**: Processing data from 3+ external sources, or data artifacts > 100MB

**Recommended additions**:
- DVC for embedding model and calibration dataset versioning (P=0.75)
- Custom Pandera expectations: `expect_field_has_uq_metadata` (P=0.65)
- Label noise detection via cleanlab integration (P=0.60)
- Great Expectations (only if distribution drift detected in production) (P=0.30)

**Estimated effort**: 5-7 tasks (2 sessions)

### Phase 3 (Multi-Team / Enterprise — If Project Grows)

**Trigger**: Team grows beyond 3 engineers, or regulatory requirements

**Recommended additions**:
- OpenMetadata catalog for schema discovery (P=0.45 for this project)
- OpenLineage + Marquez for pipeline lineage (P=0.40)
- Pact contracts if MCP server has external consumers (P=0.30)

**Estimated effort**: 8-12 tasks (3-4 sessions)

---

## Decision Network Integration

Two new decision nodes have been added to the probabilistic PRD:

1. **[`data_quality_strategy`](../prd/decisions/L3-implementation/data-quality-strategy.decision.yaml)** (L3_implementation)
   - Options: pydantic_only (0.20), pandera_statistical (0.40), great_expectations_full (0.15), composite_validation (0.25)
   - Conditional on: `build_vs_buy_posture`, `data_model_complexity`
   - Edges to: `schema_governance`, `observability_stack`

2. **[`schema_governance`](../prd/decisions/L5-operations/schema-governance.decision.yaml)** (L5_operations)
   - Options: minimal_manual (0.30), git_schema_versioning (0.30), dvc_plus_json_schema (0.25), openmetadata_catalog (0.15)
   - Conditional on: `build_vs_buy_posture`, `regulatory_posture`
   - Edges from: `data_quality_strategy`, `regulatory_posture`

### For This Project (Solo Hacker + Research/Portfolio Archetype)

**Recommended path through the new nodes**:
- `data_quality_strategy` → **composite_validation** (0.35) — Pandera + Hypothesis + Schemathesis
- `schema_governance` → **dvc_plus_json_schema** (0.30) or **git_schema_versioning** (0.35) — DVC when data artifacts grow, git versioning immediately

This balances the portfolio demonstration value against operational simplicity.

---

## See Also

- [Probabilistic PRD Decision Report](../prd/decisions/REPORT.md) — Full network visualization
- [Music Attribution Technology Landscape](music-tech-landscape/) — Broader technology research
- [Executable Plan](probabilistic-prd-executable-plan.xml) — 37-task implementation plan
- [Skill Update Plan](../../.claude/skills/self-learning-iterative-coder/skill-update-plan.md) — TDD skill v2.0 learnings
