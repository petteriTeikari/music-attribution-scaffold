# fig-landscape-19: Ethical Certification: Binary vs Graduated vs Regulatory

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-19 |
| **Title** | Ethical Certification: Binary vs Graduated vs Regulatory |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure reveals that three seemingly competing trust mechanisms -- binary certification, graduated assurance, and mandatory regulation -- are actually complementary layers of the same trust stack, using a cross-domain analogy to food safety to make the point concrete. It answers: "How do Fairly Trained, A0-A3 assurance, and the EU AI Act work together rather than against each other?"

## Key Message

Three complementary trust layers -- Fairly Trained (binary pass/fail), A0-A3 assurance (graduated), and EU AI Act (mandatory regulatory) -- work together like HACCP + health grades + FDA in food safety.

## Visual Concept

Three tall panels side by side, each representing one trust layer. Below the three panels, a cross-domain analogy bar maps each music trust layer to its food safety equivalent (HACCP, health grade, FDA). A bottom callout references de Berardinis et al. (2025) responsible AI music framework. The novelty is the cross-domain analogy that reveals complementarity -- these are not competitors but layers in a trust stack.

```
+---------------------------------------------------------------+
|  ETHICAL CERTIFICATION                                         |
|  ■ Three Complementary Trust Layers                            |
+---------------------------------------------------------------+
|                    |                    |                       |
|  I. BINARY         |  II. GRADUATED     |  III. REGULATORY      |
|  ──────────        |  ────────────      |  ──────────────       |
|                    |                    |                       |
|  Fairly Trained    |  A0-A3 Assurance   |  EU AI Act Art. 50    |
|                    |                    |                       |
|  ┌──────────┐      |  ┌──────────┐      |  ┌──────────┐        |
|  │  YES/NO  │      |  │ A3 ████  │      |  │ MANDATORY│        |
|  │          │      |  │ A2 ███   │      |  │ LABELING │        |
|  │ 19 cert. │      |  │ A1 ██    │      |  │          │        |
|  │ entities │      |  │ A0 █     │      |  │ Compliance│       |
|  └──────────┘      |  └──────────┘      |  └──────────┘        |
|                    |                    |                       |
|  Simple but        |  Nuanced but       |  Universal but       |
|  coarse            |  complex           |  compliance-driven   |
|                    |                    |                       |
+--------------------+--------------------+-----------------------+
|                                                                |
|  CROSS-DOMAIN ANALOGY: FOOD SAFETY                              |
|  ═══════════════════════════════════                            |
|  ┌──────────┐      ┌──────────┐      ┌──────────┐             |
|  │  HACCP   │      │ A-F Grade│      │   FDA    │             |
|  │  process │      │ restaurant│     │ federal  │             |
|  │  certif. │      │ health   │      │ mandate  │             |
|  └──────────┘      └──────────┘      └──────────┘             |
|                                                                |
|  ■ These are COMPLEMENTARY layers, not competing standards      |
|    cf. de Berardinis et al. (2025) responsible AI music         |
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
      text: "ETHICAL CERTIFICATION"
    - type: label_editorial
      text: "Three Complementary Trust Layers"

panel_binary:
  position: [60, 140]
  width: 560
  height: 400
  label: "I. BINARY"
  system: "Fairly Trained"
  mechanism: "Yes/No certification, 19 certified entities"
  strength: "Simple, clear signal"
  weakness: "Coarse — no granularity within pass/fail"

panel_graduated:
  position: [640, 140]
  width: 560
  height: 400
  label: "II. GRADUATED"
  system: "A0-A3 Assurance Levels"
  mechanism: "Continuous spectrum from no data (A0) to artist-verified (A3)"
  strength: "Nuanced, captures partial provenance"
  weakness: "Complex to implement and communicate"

panel_regulatory:
  position: [1220, 140]
  width: 560
  height: 400
  label: "III. REGULATORY"
  system: "EU AI Act Article 50"
  mechanism: "Mandatory labeling of AI-generated content"
  strength: "Universal, enforceable"
  weakness: "Compliance-driven, minimum bar"

analogy_bar:
  position: [60, 580]
  width: 1800
  height: 260
  elements:
    - type: label_editorial
      text: "CROSS-DOMAIN ANALOGY: FOOD SAFETY"
    - type: solution_component
      mappings:
        - { music: "Fairly Trained", food: "HACCP", role: "Process certification" }
        - { music: "A0-A3 Assurance", food: "A-F Health Grade", role: "Graduated visible score" }
        - { music: "EU AI Act", food: "FDA", role: "Federal regulatory mandate" }

callout_bottom:
  position: [60, 880]
  width: 1800
  height: 120
  elements:
    - type: callout_bar
      text: "These are COMPLEMENTARY layers, not competing standards"
    - type: label_editorial
      text: "cf. de Berardinis et al. (2025) responsible AI music framework"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "ETHICAL CERTIFICATION" with coral accent square |
| Subtitle | `label_editorial` | "Three Complementary Trust Layers" |
| Binary panel | `solution_component` | Fairly Trained: 19 certified entities, yes/no |
| Graduated panel | `solution_component` | A0-A3 assurance levels: continuous spectrum |
| Regulatory panel | `solution_component` | EU AI Act Article 50: mandatory labeling |
| Cross-domain analogy | `archetype_overlay` | Food safety mapping: HACCP / health grade / FDA |
| HACCP mapping | `solution_component` | Process certification analog |
| Health grade mapping | `solution_component` | Graduated visible score analog |
| FDA mapping | `solution_component` | Federal regulatory mandate analog |
| Roman numerals | `section_numeral` | I, II, III panel headers |
| Complementarity callout | `callout_bar` | "Complementary layers, not competing standards" |
| Academic reference | `label_editorial` | de Berardinis et al. (2025) citation |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Binary panel | HACCP | analogy | "Process certification" |
| Graduated panel | Health grade | analogy | "Graduated visible score" |
| Regulatory panel | FDA | analogy | "Federal regulatory mandate" |
| All three panels | Complementarity callout | synthesis | "Work together, not compete" |
| de Berardinis et al. | All three panels | framework | "Maps to all three layers" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Complementarity | "These are COMPLEMENTARY layers, not competing standards" | Bottom bar |
| Academic Reference | "cf. de Berardinis et al. (2025) responsible AI music framework" | Below complementarity callout |
| Fairly Trained Stats | "19 certified entities as of 2025" | Within binary panel |

## Text Content

### Labels (Max 30 chars each)

- ETHICAL CERTIFICATION
- Three Trust Layers
- BINARY
- GRADUATED
- REGULATORY
- Fairly Trained
- A0-A3 Assurance Levels
- EU AI Act Article 50
- 19 certified entities
- Yes/No certification
- Continuous spectrum
- Mandatory labeling
- HACCP process certification
- A-F Restaurant Health Grade
- FDA federal mandate
- COMPLEMENTARY, not competing

### Caption (for embedding in documentation)

Three trust layers for ethical AI music -- binary certification (Fairly Trained, 19 entities), graduated assurance (A0-A3 levels), and mandatory regulation (EU AI Act Article 50) -- are complementary rather than competing, analogous to food safety's HACCP process certification, A-F restaurant health grades, and FDA federal mandates working together as a trust stack.

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

1. There are exactly THREE trust layers -- do NOT add or remove any.
2. Fairly Trained has 19 certified entities (as of 2025) -- do NOT invent a different count.
3. A0-A3 maps to: A0 (no data), A1 (single source), A2 (multiple sources), A3 (artist-verified) -- do NOT alter this mapping.
4. EU AI Act Article 50 covers AI-generated content labeling -- do NOT describe other articles.
5. The food safety analogy is HACCP/health grade/FDA -- do NOT substitute other analogies.
6. The key insight is COMPLEMENTARITY -- do NOT frame these as alternatives to choose between.
7. de Berardinis et al. (2025) is a real citation -- do NOT alter author name or year.
8. Do NOT imply that having all three layers is currently implemented -- this is the ASPIRATION.
9. The cross-domain analogy is the novel contribution -- give it visual prominence, not a footnote.

## Alt Text

Three trust layers compared: binary Fairly Trained, graduated A0-A3 assurance, and EU AI Act regulation with food safety analogy.

## JSON Export Block

```json
{
  "id": "fig-landscape-19",
  "title": "Ethical Certification: Binary vs Graduated vs Regulatory",
  "audience": "L2",
  "priority": "P1",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "novelty": 4,
  "trust_layers": [
    { "name": "Binary", "system": "Fairly Trained", "mechanism": "Yes/No certification", "food_analog": "HACCP" },
    { "name": "Graduated", "system": "A0-A3 Assurance", "mechanism": "Continuous spectrum", "food_analog": "A-F Health Grade" },
    { "name": "Regulatory", "system": "EU AI Act Art. 50", "mechanism": "Mandatory labeling", "food_analog": "FDA" }
  ],
  "cross_domain_analogy": "food_safety",
  "academic_reference": "de Berardinis et al. (2025)",
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component", "archetype_overlay",
    "section_numeral", "callout_bar"
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
