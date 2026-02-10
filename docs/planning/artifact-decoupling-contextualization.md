# Artifact Decoupling Contextualization for the Probabilistic PRD

**Date**: 2026-02-10
**Status**: Research complete, not yet implemented
**Branch for implementation**: Future branches (not `feat/expansion-of-probabilistic-prd`)
**Related decision nodes**: [`artifact_decoupling_strategy`](../prd/decisions/L2-architecture/artifact-decoupling-strategy.decision.yaml), [`schema_governance`](../prd/decisions/L5-operations/schema-governance.decision.yaml), [`data_quality_strategy`](../prd/decisions/L3-implementation/data-quality-strategy.decision.yaml)

---

## Executive Summary

Any system whose behavior is determined by the intersection of code, configuration, data, and prompts must version each independently for reproducibility. Coupling any two forces synchronized releases and makes experiment replay impossible.

This document analyzes the **4-artifact decoupling pattern** — Code, Config, Data, Prompts — contextualized to the music attribution scaffold's probabilistic PRD, with conditional probability estimates for tool adoption at each maturity stage.

---

## The Four Artifact Types

### 1. Code (git)

**What it includes**: Pipeline implementations, Pydantic schemas, API routes, tests
**Versioning**: git (already in place)
**Iteration cadence**: Feature-driven (days to weeks)
**Stakeholders**: Engineers

This is the baseline — all other artifacts are decoupled *from* code.

### 2. Config (pydantic-settings + YAML)

**What it includes**:
- Source reliability weights (MusicBrainz: 0.9, Discogs: 0.7, AcoustID: 0.8)
- Confidence thresholds (A3 requires >= 0.85, needs_review threshold)
- Feature flags (enable_llm_disambiguation, use_embedding_match)
- Environment settings (DATABASE_URL, API keys)
- Experiment hyperparameters (conformal prediction alpha, embedding model name)

**Versioning options**:

| Tool | When | P(adopt) for this project |
|------|------|--------------------------|
| pydantic-settings + `.env` | Always (already using) | **1.00** |
| YAML config files in `config/` | When > 10 config parameters | **0.85** |
| Hydra | When running ML experiments with sweeps | 0.55 |
| Dynaconf | When multi-environment layering needed | 0.30 |
| Feature flags (Unleash) | When gradual rollout needed | 0.20 |
| Vault/AWS SSM | When handling production secrets | 0.60 |

**Key principle**: Config is **data, not code**. Store in YAML/TOML, validate with pydantic-settings, override with environment variables. Never embed thresholds as Python constants.

**Current state in scaffold**: `pydantic-settings` already in use for `Settings`. Source weights and confidence thresholds are currently hardcoded in implementation files — these should migrate to config YAML.

**Concrete next step**:
```yaml
# config/attribution.yaml
source_weights:
  musicbrainz: 0.9
  discogs: 0.7
  acoustid: 0.8
  file_metadata: 0.5
  artist_input: 1.0

confidence_thresholds:
  a3_minimum: 0.85
  needs_review: 0.5
  conformal_coverage: 0.90
  calibration_error_target: 0.05

feature_flags:
  enable_llm_disambiguation: true
  enable_embedding_match: true
  enable_splink_linkage: true
```

### 3. Data (DVC + remote storage)

**What it includes**:
- MusicBrainz/Discogs data snapshots (for reproducible ETL)
- Sentence-transformer embedding models
- Conformal prediction calibration datasets
- Evaluation gold datasets (`tests/eval/fixtures/`)
- Entity resolution training data (if using supervised methods)

**Versioning options**:

| Tool | When | P(adopt) for this project |
|------|------|--------------------------|
| Git (small fixtures) | Test fixtures < 1MB | **1.00** (already doing) |
| DVC | Any artifact > 50MB or experiment reproducibility | **0.75** |
| lakeFS | When need git-like branching for data | 0.15 |
| Delta Lake / Iceberg | When SQL warehouse layer exists | 0.10 |
| Git LFS | Simple large file tracking, no pipeline DAG | 0.25 |

**Key principle**: Data has a different lifecycle than code. A model trained on dataset v1.2 must be reproducible even after dataset v1.3 is released. DVC tags (`dvc tag v1.2`) pin data versions; code references tags, not mutable paths.

**Current state in scaffold**: Small test fixtures in `tests/`. No large data artifacts yet. Embedding models downloaded at runtime.

**Concrete DVC setup** (future branch):
```yaml
# dvc.yaml
stages:
  fetch_musicbrainz:
    cmd: python -m music_attribution.etl.musicbrainz --output data/raw/musicbrainz/
    outs:
      - data/raw/musicbrainz/

  embed_records:
    cmd: python -m music_attribution.resolution.embedding_match --input data/raw/ --output data/embeddings/
    deps:
      - data/raw/musicbrainz/
      - src/music_attribution/resolution/embedding_match.py
    outs:
      - data/embeddings/

  calibrate:
    cmd: python -m music_attribution.attribution.conformal --data data/embeddings/ --output data/calibration/
    deps:
      - data/embeddings/
    outs:
      - data/calibration/
    metrics:
      - data/calibration/metrics.json
```

### 4. Prompts (Langfuse / versioned YAML)

**What it includes**:
- LLM disambiguation templates (Task 2.3d)
- System instructions for attribution assessment
- Few-shot examples for entity resolution
- MCP query response formatting templates
- Evaluation prompts for LLM-as-judge

**Versioning options**:

| Tool | When | P(adopt) for this project |
|------|------|--------------------------|
| Strings in code | Never (anti-pattern) | 0.00 |
| YAML files in `prompts/` dir | Simple projects, single developer | **0.70** |
| Langfuse prompt management | When non-engineers iterate on prompts | **0.55** |
| PromptLayer | When need A/B testing prompts | 0.15 |
| Promptfoo (evaluation) | When need systematic prompt regression testing | 0.40 |

**Key principle**: Prompts are the most volatile artifact type — they change more frequently than code, config, or data. Their quality is empirically determined (requires evaluation), not logically determined (like code). Decoupling prompts from code enables:
- Non-engineer prompt iteration (domain experts, musicians)
- A/B testing without code deployment
- Evaluation-gated promotion (dev → staging → production labels)
- Audit trail for prompt changes (regulatory compliance)

**Current state in scaffold**: LLM disambiguation (Task 2.3d) has prompts as Python strings. MCP server has hardcoded response patterns.

**Concrete prompt YAML** (future branch):
```yaml
# prompts/disambiguation.yaml
version: "1.0"
templates:
  entity_disambiguation:
    system: |
      You are a music attribution expert. Given conflicting information
      from multiple sources about a recording's credits, determine the
      most likely correct attribution.

      Consider:
      - Source reliability (MusicBrainz > Discogs > file metadata)
      - Temporal consistency (newer sources may be more accurate)
      - Cross-reference agreement (multiple sources agreeing increases confidence)

    user: |
      Recording: {{recording_title}} by {{artist_name}}

      Source 1 ({{source_1_name}}, confidence: {{source_1_confidence}}):
      {{source_1_credits}}

      Source 2 ({{source_2_name}}, confidence: {{source_2_confidence}}):
      {{source_2_credits}}

      What are the correct attribution credits? Respond as JSON.

    model: "claude-sonnet-4-5-20250929"
    temperature: 0.1
    max_tokens: 1024
```

**Langfuse integration pattern** (future branch):
```python
from langfuse import Langfuse

langfuse = Langfuse()

# Fetch versioned prompt at runtime
prompt = langfuse.get_prompt("entity_disambiguation", label="production")

# Compile with variables
compiled = prompt.compile(
    recording_title=record.title,
    artist_name=record.artist,
    source_1_name=sources[0].name,
    # ...
)
```

---

## The Reproducibility Matrix

A fully decoupled system can reproduce any historical result by pinning all four artifact versions:

```
Experiment Run #42:
  code:    git SHA abc123
  config:  config/attribution.yaml @ git SHA abc123
  data:    dvc tag v1.2.3 (S3: s3://bucket/data/v1.2.3/)
  prompts: langfuse label "v2024-01-15" OR prompts/*.yaml @ git SHA abc123
  env:     Docker image sha256:def456 (pinned dependencies)
```

### Reproducibility Levels

| Level | What's Pinned | Can Reproduce? | Tools Needed |
|-------|---------------|----------------|-------------|
| **R0** | Nothing | No | None |
| **R1** | Code only | Partially (if data/config/prompts unchanged) | git |
| **R2** | Code + Config | Mostly (if data unchanged) | git + pydantic-settings |
| **R3** | Code + Config + Data | Yes (deterministic pipelines) | git + pydantic-settings + DVC |
| **R4** | Code + Config + Data + Prompts | Yes (including LLM steps) | git + pydantic-settings + DVC + Langfuse |
| **R5** | All + Environment | Exact reproduction | All + Docker + lock files |

**This project's current state**: R1 (code in git, everything else coupled)
**Target state**: R3-R4 (config in YAML, data in DVC, prompts versioned)
**R5 requires**: Docker + pinned `uv.lock` (already have lock file)

---

## Conditional Probabilities: When to Decouple Each Artifact

### Config Decoupling

| Condition | P(decouple) | Rationale |
|-----------|-------------|-----------|
| > 10 tunable parameters | **0.90** | Config files are cleaner than scattered constants |
| Running experiments with parameter sweeps | **0.85** | Hydra/MLflow need structured config |
| Multiple deployment environments | **0.80** | 12-Factor demands external config |
| Single hardcoded environment | 0.40 | Still good practice, lower urgency |
| Research/portfolio project (this project) | **0.85** | Demonstrates 12-Factor discipline |

### Data Decoupling

| Condition | P(decouple) | Rationale |
|-----------|-------------|-----------|
| Data artifacts > 50MB | **0.90** | Git can't handle this |
| Experiment reproducibility needed | **0.85** | `dvc repro` is the gold standard |
| Multiple data sources with versioning needs | **0.80** | Pin exact snapshot versions |
| All data generated from code at runtime | 0.30 | Code versioning may suffice |
| Research/portfolio project (this project) | **0.75** | Demonstrates MLOps maturity |

### Prompt Decoupling

| Condition | P(decouple) | Rationale |
|-----------|-------------|-----------|
| LLM pipeline in production | **0.85** | Prompts change faster than code |
| Non-engineer prompt stakeholders | **0.90** | UI-based editing essential |
| Prompt A/B testing needed | **0.80** | Requires independent versioning |
| Single LLM call, stable prompt | 0.35 | YAML file in git may suffice |
| Research/portfolio project (this project) | **0.60** | YAML files first, Langfuse when production |

---

## Cross-Cutting: How Decoupling Interacts with Other PRD Decisions

### Impact on EVERY PRD Permutation

The 4-artifact pattern is **architecture-level** (L2) and affects downstream decisions regardless of other choices:

| PRD Path | Config | Data | Prompts |
|----------|--------|------|---------|
| Custom Build + PostgreSQL + AGE | Hydra + YAML | DVC + S3 | Langfuse (self-hosted) |
| Managed Services + Supabase | pydantic-settings + env vars | DVC + Supabase Storage | Langfuse Cloud |
| SaaS Maximalist + SQLite | YAML in git | Git LFS (small data) | YAML in git |
| Enterprise + CockroachDB | Vault + Dynaconf | DVC + enterprise storage | Langfuse + PromptLayer |

### Interaction with Existing Decision Nodes

| Decision Node | How Decoupling Affects It |
|---------------|--------------------------|
| `ai_framework_strategy` | LLM-heavy → prompt decoupling critical; No-LLM → prompt decoupling irrelevant |
| `data_model_complexity` | Complex models → more config parameters → config decoupling critical |
| `schema_governance` | DVC for data + JSON Schema export for schemas → complementary |
| `data_quality_strategy` | Pandera checks on data → data must be versioned to track quality over time |
| `observability_stack` | More artifacts → more to observe; Langfuse covers both prompts and LLM tracing |
| `ci_cd_pipeline` | Decoupled artifacts need CI/CD support for each type (lint config, validate DVC, test prompts) |

---

## Prompt Cards: Documentation Standard

Inspired by Model Cards (Mitchell et al., 2018) and Data Cards (Gebru et al., 2018), a **Prompt Card** documents each production prompt:

```yaml
# prompt-cards/entity-disambiguation.yaml
name: entity_disambiguation
version: "2.0"
created: 2026-02-10
last_updated: 2026-02-10
authors: ["Petteri Teikari"]

purpose: >
  Resolve conflicting attribution credits from multiple data sources
  for a single recording entity.

model_requirements:
  min_capability: "claude-sonnet-4-5-20250929 or equivalent"
  temperature: 0.1
  max_tokens: 1024

input_schema:
  recording_title: string
  artist_name: string
  sources: list[{name, confidence, credits}]

output_schema:
  $ref: "../schemas/attribution-record.json"

known_limitations:
  - "May hallucinate credits not present in any source"
  - "Performance degrades with > 5 conflicting sources"
  - "Non-Latin script artist names may reduce accuracy"

evaluation:
  test_set: "tests/eval/fixtures/disambiguation_gold.json"
  metrics:
    accuracy: 0.87
    f1_macro: 0.83
  last_evaluated: 2026-02-10

ethical_considerations:
  - "May perpetuate attribution biases present in training data"
  - "Western music industry conventions may not apply globally"

related_prompts:
  - "attribution_assessment"
  - "conflict_resolution"
```

**P(implement prompt cards)**: 0.55 for this project — high documentation value for research companion, moderate effort.

---

## Implementation Roadmap

### Phase 0 (Now — This Branch)

**Already have**: Code in git, pydantic-settings for env config, `uv.lock` for environment
**Current reproducibility level**: R1

### Phase 1: Config Decoupling (Next Branch)

**Create**: `config/` directory with structured YAML
**Migrate**: Hardcoded thresholds, weights, feature flags → YAML
**Validate**: pydantic-settings loads from YAML + env override
**Estimated effort**: 2-3 tasks

**P(implement) = 0.85** — High value, low risk, immediate reproducibility improvement

### Phase 2: Data Decoupling (When Data Artifacts Exist)

**Setup**: DVC init, configure remote (S3/GCS)
**Track**: Evaluation gold sets, calibration datasets
**Pipeline**: `dvc.yaml` for reproducible ETL → Resolution → Calibration
**Estimated effort**: 3-4 tasks

**P(implement) = 0.75** — Triggered when embedding models or calibration sets exceed git-viable size

### Phase 3: Prompt Decoupling (When LLM Pipeline Matures)

**Create**: `prompts/` directory with versioned YAML templates
**Integrate**: Runtime prompt loading (Jinja2 or Langfuse SDK)
**Document**: Prompt Cards for each production prompt
**Evaluate**: Promptfoo regression tests in CI
**Estimated effort**: 3-5 tasks

**P(implement) = 0.60** — YAML-first, Langfuse when production deployment happens

### Phase 4: Full Reproducibility (R4-R5)

**Link**: Experiment tracking (MLflow/W&B) connecting all four artifact versions
**Reproduce**: `make reproduce-experiment RUN_ID=42`
**Audit**: OpenLineage for cross-artifact lineage
**Estimated effort**: 5-8 tasks

**P(implement) = 0.40** — Conditional on the project reaching production scale

---

## See Also

- [Probabilistic PRD Decision Report](../prd/decisions/REPORT.md)
- [Quality Tooling Contextualization](quality-tooling-contextualization.md)
- [Schema Governance Decision](../prd/decisions/L5-operations/schema-governance.decision.yaml)
- [12-Factor App Config](https://12factor.net/config)
- [Versioning, Provenance, and Reproducibility in Production ML](https://ckaestne.medium.com/versioning-provenance-and-reproducibility-in-production-machine-learning-355c48665005)
- [Langfuse Prompt Management](https://langfuse.com/docs/prompt-management/overview)
