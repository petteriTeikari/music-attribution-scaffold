# fig-landscape-20: Voice Rights & Identity Protection: 5-Layer Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-20 |
| **Title** | Voice Rights & Identity Protection: 5-Layer Stack |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure establishes that voice rights are not a single problem but a 5-layer stack requiring coordinated solutions across consent, technology, detection, law, and compensation -- and that no single company currently spans all five layers. It answers: "What does a complete voice rights infrastructure look like, and where are the gaps?"

## Key Message

Voice rights require a 5-layer stack -- consent, cloning technology, detection, legal framework, and compensation -- and no single company covers all five layers.

## Visual Concept

Five horizontal layers stacked top-to-bottom like a network protocol stack (OSI-inspired). Each layer contains its name, key functions, and the companies operating at that layer. Right side shows a coverage matrix revealing that no entity spans all five. A coral accent line at the bottom highlights the legal underdevelopment. The stack metaphor emphasizes that voice rights need ALL layers to function, not just one.

```
+---------------------------------------------------------------+
|  VOICE RIGHTS & IDENTITY PROTECTION                            |
|  ■ Five-Layer Stack                                            |
+---------------------------------------------------------------+
|                                                  COVERAGE      |
|                                               Kits Vmod Verm   |
|  ┌─────────────────────────────────────────┐  ┌───┬───┬───┐   |
|  │  L5. COMPENSATION                       │  │   │   │   │   |
|  │  Royalty models, dynamic revenue sharing │  │   │   │   │   |
|  │  Voice usage payments                   │  │   │   │   │   |
|  ├─────────────────────────────────────────┤  ├───┼───┼───┤   |
|  │  L4. LEGAL FRAMEWORK                    │  │   │   │ ■ │   |
|  │  Right of publicity, state laws         │  │   │   │   │   |
|  │  No federal standard exists             │  │   │   │   │   |
|  ├─────────────────────────────────────────┤  ├───┼───┼───┤   |
|  │  L3. DETECTION                          │  │   │   │ ■ │   |
|  │  Voice fingerprinting, deepfake detect  │  │   │   │   │   |
|  │  Authenticity verification              │  │   │   │   │   |
|  ├─────────────────────────────────────────┤  ├───┼───┼───┤   |
|  │  L2. CLONING TECHNOLOGY                 │  │ ■ │ ■ │   │   |
|  │  Ethical voice cloning, synthesis       │  │   │   │   │   |
|  │  Kits AI, Voicemod                      │  │   │   │   │   |
|  ├─────────────────────────────────────────┤  ├───┼───┼───┤   |
|  │  L1. CONSENT                            │  │ ■ │   │   │   |
|  │  Opt-in/opt-out, SoundExchange registry │  │   │   │   │   |
|  │  Voice model licensing                  │  │   │   │   │   |
|  └─────────────────────────────────────────┘  └───┴───┴───┘   |
|                                                                |
|  ■ Voice rights are the MOST legally underdeveloped area of     |
|    music AI — no entity spans all 5 layers                      |
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
      text: "VOICE RIGHTS & IDENTITY PROTECTION"
    - type: label_editorial
      text: "Five-Layer Stack"

coverage_header:
  position: [1400, 130]
  width: 460
  height: 40
  elements:
    - type: data_mono
      text: "Kits   Vmod   Verm"

layer_5_compensation:
  position: [60, 160]
  width: 1300
  height: 140
  label: "L5. COMPENSATION"
  functions:
    - "Royalty models for voice usage"
    - "Dynamic revenue sharing"
    - "Voice-specific payment structures"
  coverage: { kits: false, voicemod: false, vermillio: false }

layer_4_legal:
  position: [60, 310]
  width: 1300
  height: 140
  label: "L4. LEGAL FRAMEWORK"
  functions:
    - "Right of publicity"
    - "State-level voice protection laws"
    - "No federal standard exists"
  coverage: { kits: false, voicemod: false, vermillio: true }

layer_3_detection:
  position: [60, 460]
  width: 1300
  height: 140
  label: "L3. DETECTION"
  functions:
    - "Voice fingerprinting"
    - "Deepfake detection"
    - "Authenticity verification"
  coverage: { kits: false, voicemod: false, vermillio: true }

layer_2_cloning:
  position: [60, 610]
  width: 1300
  height: 140
  label: "L2. CLONING TECHNOLOGY"
  functions:
    - "Ethical voice cloning"
    - "Voice synthesis"
    - "Artist-authorized models"
  coverage: { kits: true, voicemod: true, vermillio: false }

layer_1_consent:
  position: [60, 760]
  width: 1300
  height: 140
  label: "L1. CONSENT"
  functions:
    - "Opt-in/opt-out mechanisms"
    - "SoundExchange registry"
    - "Voice model licensing agreements"
  coverage: { kits: true, voicemod: false, vermillio: false }

coverage_matrix:
  position: [1400, 160]
  width: 460
  height: 740
  columns: ["Kits AI", "Voicemod", "Vermillio"]
  note: "No single entity spans all 5 layers"

callout_bottom:
  position: [60, 940]
  width: 1800
  height: 100
  elements:
    - type: callout_bar
      text: "Voice rights are the MOST legally underdeveloped area of music AI"
    - type: label_editorial
      text: "No entity spans all 5 layers"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "VOICE RIGHTS & IDENTITY PROTECTION" with coral accent square |
| Subtitle | `label_editorial` | "Five-Layer Stack" |
| Layer 5 | `processing_stage` | Compensation: royalty models, dynamic revenue sharing |
| Layer 4 | `processing_stage` | Legal framework: right of publicity, no federal standard |
| Layer 3 | `processing_stage` | Detection: voice fingerprinting, deepfake detection |
| Layer 2 | `processing_stage` | Cloning technology: ethical voice cloning, synthesis |
| Layer 1 | `processing_stage` | Consent: opt-in/opt-out, SoundExchange registry |
| Coverage matrix | `archetype_overlay` | Which companies operate at which layers |
| Kits AI column | `stakeholder_platform` | Coverage: L1 consent + L2 cloning |
| Voicemod column | `stakeholder_platform` | Coverage: L2 cloning only |
| Vermillio column | `stakeholder_platform` | Coverage: L3 detection + L4 legal |
| Gap indicator | `problem_statement` | L5 compensation — no company covers this layer |
| Legal callout | `callout_bar` | "Most legally underdeveloped area of music AI" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| L1 Consent | L2 Cloning | dependency | "Consent enables ethical cloning" |
| L2 Cloning | L3 Detection | creates_need | "Cloning creates need for detection" |
| L3 Detection | L4 Legal | supports | "Detection enables legal enforcement" |
| L4 Legal | L5 Compensation | enables | "Legal framework enables compensation" |
| Coverage matrix | Gap indicator | reveals | "No entity spans all 5" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Legal Gap | "Voice rights are the MOST legally underdeveloped area of music AI" | Bottom bar |
| Coverage Gap | "No single entity spans all 5 layers" | Below coverage matrix |
| Federal Gap | "No US federal standard for voice rights exists" | Within L4 panel |

## Text Content

### Labels (Max 30 chars each)

- VOICE RIGHTS & IDENTITY
- Five-Layer Stack
- L5. COMPENSATION
- L4. LEGAL FRAMEWORK
- L3. DETECTION
- L2. CLONING TECHNOLOGY
- L1. CONSENT
- Royalty models
- Dynamic revenue sharing
- Right of publicity
- No federal standard
- Voice fingerprinting
- Deepfake detection
- Ethical voice cloning
- SoundExchange registry
- Kits AI
- Voicemod
- Vermillio
- No entity spans all 5

### Caption (for embedding in documentation)

Voice rights require a five-layer infrastructure stack: consent (opt-in/opt-out, SoundExchange), cloning technology (Kits AI, Voicemod), detection (voice fingerprinting, deepfake detection), legal framework (right of publicity, no federal standard), and compensation (royalty models, revenue sharing). No single company spans all five layers, and voice rights remain the most legally underdeveloped area of music AI.

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

1. There are exactly FIVE layers -- do NOT add or remove any.
2. The layers are ordered top-to-bottom from compensation to consent, like a protocol stack.
3. Kits AI covers L1 (consent) + L2 (cloning) -- do NOT attribute other layers.
4. Voicemod covers L2 (cloning) only -- do NOT attribute consent or detection.
5. Vermillio covers L3 (detection) + L4 (legal) -- do NOT attribute cloning or consent.
6. L5 (compensation) has NO company coverage currently -- do NOT invent coverage.
7. "No federal standard" refers to US law -- do NOT claim there is a federal voice rights statute.
8. SoundExchange registry is a real initiative -- do NOT describe as hypothetical.
9. The stack metaphor implies ALL layers are needed -- do NOT imply one layer alone is sufficient.
10. Do NOT conflate voice cloning with general audio generation -- these are IDENTITY-specific rights.

## Alt Text

Five-layer voice rights stack from consent to compensation, with coverage matrix showing no company spans all layers.

## JSON Export Block

```json
{
  "id": "fig-landscape-20",
  "title": "Voice Rights & Identity Protection: 5-Layer Stack",
  "audience": "L2",
  "priority": "P1",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "novelty": 4,
  "layers": [
    { "number": "L1", "name": "Consent", "functions": ["opt-in/opt-out", "SoundExchange registry", "voice model licensing"] },
    { "number": "L2", "name": "Cloning Technology", "functions": ["ethical voice cloning", "voice synthesis"] },
    { "number": "L3", "name": "Detection", "functions": ["voice fingerprinting", "deepfake detection"] },
    { "number": "L4", "name": "Legal Framework", "functions": ["right of publicity", "state laws", "no federal standard"] },
    { "number": "L5", "name": "Compensation", "functions": ["royalty models", "dynamic revenue sharing"] }
  ],
  "coverage": [
    { "company": "Kits AI", "layers": ["L1", "L2"] },
    { "company": "Voicemod", "layers": ["L2"] },
    { "company": "Vermillio", "layers": ["L3", "L4"] }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage", "archetype_overlay",
    "stakeholder_platform", "problem_statement", "callout_bar"
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
