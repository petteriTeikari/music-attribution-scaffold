# fig-topic-03: Uncertainty Propagation Through Decision Trajectories

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-03 |
| **Title** | Uncertainty Propagation — How Errors Compound Through Pipeline Decisions |
| **Audience** | Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card III (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Shows how uncertainty propagates through a chain of attribution decisions, inspired by UProp (Duan 2025, arXiv:2506.17419v1). Each pipeline step produces an output that becomes the input to the next step — errors compound. The figure shows a concrete music attribution trajectory: ETL extraction → entity resolution → source corroboration → final score, with uncertainty widening or narrowing at each step based on what new evidence is introduced or what ambiguity is added. Communicates: "each pipeline step can amplify OR reduce uncertainty — we track the full decision trajectory so you know exactly where confidence was gained or lost."

Key concept from UProp: In agentic systems, uncertainty flows through decision trajectories (y₁→o₁→y₂→o₂→...→yₜ). Each step's output oᵢ conditions the next step's input. This means a wrong entity resolution can cascade through all downstream scoring.

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  DECISION TRAJECTORY FOR "HIDE AND SEEK" (Imogen Heap)   │
│                                                          │
│  ETL          ENTITY         SOURCE        FINAL         │
│  EXTRACT      RESOLVE        CORROBORATE   SCORE         │
│                                                          │
│  ╔═══╗        ╔══════╗       ╔════╗       ╔═════╗       │
│  ║   ║  y₁──> ║      ║ y₂──>║    ║ y₃──> ║     ║       │
│  ║   ║  o₁    ║      ║ o₂   ║    ║ o₃    ║  ●  ║       │
│  ║   ║        ║      ║      ║    ║       ║     ║       │
│  ╚═══╝        ╚══════╝      ╚════╝       ╚═════╝       │
│  ±0.05         ±0.15        ±0.08         ±0.10         │
│  narrow        WIDENS       narrows       final         │
│                                                          │
│  ▼ WHAT HAPPENS AT EACH STEP ▼                          │
│                                                          │
│  ETL: 5 sources → "Imogen Heap" vs "iMi" vs "I Megaphone"
│        uncertainty: LOW (data exists)                    │
│                                                          │
│  RESOLVE: Which variants are the same person?            │
│        uncertainty: SPIKES (fuzzy matching ambiguity)    │
│        ⚠ if wrong here, all downstream scores wrong     │
│                                                          │
│  CORROBORATE: 3/5 sources agree on songwriter credit     │
│        uncertainty: DROPS (source agreement)             │
│                                                          │
│  SCORE: 0.91 ± 0.10 final confidence                    │
│        composed of: data ±0.02 + model ±0.05 +          │
│        operational ±0.03                                 │
│                                                          │
│  ── uncertainty ribbon  ── point estimate                │
│  ⚠ cascade risk: error at step N invalidates N+1...     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Pipeline stages | `data_primary` | Four teal boxes connected by labeled arrows (y₁→o₁→y₂→o₂→y₃→o₃) |
| Uncertainty ribbons | `data_secondary` | Semi-transparent bands: narrow → wide → narrow → medium |
| Point estimate line | `line_accent` | Coral center line through the ribbon |
| Cascade warning | `data_error` | Orange warning icon at entity resolution (widest point) |
| Stage detail panel | `region_secondary` | Below the pipeline: concrete music example at each step |
| Uncertainty decomposition | `typography_mono` | Final score breakdown: data + model + operational components |
| Decision trajectory labels | `label_editorial` | y₁, o₁, y₂, o₂, y₃, o₃ on arrows between stages |
| Confidence intervals | `typography_mono` | ± values below each stage |
| Title | `typography_display` | Concrete track name as running example |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "DECISION TRAJECTORY", "HIDE AND SEEK", "ETL EXTRACT", "ENTITY RESOLVE", "SOURCE CORROBORATE", "FINAL SCORE", y₁/o₁/y₂/o₂/y₃/o₃ labels, confidence intervals, stage descriptions, uncertainty decomposition, cascade warning.

## Alt Text

Horizontal pipeline showing uncertainty propagation through four music attribution stages for "Hide and Seek" by Imogen Heap. Each stage is a teal box connected by decision trajectory arrows (y₁→o₁→y₂→o₂→y₃→o₃). Uncertainty ribbons widen at entity resolution (where fuzzy name matching creates ambiguity), narrow at source corroboration (where 3 of 5 sources agree), and settle at the final score of 0.91 ± 0.10. An orange cascade warning highlights that errors at entity resolution invalidate all downstream scores. Below the pipeline, each step is explained with concrete music examples: variant names being resolved, source agreement counts, and the final uncertainty decomposition into data, model, and operational components.
