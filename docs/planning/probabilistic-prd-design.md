# Probabilistic PRD System — Design Document

Design rationale for the Bayesian decision network that extends the Music Attribution Scaffold's PRD system.

---

## Motivation

Traditional PRDs encode a single path: "we chose PostgreSQL, deployed on Render, using MCP." This works for a specific team with specific constraints but fails when:

1. **Different teams** want to instantiate the same system (a 1-person team can't run Terraform + AWS ECS)
2. **Different domains** share the same architecture (music attribution and DPP traceability are isomorphic)
3. **Decisions change** as technology evolves (LLM providers shift quarterly, not annually)
4. **Dependencies exist** between decisions (choosing Supabase as database makes Supabase Auth almost inevitable)

The probabilistic PRD preserves the full decision space and makes dependencies explicit.

---

## The Bayesian Network Model

### Conceptual Foundation

Each architectural decision is a random variable with a discrete set of options. Dependencies between decisions form a directed acyclic graph (DAG). The probability of choosing a specific option depends on:

1. **Prior probability** — baseline likelihood without considering parent decisions
2. **Conditional probability** — how parent decisions shift the distribution
3. **Archetype modulation** — team-specific probability overrides
4. **Domain adjustment** — domain-specific prior shifts

Formally, for a decision D with parents P1, P2, ..., Pn:

```
P(D = option_i | P1 = p1, P2 = p2, ..., archetype = a, domain = d)
```

In practice, we don't compute full joint distributions. Instead, the conditional probability tables provide **qualitative reasoning aids** — they encode expert knowledge about which choices tend to co-occur and why.

### Design Decisions

**Why conditional tables instead of continuous functions?**
Conditional probability tables (CPTs) are explicit, auditable, and editable by non-statisticians. A product manager can read "P(PostgreSQL | Custom Build) = 0.65" and understand the implication. Continuous probability functions would be more compact but opaque.

**Why not a formal Bayesian network library?**
The goal is documentation and reasoning, not inference. Teams read these tables to understand decision dependencies, not to run belief propagation algorithms. YAML is the right format for human-readable, version-controlled decision documentation.

**Why allow skip-connections?**
Real decision dependencies don't respect hierarchy boundaries. The L1 "Build vs Buy Posture" directly influences L3 "Primary Database" more strongly than any L2 decision does. Skip-connections make this explicit rather than pretending influence only flows through adjacent levels.

---

## How Conditional Probabilities Work

### Reading a Conditional Table

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

This reads: "Given that the team chose Custom Build, the probability of choosing PostgreSQL Unified as the primary database is 0.65."

### Multiple Parents

When a decision has multiple parent dependencies, each parent's conditional table is evaluated independently. In practice, humans weight the stronger influence more heavily. The `influence_strength` field (strong/moderate/weak) provides this guidance.

### Probability Normalization

All probability distributions must sum to 1.0 (tolerance: 0.01):
- Prior probabilities across options in a decision
- Each row of a conditional table
- Each archetype's probability overrides

---

## How Archetypes Modulate the Distribution

Archetypes are **probability lenses** — they represent consistent biases across all decisions that reflect team constraints.

### The Four Archetypes

| Archetype | Central Bias | Binding Constraint |
|-----------|-------------|-------------------|
| **Engineer-Heavy Startup** | Control and debuggability | Time-to-market |
| **Musician-First Team** | Simplicity and zero-ops | Technical complexity ceiling |
| **Solo Hacker** | Minimum viable everything | Cannot sustain any ongoing ops |
| **Well-Funded Startup** | Enterprise readiness | Credibility requirements |

### Archetype vs. Prior

The prior probability represents the "average team" baseline. Archetypes replace the prior with team-specific distributions. This is equivalent to saying "for this type of team, the unconditional probability of choosing PostgreSQL is 0.60, not the general-population 0.45."

### Composing Archetype + Conditional

When reasoning about a specific team's decision:

1. Start with the archetype's probability overrides (not the general prior)
2. Consider how parent decisions further shift the distribution
3. Check hard constraints that may eliminate options entirely

---

## How Domain Overlays Affect Priors

Domains modulate decisions through three mechanisms:

### 1. Applicability Filtering

Each decision node has `domain_applicability` scores (0.0-1.0). Decisions with low applicability for a domain can be de-prioritized or skipped. For example, voice agent decisions might score 0.2 for DPP traceability but 1.0 for music attribution.

### 2. Prior Adjustments

Domain overlays specify explicit prior shifts:

```yaml
prd_prior_adjustments:
  adjustments:
    - decision_id: regulatory_posture
      adjustment: "Increase compliance_first by +0.20"
      rationale: "EU ESPR mandates compliance"
```

### 3. Hard Constraints

Some domain requirements eliminate options entirely. EU ESPR compliance effectively sets P(best_effort regulatory posture) = 0 for DPP traceability.

### The Isomorphism

The key design insight: music attribution and DPP traceability are architecturally isomorphic. Both follow:

```
FRAGMENTED SOURCES → ENTITY RESOLUTION → UNIFIED RECORD + CONFIDENCE → PERMISSIONED API → AGENTIC CONSUMERS
```

The scaffold's 23 decisions apply to both domains with only vocabulary and prior adjustments changing. This validates the domain-agnostic design.

---

## The Temporal Volatility Model

### Classification System

| Classification | Review Cadence | Change Probability | Examples |
|---------------|----------------|-------------------|----------|
| **Stable** | Quarterly | < 10% per quarter | Database choice, service decomposition |
| **Shifting** | Monthly | 10-30% per quarter | API protocol, frontend framework |
| **Volatile** | Biweekly | > 30% per quarter | LLM provider, regulatory posture |

### Change Drivers

Each volatile/shifting decision tracks specific change drivers — observable signals that would trigger probability reassessment. For example:

- **LLM Provider** volatility is driven by: model capability leaps, pricing changes, open-source convergence
- **Regulatory Posture** volatility is driven by: EU AI Act enforcement timeline, GDPR actions against AI training

### Staleness Detection

A decision is stale when `next_review` date has passed without reassessment. Stale decisions should be treated as shifting regardless of their classification.

---

## Portfolio Narrative: CTO-Level Patterns Demonstrated

This probabilistic PRD system demonstrates several architectural thinking patterns relevant to CTO/VP Engineering roles:

### 1. Decision Documentation as Architecture

Architecture decisions are often hidden in Slack threads and meeting notes. This system makes every decision explicit, with rationale, alternatives, and trade-offs documented in version-controlled YAML.

### 2. Bayesian Reasoning About Uncertainty

Rather than pretending architectural decisions are deterministic, the probabilistic model acknowledges uncertainty and makes it quantifiable. "We're 60% confident PostgreSQL is the right choice" is more honest and useful than "we chose PostgreSQL."

### 3. Team-Aware Architecture

The archetype system recognizes that architecture is not team-independent. What's optimal for a 15-person engineering team is unachievable for a solo developer. Making this explicit prevents one-size-fits-all recommendations.

### 4. Domain-Agnostic Composability

The overlay system demonstrates that architectural patterns transfer across domains when properly abstracted. The same confidence-scored attribution pipeline serves music, physical goods, and knowledge graphs.

### 5. Temporal Awareness

Technology decisions decay. The volatility model acknowledges this and builds review cadences into the system rather than treating architecture as immutable.

### 6. Multi-Format Documentation

The triple-format approach (YAML for machines, mermaid for visual reasoning, narrative for humans) ensures decisions are accessible regardless of audience.

---

## Validation Criteria

The complete system satisfies:

1. **Probability sums**: All distributions sum to 1.0 (tolerance: 0.01)
2. **DAG acyclicity**: No circular dependencies in `_network.yaml`
3. **Referential integrity**: All decision_id and option_id references resolve
4. **Archetype completeness**: Every archetype covers every decision
5. **Domain coverage**: Every decision has applicability scores for all domains
6. **Scenario coherence**: Each scenario's resolved decisions form a viable system

---

## See Also

- [Probabilistic PRD Decision Network](../prd/decisions/README.md) — Implementation
- [Network Report](../prd/decisions/REPORT.md) — Visualizations
- [Archetypes](../prd/archetypes/README.md) — Team profiles
- [Domains](../prd/domains/README.md) — Domain overlays
- [Scenarios](../prd/scenarios/README.md) — Composed paths
