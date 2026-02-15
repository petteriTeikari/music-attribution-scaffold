# fig-landscape-28: Five Emerging Service Categories 2026

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-28 |
| **Title** | Five Emerging Service Categories 2026 |
| **Audience** | L1 (Music Industry) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure identifies five new service categories crystallizing in 2026 at the intersection of music, AI, and attribution infrastructure. Each represents a distinct startup opportunity with quantifiable market size, existing players, and barriers to entry. It provides a market map for investors, entrepreneurs, and strategic planners.

## Key Message

Five new service categories are emerging in 2026 -- Attribution-as-a-Service, Ethical Certification-aaS, Voice Rights Management, CMO Federation Infrastructure, and AI Detection APIs -- each representing a startup opportunity.

## Visual Concept

Five horizontal panels stacked vertically, each representing one service category. Each panel contains: category name (left, large editorial type), market intelligence (center: TAM, existing players, barriers), and maturity timeline (right, showing estimated years to maturity). Coral accent squares mark each category number. A subtle gradient from "market-ready" (top) to "nascent" (bottom) orders the panels by investability.

```
+---------------------------------------------------------------+
|  FIVE EMERGING SERVICE CATEGORIES 2026                         |
|  ■ New Markets at the Music-AI-Attribution Intersection        |
+---------------------------------------------------------------+
|                                                                |
|  ■ I. ATTRIBUTION-AS-A-SERVICE (AaaS)                         |
|  ───────────────────────────────────────────────────────────   |
|  Model: Sureel      TAM: $10M+     Barriers: data access      |
|  B2B API for attribution computation                           |
|  Players: Sureel, Pex, Audible Magic                           |
|  Timeline: ████████░░ Market-ready 2026                        |
|                                                                |
|  ■ II. ETHICAL CERTIFICATION-AAS                               |
|  ───────────────────────────────────────────────────────────   |
|  Model: Fairly Trained   TAM: $5M+   Barriers: trust, audit   |
|  Trust signaling for AI companies re: training data            |
|  Players: Fairly Trained, RIAA, IFPI                           |
|  Timeline: ██████░░░░ Growing 2026-2027                        |
|                                                                |
|  ■ III. VOICE RIGHTS MANAGEMENT                                |
|  ───────────────────────────────────────────────────────────   |
|  Model: Kits AI/Voicemod   TAM: $8M+   Barriers: legal        |
|  Consent + cloning + detection + compensation                  |
|  Players: Kits AI, Voicemod, Respeecher                        |
|  Timeline: █████░░░░░ Emerging 2026-2027                       |
|                                                                |
|  ■ IV. CMO FEDERATION INFRASTRUCTURE                           |
|  ───────────────────────────────────────────────────────────   |
|  Model: STIM pilot    TAM: $15M+    Barriers: institutional    |
|  Multi-CMO coordination tools for cross-border royalties       |
|  Players: STIM, CISAC, ICE                                     |
|  Timeline: ████░░░░░░ Piloting 2026-2028                       |
|                                                                |
|  ■ V. AI DETECTION APIs                                        |
|  ───────────────────────────────────────────────────────────   |
|  Model: Afchar ICASSP   TAM: $20M+   Barriers: cat-and-mouse  |
|  B2B detection for platforms, regulatory mandate EU AI Act      |
|  Players: Hive Moderation, Originality.AI, Reality Defender     |
|  Timeline: ███████░░░ Regulatory push 2026                     |
|                                                                |
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
      text: "FIVE EMERGING SERVICE CATEGORIES 2026"
    - type: label_editorial
      text: "New Markets at the Music-AI-Attribution Intersection"

panel_aaas:
  position: [60, 140]
  width: 1800
  height: 160
  label: "I. ATTRIBUTION-AS-A-SERVICE"
  elements:
    - { type: heading_display, text: "Attribution-as-a-Service" }
    - { type: label_editorial, text: "Model: Sureel — B2B API for attribution computation" }
    - { type: data_mono, text: "TAM: $10M+ | Barriers: data access, catalog coverage" }
    - { type: data_mono, text: "Players: Sureel, Pex, Audible Magic" }
    - { type: data_mono, text: "Maturity: Market-ready 2026" }

panel_certification:
  position: [60, 320]
  width: 1800
  height: 160
  label: "II. ETHICAL CERTIFICATION-AAS"
  elements:
    - { type: heading_display, text: "Ethical Certification-aaS" }
    - { type: label_editorial, text: "Model: Fairly Trained — trust signaling for AI training data" }
    - { type: data_mono, text: "TAM: $5M+ | Barriers: trust building, audit methodology" }
    - { type: data_mono, text: "Players: Fairly Trained, RIAA, IFPI certification programs" }
    - { type: data_mono, text: "Maturity: Growing 2026-2027" }

panel_voice:
  position: [60, 500]
  width: 1800
  height: 160
  label: "III. VOICE RIGHTS MANAGEMENT"
  elements:
    - { type: heading_display, text: "Voice Rights Management" }
    - { type: label_editorial, text: "Model: Kits AI — consent + cloning + detection + compensation" }
    - { type: data_mono, text: "TAM: $8M+ | Barriers: legal frameworks underdeveloped" }
    - { type: data_mono, text: "Players: Kits AI, Voicemod, Respeecher" }
    - { type: data_mono, text: "Maturity: Emerging 2026-2027" }

panel_cmo:
  position: [60, 680]
  width: 1800
  height: 160
  label: "IV. CMO FEDERATION INFRASTRUCTURE"
  elements:
    - { type: heading_display, text: "CMO Federation Infrastructure" }
    - { type: label_editorial, text: "Model: STIM pilot — multi-CMO coordination for cross-border royalties" }
    - { type: data_mono, text: "TAM: $15M+ | Barriers: institutional inertia, data standards" }
    - { type: data_mono, text: "Players: STIM, CISAC, ICE" }
    - { type: data_mono, text: "Maturity: Piloting 2026-2028" }

panel_detection:
  position: [60, 860]
  width: 1800
  height: 160
  label: "V. AI DETECTION APIs"
  elements:
    - { type: heading_display, text: "AI Detection APIs" }
    - { type: label_editorial, text: "Model: Afchar ICASSP — B2B detection for platforms" }
    - { type: data_mono, text: "TAM: $20M+ | Barriers: adversarial cat-and-mouse, false positives" }
    - { type: data_mono, text: "Players: Hive Moderation, Originality.AI, Reality Defender" }
    - { type: data_mono, text: "Maturity: Regulatory push (EU AI Act Art. 50) 2026" }
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FIVE EMERGING SERVICE CATEGORIES 2026" with coral accent square |
| Subtitle | `label_editorial` | "New Markets at the Music-AI-Attribution Intersection" |
| AaaS panel | `solution_component` | Attribution-as-a-Service: B2B API for attribution computation |
| Certification panel | `solution_component` | Ethical Certification: trust signaling for AI training data |
| Voice panel | `solution_component` | Voice Rights Management: consent + cloning + detection + compensation |
| CMO panel | `solution_component` | CMO Federation Infrastructure: multi-CMO coordination tools |
| Detection panel | `solution_component` | AI Detection APIs: B2B detection for platforms under regulatory mandate |
| TAM indicators | `data_mono` | Total addressable market estimates per category |
| Player lists | `data_mono` | Existing companies in each category |
| Maturity timelines | `data_mono` | Estimated timeline to market maturity |
| Panel dividers | `callout_bar` | Coral accent lines between panels |
| Panel numerals | `section_numeral` | Roman numerals I-V for each category |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| AaaS | Certification | complementary | "Attribution feeds certification evidence" |
| Voice Rights | AaaS | dependency | "Voice attribution is a subset of general attribution" |
| CMO Federation | AaaS | enabling | "Federated data enables broader attribution" |
| AI Detection | Certification | complementary | "Detection validates certification claims" |
| EU AI Act Art. 50 | Detection APIs | regulatory_driver | "Mandatory transparency labeling" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Regulatory Tailwind | "EU AI Act Article 50 mandates AI content labeling -- detection APIs get regulatory push" | Right of detection panel |
| Investment Gap | "Combined TAM $58M+ but vastly underfunded compared to generation ($375M+)" | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- Attribution-as-a-Service
- Ethical Certification-aaS
- Voice Rights Management
- CMO Federation Infra
- AI Detection APIs
- TAM
- Barriers to Entry
- Existing Players
- Maturity Timeline
- Sureel Model
- Fairly Trained Model
- Kits AI / Voicemod Model
- STIM Pilot Model
- Afchar ICASSP Model
- EU AI Act Article 50

### Caption (for embedding in documentation)

Five new service categories are crystallizing in 2026 at the music-AI-attribution intersection: Attribution-as-a-Service (Sureel model, $10M+ TAM), Ethical Certification-aaS (Fairly Trained model, trust signaling), Voice Rights Management (Kits AI model, legally underdeveloped), CMO Federation Infrastructure (STIM pilot scaling globally), and AI Detection APIs (Afchar ICASSP model, EU AI Act Article 50 mandate). Each represents a distinct startup opportunity with identified players, barriers, and maturity timelines.

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

1. There are exactly FIVE categories -- do NOT add or remove any.
2. TAM figures are ESTIMATES based on landscape analysis -- do NOT present as audited market research.
3. Named companies (Sureel, Fairly Trained, Kits AI, STIM, Afchar) are REAL entities -- do NOT invent fictional companies.
4. EU AI Act Article 50 is a SPECIFIC legal provision -- do NOT generalize to "regulation."
5. "Ethical Certification" is about TRAINING DATA provenance, not general AI ethics -- do NOT conflate.
6. Voice Rights Management covers FOUR sub-problems (consent, cloning, detection, compensation) -- do NOT reduce to just "voice cloning."
7. CMO Federation is about INFRASTRUCTURE, not policy -- do NOT confuse with CISAC policy advocacy.
8. Do NOT rank categories by investment attractiveness -- present as parallel opportunities.
9. Do NOT imply any single company dominates a category -- these are EMERGING markets.

## Alt Text

Five emerging 2026 service categories: attribution-aaS, ethical certification, voice rights, CMO federation, AI detection.

## JSON Export Block

```json
{
  "id": "fig-landscape-28",
  "title": "Five Emerging Service Categories 2026",
  "audience": "L1",
  "priority": "P1",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 4,
  "categories": [
    {
      "name": "Attribution-as-a-Service (AaaS)",
      "model_company": "Sureel",
      "tam_estimate": "$10M+",
      "barriers": "data access, catalog coverage",
      "players": ["Sureel", "Pex", "Audible Magic"],
      "maturity": "Market-ready 2026"
    },
    {
      "name": "Ethical Certification-aaS",
      "model_company": "Fairly Trained",
      "tam_estimate": "$5M+",
      "barriers": "trust building, audit methodology",
      "players": ["Fairly Trained", "RIAA", "IFPI"],
      "maturity": "Growing 2026-2027"
    },
    {
      "name": "Voice Rights Management",
      "model_company": "Kits AI",
      "tam_estimate": "$8M+",
      "barriers": "legal frameworks underdeveloped",
      "players": ["Kits AI", "Voicemod", "Respeecher"],
      "maturity": "Emerging 2026-2027"
    },
    {
      "name": "CMO Federation Infrastructure",
      "model_company": "STIM",
      "tam_estimate": "$15M+",
      "barriers": "institutional inertia, data standards",
      "players": ["STIM", "CISAC", "ICE"],
      "maturity": "Piloting 2026-2028"
    },
    {
      "name": "AI Detection APIs",
      "model_company": "Afchar (ICASSP)",
      "tam_estimate": "$20M+",
      "barriers": "adversarial cat-and-mouse, false positives",
      "players": ["Hive Moderation", "Originality.AI", "Reality Defender"],
      "maturity": "Regulatory push 2026",
      "regulatory_driver": "EU AI Act Article 50"
    }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component",
    "data_mono", "callout_bar", "section_numeral"
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
