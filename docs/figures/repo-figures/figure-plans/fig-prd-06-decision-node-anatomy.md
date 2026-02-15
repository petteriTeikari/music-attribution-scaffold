# fig-prd-06: Decision Node Anatomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-06 |
| **Title** | Decision Node Anatomy -- What a Single Node Contains |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md, docs/prd/decisions/_schema.yaml |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Dissects a single decision node to show its internal structure. Uses the `llm_provider` node as a concrete example. Shows: title, decision_level, options[] with prior_probability and status, conditional_on[] with parent-to-child probability tables, archetype_weights{} with per-team overrides, volatility classification, and domain_applicability scores.

The key message is: "Each decision node is a self-contained Bayesian unit with options, conditional probabilities, archetype overrides, and volatility classification."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DECISION NODE ANATOMY                                         |
|  ■ Example: llm_provider                                       |
+---------------------------------------------------------------+
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  decision_id: llm_provider                              │   |
|  │  title: "LLM Provider"                                  │   |
|  │  decision_level: L3_implementation                      │   |
|  │  status: active                                         │   |
|  ├─────────────────────────────────────────────────────────┤   |
|  │  OPTIONS (prior probabilities sum to 1.0)               │   |
|  │  ┌──────────────────────┐  ┌────────────────────────┐   │   |
|  │  │ anthropic_primary    │  │ openai_primary         │   │   |
|  │  │ P=0.45  ■ selected   │  │ P=0.25  viable         │   │   |
|  │  └──────────────────────┘  └────────────────────────┘   │   |
|  │  ┌──────────────────────┐  ┌────────────────────────┐   │   |
|  │  │ google_gemini        │  │ multi_provider         │   │   |
|  │  │ P=0.10  viable       │  │ P=0.15  viable         │   │   |
|  │  └──────────────────────┘  └────────────────────────┘   │   |
|  ├─────────────────────────────────────────────────────────┤   |
|  │  CONDITIONAL ON: ai_framework_strategy (moderate)       │   |
|  │  P(anthropic | direct_api_pydantic) = 0.45              │   |
|  │  P(anthropic | orchestration_framework) = 0.25          │   |
|  ├─────────────────────────────────────────────────────────┤   |
|  │  ARCHETYPE WEIGHTS                                      │   |
|  │  Engineer: anthropic 0.35 | Musician: anthropic 0.40    │   |
|  │  Solo:     anthropic 0.40 | Funded:   anthropic 0.35    │   |
|  ├─────────────────────────────────────────────────────────┤   |
|  │  VOLATILITY: volatile  │  DOMAIN: music 1.0, dpp 0.8   │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DECISION NODE ANATOMY" with coral accent square |
| Node container | `decision_point` | Full node card showing all sections |
| Header section | `label_editorial` | decision_id, title, level, status fields |
| Options section | `branching_path` | Four option cards with prior_probability and status |
| Selected option highlight | `selected_option` | anthropic_primary highlighted with solid border and coral accent |
| Conditional table section | `data_flow` | Parent decision influence with conditional probabilities |
| Archetype weights section | `archetype_overlay` | Four archetype override values |
| Volatility badge | `decision_point` | Classification badge: volatile |
| Domain applicability | `decision_point` | Per-domain relevance scores |

## Anti-Hallucination Rules

1. The llm_provider node has FIVE options: anthropic_primary (0.45, selected), openai_primary (0.25, viable), google_gemini (0.10, viable), multi_provider (0.15, viable), open_source_local (0.05, experimental).
2. The conditional table for ai_framework_strategy shows P(anthropic | direct_api_pydantic) = 0.45 and P(anthropic | orchestration_framework) = 0.25 -- these are exact values from the YAML.
3. Archetype weights: Engineer 0.35, Musician 0.40, Solo 0.40, Well-Funded 0.35 for anthropic_primary -- exact values from the YAML.
4. Domain applicability: music_attribution 1.0, dpp_traceability 0.8 -- exact values from the YAML.
5. Volatility classification is "volatile" -- exact value from the YAML.
6. The schema requires options priors to sum to 1.0 (tolerance 0.01).
7. Option statuses are: recommended, viable, experimental, deferred, rejected -- per _schema.yaml. The "selected" status shown in the llm_provider YAML is a custom addition.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Annotated diagram: anatomy of a single Bayesian decision node in the music attribution scaffold probabilistic PRD, using the LLM provider node as example -- showing options with prior probabilities, conditional dependencies, team archetype weight overrides, volatility classification, and domain applicability scores for transparent confidence scoring.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Annotated diagram: anatomy of a single Bayesian decision node in the music attribution scaffold probabilistic PRD, using the LLM provider node as example -- showing options with prior probabilities, conditional dependencies, team archetype weight overrides, volatility classification, and domain applicability scores for transparent confidence scoring.](docs/figures/repo-figures/assets/fig-prd-06-decision-node-anatomy.jpg)

*Figure 6. Each decision node in the probabilistic PRD is a self-contained Bayesian unit: options with prior probabilities summing to 1.0, conditional tables linking to parent decisions, archetype-specific weight overrides, and volatility classification -- all defined in a machine-readable YAML schema.*

### From this figure plan (relative)

![Annotated diagram: anatomy of a single Bayesian decision node in the music attribution scaffold probabilistic PRD, using the LLM provider node as example -- showing options with prior probabilities, conditional dependencies, team archetype weight overrides, volatility classification, and domain applicability scores for transparent confidence scoring.](../assets/fig-prd-06-decision-node-anatomy.jpg)
