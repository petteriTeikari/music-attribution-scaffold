# fig-theory-11: Confidence vs Uncertainty -- ELI5 (Weather Analogy)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-11 |
| **Title** | Confidence vs Uncertainty -- ELI5 (Weather Analogy) |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction -- no code, everyday analogy) |
| **Location** | docs/theory/confidence-scoring.md, README.md theory section |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure introduces the difference between a point estimate ("80% confident") and an interval estimate ("70-90% confident") using weather forecasting as the analogy. It answers: "Why does this system give a range instead of just a single number?"

The key message is: "A single confidence number hides uncertainty -- a range tells you how much the system actually knows, just like '70-90% chance of rain' is more honest than '80% chance of rain.'"

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  CONFIDENCE vs UNCERTAINTY                                     |
|  ■ Why Ranges Are More Honest Than Numbers                     |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. POINT ESTIMATE            |  II. INTERVAL ESTIMATE         |
|  ─────────────────            |  ──────────────────            |
|  (What most systems give)     |  (What THIS system gives)      |
|                               |                               |
|  ┌─────────────────────┐     |  ┌─────────────────────┐      |
|  │                     │     |  │                     │      |
|  │  WEATHER APP:       │     |  │  WEATHER APP:       │      |
|  │                     │     |  │                     │      |
|  │     ☁ 80%           │     |  │     ☁ 70-90%        │      |
|  │  "chance of rain"   │     |  │  "chance of rain"   │      |
|  │                     │     |  │                     │      |
|  │  Sounds precise.    │     |  │  More honest.       │      |
|  │  But HOW SURE       │     |  │  Tells you the      │      |
|  │  is the 80%?        │     |  │  system's actual    │      |
|  │                     │     |  │  knowledge.         │      |
|  └─────────────────────┘     |  └─────────────────────┘      |
|                               |                               |
|  ┌─────────────────────┐     |  ┌─────────────────────┐      |
|  │                     │     |  │                     │      |
|  │  ATTRIBUTION:       │     |  │  ATTRIBUTION:       │      |
|  │                     │     |  │                     │      |
|  │  "Composer:         │     |  │  "Composer:         │      |
|  │   Imogen Heap"      │     |  │   Imogen Heap"      │      |
|  │   Confidence: 0.85  │     |  │   Confidence:       │      |
|  │                     │     |  │   0.78 - 0.92       │      |
|  │  Is that good? Bad? │     |  │                     │      |
|  │  Depends on what    │     |  │  Narrow range =     │      |
|  │  you don't know.    │     |  │  system is sure.    │      |
|  │                     │     |  │  Wide range =       │      |
|  │                     │     |  │  more evidence      │      |
|  │                     │     |  │  needed.            │      |
|  └─────────────────────┘     |  └─────────────────────┘      |
|                               |                               |
+-------------------------------+-------------------------------+
|  ■ Narrow interval = "We're pretty sure."                      |
|    Wide interval = "We need more evidence."                    |
|    Both are more useful than a single number.                  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "CONFIDENCE vs UNCERTAINTY" with coral accent square |
| Subtitle | `label_editorial` | "Why Ranges Are More Honest Than Numbers" |
| Left panel header | `section_numeral` | "I. POINT ESTIMATE" with "(What most systems give)" |
| Right panel header | `section_numeral` | "II. INTERVAL ESTIMATE" with "(What THIS system gives)" |
| Weather: point estimate | `problem_statement` | Cloud icon with "80%" -- precise but uninformative about uncertainty |
| Weather: interval estimate | `solution_component` | Cloud icon with "70-90%" -- honest about uncertainty |
| Attribution: point estimate | `problem_statement` | "Confidence: 0.85" with "Is that good?" question |
| Attribution: interval estimate | `solution_component` | "Confidence: 0.78-0.92" with narrow/wide range explanation |
| Confidence values | `data_mono` | 0.85, 0.78-0.92 in monospace |
| Vertical divider | `accent_line_v` | Coral red vertical line between panels |
| Footer callout | `callout_box` | Narrow = sure, wide = need evidence, both better than single number |

## Anti-Hallucination Rules

1. The weather analogy uses 80% (point) and 70-90% (interval) -- do NOT change these specific values.
2. Attribution example uses "Imogen Heap" as the artist name -- this is the project's persona. Do NOT use a different name.
3. Point estimate example: 0.85. Interval example: 0.78-0.92. Do NOT change these values.
4. Do NOT use the term "conformal prediction" -- that is for fig-theory-12 (L4 audience).
5. Do NOT include mathematical formulas, Greek letters, or statistical notation.
6. The message is that intervals are MORE HONEST, not that point estimates are wrong.
7. Do NOT reference specific weather services or attribution products.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Split panel comparing point estimate (80 percent rain, 0.85 confidence) with interval estimate (70-90 percent rain, 0.78-0.92 confidence), showing intervals are more honest about uncertainty.
