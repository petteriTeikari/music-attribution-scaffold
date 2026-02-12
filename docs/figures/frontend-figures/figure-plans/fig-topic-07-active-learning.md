# fig-topic-07: Active Learning & Feedback Cards

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-07 |
| **Title** | Active Learning — Decision Boundary & Human-in-the-Loop |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card VII (Pipeline & Data group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Decision boundary visualization where uncertain points near the boundary are actively selected for human review. Communicates: "human expertise is directed where it adds the most value."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ● ●        ── decision boundary     │
│  ● ●  ●   /                         │
│  ●    ○  /  ○                        │
│       ○ /  ○ ○                       │
│      ──/──────                       │
│       / ○  ○ ○                       │
│      /   ○                           │
│     /  ○  ○ ○                        │
│                                      │
│  ● auto-approved (confident)         │
│  ○ selected for review (uncertain)   │
│  ──→ boundary shifts with feedback   │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Confident points | `data_primary` | Teal filled circles, far from boundary |
| Uncertain points | `data_warning` | Orange hollow circles, near boundary |
| Decision boundary | `line_accent` | Coral diagonal line |
| Boundary shift arrow | `line_flow` | Navy arrow showing boundary movement |
| Labels | `label_editorial` | ALL-CAPS "AUTO-APPROVED" / "HUMAN REVIEW" |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "ACTIVE LEARNING", "AUTO-APPROVED", "HUMAN REVIEW", "DECISION BOUNDARY", "FEEDBACK".

## Alt Text

Scatter plot with a diagonal decision boundary in coral. Teal filled points far from the boundary are auto-approved. Orange hollow points near the boundary are actively selected for human review. An arrow shows the boundary shifting as feedback accumulates.
