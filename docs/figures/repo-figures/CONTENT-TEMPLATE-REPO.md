# Figure Content Specification Template -- Repository Documentation

**Version:** 1.0.0
**Purpose:** Define WHAT a repo documentation figure shows (content), not HOW it looks (style).
**Style Reference:** See `STYLE-GUIDE-REPO.md` for all visual specifications.
**Domain:** Music attribution with transparent confidence scoring.

---

## Key Principle: Content/Style Decoupling

Content specs use **semantic tags** (not colors or fonts). The STYLE-GUIDE-REPO.md maps semantic tags to visual properties.

**DO write:** `role: "etl_extract"`
**DO NOT write:** `color: "#1E3A5F"` or `font: "Instrument Serif"`

---

## Figure Type Decision

| Your Figure Has... | Recommended Tool | Use This Template? |
|--------------------|------------------|-------------------|
| Pipeline architecture | **Nano Banana Pro** | YES |
| Module relationships | **Nano Banana Pro** | YES |
| Decision trees (PRD nodes) | **Nano Banana Pro** | YES |
| Before/after comparisons | **Nano Banana Pro** | YES |
| Confidence scoring walkthrough | **Nano Banana Pro** | YES |
| Archetype comparison | **Nano Banana Pro** | YES |
| Simple hierarchy diagrams | **Mermaid** | NO -- use diagram code |
| Tables with exact data | **Markdown tables** | NO |
| Precise code architecture | **Mermaid** | NO -- use diagram code |

---

## Complexity Levels

Every figure targets one audience complexity level. This determines vocabulary, abstraction, and detail density.

| Level | Audience | Vocabulary | Abstraction | Detail |
|-------|----------|-----------|-------------|--------|
| **L1** | Music Industry Professional | Business terms, no code | High -- conceptual | Low -- big picture only |
| **L2** | PhD Student / Policy Researcher | Academic terms, light technical | Medium -- structural | Medium -- named components |
| **L3** | Software Engineer | Code terms, API references | Low -- implementation | High -- module-level |
| **L4** | AI/ML Architect | ML terms, statistical concepts | Low -- algorithmic | High -- mathematical detail |

### Level-Specific Guidelines

**L1 -- Music Industry Professional:**
- Use "credits" not "attribution records"
- Use "trust level" not "assurance tier"
- Use "how sure" not "confidence score"
- NO: code identifiers, database names, protocol acronyms
- YES: dollar amounts, percentage improvements, real-world analogies

**L2 -- PhD Student / Policy Researcher:**
- Use "assurance levels A0-A3" with plain-English definitions
- Use "provenance tracking" with brief context
- Reference regulatory frameworks (EU AI Act, DSA) by name
- NO: function signatures, SQL schemas, Docker commands
- YES: citation-style references, formal definitions, taxonomy names

**L3 -- Software Engineer:**
- Use module names (`music_attribution.etl`, `music_attribution.resolution`)
- Reference specific tools and libraries (Splink, pgvector, FastAPI)
- Show API contracts and data flow directions
- NO: mathematical notation, academic citations
- YES: endpoint paths, Pydantic model names, database table references

**L4 -- AI/ML Architect:**
- Use statistical terms (conformal prediction, Bayesian updating, calibration)
- Reference model architectures and loss functions
- Show confidence intervals and uncertainty propagation
- NO: business justification, regulatory context
- YES: formal notation, algorithm pseudocode, mathematical relationships

---

## Template

Copy everything below for each figure plan.

```markdown
# fig-repo-{NN}: {Title}

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-{NN} |
| **Title** | {Descriptive title} |
| **Audience** | L1 (Music Industry) / L2 (PhD/Policy) / L3 (Engineer) / L4 (AI/ML) |
| **Location** | Where this figure appears (README, docs/architecture/, docs/prd/, etc.) |
| **Priority** | P0 (Critical) / P1 (High) / P2 (Medium) |
| **Aspect Ratio** | 16:9 / 16:10 / 3:4 (portrait) |
| **Layout Template** | A (Hero) / B (Multi-Panel) / C (Flowchart) / D (Split-Panel) / E (Steps) |

## Purpose

{1-2 sentences: WHY this figure exists and what question it answers for the target audience}

## Key Message

{Single sentence: the one thing the viewer should take away in 5 seconds}

## Visual Concept

{Describe the visual approach in natural language, then include ASCII mockup}

```
+-----------------------------------------------------------+
|  FIGURE TITLE                                             |
+-----------------------------------------------------------+
|                                                           |
|   [ASCII layout of figure structure]                      |
|                                                           |
+-----------------------------------------------------------+
```

## Spatial Anchors

Define the spatial layout in YAML for precise element positioning.

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "FIGURE TITLE"
    role: title

  - id: main_zone
    bounds: [80, 140, 1760, 800]
    role: content_area

  - id: callout_zone
    bounds: [80, 960, 1760, 100]
    role: callout_box

anchors:
  - id: stage_1
    position: [200, 400]
    size: [300, 200]
    role: etl_extract

  - id: stage_2
    position: [600, 400]
    size: [300, 200]
    role: entity_resolve

  - id: flow_1_to_2
    from: stage_1
    to: stage_2
    type: arrow
    label: "normalized records"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| {Element name} | `{semantic_tag}` | {What it represents} |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| {Source element} | {Target element} | arrow / dashed / bidirectional | "{flow description}" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "{CALLOUT TITLE}" | {Key insight text} | top-right / bottom-center / etc. |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "{text}"
- Label 2: "{text}"

### Caption (for embedding in documentation)

{1-2 sentence caption for when figure is linked from markdown files}

## Anti-Hallucination Rules

These are INTERNAL instructions. They MUST NEVER appear as visible text in the output.

1. **Font names are internal** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels.
2. **Semantic tags are internal** -- `etl_extract`, `entity_resolve`, `source_corroborate`, `final_score`, `confidence_high`, `assurance_a2`, `source_musicbrainz` etc. Do NOT render them as visible text.
3. **Hex codes are internal** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be #f6f3e6** -- exact match to frontend surface color. No off-white, no pure white, no gray.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.

## Alt Text

{Accessible description for screen readers, 125 characters max}

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "repo-{NN}",
    "title": "{Figure Title}",
    "audience": "L1|L2|L3|L4",
    "layout_template": "A|B|C|D|E"
  },
  "content_architecture": {
    "primary_message": "{Single sentence key message}",
    "layout_flow": "left-to-right|top-to-bottom|centered|radial",
    "key_structures": [
      {
        "name": "{Structure Name}",
        "role": "{semantic_tag}",
        "is_highlighted": true,
        "labels": ["{Label 1}", "{Label 2}"]
      }
    ],
    "relationships": [
      {
        "from": "{Structure A}",
        "to": "{Structure B}",
        "type": "arrow|dashed|bidirectional",
        "label": "{relationship description}"
      }
    ],
    "callout_boxes": [
      {
        "heading": "{CALLOUT TITLE}",
        "body_text": "{Explanation text}",
        "position": "top-right|bottom-center|left-margin"
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors, hex codes, or font names in content spec)
- [ ] ASCII layout sketched
- [ ] Spatial anchors defined in YAML
- [ ] Labels under 30 characters
- [ ] Anti-hallucination rules listed
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L1/L2/L3/L4)
- [ ] Layout template identified (A/B/C/D/E)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 17/20 (see STYLE-GUIDE-REPO.md)
- [ ] Embedded in documentation
```

---

## Semantic Tag Reference -- Music Attribution Domain

### Pipeline Stages

| Semantic Tag | When to Use | Maps to |
|--------------|-------------|---------|
| `etl_extract` | Data ingestion, normalization, quality gates | Pipeline Stage I |
| `entity_resolve` | Fuzzy matching, deduplication, identity resolution | Pipeline Stage II |
| `source_corroborate` | Multi-source agreement, weighted voting, conflict resolution | Pipeline Stage III |
| `final_score` | Calibrated confidence output, conformal prediction bounds | Pipeline Stage IV |

### Confidence Tiers

| Semantic Tag | When to Use | Threshold |
|--------------|-------------|-----------|
| `confidence_high` | Scores >= 0.85 -- multiple sources agree, high authority | >= 0.85 |
| `confidence_medium` | Scores 0.50-0.84 -- partial agreement or single high-authority source | 0.50 -- 0.84 |
| `confidence_low` | Scores < 0.50 -- contradictions, single low-authority source, or no data | < 0.50 |

### Assurance Levels (A0 -- A3)

| Semantic Tag | When to Use | Level | Plain English |
|--------------|-------------|-------|---------------|
| `assurance_a0` | No provenance data found | A0 | "Unknown" |
| `assurance_a1` | Single source claims the attribution | A1 | "Claimed" |
| `assurance_a2` | Multiple independent sources agree | A2 | "Corroborated" |
| `assurance_a3` | Artist has directly verified the attribution | A3 | "Verified" |

### Data Sources

| Semantic Tag | When to Use | Authority Weight |
|--------------|-------------|------------------|
| `source_musicbrainz` | MusicBrainz open database references | Medium |
| `source_discogs` | Discogs catalog/vinyl data references | Medium |
| `source_acoustid` | AcoustID audio fingerprint references | Low-Medium |
| `source_file` | ID3/Vorbis file metadata references | Low |
| `source_artist` | Direct artist input or verification | Highest |

### Pipeline Infrastructure

| Semantic Tag | When to Use |
|--------------|-------------|
| `processing_stage` | Generic data transformation step |
| `storage_layer` | Database, persistence, pgvector |
| `api_endpoint` | REST/MCP external interface |
| `security_layer` | Auth, permissions, MCP access tiers |
| `data_flow` | Arrow/line showing information movement |
| `feedback_loop` | Correction path, human-in-the-loop return |
| `decision_point` | PRD branching node, archetype fork |

### Domain -- Music Industry

| Semantic Tag | When to Use |
|--------------|-------------|
| `stakeholder_artist` | Artist-related elements (Mogen persona) |
| `stakeholder_label` | Record label or distributor elements |
| `stakeholder_platform` | Streaming/AI platform elements |
| `problem_statement` | Attribution crisis, unclaimed royalties |
| `solution_component` | System capability or benefit |

### Scaffold Concepts

| Semantic Tag | When to Use |
|--------------|-------------|
| `archetype_overlay` | Team archetype-specific configuration |
| `branching_path` | Alternative implementation choice |
| `selected_option` | Chosen PRD decision (solid line) |
| `deferred_option` | Unchosen PRD decision (dashed line) |

---

## Content Review Questions

Before finalizing any content spec, answer these:

1. **5-Second Test**: Can someone identify the key message in 5 seconds?
2. **Necessity Test**: Is every element essential? (Remove anything decorative-only)
3. **Hierarchy Test**: Is the information hierarchy clear? (Title > sections > labels > annotations)
4. **Scale Test**: Would this be readable at 50% zoom on GitHub?
5. **Audience Test**: Would an L{N} reader understand this without needing L{N+1} knowledge?
6. **Accuracy Test**: Are pipeline stages in the correct order? Are confidence thresholds correct?
7. **Scaffold Test**: Does this show branching paths where appropriate, or does it imply a single architecture?

---

*Music Attribution Scaffold -- Repository Documentation Content Template v1.0.0*
