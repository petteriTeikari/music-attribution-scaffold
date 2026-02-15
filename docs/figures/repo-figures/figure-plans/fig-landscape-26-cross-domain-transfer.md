# fig-landscape-26: Cross-Domain Method Transfer: Supply Chain / Pharma / Finance to Music

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-26 |
| **Title** | Cross-Domain Method Transfer: Supply Chain / Pharma / Finance to Music |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

This is THE signature Markovian novelty figure for the entire landscape analysis. It demonstrates that music attribution is not an unsolved problem requiring novel invention -- it is a problem with mature solutions in four adjacent domains (supply chain, finance, pharma, game theory) that can be structurally imported. The figure exposes the structural isomorphisms -- identical mathematical frameworks operating under different domain vocabularies -- that make this transfer rigorous, not metaphorical. This directly extends the AI Passport manuscripts' cross-domain analysis.

## Key Message

GS1 EPCIS gives us entity resolution patterns, SOX gives us audit trails, EU FMD gives us provenance chains, and Shapley values give us contribution attribution -- music can import mature solutions from these four domains.

## Visual Concept

A hero layout with four source domains arranged vertically on the left side, each flowing rightward through a central "structural isomorphism" zone into a unified music attribution column on the right. The left column shows mature, solved-problem domains. The center shows the mathematical mapping (not metaphor -- actual structural equivalence). The right column shows the music attribution target. Coral accent lines connect corresponding elements across the isomorphism boundary. The overall visual metaphor is a translation table: same structure, different vocabulary.

```
+---------------------------------------------------------------+
|  CROSS-DOMAIN METHOD TRANSFER                                  |
|  ■ Solved Problems → Structural Isomorphisms → Music           |
+---------------------------------------------------------------+
|                                                                |
|  SOURCE DOMAINS          ISOMORPHISMS       MUSIC ATTRIBUTION  |
|                                                                |
|  ┌─────────────────┐    ┌──────────┐    ┌─────────────────┐   |
|  │ SUPPLY CHAIN    │    │ Entity   │    │ ISRC/ISWC/ISNI  │   |
|  │ GS1 EPCIS       │───▶│ Resolut. │───▶│ resolution      │   |
|  │ Serialization    │    │ at scale │    │ across catalogs │   |
|  │ Track-and-trace  │    └──────────┘    └─────────────────┘   |
|  └─────────────────┘                                           |
|         ■                                                      |
|  ┌─────────────────┐    ┌──────────┐    ┌─────────────────┐   |
|  │ FINANCE         │    │ Audit    │    │ A0-A3 assurance  │   |
|  │ SOX / Basel III  │───▶│ trails + │───▶│ compliance      │   |
|  │ Compliance rptg  │    │ risk UQ  │    │ provenance logs │   |
|  │ Risk quantificn  │    └──────────┘    └─────────────────┘   |
|  └─────────────────┘                                           |
|         ■                                                      |
|  ┌─────────────────┐    ┌──────────┐    ┌─────────────────┐   |
|  │ PHARMA          │    │ Hybrid   │    │ Watermark +      │   |
|  │ EU FMD           │───▶│ on/off   │───▶│ metadata hybrid │   |
|  │ Falsified Meds   │    │ chain    │    │ provenance chain│   |
|  │ Serialization    │    │ provennce│    └─────────────────┘   |
|  └─────────────────┘    └──────────┘                           |
|         ■                                                      |
|  ┌─────────────────┐    ┌──────────┐    ┌─────────────────┐   |
|  │ GAME THEORY     │    │ Fair     │    │ Proportional     │   |
|  │ Shapley Values   │───▶│ contribn │───▶│ royalty          │   |
|  │ Cooperative games│    │ allocatn │    │ distribution    │   |
|  │ Axiomatic proof  │    └──────────┘    └─────────────────┘   |
|  └─────────────────┘                                           |
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │ KEY INSIGHT: These are STRUCTURAL ISOMORPHISMS,          │   |
|  │ not metaphors. The mathematical frameworks are identical. │   |
|  └─────────────────────────────────────────────────────────┘   |
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
      text: "CROSS-DOMAIN METHOD TRANSFER"
    - type: label_editorial
      text: "Solved Problems → Structural Isomorphisms → Music Attribution"

column_headers:
  position: [60, 130]
  width: 1800
  height: 40
  elements:
    - { type: label_editorial, text: "SOURCE DOMAINS", x: 100 }
    - { type: label_editorial, text: "ISOMORPHISMS", x: 800 }
    - { type: label_editorial, text: "MUSIC ATTRIBUTION", x: 1400 }

source_supply_chain:
  position: [60, 180]
  width: 520
  height: 180
  label: "I. SUPPLY CHAIN"
  elements:
    - { type: heading_display, text: "GS1 EPCIS" }
    - { type: data_mono, text: "Serialization: GTIN → SGTIN" }
    - { type: data_mono, text: "Track-and-trace: event-level visibility" }
    - { type: data_mono, text: "Entity resolution: GLN matching at global scale" }
    - { type: label_editorial, text: "Maturity: 20+ years, billions of items" }

isomorphism_entity:
  position: [640, 180]
  width: 360
  height: 180
  label: "Entity Resolution at Scale"
  elements:
    - { type: callout_bar, text: "Same problem structure" }
    - { type: data_mono, text: "Unique ID → disambiguated entity" }
    - { type: data_mono, text: "Probabilistic matching across registries" }
    - { type: data_mono, text: "Hierarchical: item → lot → product" }

target_entity:
  position: [1060, 180]
  width: 520
  height: 180
  label: "ISRC/ISWC/ISNI Resolution"
  elements:
    - { type: data_mono, text: "ISRC (recording) → ISWC (work) → ISNI (person)" }
    - { type: data_mono, text: "Cross-catalog matching: MusicBrainz ↔ Discogs" }
    - { type: data_mono, text: "Splink probabilistic linkage" }

source_finance:
  position: [60, 390]
  width: 520
  height: 180
  label: "II. FINANCE"
  elements:
    - { type: heading_display, text: "SOX / Basel III" }
    - { type: data_mono, text: "Audit trails: immutable transaction logs" }
    - { type: data_mono, text: "Compliance reporting: tiered requirements" }
    - { type: data_mono, text: "Risk quantification: VaR, stress testing" }
    - { type: label_editorial, text: "Maturity: 20+ years, regulatory mandate" }

isomorphism_audit:
  position: [640, 390]
  width: 360
  height: 180
  label: "Audit Trails + Risk UQ"
  elements:
    - { type: callout_bar, text: "Same problem structure" }
    - { type: data_mono, text: "Action → immutable log → compliance proof" }
    - { type: data_mono, text: "Tiered requirements by risk level" }
    - { type: data_mono, text: "Quantified uncertainty on outcomes" }

target_assurance:
  position: [1060, 390]
  width: 520
  height: 180
  label: "A0-A3 Assurance Levels"
  elements:
    - { type: data_mono, text: "A0 (none) → A3 (artist-verified)" }
    - { type: data_mono, text: "Attribution provenance logs per record" }
    - { type: data_mono, text: "Conformal prediction confidence intervals" }

source_pharma:
  position: [60, 600]
  width: 520
  height: 180
  label: "III. PHARMA"
  elements:
    - { type: heading_display, text: "EU FMD" }
    - { type: data_mono, text: "Falsified Medicines Directive 2011/62/EU" }
    - { type: data_mono, text: "Hybrid on-chain/off-chain provenance" }
    - { type: data_mono, text: "Serialization: unique ID per package" }
    - { type: label_editorial, text: "Maturity: 10+ years, legal mandate" }

isomorphism_provenance:
  position: [640, 600]
  width: 360
  height: 180
  label: "Hybrid Provenance Chains"
  elements:
    - { type: callout_bar, text: "Same problem structure" }
    - { type: data_mono, text: "Physical item → digital twin → chain of custody" }
    - { type: data_mono, text: "On-chain hash + off-chain data" }
    - { type: data_mono, text: "Verification at point of use" }

target_provenance:
  position: [1060, 600]
  width: 520
  height: 180
  label: "Watermark + Metadata Hybrid"
  elements:
    - { type: data_mono, text: "Audio watermark (embedded) + ISRC metadata (registry)" }
    - { type: data_mono, text: "Verification at playback/licensing point" }
    - { type: data_mono, text: "Hybrid on-chain hash + off-chain audio" }

source_game_theory:
  position: [60, 810]
  width: 520
  height: 180
  label: "IV. GAME THEORY"
  elements:
    - { type: heading_display, text: "Shapley Values" }
    - { type: data_mono, text: "Cooperative game theory: N-player coalitions" }
    - { type: data_mono, text: "Axiomatic fairness: efficiency, symmetry, null player" }
    - { type: data_mono, text: "Marginal contribution computation" }
    - { type: label_editorial, text: "Maturity: 70+ years, Nobel Prize 2012" }

isomorphism_allocation:
  position: [640, 810]
  width: 360
  height: 180
  label: "Fair Contribution Allocation"
  elements:
    - { type: callout_bar, text: "Same problem structure" }
    - { type: data_mono, text: "N contributors → fair share of total value" }
    - { type: data_mono, text: "Axiomatic justification (not ad hoc)" }
    - { type: data_mono, text: "Marginal contribution = counterfactual impact" }

target_royalty:
  position: [1060, 810]
  width: 520
  height: 180
  label: "Proportional Royalty Distribution"
  elements:
    - { type: data_mono, text: "Songwriter + producer + performer → royalty split" }
    - { type: data_mono, text: "Shapley-based proportional allocation" }
    - { type: data_mono, text: "Handles complex multi-contributor works" }

insight_box:
  position: [60, 1010]
  width: 1800
  height: 50
  elements:
    - type: callout_bar
      text: "These are STRUCTURAL ISOMORPHISMS, not metaphors -- the mathematical frameworks are identical across domains"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "CROSS-DOMAIN METHOD TRANSFER" with coral accent square |
| Subtitle | `label_editorial` | "Solved Problems -> Structural Isomorphisms -> Music Attribution" |
| Column headers | `label_editorial` | Three column labels: SOURCE DOMAINS, ISOMORPHISMS, MUSIC ATTRIBUTION |
| Supply chain source | `solution_component` | GS1 EPCIS: serialization, track-and-trace, entity resolution |
| Finance source | `solution_component` | SOX/Basel III: audit trails, compliance, risk quantification |
| Pharma source | `solution_component` | EU FMD: falsified medicines, hybrid provenance, serialization |
| Game theory source | `solution_component` | Shapley values: cooperative games, axiomatic fairness |
| Isomorphism bridges | `branching_path` | Four structural mapping zones connecting source to target |
| Entity resolution target | `selected_option` | ISRC/ISWC/ISNI resolution across catalogs |
| Assurance target | `selected_option` | A0-A3 compliance levels with conformal prediction |
| Provenance target | `selected_option` | Watermark + metadata hybrid provenance chain |
| Royalty target | `selected_option` | Shapley-based proportional royalty distribution |
| Panel numerals | `section_numeral` | Roman numerals I-IV for source domains |
| Insight callout | `callout_bar` | "Structural isomorphisms, not metaphors" at bottom |
| Domain accent squares | `callout_bar` | Coral accent squares between source domain rows |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| GS1 EPCIS | ISRC/ISWC/ISNI resolution | structural_isomorphism | "Serialization → unique music ID" |
| SOX/Basel III | A0-A3 assurance levels | structural_isomorphism | "Tiered compliance → tiered assurance" |
| EU FMD | Watermark + metadata hybrid | structural_isomorphism | "Physical-digital twin → audio-metadata twin" |
| Shapley values | Proportional royalty | structural_isomorphism | "Coalition value → royalty pool" |
| All sources | Center isomorphism column | convergence | "Mature solutions from 10-70 year old fields" |
| Center isomorphism | Music attribution targets | application | "Import, do not reinvent" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| The Novelty | "These are SOLVED PROBLEMS being imported to an unsolved domain -- the innovation is recognizing the structural equivalence" | Bottom center |
| Manuscript Reference | "Extends AI Passport v1/v2 cross-domain analysis (SSRN 6109087)" | Top-right corner |
| Maturity Gradient | "Supply chain 20yr, Finance 20yr, Pharma 10yr, Game theory 70yr -- music attribution 3yr" | Right margin |

## Text Content

### Labels (Max 30 chars each)

- Supply Chain (GS1 EPCIS)
- Finance (SOX / Basel III)
- Pharma (EU FMD)
- Game Theory (Shapley Values)
- Entity Resolution at Scale
- Audit Trails + Risk UQ
- Hybrid Provenance Chains
- Fair Contribution Allocation
- ISRC/ISWC/ISNI Resolution
- A0-A3 Assurance Levels
- Watermark + Metadata Hybrid
- Proportional Royalty Distrib.
- Structural Isomorphisms
- SOURCE DOMAINS
- MUSIC ATTRIBUTION

### Caption (for embedding in documentation)

Music attribution can import mature solutions from four adjacent domains through structural isomorphisms: GS1 EPCIS entity resolution maps to ISRC/ISWC/ISNI cross-catalog matching, SOX/Basel III audit trails map to A0-A3 assurance levels, EU FMD hybrid provenance maps to watermark-plus-metadata chains, and Shapley values from cooperative game theory map to proportional royalty distribution. These are not metaphors but identical mathematical frameworks operating under different domain vocabularies -- the innovation is recognizing the structural equivalence and importing 10-70 years of proven solutions.

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

1. There are exactly FOUR source domains -- do NOT add or remove any.
2. The mappings are STRUCTURAL ISOMORPHISMS, not loose analogies -- do NOT use words like "similar to" or "reminds of."
3. GS1 EPCIS is a SPECIFIC standard (ISO/IEC 19987) -- do NOT generalize to "supply chain tech."
4. SOX is the Sarbanes-Oxley Act of 2002 -- do NOT confuse with other financial regulations.
5. EU FMD is Directive 2011/62/EU -- do NOT confuse with EU AI Act or other EU legislation.
6. Shapley values have AXIOMATIC justification (efficiency, symmetry, linearity, null player) -- do NOT describe as "a method" or "an approach."
7. Do NOT imply music attribution is trivial because solutions exist elsewhere -- the TRANSFER is the novel contribution.
8. Do NOT render the three-column layout as a simple left-right arrow diagram -- show the structural mapping in the center column.
9. The maturity gap is the point: 10-70 years vs. 3 years -- make this contrast visible.
10. Do NOT include blockchain as a fifth domain -- pharma's hybrid on/off-chain is sufficient.

## Alt Text

Four-domain method transfer: supply chain, finance, pharma, game theory solutions mapped to music attribution targets.

## JSON Export Block

```json
{
  "id": "fig-landscape-26",
  "title": "Cross-Domain Method Transfer: Supply Chain / Pharma / Finance to Music",
  "audience": "L2",
  "priority": "P0",
  "layout": "A",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 5,
  "signature_figure": true,
  "source_domains": [
    {
      "name": "Supply Chain",
      "standard": "GS1 EPCIS (ISO/IEC 19987)",
      "maturity_years": 20,
      "key_pattern": "Entity resolution at global scale",
      "music_target": "ISRC/ISWC/ISNI resolution across catalogs",
      "isomorphism": "Serialization → unique music ID"
    },
    {
      "name": "Finance",
      "standard": "SOX (Sarbanes-Oxley 2002) / Basel III",
      "maturity_years": 20,
      "key_pattern": "Audit trails + tiered compliance + risk UQ",
      "music_target": "A0-A3 assurance levels with conformal prediction",
      "isomorphism": "Tiered compliance → tiered assurance"
    },
    {
      "name": "Pharma",
      "standard": "EU FMD (Directive 2011/62/EU)",
      "maturity_years": 10,
      "key_pattern": "Hybrid on-chain/off-chain provenance",
      "music_target": "Watermark + metadata hybrid provenance chain",
      "isomorphism": "Physical-digital twin → audio-metadata twin"
    },
    {
      "name": "Game Theory",
      "standard": "Shapley Values (1953, Nobel 2012)",
      "maturity_years": 70,
      "key_pattern": "Axiomatic fair contribution allocation",
      "music_target": "Proportional royalty distribution",
      "isomorphism": "Coalition value → royalty pool"
    }
  ],
  "manuscript_references": [
    "AI Passport v1 (SSRN)",
    "AI Passport v2 (SSRN)",
    "Music Attribution primary (SSRN 6109087)"
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component", "branching_path",
    "selected_option", "section_numeral", "callout_bar", "data_mono"
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
