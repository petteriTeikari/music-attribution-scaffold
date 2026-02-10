# Figure Content Specification Template - The system

**Version:** 1.0.0
**Purpose:** Define WHAT a figure shows (content), not HOW it looks (style).
**Style Reference:** See `STYLE-GUIDE.md` for all visual specifications.

---

## Key Principle: Content/Style Decoupling

Content specs use **semantic tags** (not colors/fonts). The STYLE-GUIDE.md maps semantic tags to visual properties.

**DO write:** `role: "source_system"`
**DON'T write:** `color: "#1E3A5F"`

---

## Figure Type Decision

| Your Figure Has... | Recommended Tool | Use This Template? |
|--------------------|------------------|-------------------|
| Conceptual flows, pipelines | **Nano Banana Pro** | YES |
| Architecture diagrams | **Nano Banana Pro** | YES |
| Before/after comparisons | **Nano Banana Pro** | YES |
| Trust tier visualizations | **Nano Banana Pro** | YES |
| Simple hierarchy diagrams | **Mermaid** | NO - use diagram code |
| Tables with exact data | **Markdown tables** | NO |
| Code architecture | **Mermaid** | NO - use diagram code |

---

## Template

Copy this template for each figure plan:

```markdown
# fig-{type}-{NN}: {Title}

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-{type}-{NN} |
| **Title** | {Descriptive title} |
| **Audience** | Technical (developer) / Domain (music industry) |
| **Complexity** | L1 (concept) / L2 (overview) / L3 (detailed) |
| **Location** | Where this figure appears (README, docs/, etc.) |
| **Priority** | P0 (Critical) / P1 (High) / P2 (Medium) |
| **Aspect Ratio** | 16:9 / 16:10 |

## Purpose

{1-2 sentences: WHY this figure exists and what question it answers}

## Key Message

{Single sentence: the one thing the viewer should understand}

## Visual Concept

{Describe the visual approach and include ASCII mockup}

```
┌─────────────────────────────────────────────────────┐
│  FIGURE TITLE                                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│   [ASCII layout of figure structure]                │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Element 1 | `source_system` | Main database |
| Element 2 | `processing_stage` | Entity resolution |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Element A | Element B | Arrow | "feeds into" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "KEY INSIGHT" | Main takeaway text | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: {text}
- Label 2: {text}

### Caption (for embedding)

{1-2 sentence caption for when figure is embedded in documentation}

## Prompts for Nano Banana Pro

### Style Prompt

See STYLE-GUIDE.md. Include:
- Background: warm off-white (#F8F6F0)
- Power keywords for the system aesthetic
- Reference negative prompt

### Content Prompt

{Describe what to show, translating semantic tags to visual descriptions}

Example:
"Show data flowing from three sources (Discogs in dark gray, MusicBrainz in purple,
The system in deep blue) through an entity resolution stage to a unified database."

### Refinement Notes

{Any specific adjustments after initial generation}

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "{type}-{NN}",
    "title": "Figure Title",
    "audience": "technical|domain"
  },
  "content_architecture": {
    "primary_message": "Single sentence key message",
    "layout_flow": "left-to-right|top-to-bottom|centered",
    "key_structures": [
      {
        "name": "Structure Name",
        "role": "semantic_tag",
        "is_highlighted": true,
        "labels": ["Label 1", "Label 2"]
      }
    ],
    "relationships": [
      {
        "from": "Structure A",
        "to": "Structure B",
        "type": "arrow|bidirectional|dashed",
        "label": "relationship description"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CALLOUT TITLE",
        "body_text": "Explanation text.",
        "position": "top-right|bottom-center"
      }
    ]
  }
}
```

## Alt Text

{Accessible description for screen readers, 125 chars max}

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
```

---

## Semantic Tag Reference (System-Specific)

### Attribution Levels

| Tag | When to Use |
|-----|-------------|
| `attribution_verified` | A3: Artist-confirmed data |
| `attribution_corroborated` | A2: Multiple sources agree |
| `attribution_claimed` | A1: Single source only |
| `attribution_unknown` | A0: No data found |

### Data Sources

| Tag | When to Use |
|-----|-------------|
| `source_system` | System own database (primary) |
| `source_musicbrainz` | MusicBrainz data |
| `source_discogs` | Discogs data |

### Access Tiers

| Tag | When to Use |
|-----|-------------|
| `tier_internal` | Internal system apps |
| `tier_verified` | Verified partners (Mogen) |
| `tier_public` | Public/unknown clients |

### Confidence Levels

| Tag | When to Use |
|-----|-------------|
| `confidence_high` | 0.85+ confidence score |
| `confidence_medium` | 0.50-0.84 confidence |
| `confidence_low` | <0.50 confidence |

### Pipeline Elements

| Tag | When to Use |
|-----|-------------|
| `processing_stage` | Data transformation step |
| `storage_layer` | Database/persistence |
| `api_endpoint` | External interface |
| `security_layer` | Auth/permissions |
| `data_flow` | Information movement |

### Domain (Music Industry)

| Tag | When to Use |
|-----|-------------|
| `stakeholder_artist` | Artist-related elements |
| `stakeholder_platform` | Platform/label elements |
| `problem_statement` | Issue visualization |
| `solution_component` | system solution part |

---

## Audience Guidelines

### Technical Figures (fig-tech-*)

**Audience:** Developers implementing the system

**Include:**
- Database schemas, table relationships
- API contracts, MCP tool signatures
- Algorithm steps, confidence calculations
- Code-level architecture

**Tone:** Precise, implementation-focused

### Domain Figures (fig-domain-*)

**Audience:** Music industry professionals (think Imogen Heap's readers)

**Include:**
- Problem context (attribution crisis)
- Solution benefits (not implementation)
- Business value (royalties, AI consent)
- Trust model in business terms

**Tone:** Accessible, benefit-focused

---

## Quality Checklist

### Before Finalizing Content Spec

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors/hex codes)
- [ ] ASCII layout sketched
- [ ] Labels under 30 characters
- [ ] JSON export block included
- [ ] Alt text provided
- [ ] Audience level appropriate

### Content Review Questions

1. Can someone understand the key message in 5 seconds?
2. Are all elements necessary? (Remove clutter)
3. Is the information hierarchy clear?
4. Would this work at half the size? (GitHub embeds)

---

*the system Content Template v1.0.0 - For content/style decoupled figure generation*
