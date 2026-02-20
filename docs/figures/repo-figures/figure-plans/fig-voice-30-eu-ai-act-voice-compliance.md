# fig-voice-30: EU AI Act: Voice Agent Compliance Checklist

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-30 |
| **Title** | EU AI Act: Voice Agent Compliance Checklist |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Present the five key EU AI Act compliance requirements specifically relevant to voice agents, laid out as vertical implementation steps with a timeline bar showing enforcement dates. Answers: "What does the EU AI Act require of voice agent systems, and when does enforcement begin?"

## Key Message

The EU AI Act imposes five specific obligations on voice agent systems: AI disclosure in voice interactions (Article 50), synthetic audio labeling for all TTS output, explicit consent for voice cloning, transparency documentation, and risk classification. Voice agents likely fall in the "limited risk" tier. Enforcement begins August 2026 -- systems must comply by then.

## Visual Concept

Five vertical steps (Template E) arranged top-to-bottom, each labeled with a Roman numeral and the specific EU AI Act provision. Each step includes the requirement title, a brief description, and an implementation note. A horizontal timeline bar at the bottom shows the enforcement schedule through August 2026. The steps descend from most immediately actionable (Article 50 disclosure) to most strategic (risk classification).

```
+-------------------------------------------------------------------+
|  EU AI ACT: VOICE AGENT COMPLIANCE                           [sq]   |
|  -- Five Requirements for Voice Systems                            |
+-------------------------------------------------------------------+
|                                                                    |
|  I. ARTICLE 50 DISCLOSURE                                          |
|  ─────────────────────────                                         |
|  ■ Voice agent MUST identify itself as an AI system                |
|  ■ Clear disclosure at start of every voice interaction            |
|  ■ Implementation: "I'm an AI assistant for music attribution"     |
|                                                           [line]   |
|                                                                    |
|  II. SYNTHETIC AUDIO LABELING                                      |
|  ────────────────────────────                                      |
|  ■ ALL TTS output must be marked as AI-generated                   |
|  ■ Machine-readable watermark in audio stream                      |
|  ■ Implementation: C2PA metadata + audio watermarking              |
|                                                           [line]   |
|                                                                    |
|  III. DEEPFAKE PROVISIONS                                          |
|  ────────────────────────                                          |
|  ■ Voice cloning requires explicit, informed consent               |
|  ■ Applies to digital twin / persona features                     |
|  ■ Implementation: Consent framework + MCP permission queries      |
|                                                           [line]   |
|                                                                    |
|  IV. TRANSPARENCY REQUIREMENTS                                     |
|  ──────────────────────────────                                    |
|  ■ Document training data sources and model capabilities           |
|  ■ Publish technical documentation for deployers                   |
|  ■ Implementation: Model cards + data provenance chain             |
|                                                           [line]   |
|                                                                    |
|  V. RISK CLASSIFICATION                                            |
|  ──────────────────────                                            |
|  ■ Voice agents likely classified as "limited risk"                |
|  ■ Not "high risk" unless used for biometric identification        |
|  ■ Implementation: Self-assessment + documentation                 |
|                                                                    |
|  ─────────────────────────────────────────────── [accent line]     |
|                                                                    |
|  TIMELINE                                                          |
|  ┌────────┬────────┬────────┬────────┬────────┐                   |
|  │ Feb 26 │ Apr 26 │ Jun 26 │ Aug 26 │ 2027+  │                   |
|  │ NOW    │ Prep   │ Test   │ ENFORCE│ Audit  │                   |
|  └────────┴────────┴────────┴────────┴────────┘                   |
|                                                                    |
+-------------------------------------------------------------------+
|  YOUR VOICE AGENT MUST IDENTIFY ITSELF AS AI --                    |
|  ENFORCEMENT BEGINS AUG 2026                                       |
+-------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "EU AI ACT: VOICE AGENT COMPLIANCE"
    role: title

  - id: steps_zone
    bounds: [60, 140, 1800, 600]
    role: content_area

  - id: timeline_zone
    bounds: [60, 780, 1800, 100]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "ENFORCEMENT BEGINS AUG 2026"
    role: callout_box

anchors:
  - id: step_i
    position: [480, 200]
    size: [1600, 100]
    role: processing_stage
    label: "I. ARTICLE 50 DISCLOSURE"

  - id: step_ii
    position: [480, 320]
    size: [1600, 100]
    role: processing_stage
    label: "II. SYNTHETIC AUDIO LABELING"

  - id: step_iii
    position: [480, 440]
    size: [1600, 100]
    role: processing_stage
    label: "III. DEEPFAKE PROVISIONS"

  - id: step_iv
    position: [480, 560]
    size: [1600, 100]
    role: processing_stage
    label: "IV. TRANSPARENCY REQUIREMENTS"

  - id: step_v
    position: [480, 680]
    size: [1600, 100]
    role: processing_stage
    label: "V. RISK CLASSIFICATION"

  - id: divider_i_ii
    position: [140, 260]
    size: [1640, 2]
    role: accent_line

  - id: divider_ii_iii
    position: [140, 380]
    size: [1640, 2]
    role: accent_line

  - id: divider_iii_iv
    position: [140, 500]
    size: [1640, 2]
    role: accent_line

  - id: divider_iv_v
    position: [140, 620]
    size: [1640, 2]
    role: accent_line

  - id: timeline_bar
    position: [960, 830]
    size: [1600, 60]
    role: data_flow
    label: "Feb 2026 → Aug 2026 enforcement"

  - id: timeline_now
    position: [200, 830]
    size: [120, 60]
    role: selected_option
    label: "NOW"

  - id: timeline_enforce
    position: [1360, 830]
    size: [200, 60]
    role: warning_box
    label: "ENFORCEMENT"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "EU AI ACT: VOICE AGENT COMPLIANCE" with coral accent square |
| Step I: Article 50 | `processing_stage` | AI system must identify itself in voice interactions |
| Step II: Synthetic Audio | `processing_stage` | All TTS output marked as AI-generated with machine-readable watermark |
| Step III: Deepfake Provisions | `processing_stage` | Voice cloning requires explicit consent, applies to digital twin features |
| Step IV: Transparency | `processing_stage` | Document training data, publish technical docs for deployers |
| Step V: Risk Classification | `processing_stage` | Voice agents likely "limited risk" unless biometric identification |
| Step dividers | `accent_line` | Coral accent lines separating each step |
| Timeline bar | `data_flow` | Horizontal timeline Feb 2026 through 2027+ |
| NOW marker | `selected_option` | Current position on timeline |
| ENFORCEMENT marker | `warning_box` | August 2026 enforcement date |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Step I | Step II | arrow | "sequential compliance" |
| Step II | Step III | arrow | "sequential compliance" |
| Step III | Step IV | arrow | "sequential compliance" |
| Step IV | Step V | arrow | "sequential compliance" |
| Timeline NOW | Timeline ENFORCEMENT | arrow | "6 months remaining" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "YOUR VOICE AGENT MUST IDENTIFY ITSELF AS AI -- ENFORCEMENT BEGINS AUG 2026" | Article 50 disclosure is the most immediate requirement. Systems deployed after August 2026 must comply with all five provisions. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. ARTICLE 50 DISCLOSURE"
- Label 2: "II. SYNTHETIC AUDIO LABELING"
- Label 3: "III. DEEPFAKE PROVISIONS"
- Label 4: "IV. TRANSPARENCY REQUIREMENTS"
- Label 5: "V. RISK CLASSIFICATION"
- Label 6: "Identify as AI system"
- Label 7: "Mark TTS as AI-generated"
- Label 8: "Consent for voice cloning"
- Label 9: "Document training data"
- Label 10: "Limited risk tier"
- Label 11: "Feb 2026 -- NOW"
- Label 12: "Aug 2026 -- ENFORCEMENT"
- Label 13: "C2PA metadata"
- Label 14: "MCP consent framework"
- Label 15: "Model cards"

### Caption (for embedding in documentation)

Five EU AI Act compliance requirements for voice agent systems -- Article 50 disclosure, synthetic audio labeling, deepfake consent provisions, transparency documentation, and risk classification -- with enforcement timeline through August 2026.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `selected_option`, `warning_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The EU AI Act was formally adopted in 2024. The "Article 50" reference is to the transparency obligations for AI systems that interact with humans.
10. "Limited risk" classification for voice agents is the LIKELY outcome based on current guidance -- it is NOT confirmed by a regulatory decision. Do not present as definitive.
11. If a voice agent is used for biometric identification (e.g., speaker verification for access control), it WOULD be classified as "high risk". The scaffold does not do this.
12. August 2026 is the enforcement date for the transparency and limited-risk provisions. Some high-risk provisions apply earlier (February 2025 for prohibited practices).
13. C2PA is a real content provenance standard backed by Adobe, Microsoft, and others. It can be applied to audio streams.
14. The EU AI Act requires disclosure "in a timely, clear and intelligible manner" -- the exact wording of the disclosure is not prescribed.
15. Voice cloning provisions specifically target systems that generate synthetic audio resembling a specific person -- this directly applies to digital twin features.
16. Do NOT present this as legal advice -- it is a technical interpretation of the regulation for implementation planning.

## Alt Text

Five-step EU AI Act compliance checklist for voice agent systems covering Article 50 disclosure, synthetic audio labeling, deepfake consent provisions, transparency documentation, and risk classification, with enforcement timeline from February 2026 through August 2026 deadline.

## Image Embed

![Five-step EU AI Act compliance checklist for voice agent systems covering Article 50 disclosure, synthetic audio labeling, deepfake consent provisions, transparency documentation, and risk classification, with enforcement timeline from February 2026 through August 2026 deadline.](docs/figures/repo-figures/assets/fig-voice-30-eu-ai-act-voice-compliance.jpg)

*Five EU AI Act compliance requirements for voice agent systems -- Article 50 disclosure, synthetic audio labeling, deepfake consent provisions, transparency documentation, and risk classification -- with enforcement timeline through August 2026.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-30",
    "title": "EU AI Act: Voice Agent Compliance Checklist",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Five EU AI Act requirements apply to voice agents: AI disclosure, synthetic audio labeling, deepfake consent, transparency documentation, and risk classification. Enforcement begins August 2026.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Article 50 Disclosure",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["I. ARTICLE 50 DISCLOSURE", "Identify as AI system"]
      },
      {
        "name": "Synthetic Audio Labeling",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. SYNTHETIC AUDIO LABELING", "Mark TTS as AI-generated"]
      },
      {
        "name": "Deepfake Provisions",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III. DEEPFAKE PROVISIONS", "Consent for voice cloning"]
      },
      {
        "name": "Transparency Requirements",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV. TRANSPARENCY", "Document training data"]
      },
      {
        "name": "Risk Classification",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V. RISK CLASSIFICATION", "Limited risk tier"]
      },
      {
        "name": "Timeline",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["Feb 2026 NOW", "Aug 2026 ENFORCEMENT"]
      }
    ],
    "relationships": [
      {
        "from": "Step I",
        "to": "Step V",
        "type": "arrow",
        "label": "sequential compliance steps"
      },
      {
        "from": "Timeline NOW",
        "to": "Timeline ENFORCEMENT",
        "type": "arrow",
        "label": "6 months"
      }
    ],
    "callout_boxes": [
      {
        "heading": "YOUR VOICE AGENT MUST IDENTIFY ITSELF AS AI",
        "body_text": "Enforcement begins August 2026. Article 50 disclosure is the most immediate requirement.",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
