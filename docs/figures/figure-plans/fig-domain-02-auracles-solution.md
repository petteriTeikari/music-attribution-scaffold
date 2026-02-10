# fig-domain-02: Attribution Solution Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-domain-02 |
| **Title** | How the system Solves the Attribution Crisis |
| **Audience** | Domain (music industry professionals) |
| **Complexity** | L1 (concept explanation) |
| **Location** | docs/prd/vision-v1.md, README.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |

## Purpose

Show how the system solves the attribution crisis through multi-source aggregation, transparent confidence, and artist-controlled identity.

## Key Message

"the system cross-references multiple sources to build complete attribution with transparent confidence levels—giving artists control over their identity and AI permissions."

## Visual Concept

Before/after comparison or solution-focused diagram showing the system' key components.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HOW ATTRIBUTION SOLVES THE ATTRIBUTION CRISIS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────┐   ┌───────────────────────────────────┐ │
│  │        THE PROBLEM            │   │        THE SOLUTION               │ │
│  │        (Before)               │   │        (the system)                 │ │
│  ├───────────────────────────────┤   ├───────────────────────────────────┤ │
│  │                               │   │                                   │ │
│  │  ❌ Data silos               │   │  ✓ Multi-source aggregation      │ │
│  │  ❌ Hidden confidence        │   │  ✓ Transparent A0-A3 levels      │ │
│  │  ❌ No artist control        │   │  ✓ Artist-controlled identity    │ │
│  │  ❌ AI trains without consent│   │  ✓ Explicit AI permissions       │ │
│  │                               │   │                                   │ │
│  └───────────────────────────────┘   └───────────────────────────────────┘ │
│                                                                             │
│  FOUR PILLARS OF ATTRIBUTION                                                   │
│  ─────────────────────────                                                  │
│                                                                             │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│   │  AGGREGATE  │  │ CONFIDENCE  │  │  IDENTITY   │  │     AI      │      │
│   │             │  │             │  │             │  │ PERMISSIONS │      │
│   │ Cross-ref   │  │ A0-A3       │  │ Artist ID  │  │             │      │
│   │ Discogs,    │  │ levels show │  │ artist-     │  │ MCP-based   │      │
│   │ MusicBrainz,│  │ exactly how │  │ controlled  │  │ consent     │      │
│   │ + more      │  │ sure we are │  │ canonical   │  │ management  │      │
│   └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  RESULT: Complete attribution with verifiable confidence and artist control │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Problem Panel | `problem_statement` | Current state (red/gray) |
| Solution Panel | `solution_component` | The System benefits (green/blue) |
| Aggregate Pillar | `source_system` | Multi-source cross-ref |
| Confidence Pillar | `attribution_verified` | A0-A3 transparency |
| Identity Pillar | `benefit_artist` | Artist ID |
| AI Permissions Pillar | `benefit_platform` | MCP consent |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Problem | Solution | Transform | "The system enables" |
| Four Pillars | Result | Support | "together deliver" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "RESULT" | Complete attribution with verifiable confidence and artist control | Bottom |

## Text Content

### Labels (Max 30 chars each)

- "Multi-source aggregation"
- "Transparent A0-A3 levels"
- "Artist-controlled identity"
- "Explicit AI permissions"
- "Artist ID"
- "MCP-based consent"
- "Cross-reference sources"
- "Show confidence clearly"

### Caption (for embedding)

How the system solves the attribution crisis: multi-source aggregation (Discogs, MusicBrainz, more), transparent A0-A3 confidence levels, artist-controlled canonical identity (Artist ID), and MCP-based AI permission management. Result: complete attribution with verifiable confidence and artist control.

## Prompts for Nano Banana Pro

### Style Prompt

Solution-focused infographic on warm off-white background (#F8F6F0).
Before/after comparison layout with clear visual distinction.
Problem side: muted grays and subtle reds (not alarming).
Solution side: deep blues and greens (confident, trustworthy).
Four pillars as equal-width columns below comparison.
Clean sans-serif typography, professional tone.

### Content Prompt

Create an the system solution infographic:
- TOP: Two-panel comparison
  - LEFT "THE PROBLEM": Gray/red tones, list of issues with X marks
    - Data silos, Hidden confidence, No artist control, AI without consent
  - RIGHT "THE SOLUTION": Blue/green tones, list of solutions with checkmarks
    - Multi-source aggregation, Transparent A0-A3, Artist identity, AI permissions
- MIDDLE: "FOUR PILLARS OF ATTRIBUTION" header
- BOTTOM: Four equal columns
  - AGGREGATE: Cross-reference Discogs, MusicBrainz, + more
  - CONFIDENCE: A0-A3 levels show exactly how sure we are
  - IDENTITY: Artist ID, artist-controlled canonical
  - AI PERMISSIONS: MCP-based consent management
- FOOTER: Result statement callout

### Refinement Notes

- Clear visual contrast between problem (left) and solution (right)
- Four pillars should feel balanced and foundational
- The system branding (deep blue) should be prominent
- Accessible to non-technical music industry readers

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "domain-02",
    "title": "How the system Solves the Attribution Crisis",
    "audience": "domain"
  },
  "content_architecture": {
    "primary_message": "the system cross-references sources for complete attribution with transparent confidence and artist control",
    "layout_flow": "comparison-then-pillars",
    "key_structures": [
      {
        "name": "Problem Panel",
        "role": "problem_statement",
        "is_highlighted": false,
        "labels": ["Data silos", "Hidden confidence", "No control", "AI without consent"]
      },
      {
        "name": "Solution Panel",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Multi-source", "Transparent A0-A3", "Artist identity", "AI permissions"]
      },
      {
        "name": "Aggregate Pillar",
        "role": "source_system",
        "is_highlighted": true,
        "labels": ["Cross-reference", "Multiple sources"]
      },
      {
        "name": "Confidence Pillar",
        "role": "attribution_verified",
        "is_highlighted": true,
        "labels": ["A0-A3 levels", "Transparent uncertainty"]
      },
      {
        "name": "Identity Pillar",
        "role": "benefit_artist",
        "is_highlighted": true,
        "labels": ["Artist ID", "Artist-controlled"]
      },
      {
        "name": "AI Permissions Pillar",
        "role": "benefit_platform",
        "is_highlighted": true,
        "labels": ["MCP-based", "Consent management"]
      }
    ],
    "callout_boxes": [
      {
        "heading": "RESULT",
        "body_text": "Complete attribution with verifiable confidence and artist control",
        "position": "bottom-full-width"
      }
    ]
  }
}
```

## Alt Text

The system solution infographic: before/after comparison shows problems (data silos, hidden confidence, no control) versus solutions (multi-source aggregation, transparent A0-A3 levels, artist identity, AI permissions). Four pillars: Aggregate, Confidence, Identity, AI Permissions.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
