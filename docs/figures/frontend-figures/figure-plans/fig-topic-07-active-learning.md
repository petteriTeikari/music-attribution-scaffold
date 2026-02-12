# fig-topic-07: Active Learning for Music Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-07 |
| **Title** | Active Learning — Saving Artist Time Through Smart Review Prioritization |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card VII (Pipeline & Data group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Contextualizes active learning specifically for music attribution workflow: an artist like Imogen Heap has 200 tracks needing attribution review. Instead of reviewing all 200, the system identifies the 30 tracks where human judgment adds the most value (near the decision boundary), auto-approves the 170 confident ones, and *learns from each review to improve future routing*. The agentic UI (PostHog analytics) observes which corrections the artist makes and adapts its confidence thresholds. Communicates: "we direct your expertise to where it matters most — and the system gets smarter with every review you do."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  ARTIST'S CATALOG: 200 TRACKS                            │
│  ─────────────────────────────                          │
│                                                          │
│  ┌──── AUTO-APPROVED (170) ──┐  ┌── REVIEW QUEUE (30)─┐│
│  │  ●●●●●●●●●●●●●●●●●●●●   │  │  ○ "Mic'd Up" 0.52  ││
│  │  ●●●●●●●●●●●●●●●●●●●●   │  │  ○ "Aha!" remix 0.48││
│  │  ●●●●●●●●●●●●●●●●●●●●   │  │  ○ "Blanket" 0.61   ││
│  │  High confidence (>0.85)  │  │  ○ "Tidal" 0.55     ││
│  │  "Hide and Seek" 0.95     │  │  ...26 more         ││
│  │  "Headlock" 0.91          │  │                      ││
│  │  "Goodnight & Go" 0.88   │  │  Near decision       ││
│  │                           │  │  boundary (0.45-0.70)││
│  └───────────────────────────┘  └──────────────────────┘│
│                                                          │
│  ── DECISION BOUNDARY ──                                │
│  shifts with each artist review                         │
│                                                          │
│  FEEDBACK LOOP (how the system learns)                  │
│  ─────────────────────────────────────                  │
│                                                          │
│  ① Artist reviews "Mic'd Up" → corrects producer credit │
│  ② PostHog records: correction type, time spent, pattern│
│  ③ Model updates: similar producer credits flagged more │
│  ④ Next batch: fewer reviews needed (25 → 20 → 15...)  │
│                                                          │
│  RESULT: 200-track catalog reviewed in ~2 hours          │
│  (vs ~12 hours reviewing every track manually)           │
│                                                          │
│  ●  AUTO-APPROVED    ○  REVIEW QUEUE                    │
│  ──→ BOUNDARY SHIFT  ①②③④ FEEDBACK LOOP                │
│                                                          │
│  TIME SAVED PER REVIEW CYCLE                            │
│  ████████████████████░░░░  85% auto  15% human         │
│  ██████████████████████░░  90% auto  10% human (iter 2)│
│  ████████████████████████  95% auto   5% human (iter 3)│
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Catalog overview | `region_secondary` | "200 TRACKS" with split into auto-approved and review queue |
| Auto-approved block | `data_primary` | Teal filled circles with example tracks and high confidence scores |
| Review queue block | `data_warning` | Orange hollow circles with borderline tracks and scores |
| Decision boundary | `line_accent` | Coral horizontal line that shifts with feedback |
| Feedback loop steps | `data_accent` | Numbered ①②③④ cycle: review → PostHog → model update → fewer reviews |
| Time savings bars | `data_gradient` | Progressive improvement bars: 85% → 90% → 95% auto-approved |
| Concrete track names | `label_editorial` | Real Imogen Heap tracks with confidence scores |
| Result callout | `typography_display` | "~2 hours vs ~12 hours" comparison |
| PostHog reference | `label_subtle` | Analytics integration for behavior tracking |
| Boundary shift arrow | `line_flow` | Arrow showing boundary movement with each iteration |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "ACTIVE LEARNING", "200 TRACKS", "AUTO-APPROVED", "REVIEW QUEUE", "DECISION BOUNDARY", track names with confidence scores, "FEEDBACK LOOP" with steps ①②③④, time comparison, time savings percentages, "BOUNDARY SHIFT".

## Alt Text

Active learning infographic contextualized for music attribution. An artist's 200-track catalog is split: 170 high-confidence tracks (teal, auto-approved with examples like "Hide and Seek" at 0.95) and 30 near-boundary tracks routed to a review queue (orange, with examples like "Mic'd Up" at 0.52). A coral decision boundary separates them and shifts with each review. Below, a numbered feedback loop shows how the system learns: the artist corrects a producer credit, PostHog records the correction pattern, the model updates, and the next batch needs fewer reviews. Progressive time savings bars show auto-approval rates improving from 85% to 90% to 95% across iterations, reducing a 12-hour manual review to approximately 2 hours.
