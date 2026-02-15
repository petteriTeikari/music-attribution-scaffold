# fig-landscape-08: Geographic Regulatory Fragmentation: Five Jurisdictions

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-08 |
| **Title** | Geographic Regulatory Fragmentation: Five Jurisdictions |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure maps the five major regulatory jurisdictions and their fundamentally different approaches to AI music governance. It answers: "Why is building a global attribution system so hard, and what does each jurisdiction actually require?"

## Key Message

EU, US, UK, Nordic, and Asia-Pacific represent 5 fundamentally different regulatory approaches to AI music -- any global attribution system must handle all five.

## Visual Concept

Five vertical panels of equal width, each representing one jurisdiction. Each panel contains the jurisdiction name, the regulatory approach label, key regulatory instruments, and an overall stance indicator (strict/moderate/permissive). A bottom callout bar highlights the fragmentation problem. The panels read left-to-right in order of regulatory strictness.

```
+---------------------------------------------------------------+
|  REGULATORY FRAGMENTATION                                      |
|  ■ Five Jurisdictions, Five Approaches                         |
+---------------------------------------------------------------+
|                                                                |
| ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ |
| │  I. EU  │ │ II. US  │ │ III. UK │ │ IV.NORDIC│ │V. APAC  │ |
| │─────────│ │─────────│ │─────────│ │─────────│ │─────────│ |
| │         │ │         │ │         │ │         │ │         │ |
| │LEGISLA- │ │CASE-LAW │ │PROPOSED │ │COLLECTVE│ │MIXED    │ |
| │TIVE     │ │DRIVEN   │ │EXCEPTION│ │LICENSING│ │REGIMES  │ |
| │         │ │         │ │         │ │         │ │         │ |
| │■ AI Act │ │■ DMCA   │ │■ TDM    │ │■ STIM   │ │■ JP:    │ |
| │  Art. 50│ │■ Copy-  │ │  except.│ │  model  │ │  fair   │ |
| │■ DSA    │ │  right  │ │■ Bletch-│ │■ Nordic │ │  use    │ |
| │■ GDPR   │ │  Office │ │  ley    │ │  collab │ │■ CN:    │ |
| │  (data) │ │  inquiry│ │  process│ │  frame- │ │  interim│ |
| │         │ │■ Thomsn │ │■ IPO    │ │  work   │ │  rules  │ |
| │         │ │  Reuter │ │  code of│ │         │ │■ KR:    │ |
| │         │ │  v OpenA│ │  practce│ │         │ │  AI Act │ |
| │         │ │         │ │         │ │         │ │         │ |
| │ STRICT  │ │MODERATE │ │IN FLUX  │ │PROGRESS.│ │VARIABLE │ |
| └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ |
|                                                                |
+---------------------------------------------------------------+
|  ■ REGULATORY FRAGMENTATION = COMPLIANCE NIGHTMARE             |
|    Any global system must handle all five approaches.          |
|    Fragmentation also creates regulatory arbitrage.            |
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
      text: "REGULATORY FRAGMENTATION"
    - type: label_editorial
      text: "Five Jurisdictions, Five Approaches"

panel_eu:
  position: [60, 140]
  width: 340
  height: 700
  label: "I. EU"
  approach: "Legislative"
  instruments:
    - "AI Act Article 50"
    - "Digital Services Act"
    - "GDPR (data rights)"
  stance: "Strict"

panel_us:
  position: [420, 140]
  width: 340
  height: 700
  label: "II. US"
  approach: "Case-Law Driven"
  instruments:
    - "DMCA"
    - "Copyright Office inquiry"
    - "Thomson Reuters v OpenAI"
  stance: "Moderate"

panel_uk:
  position: [780, 140]
  width: 340
  height: 700
  label: "III. UK"
  approach: "Proposed Exception"
  instruments:
    - "TDM exception proposal"
    - "Bletchley process"
    - "IPO code of practice"
  stance: "In Flux"

panel_nordic:
  position: [1140, 140]
  width: 340
  height: 700
  label: "IV. NORDIC"
  approach: "Collective Licensing"
  instruments:
    - "STIM collective model"
    - "Nordic collaborative framework"
  stance: "Progressive"

panel_apac:
  position: [1500, 140]
  width: 340
  height: 700
  label: "V. ASIA-PACIFIC"
  approach: "Mixed Regimes"
  instruments:
    - "Japan: fair use approach"
    - "China: interim measures"
    - "Korea: AI Act"
  stance: "Variable"

callout_bottom:
  position: [60, 880]
  width: 1800
  height: 140
  elements:
    - type: callout_bar
      text: "REGULATORY FRAGMENTATION = COMPLIANCE NIGHTMARE"
    - type: label_editorial
      text: "Any global system must handle all five approaches."
    - type: label_editorial
      text: "Fragmentation also creates regulatory arbitrage."
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "REGULATORY FRAGMENTATION" with coral accent square |
| Subtitle | `label_editorial` | "Five Jurisdictions, Five Approaches" |
| EU panel | `processing_stage` | Legislative approach: AI Act, DSA, GDPR |
| US panel | `processing_stage` | Case-law driven: DMCA, Copyright Office, litigation |
| UK panel | `processing_stage` | Proposed exception: TDM, Bletchley, IPO code |
| Nordic panel | `processing_stage` | Collective licensing: STIM model, Nordic framework |
| APAC panel | `processing_stage` | Mixed regimes: Japan fair use, China interim, Korea AI Act |
| Approach labels | `label_editorial` | "LEGISLATIVE", "CASE-LAW DRIVEN", etc. |
| Instrument lists | `data_mono` | Specific regulatory instruments per jurisdiction |
| Stance badges | `badge_label` | Strict/Moderate/In Flux/Progressive/Variable |
| Panel dividers | `callout_bar` | Thin coral accent lines between panels |
| Roman numerals | `section_numeral` | I through V for each panel |
| Bottom callout | `callout_bar` | Fragmentation = compliance nightmare |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| EU (strict) | US (moderate) | contrast | "Different enforcement mechanisms" |
| UK (in flux) | EU (strict) | diverging | "Post-Brexit regulatory divergence" |
| Nordic (progressive) | EU (strict) | complementary | "Collective licensing within EU framework" |
| APAC (variable) | All others | fragmented | "Three sub-jurisdictions with different approaches" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Bottom callout | "Regulatory fragmentation = compliance nightmare" | Full-width bottom bar |
| Arbitrage note | "Fragmentation creates regulatory arbitrage" | Within bottom callout |

## Text Content

### Labels (Max 30 chars each)

- REGULATORY FRAGMENTATION
- Five Jurisdictions
- EU
- US
- UK
- NORDIC
- ASIA-PACIFIC
- LEGISLATIVE
- CASE-LAW DRIVEN
- PROPOSED EXCEPTION
- COLLECTIVE LICENSING
- MIXED REGIMES
- AI Act Article 50
- DMCA
- TDM exception proposal
- STIM collective model
- Japan fair use
- China interim measures
- Korea AI Act
- Strict
- Moderate
- In Flux
- Progressive
- Variable

### Caption (for embedding in documentation)

Five major jurisdictions take fundamentally different approaches to AI music regulation: EU (legislative, strict -- AI Act Article 50, DSA), US (case-law driven, moderate -- DMCA, Copyright Office), UK (proposed exceptions, in flux -- TDM, Bletchley process), Nordic (collective licensing, progressive -- STIM model), and Asia-Pacific (mixed regimes, variable -- Japan fair use, China interim measures, Korea AI Act). Any global attribution system must handle all five.

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

1. There are exactly 5 jurisdictions: EU, US, UK, Nordic, Asia-Pacific -- do NOT add or remove any.
2. Regulatory instruments named are REAL -- AI Act Article 50, DMCA, STIM are real instruments. Do NOT invent regulatory names.
3. "Thomson Reuters v OpenAI" is a reference to active litigation as of 2025 -- do NOT claim a resolution.
4. STIM is the Swedish collective management organization -- do NOT expand incorrectly.
5. The Bletchley process refers to the UK AI Safety Summit and follow-on process -- do NOT rename it.
6. Asia-Pacific contains THREE sub-jurisdictions (Japan, China, Korea) -- do NOT add others (e.g., no India, Australia).
7. Stance labels (Strict/Moderate/In Flux/Progressive/Variable) are CHARACTERIZATIONS, not official classifications.
8. Do NOT imply that any jurisdiction has "solved" AI music regulation -- all are evolving.
9. "Regulatory arbitrage" means companies choosing jurisdictions to minimize compliance burden -- do NOT define it differently.

## Alt Text

Five jurisdiction panels showing EU, US, UK, Nordic, Asia-Pacific regulatory approaches to AI music attribution.

## JSON Export Block

```json
{
  "id": "fig-landscape-08",
  "title": "Geographic Regulatory Fragmentation: Five Jurisdictions",
  "audience": "L2",
  "priority": "P1",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "jurisdictions": [
    {
      "name": "EU",
      "approach": "Legislative",
      "instruments": ["AI Act Article 50", "DSA", "GDPR"],
      "stance": "Strict"
    },
    {
      "name": "US",
      "approach": "Case-Law Driven",
      "instruments": ["DMCA", "Copyright Office inquiry", "Thomson Reuters v OpenAI"],
      "stance": "Moderate"
    },
    {
      "name": "UK",
      "approach": "Proposed Exception",
      "instruments": ["TDM exception proposal", "Bletchley process", "IPO code of practice"],
      "stance": "In Flux"
    },
    {
      "name": "Nordic",
      "approach": "Collective Licensing",
      "instruments": ["STIM collective model", "Nordic collaborative framework"],
      "stance": "Progressive"
    },
    {
      "name": "Asia-Pacific",
      "approach": "Mixed Regimes",
      "instruments": ["Japan fair use", "China interim measures", "Korea AI Act"],
      "stance": "Variable"
    }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage",
    "data_mono", "badge_label", "callout_bar", "section_numeral"
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
