# fig-domain-01: The Attribution Crisis

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-domain-01 |
| **Title** | The Attribution Crisis: Why 40%+ of Music Metadata is Wrong |
| **Audience** | Domain (music industry professionals) |
| **Complexity** | L1 (concept explanation) |
| **Location** | docs/prd/vision-v1.md, README.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |

## Purpose

Explain the music attribution crisis to industry professionals: why metadata is broken, what it costs, and why existing solutions fail.

## Key Message

"40%+ of music metadata is incorrect or incomplete, causing billions in lost royalties and enabling unauthorized AI training—because no single source has the complete picture."

## Visual Concept

Problem-focused infographic showing data silos, statistics, and consequences.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  THE ATTRIBUTION CRISIS                                                      │
│  Why 40%+ of Music Metadata is Wrong                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  THE PROBLEM: DATA SILOS                        THE COST                    │
│  ──────────────────────────                     ────────                    │
│                                                                             │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐       ┌─────────────────────────┐  │
│   │ Labels  │  │Streaming│  │ Rights  │       │                         │  │
│   │   DB    │  │Platforms│  │ Orgs    │       │  $2.5B+ annually        │  │
│   │  (30%)  │  │  (40%)  │  │  (25%)  │       │  in unclaimed royalties │  │
│   └────┬────┘  └────┬────┘  └────┬────┘       │                         │  │
│        │            │            │            │  Independent artists     │  │
│        └────────────┼────────────┘            │  hit hardest             │  │
│              NO SINGLE SOURCE                 │                         │  │
│              HAS COMPLETE DATA                └─────────────────────────┘  │
│                                                                             │
│  WHO SUFFERS                                   AI MAKES IT WORSE           │
│  ──────────                                    ────────────────            │
│                                                                             │
│   👤 Artists: Can't prove credits             AI platforms train on        │
│   🎵 Producers: Ghost credits                 music without consent        │
│   🏢 Labels: Compliance headaches             because attribution          │
│   📱 Platforms: Legal exposure                data doesn't exist           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  "The industry has dozens of databases, but none of them talk to each      │
│   other. Every time a song crosses a border, attribution gets lost."       │
│                                                    — Industry Expert        │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Labels DB | `problem_statement` | Partial data (30%) |
| Streaming Platforms | `problem_statement` | Partial data (40%) |
| Rights Orgs | `problem_statement` | Partial data (25%) |
| Cost Statistic | `stakeholder_artist` | $2.5B+ lost |
| AI Problem | `problem_statement` | Unauthorized training |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Labels | Center | Dashed | "incomplete" |
| Streaming | Center | Dashed | "incomplete" |
| Rights | Center | Dashed | "incomplete" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Quote | "The industry has dozens of databases..." | Bottom |

## Text Content

### Labels (Max 30 chars each)

- "Labels Database (30%)"
- "Streaming Platforms (40%)"
- "Rights Organizations (25%)"
- "$2.5B+ unclaimed annually"
- "Independent artists hit hardest"
- "No consent for AI training"
- "Ghost credits"
- "Attribution lost at borders"

### Caption (for embedding)

The attribution crisis: music metadata is fragmented across dozens of databases with no single source of truth. This causes $2.5B+ in unclaimed royalties annually, with independent artists hit hardest. AI platforms compound the problem by training on music without proper attribution or consent.

## Prompts for Nano Banana Pro

### Style Prompt

Problem-focused infographic on warm off-white background (#F8F6F0).
Economist-style data visualization, professional and serious tone.
Use muted reds and grays for problem elements, amber for warnings.
Clean sans-serif typography, clear information hierarchy.
Data silos shown as disconnected boxes, statistics prominently displayed.
Quote callout at bottom with attribution line.

### Content Prompt

Create an attribution crisis infographic:
- TOP: Title "The Attribution Crisis" with subtitle
- LEFT PANEL: Three database silos (Labels 30%, Streaming 40%, Rights 25%)
  - Shown as disconnected boxes with dashed lines
  - "NO SINGLE SOURCE HAS COMPLETE DATA" label
- TOP RIGHT: Cost statistics
  - "$2.5B+ annually in unclaimed royalties"
  - "Independent artists hit hardest"
- BOTTOM LEFT: "Who Suffers" list
  - Artists, Producers, Labels, Platforms with brief pain points
- BOTTOM RIGHT: "AI Makes It Worse" section
  - AI training without consent because attribution data doesn't exist
- BOTTOM: Quote callout with industry expert quote

### Refinement Notes

- Should feel urgent but not alarmist
- Statistics should be prominently displayed
- Data silos should look disconnected/fragmented
- Target audience: music industry decision-makers

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "domain-01",
    "title": "The Attribution Crisis",
    "audience": "domain"
  },
  "content_architecture": {
    "primary_message": "40%+ of music metadata is wrong because no single source has the complete picture",
    "layout_flow": "quad-panel",
    "key_structures": [
      {
        "name": "Labels Database",
        "role": "problem_statement",
        "is_highlighted": false,
        "labels": ["30% coverage", "Incomplete"]
      },
      {
        "name": "Streaming Platforms",
        "role": "problem_statement",
        "is_highlighted": false,
        "labels": ["40% coverage", "Siloed"]
      },
      {
        "name": "Rights Organizations",
        "role": "problem_statement",
        "is_highlighted": false,
        "labels": ["25% coverage", "Fragmented"]
      },
      {
        "name": "Lost Royalties",
        "role": "stakeholder_artist",
        "is_highlighted": true,
        "labels": ["$2.5B+ annually", "Indies hit hardest"]
      },
      {
        "name": "AI Problem",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["Training without consent", "No attribution data"]
      }
    ],
    "callout_boxes": [
      {
        "heading": "INDUSTRY QUOTE",
        "body_text": "The industry has dozens of databases, but none of them talk to each other.",
        "position": "bottom-full-width"
      }
    ]
  }
}
```

## Alt Text

Attribution crisis infographic: three disconnected database silos (Labels 30%, Streaming 40%, Rights Orgs 25%) illustrate fragmented metadata. Statistics show $2.5B+ in unclaimed royalties annually. Stakeholder impacts listed for artists, producers, labels, platforms. AI section highlights training without consent.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
