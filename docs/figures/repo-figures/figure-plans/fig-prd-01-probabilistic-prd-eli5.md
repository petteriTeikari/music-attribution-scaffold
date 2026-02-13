# fig-prd-01: Probabilistic PRD -- What Is It?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-01 |
| **Title** | Probabilistic PRD -- What Is It? |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction) |
| **Location** | docs/prd/decisions/REPORT.md, README.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the core concept of a probabilistic PRD to non-technical audiences. A traditional PRD says "we will use X." A probabilistic PRD says "we will probably use X (60%), but Y (25%) and Z (15%) are viable depending on your team." This figure must make the concept click in 5 seconds for someone who has never seen a decision network.

The key message is: "A probabilistic PRD is a decision tree where every branch has a weight -- not a fixed spec, but a map of weighted options that adapts to your team."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  PROBABILISTIC PRD                                             |
|  ■ Decisions with Weights, Not Fixed Specs                     |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. TRADITIONAL PRD           |  II. PROBABILISTIC PRD        |
|  ─────────────────            |  ──────────────────           |
|                               |                               |
|  "We will use PostgreSQL"     |  PostgreSQL     ████████ 60%  |
|                               |  Supabase       ████     25%  |
|  One answer.                  |  SQLite         ██       15%  |
|  One team.                    |                               |
|  No flexibility.              |  Multiple paths.              |
|                               |  Weighted by your team.       |
|  ┌───────────────────┐       |  Adapts to constraints.       |
|  │   THE ANSWER      │       |                               |
|  │   PostgreSQL      │       |  ┌───── Engineer Team ──────┐ |
|  │   (take it or     │       |  │ PostgreSQL 60%           │ |
|  │    leave it)      │       |  └──────────────────────────┘ |
|  └───────────────────┘       |  ┌───── Musician Team ──────┐ |
|                               |  │ Supabase 55%            │ |
|                               |  └──────────────────────────┘ |
|                               |  ┌───── Solo Hacker ────────┐ |
|                               |  │ SQLite 40%               │ |
|                               |  └──────────────────────────┘ |
+-------------------------------+-------------------------------+
|  "Same decision, different teams, different best answers"      |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "PROBABILISTIC PRD" in display type with coral accent square |
| Subtitle | `label_editorial` | "Decisions with Weights, Not Fixed Specs" |
| Traditional panel (left) | `problem_zone` | Single-answer PRD, rigid, one-size-fits-all |
| Probabilistic panel (right) | `solution_zone` | Weighted options with probability bars |
| Probability bars | `data_mono` | Horizontal bars showing 60% / 25% / 15% splits |
| Team archetype cards | `archetype_overlay` | Three mini-cards showing different teams picking different options |
| Roman numerals I/II | `section_numeral` | Panel headers in editorial style |
| Vertical divider | `accent_line_v` | Coral red vertical line separating panels |
| Footer insight | `callout_bar` | "Same decision, different teams, different best answers" |

## Anti-Hallucination Rules

1. The probability example uses the PRIMARY DATABASE decision -- PostgreSQL 60%, Supabase 25%, SQLite 15% for engineer-heavy archetype. These are APPROXIMATE from the actual archetype weights.
2. The four team archetypes are: Engineer-Heavy Startup, Musician-First Team, Solo Hacker, Well-Funded Startup. Do not invent others.
3. This is an ELI5 figure -- NO code, NO technical jargon, NO database internals.
4. The repo is a SCAFFOLD, not a deployed product.
5. Do NOT show more than 3 options in the probability bars -- keep it simple for L1 audience.
6. Background must be warm cream (#f6f3e6).

## Alt Text

Split-panel comparison: left shows traditional PRD with one fixed answer, right shows probabilistic PRD with weighted options that adapt to different team types.
