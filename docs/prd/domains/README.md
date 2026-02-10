# Domain Overlay System

The probabilistic PRD is **domain-agnostic by design**. Domain overlays customize the generic decision network for specific application domains without modifying the core decision structure.

---

## The Isomorphism

All supported domains follow the same fundamental pipeline:

```
FRAGMENTED SOURCES → ENTITY RESOLUTION → UNIFIED RECORD + CONFIDENCE → PERMISSIONED API → AGENTIC CONSUMERS
```

| Stage | Music Attribution | DPP Traceability | Generic Graph RAG |
|-------|-------------------|-------------------|-------------------|
| **Sources** | Discogs, MusicBrainz, artist input | GS1, EPCIS, supplier declarations | Web crawlers, document parsers, APIs |
| **Entity Resolution** | Artist/track/release matching | Product/component/material matching | Entity/concept/relation extraction |
| **Unified Record** | Artist credit + A0-A3 assurance | Product passport + T0-T3 assurance | Knowledge graph node + confidence |
| **Permissioned API** | MCP for AI training consent | Digital Link for supply chain queries | GraphQL/REST for knowledge queries |
| **Consumers** | AI platforms, streaming services | Regulators, retailers, consumers | AI agents, search engines, analysts |

The scaffold's architectural decisions (database, graph strategy, confidence scoring, API protocol) apply isomorphically across all domains. What changes is the **vocabulary**, **entities**, **compliance requirements**, and **probability priors**.

---

## Domain Overlay Structure

Each domain overlay file (`<domain>/overlay.yaml`) contains:

### Core Entities
Domain-specific entity types that map to the generic entity resolution system.

### Data Sources
Available data sources with reliability and coverage metadata.

### Assurance Levels
Domain-specific confidence tiers (A0-A3 for music, T0-T3 for DPP).

### Compliance Requirements
Regulatory frameworks that affect decision probabilities.

### Vocabulary
Domain-specific terminology mapped to generic scaffold concepts.

### PRD Prior Adjustments
Per-decision probability adjustments based on domain characteristics.

---

## How Domains Affect Decisions

Domain overlays modulate the decision network through:

1. **`domain_applicability` scores** — Each decision node has relevance scores per domain (0.0-1.0). Decisions with low relevance can be skipped.

2. **PRD prior adjustments** — Domains can shift the prior probabilities for specific options (e.g., DPP traceability increases `compliance_first` probability).

3. **Hard constraints** — Some domain requirements eliminate options (e.g., EU ESPR mandates audit trails, eliminating `best_effort` regulatory posture for DPP).

---

## Available Domains

See [`registry.yaml`](registry.yaml) for the current list.

| Domain | Status | Overlay |
|--------|--------|---------|
| [Music Attribution](music-attribution/overlay.yaml) | Active | Full overlay with A0-A3 assurance |
| [DPP Traceability](dpp-traceability/overlay.yaml) | Active | Full overlay with T0-T3 assurance |
| Generic Graph RAG | Planned | Backbone defaults only |

---

## Adding a New Domain

1. Create `<domain-name>/overlay.yaml` following the structure of existing overlays
2. Register in `registry.yaml`
3. Add `domain_applicability` scores to all decision nodes
4. Create at least one scenario in `../scenarios/` demonstrating the domain
5. Document domain-specific vocabulary and entity mappings

---

## Backbone Defaults

[`backbone-defaults.yaml`](backbone-defaults.yaml) defines the domain-agnostic defaults — what's shared across all domains. Domain overlays extend these defaults, they don't replace them.

---

## See Also

- [`../decisions/`](../decisions/) — Decision nodes with domain_applicability scores
- [`../archetypes/`](../archetypes/) — Team profiles (orthogonal to domain)
- [`../scenarios/`](../scenarios/) — Archetype + Domain compositions
- [`backbone-defaults.yaml`](backbone-defaults.yaml) — Domain-agnostic defaults
