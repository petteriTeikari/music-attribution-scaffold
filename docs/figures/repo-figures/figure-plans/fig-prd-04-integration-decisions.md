# fig-prd-04: Level 2 Integration Decisions

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-04 |
| **Title** | Level 2: Architecture Decisions -- LLM Provider, Routing, UI Framework |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Details the L2 architecture decisions and key L3 implementation decisions that define the integration layer. Focuses on the "selected" options for this scaffold's reference implementation: Anthropic primary (LLM), PydanticAI native (routing), CopilotKit + AG-UI (agentic UI). Shows how these three selections reinforce each other.

The key message is: "The scaffold's reference implementation selects Anthropic + PydanticAI + CopilotKit -- a coherent stack where each choice reinforces the others."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  INTEGRATION DECISIONS                                         |
|  ■ L2 Architecture + L3 Selected Options                       |
+---------------------------------------------------------------+
|                                                                |
|  L2: ARCHITECTURE LAYER                                        |
|  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐        |
|  │ Data Model   │  │ API Protocol│  │ AI Framework    │        |
|  │ Complexity   │  │             │  │ Strategy        │        |
|  │ ────────     │  │ ────────    │  │ ──────────      │        |
|  │ Graph-       │  │ MCP         │  │ Direct API +    │        |
|  │ Enriched     │  │ Primary     │  │ PydanticAI      │        |
|  │ Relational   │  │             │  │ (selected)      │        |
|  └──────┬───────┘  └──────┬──────┘  └───────┬─────────┘        |
|         │                 │                  │                  |
|         ▼                 ▼                  ▼                  |
|  L3: SELECTED IMPLEMENTATION STACK                             |
|  ┌──────────────────────────────────────────────────────┐      |
|  │                                                      │      |
|  │  LLM Provider         Routing Strategy               │      |
|  │  ══════════════       ═══════════════════            │      |
|  │  Anthropic Primary    PydanticAI Native              │      |
|  │  (Haiku 4.5 default)  (FallbackModel + env var)      │      |
|  │  P=0.45 selected      P=0.45 selected                │      |
|  │                                                      │      |
|  │  Agentic UI            Frontend Framework            │      |
|  │  ══════════            ══════════════════            │      |
|  │  CopilotKit + AG-UI   Next.js 15 (App Router)       │      |
|  │  P=0.50 selected       (required by CopilotKit)      │      |
|  │                                                      │      |
|  └──────────────────────────────────────────────────────┘      |
|                                                                |
|  REINFORCEMENT: MCP Protocol → CopilotKit (P=0.55 | MCP)      |
|  PydanticAI → Anthropic (P=0.45 | direct_api_pydantic)        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "INTEGRATION DECISIONS" with coral accent square |
| L2 architecture nodes | `decision_point` | Data Model Complexity, API Protocol, AI Framework Strategy with selected options |
| L3 selected stack | `selected_option` | Four selected options in a unified panel: Anthropic, PydanticAI Native, CopilotKit, Next.js |
| Probability labels | `data_mono` | Prior probabilities for each selected option |
| Cascade arrows | `data_flow` | L2 to L3 influence arrows |
| Reinforcement callout | `callout_bar` | Conditional probability reinforcement between selections |

## Anti-Hallucination Rules

1. LLM Provider selected option is `anthropic_primary` with prior P=0.45. Status: selected.
2. LLM Routing selected option is `pydantic_ai_native` with prior P=0.45. Status: selected.
3. Agentic UI selected option is `copilotkit_agui` with prior P=0.50. Status: selected.
4. AI Framework Strategy selected option is `direct_api_pydantic`. This is L2, not L3.
5. The conditional P(CopilotKit | MCP Primary) = 0.55 -- from the actual conditional table.
6. CopilotKit requires Next.js -- this is a hard constraint from the decision node.
7. Haiku 4.5 is the default agent model, not Sonnet or Opus.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture overview: integration-layer decisions in the music attribution scaffold showing how L2 architecture choices cascade into the selected implementation stack -- Anthropic LLM provider, PydanticAI routing, and CopilotKit agentic UI -- with conditional probability reinforcement between each open-source component selection.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture overview: integration-layer decisions in the music attribution scaffold showing how L2 architecture choices cascade into the selected implementation stack -- Anthropic LLM provider, PydanticAI routing, and CopilotKit agentic UI -- with conditional probability reinforcement between each open-source component selection.](docs/figures/repo-figures/assets/fig-prd-04-integration-decisions.jpg)

*Figure 4. The scaffold's reference implementation selects a coherent integration stack where each choice reinforces the others: Anthropic primary, PydanticAI native routing, and CopilotKit AG-UI, all connected by Bayesian conditional probabilities in the decision network.*

### From this figure plan (relative)

![Architecture overview: integration-layer decisions in the music attribution scaffold showing how L2 architecture choices cascade into the selected implementation stack -- Anthropic LLM provider, PydanticAI routing, and CopilotKit agentic UI -- with conditional probability reinforcement between each open-source component selection.](../assets/fig-prd-04-integration-decisions.jpg)
