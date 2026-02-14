# fig-supplementary-08: Ecosystem Integration Map (Academic)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-08 |
| **Title** | Ecosystem Integration Map (Academic) |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | Supplementary materials (supplementary.tex \missingfigure placeholder), docs/figures/repo-figures/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 3:4 (portrait, for print) |
| **Layout Template** | B (Multi-Panel) |
| **Medium** | Nano Banana Pro (print-ready) |

## Purpose

Adapts fig-repo-16 and fig-ecosystem-01 content for academic print -- company landscape with PRD node annotations. Answers: "How does the scaffold's ecosystem integration map to real companies and platforms in the music AI space?"

## Key Message

The music AI attribution ecosystem mapped across four tiers -- attribution infrastructure, AI generation, licensing/certification, and open-source tools -- with 28 PRD ecosystem nodes annotating integration surfaces.

## Visual Concept

Portrait layout with four-tier company landscape adapted from fig-repo-16. Each company card has a PRD node annotation showing which ecosystem node(s) map to it. Integration archetype indicators use line styles (thin/medium/thick) for B&W compatibility. Scaffold position highlighted at bottom.

```
+-------------------------------------------+
|  ECOSYSTEM INTEGRATION MAP                 |
|  Music AI Landscape + PRD Node Annotations |
+-------------------------------------------+
|                                            |
|  I. ATTRIBUTION INFRASTRUCTURE             |
|  ─────────────────────────────             |
|  ┌──────────────┐ ┌──────────────┐         |
|  │ Sureel       │ │ Musical AI   │         |
|  │ 86-90%       │ │ $6M, cert'd  │         |
|  │ ▸ sureel_ai_ │ │ ▸ musical_ai_│         |
|  │   partnership│ │   partnership│         |
|  └──────────────┘ └──────────────┘         |
|  ┌──────────────┐ ┌──────────────┐         |
|  │ Vermillio    │ │ ProRata      │         |
|  │ $16M, Sony   │ │ $40M, UMG    │         |
|  └──────────────┘ └──────────────┘         |
|                                            |
|  II. AI MUSIC GENERATION                   |
|  ───────────────────────                   |
|  ┌──────────────┐ ┌──────────────┐         |
|  │ Suno         │ │ Udio         │         |
|  │ $2.45B       │ │ settled      │         |
|  │ ▸ suno_udio_ │ │ ▸ suno_udio_ │         |
|  │   licensing  │ │   licensing  │         |
|  └──────────────┘ └──────────────┘         |
|                                            |
|  III. LICENSING & CERTIFICATION            |
|  ──────────────────────────────            |
|  ┌──────────────┐ ┌──────────────┐         |
|  │ STIM         │ │ SoundExchange│         |
|  │ 1st AI lic.  │ │ ISRC opt-in  │         |
|  │ ▸ stim_cmo_  │ │ ▸ soundexch_ │         |
|  │   pilot      │ │   registry   │         |
|  └──────────────┘ └──────────────┘         |
|  ┌──────────────┐ ┌──────────────┐         |
|  │ Fairly       │ │ LANDR        │         |
|  │ Trained (19) │ │ Fair AI      │         |
|  │ ▸ fairly_    │ │              │         |
|  │   trained_   │ │              │         |
|  │   certific.  │ │              │         |
|  └──────────────┘ └──────────────┘         |
|                                            |
|  IV. OPEN-SOURCE TOOLS                     |
|  ─────────────────────                     |
|  ┌──────────────┐ ┌──────────────┐         |
|  │ librosa      │ │ Splink       │         |
|  │ 8.2k stars   │ │ 4k+ stars    │         |
|  └──────────────┘ └──────────────┘         |
|                                            |
|  ┌─────────────────────────────────────┐   |
|  │  THIS SCAFFOLD                       │   |
|  │  ■ Open-source · 28 ecosystem nodes  │   |
|  │  3 archetypes: Simple MCP ─          │   |
|  │    Platform ── CMO Federation ═══    │   |
|  └─────────────────────────────────────┘   |
|                                            |
+-------------------------------------------+
|  LEGEND                                    |
|  ─ Simple MCP   ── Platform   ═══ CMO Fed |
|  ▸ = PRD ecosystem node annotation         |
+-------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1080
  height: 1440
  background: white  # Academic print -- WHITE, not cream

zones:
  - id: title_zone
    bounds: [0, 0, 1080, 100]
    content: "ECOSYSTEM INTEGRATION MAP"
    role: title

  - id: tier_1_zone
    bounds: [40, 120, 1000, 260]
    role: content_area
    label: "I. ATTRIBUTION INFRASTRUCTURE"

  - id: tier_2_zone
    bounds: [40, 400, 1000, 180]
    role: content_area
    label: "II. AI MUSIC GENERATION"

  - id: tier_3_zone
    bounds: [40, 600, 1000, 280]
    role: content_area
    label: "III. LICENSING & CERTIFICATION"

  - id: tier_4_zone
    bounds: [40, 900, 1000, 160]
    role: content_area
    label: "IV. OPEN-SOURCE TOOLS"

  - id: scaffold_zone
    bounds: [40, 1080, 1000, 120]
    role: primary_outcome
    label: "THIS SCAFFOLD"

  - id: legend_zone
    bounds: [40, 1220, 1000, 80]
    role: callout_bar

anchors:
  - id: sureel_card
    position: [80, 160]
    size: [440, 100]
    role: entity_card
    label: "Sureel + sureel_ai_partnership node"

  - id: musical_ai_card
    position: [560, 160]
    size: [440, 100]
    role: entity_card
    label: "Musical AI + musical_ai_partnership node"

  - id: suno_card
    position: [80, 440]
    size: [440, 100]
    role: entity_card
    label: "Suno + suno_udio_licensing node"

  - id: udio_card
    position: [560, 440]
    size: [440, 100]
    role: entity_card
    label: "Udio + suno_udio_licensing node"

  - id: stim_card
    position: [80, 640]
    size: [440, 100]
    role: entity_card
    label: "STIM + stim_cmo_pilot node"

  - id: soundexchange_card
    position: [560, 640]
    size: [440, 100]
    role: entity_card
    label: "SoundExchange + soundexchange_registry node"

  - id: fairly_trained_card
    position: [80, 760]
    size: [440, 100]
    role: entity_card
    label: "Fairly Trained + fairly_trained_certification node"

  - id: integration_lines
    from: scaffold_zone
    to: tier_1_zone
    type: arrow
    label: "integration surfaces"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "ECOSYSTEM INTEGRATION MAP" -- high contrast, B&W |
| Subtitle | `label_editorial` | "Music AI Landscape + PRD Node Annotations" |
| Tier I heading | `section_numeral` | "I. ATTRIBUTION INFRASTRUCTURE" |
| Tier II heading | `section_numeral` | "II. AI MUSIC GENERATION" |
| Tier III heading | `section_numeral` | "III. LICENSING & CERTIFICATION" |
| Tier IV heading | `section_numeral` | "IV. OPEN-SOURCE TOOLS" |
| Company cards | `entity_card` | Name, key metric, status, PRD node annotation |
| PRD node annotations | `decision_point` | Small labels showing mapped ecosystem node IDs |
| Scaffold highlight bar | `primary_outcome` | Full-width bar showing scaffold's position and features |
| Integration lines | `data_flow` | Line styles differentiate archetypes for B&W |
| Legend bar | `callout_bar` | Integration archetype legend using line weight |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| sureel_ai_partnership node | Sureel company | annotation | "PRD node maps to company" |
| musical_ai_partnership node | Musical AI company | annotation | "PRD node maps to company" |
| stim_cmo_pilot node | STIM company | annotation | "PRD node maps to company" |
| soundexchange_registry node | SoundExchange company | annotation | "PRD node maps to company" |
| fairly_trained_certification node | Fairly Trained company | annotation | "PRD node maps to company" |
| suno_udio_licensing node | Suno + Udio companies | annotation | "PRD node maps to companies" |
| Scaffold | All tiers | dashed | "integration surfaces" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "INTEGRATION ARCHETYPES" | Simple MCP (thin), Platform (medium), CMO Federation (thick) | bottom-center |
| "28 PRD NODES" | Ecosystem expansion v3.0.0 | top-right |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Ecosystem Map (Academic)"
- Label 2: "4-Tier Company Landscape"
- Label 3: "28 PRD Node Annotations"
- Label 4: "3 Integration Archetypes"
- Label 5: "B&W Print Format"

### Caption (for embedding in documentation)

The music AI attribution ecosystem mapped across four tiers with 28 PRD ecosystem node annotations showing integration surfaces. Line styles differentiate three integration archetypes: Simple MCP (thin), Platform (medium), and CMO Federation (thick) -- adapted from fig-repo-16 and fig-ecosystem-01 for academic print.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `entity_card`, `decision_point`, `section_numeral` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be WHITE** -- EXCEPTION to default cream rule. This is an academic print figure for LaTeX/PDF. Pure white background for print compatibility.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This ADAPTS fig-repo-16 + fig-ecosystem-01 for academic print.** Key differences from repo versions: (1) WHITE background for LaTeX, (2) HIGH CONTRAST for B&W, (3) PORTRAIT 3:4 for journal/preprint column format.
10. Company data from fig-repo-16: Sureel (86-90% claimed accuracy), Musical AI ($6M, certified), Suno ($2.45B valuation, settling lawsuits), Udio (settled), Vermillio ($16M, Sony), ProRata ($40M, UMG), STIM (1st collective AI licence), SoundExchange (ISRC opt-in registry), Fairly Trained (19 certifications).
11. PRD node annotations: `sureel_ai_partnership`, `musical_ai_partnership`, `stim_cmo_pilot`, `soundexchange_registry`, `fairly_trained_certification`, `suno_udio_licensing`. These MUST match the `_network.yaml` v3.0.0 node IDs.
12. Line styles differentiate integration archetypes: **thin** = Simple MCP, **medium** = Platform, **thick** = CMO Federation. Use line weight (not color) for B&W print.
13. The supplementary.tex file has `\missingfigure{Ecosystem Integration Map}` placeholder that this figure will replace.
14. Sureel accuracy claims (86-90%) are CLAIMED, not independently verified. Suno is SETTLING (not settled). Udio HAS settled.
15. The scaffold is the ONLY open-source entry in the attribution tier.

## Alt Text

Academic ecosystem map: four-tier company landscape with 28 PRD node annotations

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-08",
    "title": "Ecosystem Integration Map (Academic)",
    "audience": "L2",
    "layout_template": "B",
    "medium": "nano_banana_pro_print"
  },
  "content_architecture": {
    "primary_message": "Music AI attribution ecosystem across four tiers with 28 PRD ecosystem node annotations showing integration surfaces.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Tier I: Attribution Infrastructure",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Sureel", "Musical AI", "Vermillio", "ProRata"]
      },
      {
        "name": "Tier II: AI Music Generation",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Suno", "Udio", "Soundverse", "Boomy"]
      },
      {
        "name": "Tier III: Licensing & Certification",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Fairly Trained", "STIM", "SoundExchange", "LANDR"]
      },
      {
        "name": "Tier IV: Open-Source Tools",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["librosa", "Splink", "chromaprint", "CLAP"]
      },
      {
        "name": "Scaffold Position",
        "role": "primary_outcome",
        "is_highlighted": true,
        "labels": ["Open-source", "28 ecosystem nodes", "MIT License"]
      },
      {
        "name": "PRD Node Annotations",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["sureel_ai_partnership", "musical_ai_partnership", "stim_cmo_pilot", "soundexchange_registry", "fairly_trained_certification", "suno_udio_licensing"]
      }
    ],
    "relationships": [
      {
        "from": "Scaffold",
        "to": "Tier I companies",
        "type": "dashed",
        "label": "integration surfaces"
      },
      {
        "from": "PRD nodes",
        "to": "Companies",
        "type": "annotation",
        "label": "node-to-company mapping"
      }
    ],
    "callout_boxes": [
      {
        "heading": "INTEGRATION ARCHETYPES",
        "body_text": "Simple MCP (thin), Platform (medium), CMO Federation (thick)",
        "position": "bottom-center"
      },
      {
        "heading": "28 PRD NODES",
        "body_text": "Ecosystem expansion v3.0.0",
        "position": "top-right"
      }
    ]
  },
  "print_spec": {
    "background": "white",
    "color_mode": "B&W compatible (high contrast)",
    "aspect_ratio": "3:4 portrait",
    "target": "LaTeX supplementary materials",
    "placeholder": "\\missingfigure{Ecosystem Integration Map}"
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 7 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro (print-ready variant)
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in supplementary.tex
