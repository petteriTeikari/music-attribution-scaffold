# fig-landscape-31: Open Problems: Solvable (2yr) / Hard (5yr) / Fundamental

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-31 |
| **Title** | Open Problems: Solvable (2yr) / Hard (5yr) / Fundamental |
| **Audience** | L4 (AI/ML) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure maps research gaps to investor time horizons, creating an actionable research planning framework. It organizes open problems into three temporal bands -- solvable in 2 years (seed-stage, engineering problems), hard in 5 years (Series A, research breakthroughs needed), and fundamental (10+ years, grant-funded) -- while exposing the ironic inversion where the most-funded problem (generation) is technically the least hard, and the least-funded problem (attribution) is technically the hardest.

## Key Message

Research gaps mapped to investor time horizons -- solvable problems (2yr, seed-stage), hard problems (5yr, Series A), and fundamental problems (10yr+, grant-funded) -- with the irony that the most-funded problem is technically the least hard.

## Visual Concept

Three vertical panels arranged left-to-right, each representing a time horizon. Each panel contains a list of open problems with brief descriptions. The panels progress from green-coded (solvable, actionable) through amber (hard, research-dependent) to red-coded (fundamental, philosophical). A prominent callout bar at the bottom highlights the funding-difficulty inversion: a funding bar (tall for generation, short for attribution) placed next to a difficulty bar (short for generation, tall for attribution), creating a visible X-shaped inversion.

```
+---------------------------------------------------------------+
|  OPEN PROBLEMS                                                 |
|  ■ Mapped to Investor Time Horizons                            |
+---------------------------------------------------------------+
|                    |                    |                       |
|  SOLVABLE (2yr)    |  HARD (5yr)        |  FUNDAMENTAL (10yr+) |
|  Seed-Stage        |  Series A          |  Grant-Funded        |
|  ─────────────     |  ──────────        |  ─────────────       |
|                    |                    |                       |
|  ■ Metadata        |  ■ Cross-model     |  ■ The Oracle        |
|    interoperablty  |    TDA             |    Problem           |
|    Engineering     |    Which model     |    Digital cannot     |
|    problem, not    |    generated this? |    verify physical    |
|    research        |    Needs new       |    /training reality  |
|                    |    embeddings      |                       |
|  ■ Real-time       |                    |  ■ Compositional vs  |
|    fingerprinting  |  ■ Multimodal      |    Recording Rights  |
|    Scale existing  |    attribution     |    Separation at     |
|    methods to      |    Beyond audio    |    scale             |
|    streaming       |    to lyrics,      |    Legal + technical  |
|                    |    video, style    |    entanglement      |
|  ■ Basic embedding |                    |                       |
|    attribution     |  ■ Federated       |  ■ Cultural Context  |
|    Single-model    |    attribution     |    in Attribution    |
|    TDA with known  |    Cross-CMO       |    Same notes =      |
|    architecture    |    privacy-safe    |    different meaning  |
|                    |    coordination    |    across cultures   |
|  ■ Binary AI       |                    |                       |
|    detection       |  ■ Robust          |                       |
|    Human vs AI     |    watermarking    |                       |
|    (not which AI)  |    Survives codec  |                       |
|                    |    + manipulation  |                       |
+---------------------------------------------------------------+
|                                                                |
|  THE FUNDING-DIFFICULTY INVERSION                              |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │ Generation:  ████████████ $375M+  │ Difficulty: ██░░░░  │   |
|  │ Attribution: ███░░░░░░░░ $70M     │ Difficulty: ██████  │   |
|  │                                                         │   |
|  │ ■ Funding inversely correlates with technical difficulty │   |
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
      text: "OPEN PROBLEMS"
    - type: label_editorial
      text: "Mapped to Investor Time Horizons"

panel_solvable:
  position: [60, 140]
  width: 560
  height: 580
  label: "SOLVABLE (2yr) — Seed-Stage"
  confidence_tag: confidence_high
  elements:
    - type: heading_display
      text: "SOLVABLE (2yr)"
    - type: label_editorial
      text: "Seed-Stage — Engineering Problems"
    - problems:
      - { type: solution_component, name: "Metadata interoperability", detail: "Engineering problem: harmonize ISRC, ISWC, ISNI across registries. Standards exist, implementation lags." }
      - { type: solution_component, name: "Real-time fingerprinting", detail: "Scale existing Chromaprint/Dejavu methods to streaming latency. Optimization, not invention." }
      - { type: solution_component, name: "Basic embedding attribution", detail: "Single-model TDA with known architecture. CLAP embeddings + cosine similarity + conformal bounds." }
      - { type: solution_component, name: "Binary AI detection", detail: "Human vs AI classification (not which AI model). Afchar ICASSP methods, EU AI Act Art. 50 driver." }

panel_hard:
  position: [660, 140]
  width: 560
  height: 580
  label: "HARD (5yr) — Series A"
  confidence_tag: confidence_medium
  elements:
    - type: heading_display
      text: "HARD (5yr)"
    - type: label_editorial
      text: "Series A — Research Breakthroughs Needed"
    - problems:
      - { type: problem_statement, name: "Cross-model TDA", detail: "Which specific model generated this audio? Requires model-specific embedding signatures. Active research area." }
      - { type: problem_statement, name: "Multimodal attribution", detail: "Extend TDA beyond audio to lyrics, video, style transfer. No existing frameworks for multimodal music attribution." }
      - { type: problem_statement, name: "Federated attribution", detail: "Multi-CMO coordination without sharing proprietary catalog data. Requires privacy-preserving ML (FL, MPC)." }
      - { type: problem_statement, name: "Robust watermarking", detail: "Watermarks that survive codec conversion, remastering, and adversarial manipulation. Active arms race." }

panel_fundamental:
  position: [1260, 140]
  width: 560
  height: 580
  label: "FUNDAMENTAL (10yr+) — Grant-Funded"
  confidence_tag: confidence_low
  elements:
    - type: heading_display
      text: "FUNDAMENTAL (10yr+)"
    - type: label_editorial
      text: "Grant-Funded — May Not Be Fully Solvable"
    - problems:
      - { type: problem_statement, name: "The Oracle Problem", detail: "Digital systems cannot fully verify physical/training reality. Design for deterrence, not detection. Manuscript core thesis." }
      - { type: problem_statement, name: "Compositional vs Recording Rights", detail: "Legal and technical entanglement: same composition, different recordings, different rights chains. Separation at scale is unsolved." }
      - { type: problem_statement, name: "Cultural Context in Attribution", detail: "Same note sequence has different meaning across cultures. Attribution confidence must account for cultural framing. No formal models exist." }

funding_inversion:
  position: [60, 760]
  width: 1800
  height: 200
  label: "THE FUNDING-DIFFICULTY INVERSION"
  elements:
    - type: callout_bar
      text: "Funding inversely correlates with technical difficulty"
    - { type: data_mono, text: "Generation: $375M+ funded, technically easier (known architectures, clear evaluation metrics)" }
    - { type: data_mono, text: "Attribution: $70M funded, technically harder (oracle problem, cross-domain, cultural context)" }
    - { type: label_editorial, text: "The most-funded problem is technically the least hard" }
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "OPEN PROBLEMS" with coral accent square |
| Subtitle | `label_editorial` | "Mapped to Investor Time Horizons" |
| Solvable panel | `confidence_high` | 2yr problems: metadata interop, real-time fingerprinting, basic TDA, binary detection |
| Hard panel | `confidence_medium` | 5yr problems: cross-model TDA, multimodal attribution, federated attribution, robust watermarking |
| Fundamental panel | `confidence_low` | 10yr+ problems: Oracle Problem, compositional vs recording rights, cultural context |
| Problem entries | `solution_component` / `problem_statement` | Individual problem descriptions with time-to-solution |
| Funding inversion box | `callout_bar` | Prominent visual showing $375M generation vs $70M attribution |
| Funding bars | `data_mono` | Visual bars showing funding-difficulty inversion |
| Panel headers | `section_numeral` | Time horizon labels for each panel |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Solvable problems | Hard problems | prerequisite | "Solving metadata enables cross-model TDA" |
| Hard problems | Fundamental | dependency | "Federated attribution exposes Oracle Problem" |
| Binary detection | Cross-model TDA | progression | "Which AI → which specific model" |
| Basic TDA | Multimodal | extension | "Audio-only → multimodal" |
| Generation funding | Attribution funding | inversion | "$375M vs $70M — inverse of difficulty" |
| Oracle Problem | All attribution | constraint | "Fundamental limit on verification confidence" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| The Irony | "The most-funded problem (generation) is technically the least hard; the least-funded (attribution) is the hardest" | Bottom center, prominent |
| Seed-Stage Opportunity | "Solvable problems are engineering, not research -- startups can ship in 2 years with known methods" | Below solvable panel |
| The Oracle Problem | "Design for deterrence, not detection -- digital systems cannot fully verify physical/training reality" | Inside fundamental panel |

## Text Content

### Labels (Max 30 chars each)

- SOLVABLE (2yr)
- HARD (5yr)
- FUNDAMENTAL (10yr+)
- Seed-Stage
- Series A
- Grant-Funded
- Metadata Interoperability
- Real-Time Fingerprinting
- Basic Embedding Attribution
- Binary AI Detection
- Cross-Model TDA
- Multimodal Attribution
- Federated Attribution
- Robust Watermarking
- The Oracle Problem
- Comp. vs Recording Rights
- Cultural Context
- Funding-Difficulty Inversion
- Generation: $375M+
- Attribution: $70M

### Caption (for embedding in documentation)

Open research problems in music attribution mapped to investor time horizons: solvable in 2 years (metadata interoperability, real-time fingerprinting, basic embedding attribution, binary AI detection -- engineering problems suitable for seed-stage startups), hard in 5 years (cross-model TDA, multimodal attribution, federated attribution, robust watermarking -- research breakthroughs needed for Series A), and fundamental at 10+ years (the Oracle Problem, compositional vs recording rights separation, cultural context in attribution -- grant-funded long-term research that may not be fully solvable). The ironic funding-difficulty inversion: generation ($375M+ funded) is technically easier than attribution ($70M funded), with funding inversely correlated to technical difficulty.

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

1. There are exactly THREE time horizons (2yr, 5yr, 10yr+) -- do NOT add intermediate bands.
2. The Oracle Problem is from the MANUSCRIPT -- do NOT invent or rename it.
3. Funding figures ($375M generation, $70M attribution) are from landscape analysis -- present as ORDER-OF-MAGNITUDE estimates, not precise figures.
4. "Solvable" means ENGINEERING problems, not trivial -- do NOT diminish the work required.
5. "Fundamental" means MAY NOT BE FULLY SOLVABLE -- do NOT promise future solutions.
6. The funding-difficulty inversion is an OBSERVATION, not a criticism of investors -- do NOT editorialize.
7. Do NOT conflate "binary AI detection" (human vs AI) with "cross-model TDA" (which specific model) -- they are DIFFERENT problems in different time bands.
8. Do NOT list specific company names in the problem descriptions -- these are RESEARCH problems, not product gaps.
9. Cultural context in attribution is a REAL unsolved problem -- do NOT trivialize or reduce to "internationalization."
10. The Oracle Problem applies to ALL attribution, not just music -- but music is the domain of application here.

## Alt Text

Three-panel open problems by time horizon: solvable 2yr, hard 5yr, fundamental 10yr+ with funding inversion.

## JSON Export Block

```json
{
  "id": "fig-landscape-31",
  "title": "Open Problems: Solvable (2yr) / Hard (5yr) / Fundamental",
  "audience": "L4",
  "priority": "P1",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 4,
  "time_horizons": [
    {
      "horizon": "2yr",
      "label": "Solvable",
      "investor_stage": "Seed",
      "problem_type": "Engineering",
      "problems": [
        { "name": "Metadata interoperability", "nature": "Standards exist, implementation lags" },
        { "name": "Real-time fingerprinting", "nature": "Scale existing methods to streaming latency" },
        { "name": "Basic embedding attribution", "nature": "Single-model TDA with known architecture" },
        { "name": "Binary AI detection", "nature": "Human vs AI, not which AI model" }
      ]
    },
    {
      "horizon": "5yr",
      "label": "Hard",
      "investor_stage": "Series A",
      "problem_type": "Research breakthrough needed",
      "problems": [
        { "name": "Cross-model TDA", "nature": "Model-specific embedding signatures" },
        { "name": "Multimodal attribution", "nature": "Beyond audio to lyrics, video, style" },
        { "name": "Federated attribution", "nature": "Privacy-preserving cross-CMO coordination" },
        { "name": "Robust watermarking", "nature": "Survives codec + adversarial manipulation" }
      ]
    },
    {
      "horizon": "10yr+",
      "label": "Fundamental",
      "investor_stage": "Grant-funded",
      "problem_type": "May not be fully solvable",
      "problems": [
        { "name": "The Oracle Problem", "nature": "Digital cannot verify physical/training reality" },
        { "name": "Compositional vs Recording Rights", "nature": "Legal-technical entanglement at scale" },
        { "name": "Cultural Context in Attribution", "nature": "Same notes, different meaning across cultures" }
      ]
    }
  ],
  "funding_inversion": {
    "generation_funding": "$375M+",
    "attribution_funding": "$70M",
    "insight": "Funding inversely correlates with technical difficulty"
  },
  "semantic_tags_used": [
    "heading_display", "label_editorial", "confidence_high", "confidence_medium",
    "confidence_low", "solution_component", "problem_statement", "callout_bar",
    "data_mono", "section_numeral"
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
