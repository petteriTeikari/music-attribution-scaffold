# Probabilistic Decision Network

This directory contains the **Bayesian decision network** for the Music Attribution Scaffold PRD system. Each `.decision.yaml` file represents a node in a directed acyclic graph (DAG) of architectural decisions, with conditional probability tables encoding how upstream choices influence downstream options.

---

## Conceptual Model

Traditional PRDs collapse decisions into a single path. A probabilistic PRD preserves the full decision space as a Bayesian network:

```
P(L3_database | L2_data_model, L1_build_vs_buy) =
    P(postgresql | complex_graph, custom_build) = 0.65
    P(supabase   | complex_graph, custom_build) = 0.10
    ...
```

This enables:

1. **Multi-team applicability** — Different team archetypes (engineer-heavy, musician-first, solo hacker) produce different probability distributions over the same decision space
2. **Domain portability** — The same network structure applies to music attribution, DPP traceability, and generic Graph RAG systems
3. **Temporal tracking** — Decisions are flagged as stable/shifting/volatile with scheduled review dates
4. **Scenario composition** — A "scenario" is a specific path through the network (a joint probability assignment)

---

## Hierarchy: 5 Decision Levels

| Level | Scope | Example Decisions |
|-------|-------|-------------------|
| **L1 Business** | Market, revenue, regulatory posture | Build-vs-buy, target market, revenue model |
| **L2 Architecture** | System shape, protocols, decomposition | Data model complexity, API protocol, service boundaries |
| **L3 Implementation** | Specific technology choices | Database, graph engine, LLM provider, frontend framework |
| **L4 Deployment** | Where and how code runs | Compute platform, CI/CD, IaC tooling, container strategy |
| **L5 Operations** | Runtime concerns | Observability, scaling, backup/DR, secrets management |

Edges flow **downward** (L1 → L2 → L3 → L4 → L5) with occasional **skip-connections** (e.g., L1 build-vs-buy directly influences L4 compute platform).

---

## How to Read a Decision Node

Each `.decision.yaml` file follows the schema defined in [`_schema.yaml`](_schema.yaml). Key sections:

### Options and Prior Probabilities

```yaml
options:
  - option_id: postgresql_unified
    prior_probability: 0.55
    status: recommended
    description: "PostgreSQL with pgvector + Apache AGE extensions"
```

Prior probabilities represent **unconditional** baseline likelihoods before considering parent decisions. They must sum to 1.0 across all options in a decision.

### Conditional Probability Tables

```yaml
conditional_on:
  - parent_decision_id: build_vs_buy_posture
    conditional_table:
      - given_parent_option: custom_build
        then_probabilities:
          postgresql_unified: 0.65
          supabase: 0.10
          sqlite_turso: 0.05
          cockroachdb: 0.20
```

Each row specifies: "Given that the parent decided X, here are the updated probabilities for this decision's options." Rows for each parent must independently sum to 1.0.

### Archetype Weights

```yaml
archetype_weights:
  engineer_heavy_startup:
    probability_overrides:
      postgresql_unified: 0.70
      supabase: 0.05
      sqlite_turso: 0.05
      cockroachdb: 0.20
```

Per-team-archetype probability overrides. These replace the prior probabilities when reasoning from a specific team profile. Each archetype's overrides must sum to 1.0.

### Volatility Classification

```yaml
volatility:
  classification: stable
  last_assessed: 2026-02-10
  next_review: 2026-05-10
  change_drivers:
    - "PostgreSQL extension ecosystem maturity"
```

- **stable**: Unlikely to change within 6 months. Review quarterly.
- **shifting**: Actively evolving, may change within 3 months. Review monthly.
- **volatile**: High uncertainty, could change within weeks. Review biweekly.

### Domain Applicability

```yaml
domain_applicability:
  music_attribution: 1.0
  dpp_traceability: 1.0
  generic_graph_rag: 0.9
```

Relevance scores (0.0-1.0) per domain. A score of 1.0 means the decision is fully applicable; 0.0 means irrelevant. Used to filter decisions when instantiating the network for a specific domain.

---

## File Index

| File | Purpose |
|------|---------|
| [`_schema.yaml`](_schema.yaml) | JSON Schema for `.decision.yaml` files |
| [`_network.yaml`](_network.yaml) | DAG topology: all nodes and edges |
| [`REPORT.md`](REPORT.md) | Human-readable report with mermaid visualizations |
| `L1-business/*.decision.yaml` | Business-level decisions |
| `L2-architecture/*.decision.yaml` | Architecture-level decisions |
| `L3-implementation/*.decision.yaml` | Implementation-level decisions |
| `L4-deployment/*.decision.yaml` | Deployment-level decisions |
| `L5-operations/*.decision.yaml` | Operations-level decisions |

---

## Validation Invariants

All decision files must satisfy:

1. **Probability sums**: All `prior_probability` arrays sum to 1.0 (tolerance: 0.01)
2. **Conditional table completeness**: Each conditional table row covers all options for this decision
3. **Conditional table sums**: Each row's `then_probabilities` sums to 1.0 (tolerance: 0.01)
4. **Archetype completeness**: Each archetype's `probability_overrides` covers all options and sums to 1.0
5. **DAG acyclicity**: The `_network.yaml` graph contains no cycles
6. **Referential integrity**: All `parent_decision_id` references resolve to existing nodes in `_network.yaml`
7. **Option consistency**: Option IDs in conditional tables match the decision's own `options` list

---

## See Also

- [`../archetypes/`](../archetypes/) — Team archetype profiles that modulate probabilities
- [`../scenarios/`](../scenarios/) — Composed decision paths through the network
- [`../domains/`](../domains/) — Domain overlay definitions
- [`../schema.yaml`](../schema.yaml) — PRD frontmatter schema (extended with probabilistic block)
