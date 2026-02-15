# fig-landscape-04: AI Disruption Points in the Music Value Chain

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-04 |
| **Title** | AI Disruption Points in the Music Value Chain |
| **Audience** | L1 (Music Industry) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure maps the traditional music value chain and marks the five points where AI creates disruption, showing that each disruption point generates a corresponding attribution need. It answers: "Where exactly does AI disrupt the music industry, and why does each disruption point demand new attribution infrastructure?"

## Key Message

AI disrupts at 5 points in the music value chain (creation, distribution, discovery, licensing, royalty), and each disruption point creates a corresponding attribution need.

## Visual Concept

A horizontal value chain flows left-to-right across the top half of the figure, with six stages connected by thin arrows. Five disruption markers drop vertically from the chain, each leading to a corresponding attribution challenge box below. The chain is the stable anchor; the disruption markers are the visual tension. The layout reads like a timeline with vertical callouts.

```
+---------------------------------------------------------------+
|  AI DISRUPTION POINTS                                          |
|  ■ Five Fractures in the Music Value Chain                     |
+---------------------------------------------------------------+
|                                                                |
|  VALUE CHAIN                                                   |
|  ───────────                                                   |
|                                                                |
|  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐   ┌──────┐|
|  │Creation│──▶│Recordng│──▶│Distrib.│──▶│Discovry│──▶│Licens│||
|  └───┬────┘   └────────┘   └───┬────┘   └───┬────┘   └──┬───┘|
|      │                         │             │            │    |
|      ▼                         ▼             ▼            ▼    |
|  ┌────────┐               ┌────────┐   ┌────────┐   ┌──────┐ |
|  │AI gen. │               │AI dist.│   │AI rec. │   │AI lic│ |
|  │content │               │flood   │   │gatekeep│   │ambig.│ |
|  └───┬────┘               └───┬────┘   └───┬────┘   └──┬───┘ |
|      │                         │             │            │    |
|      ▼                         ▼             ▼            ▼    |
|  ┌────────┐               ┌────────┐   ┌────────┐   ┌──────┐ |
|  │Who made│               │What is │   │Who gets│   │What  │ |
|  │this?   │               │human?  │   │credit? │   │rights│ |
|  │■ ATTR. │               │■ ATTR. │   │■ ATTR. │   │exist?│ |
|  │ NEED   │               │ NEED   │   │ NEED   │   │■ ATTR│ |
|  └────────┘               └────────┘   └────────┘   └──────┘ |
|                                                                |
|                                          ┌────────┐            |
|                                          │Royalty │──▶ END     |
|                                          └───┬────┘            |
|                                              ▼                 |
|                                          ┌────────┐            |
|                                          │How to  │            |
|                                          │split?  │            |
|                                          │■ ATTR. │            |
|                                          └────────┘            |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "AI DISRUPTION POINTS"
    - type: label_editorial
      text: "Five Fractures in the Music Value Chain"

value_chain:
  position: [60, 160]
  width: 1800
  height: 80
  stages:
    - { label: "Creation", x: 60 }
    - { label: "Recording", x: 380 }
    - { label: "Distribution", x: 700 }
    - { label: "Discovery", x: 1020 }
    - { label: "Licensing", x: 1340 }
    - { label: "Royalty", x: 1620 }

disruption_creation:
  position: [60, 280]
  width: 300
  height: 280
  disruption: "AI-generated content"
  attribution_need: "Who made this?"

disruption_distribution:
  position: [700, 280]
  width: 300
  height: 280
  disruption: "AI content flood"
  attribution_need: "What is human-made?"

disruption_discovery:
  position: [1020, 280]
  width: 300
  height: 280
  disruption: "AI recommendation gatekeeping"
  attribution_need: "Who gets credit?"

disruption_licensing:
  position: [1340, 280]
  width: 300
  height: 280
  disruption: "AI licensing ambiguity"
  attribution_need: "What rights exist?"

disruption_royalty:
  position: [1620, 280]
  width: 300
  height: 280
  disruption: "AI royalty splitting"
  attribution_need: "How to split fairly?"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "AI DISRUPTION POINTS" with coral accent square |
| Subtitle | `label_editorial` | "Five Fractures in the Music Value Chain" |
| Value chain stages | `processing_stage` | Six horizontal boxes: Creation, Recording, Distribution, Discovery, Licensing, Royalty |
| Chain arrows | `data_flow` | Thin directional arrows connecting stages |
| Disruption markers | `problem_statement` | Five vertical callout boxes showing AI disruption type |
| Attribution need boxes | `solution_component` | Five boxes below disruptions showing the corresponding attribution question |
| Vertical drop arrows | `data_flow` | Arrows from chain stages down to disruption markers |
| Attribution need labels | `badge_label` | "ATTR. NEED" badges on bottom boxes |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Creation | AI-generated content | disrupts | "AI can create from scratch" |
| Distribution | AI content flood | disrupts | "Volume overwhelms curation" |
| Discovery | AI recommendation | disrupts | "Algorithms decide visibility" |
| Licensing | AI licensing ambiguity | disrupts | "Training rights unclear" |
| Royalty | AI royalty splitting | disrupts | "No formula for AI contribution" |
| Each disruption | Each attribution need | creates | "Generates attribution question" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Creation disruption | "AI-generated content: who made this?" | Below Creation stage |
| Distribution disruption | "AI content flood: what is human-made?" | Below Distribution stage |
| Discovery disruption | "AI gatekeeping: who gets credit?" | Below Discovery stage |
| Licensing disruption | "AI ambiguity: what rights exist?" | Below Licensing stage |
| Royalty disruption | "AI splitting: how to divide fairly?" | Below Royalty stage |

## Text Content

### Labels (Max 30 chars each)

- AI DISRUPTION POINTS
- Five Fractures in the Chain
- Creation
- Recording
- Distribution
- Discovery
- Licensing
- Royalty
- AI-generated content
- AI content flood
- AI recommendation gatekeeping
- AI licensing ambiguity
- AI royalty splitting
- Who made this?
- What is human-made?
- Who gets credit?
- What rights exist?
- How to split fairly?

### Caption (for embedding in documentation)

AI disrupts the music value chain at five points: creation (AI-generated content raises authorship questions), distribution (content flood obscures human work), discovery (algorithmic gatekeeping determines credit), licensing (training rights are ambiguous), and royalty distribution (no formula for AI contribution splits). Each disruption creates a corresponding attribution need.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. There are exactly 6 value chain stages and 5 disruption points -- Recording has no AI disruption marker in this figure.
2. Do NOT name specific AI companies or platforms at the disruption points.
3. The value chain is SIMPLIFIED -- real music industry chains are more complex. Do NOT add stages.
4. Attribution needs are phrased as QUESTIONS, not solutions -- keep the question format.
5. Arrows should be thin and elegant, not thick block arrows.
6. Disruption markers should feel like fracture points, not additions -- they represent breaks in the chain.
7. Do NOT imply that AI is entirely negative -- disruption creates both problems and opportunities.
8. The "Recording" stage has no disruption marker because AI recording tools are augmentative, not disruptive to attribution.

## Alt Text

Music value chain with five AI disruption points, each creating a corresponding attribution question below.

## JSON Export Block

```json
{
  "id": "fig-landscape-04",
  "title": "AI Disruption Points in the Music Value Chain",
  "audience": "L1",
  "priority": "P1",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "value_chain_stages": [
    "Creation", "Recording", "Distribution", "Discovery", "Licensing", "Royalty"
  ],
  "disruption_points": [
    { "stage": "Creation", "disruption": "AI-generated content", "attribution_need": "Who made this?" },
    { "stage": "Distribution", "disruption": "AI content flood", "attribution_need": "What is human-made?" },
    { "stage": "Discovery", "disruption": "AI recommendation gatekeeping", "attribution_need": "Who gets credit?" },
    { "stage": "Licensing", "disruption": "AI licensing ambiguity", "attribution_need": "What rights exist?" },
    { "stage": "Royalty", "disruption": "AI royalty splitting", "attribution_need": "How to split fairly?" }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage", "data_flow",
    "problem_statement", "solution_component", "badge_label"
  ]
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
