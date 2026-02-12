# fig-topic-04: Conformal Prediction, Selective Prediction & SConU

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-04 |
| **Title** | From Coverage Guarantees to Risk-Aware Abstention |
| **Audience** | Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card IV (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Three-layer infographic distinguishing conformal prediction (coverage sets), selective prediction (abstention gate), and SConU (their principled synthesis via conformal p-values). Shows how the user-controllable risk parameter α operationalizes the human attributer's risk tolerance. Communicates: "conformal prediction provides coverage guarantees, selective prediction adds the ability to abstain, and SConU unifies both so the abstention decision is itself statistically principled — and the artist controls how cautious the system is."

Key concepts from Li et al. (arXiv:2504.14154):
- Standard conformal prediction fails silently when exchangeability is violated
- SConU adds a hypothesis test: if a sample's uncertainty deviates from calibration data, abstain
- The conformal p-value test makes the abstention decision itself distribution-free
- α (risk level) is user-controllable: cautious archivist → low α; discovery platform → high α

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  THREE LAYERS — NOT THE SAME THING                       │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ LAYER 1: CONFORMAL PREDICTION                    │    │
│  │                                                   │    │
│  │    ╭───────────────╮                              │    │
│  │  ╭─╯ {Heap, iMi,   ╰─╮   coverage: 1−α = 90%   │    │
│  │  │    Frou Frou}      │   "true answer is in     │    │
│  │  ╰─╮       ●       ╭─╯    this set 90% of time" │    │
│  │    ╰───────────────╯                              │    │
│  │  Guarantee: IF exchangeability holds              │    │
│  │  Problem: fails silently when it doesn't          │    │
│  └─────────────────────────────────────────────────┘    │
│                    ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │ LAYER 2: SELECTIVE PREDICTION (ABSTENTION GATE)  │    │
│  │                                                   │    │
│  │  ── ── ── ABSTENTION THRESHOLD ── ── ──          │    │
│  │  above: system answers     below: → HUMAN REVIEW │    │
│  │  General idea: "refuse when uncertain"            │    │
│  │  Problem: where to set the threshold?             │    │
│  └─────────────────────────────────────────────────┘    │
│                    ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │ LAYER 3: SConU (PRINCIPLED SYNTHESIS)            │    │
│  │                                                   │    │
│  │  Conformal p-value test:                          │    │
│  │  p = (1 + Σ 𝟙{uᵢ ≥ u_test}) / (N+1)            │    │
│  │  if p ≤ δ → ABSTAIN (exchangeability violated)   │    │
│  │  if p > δ → PREDICT (coverage guarantee holds)   │    │
│  │                                                   │    │
│  │  The abstention decision IS conformal             │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  USER-CONTROLLABLE RISK: α SLIDER                       │
│  ◄──────────────●────────────────────────►              │
│  α=0.05         α=0.10              α=0.20              │
│  CAUTIOUS        DEFAULT            TOLERANT             │
│  ARCHIVIST                          DISCOVERY            │
│  (more abstain,   (balanced)        (fewer abstain,     │
│   larger sets)                       smaller sets)       │
│                                                          │
│  ■ COVERAGE SET  ■ ABSTAIN ZONE  ◄► RISK SLIDER       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Layer 1 box | `data_primary` | Teal panel — conformal prediction with coverage arc |
| Layer 2 box | `data_warning` | Orange panel — selective prediction with threshold line |
| Layer 3 box | `data_accent` | Coral panel — SConU synthesis with p-value formula |
| Coverage arc | `data_primary` | Teal concentric band around point estimate |
| Point estimate | `data_accent` | Coral dot at center of coverage arc |
| Abstention threshold | `line_warning` | Dashed line separating predict/abstain zones |
| P-value formula | `typography_mono` | SConU conformal p-value equation |
| Risk slider | `region_interactive` | Horizontal slider showing α from 0.05 to 0.20 |
| Persona labels | `label_editorial` | "CAUTIOUS ARCHIVIST" vs "DISCOVERY PLATFORM" |
| Downward arrows | `line_flow` | Connecting Layer 1 → 2 → 3 |
| Music example | `data_accent` | {Heap, iMi, Frou Frou} as concrete prediction set |
| Legend | `label_editorial` | ALL-CAPS labels with markers |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "THREE LAYERS", "CONFORMAL PREDICTION", "SELECTIVE PREDICTION", "ABSTENTION GATE", "SConU", "PRINCIPLED SYNTHESIS", coverage formula (1−α = 90%), p-value formula, "ABSTAIN", "PREDICT", "HUMAN REVIEW", α values (0.05, 0.10, 0.20), "CAUTIOUS ARCHIVIST", "DISCOVERY PLATFORM", music example names, "COVERAGE SET", "ABSTAIN ZONE", "RISK SLIDER".

## Alt Text

Three-layer infographic distinguishing conformal prediction, selective prediction, and SConU. Layer 1 (teal): conformal prediction shown as a concentric arc around a point estimate, producing prediction sets like {Heap, iMi, Frou Frou} with 90% coverage guarantee, noting it fails silently when exchangeability is violated. Layer 2 (orange): selective prediction as an abstention gate with a threshold line — above it the system answers, below it routes to human review, but the threshold placement is unprincipled. Layer 3 (coral): SConU as the principled synthesis, using conformal p-values to make the abstention decision itself distribution-free. At the bottom, a risk slider shows the user-controllable α parameter ranging from 0.05 (cautious archivist: more abstentions, larger sets) to 0.20 (discovery platform: fewer abstentions, smaller sets).
