# fig-pitch-adv-12: Voice Agent Upsell Path: 3x Pricing, Pro Tier Launch (M9+)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | pitch-adv-12 |
| **Title** | Voice Agent Upsell Path: 3x Pricing, Pro Tier Launch (M9+) |
| **Audience** | L1/L2 (Music Industry + PhD/Policy) |
| **Location** | docs/planning/managerial-roadmap-planning.md, pitch deck |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure shows voice as premium upsell with pricing progression and revenue projection. It answers: "How does voice create a premium pricing tier?"

## Key Message

Voice agent as Pro tier upsell -- mic animation + example queries in MVP (aspirational), full Pipecat implementation at M9+, 3x pricing premium ($49/mo Pro vs Free), with projected voice-specific ARR.

## Visual Concept

A three-panel horizontal flow. Panel 1: Voice UI mockup -- mic button, example queries ("What are Imogen Heap's co-writers?", "Suggest missing credits"), waveform animation, "PRO" badge. Panel 2: Pricing tiers -- Free ($0, no voice) to Pro ($49/mo, voice + batch). Panel 3: Revenue projection curve for voice tier specifically, with annotations at M9 (launch), M12 (100 users), M18 (contribution to ARR). Bottom callout: "Voice requires infrastructure costs = defensible against forks."

```
+---------------------------------------------------------------+
|  VOICE AGENT UPSELL                                            |
|  ■ 3x Pricing, Pro Tier Launch (M9+)                           |
+---------------------------------------------------------------+
|                                                                |
|  PANEL 1: VOICE UI          PANEL 2: TIERS    PANEL 3: ARR    |
|  ┌────────────────┐        ┌──────────┐      ┌──────────┐     |
|  │                 │        │          │      │          │     |
|  │  ┌───┐  PRO    │        │  FREE    │      │     /──  │     |
|  │  │ 🎤 │ badge   │        │  $0/mo   │      │    /     │     |
|  │  └───┘          │        │  No voice│      │   /      │     |
|  │                 │        │          │      │  /       │     |
|  │  "What are      │        │  ── ── ──│      │ /        │     |
|  │   Imogen Heap's │        │          │      │/         │     |
|  │   co-writers?"  │        │  PRO     │      ├──────────│     |
|  │                 │        │  $49/mo  │      │M9  M12 M18│    |
|  │  "Suggest       │        │  Voice + │      │          │     |
|  │   missing       │        │  Batch   │      │ Launch   │     |
|  │   credits"      │        │          │      │ 100 users│     |
|  │                 │        │  3x      │      │ ARR      │     |
|  │  ≋≋≋≋≋≋≋≋≋≋≋    │        │  premium │      │ contrib  │     |
|  │  waveform       │        │          │      │          │     |
|  └────────────────┘        └──────────┘      └──────────┘     |
|                                                                |
|  Pipecat: $0.02/conv vs Vapi $0.12/conv = 6x savings          |
|                                                                |
+---------------------------------------------------------------+
|  ■ "Voice requires infrastructure costs = defensible against   |
|     open-source forks"                                         |
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
      text: "VOICE AGENT UPSELL"
    - type: label_editorial
      text: "3x Pricing, Pro Tier Launch (M9+)"

voice_ui_panel:
  position: [60, 160]
  width: 580
  height: 640
  elements:
    - type: label_editorial
      text: "VOICE UI MOCKUP"
    - type: mockup_voice
      mic_button: true
      pro_badge: true
      example_queries:
        - "What are Imogen Heap's co-writers?"
        - "Suggest missing credits"
      waveform: true
      annotation: "Aspirational in MVP -- UI only"

pricing_panel:
  position: [700, 160]
  width: 520
  height: 640
  elements:
    - type: label_editorial
      text: "PRICING TIERS"
    - type: pricing_table
      tiers:
        - { name: "Free", price: "$0/mo", features: ["No voice", "Basic attribution"] }
        - { name: "Pro", price: "$49/mo", features: ["Voice agent", "Batch review", "Priority support"] }
      annotation: "3x pricing premium"

revenue_panel:
  position: [1280, 160]
  width: 580
  height: 640
  elements:
    - type: label_editorial
      text: "VOICE TIER ARR"
    - type: revenue_curve
      milestones:
        - { month: "M9", label: "Launch" }
        - { month: "M12", label: "100 users" }
        - { month: "M18", label: "ARR contribution" }

cost_comparison:
  position: [60, 820]
  width: 1800
  height: 40
  elements:
    - type: label_editorial
      text: "Pipecat: $0.02/conv vs Vapi $0.12/conv = 6x savings"

callout_bar:
  position: [60, 900]
  width: 1800
  height: 120
  elements:
    - type: callout_bar
      text: "Voice requires infrastructure costs = defensible against open-source forks"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "VOICE AGENT UPSELL" with coral accent square |
| Subtitle | `label_editorial` | "3x Pricing, Pro Tier Launch (M9+)" |
| Voice UI panel | `processing_stage` | Mic button, example queries, waveform, PRO badge mockup |
| Pricing panel | `processing_stage` | Free ($0) vs Pro ($49/mo) tier comparison |
| Revenue panel | `processing_stage` | Voice tier ARR projection curve with milestones |
| Mic button | `selected_option` | Microphone icon with PRO badge |
| Example queries | `label_editorial` | Natural language query examples |
| Waveform animation | `label_editorial` | Voice waveform visualization |
| Cost comparison | `label_editorial` | Pipecat vs Vapi cost savings |
| Callout bar | `callout_bar` | Bottom insight statement |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Voice UI panel | Pricing panel | flow | "Voice drives Pro tier" |
| Pricing panel | Revenue panel | flow | "Pro tier drives ARR" |
| Cost comparison | Callout bar | emphasis | "Infrastructure costs = defensibility" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Cost Savings | "Pipecat: $0.02/conv vs Vapi $0.12/conv = 6x savings" | above-callout-bar |
| Defensibility | "Voice requires infrastructure costs = defensible against open-source forks" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- VOICE AGENT UPSELL
- 3x Pricing, Pro Tier (M9+)
- VOICE UI MOCKUP
- PRICING TIERS
- VOICE TIER ARR
- PRO badge
- Mic button
- Waveform animation
- Imogen Heap's co-writers?
- Suggest missing credits
- FREE $0/mo
- PRO $49/mo
- Voice + Batch
- 3x premium
- M9 Launch
- M12 100 users
- M18 ARR contribution
- Pipecat $0.02/conv
- Vapi $0.12/conv
- 6x savings

### Caption (for embedding in documentation)

Voice agent as premium Pro tier upsell: MVP shows aspirational UI (mic animation, example queries), full Pipecat implementation launches at M9+ with 6x cost savings over Vapi, driving 3x pricing premium at $49/month Pro tier -- voice infrastructure costs create a natural moat against open-source forks that cannot replicate the hosted service.

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

1. Voice is ASPIRATIONAL in MVP -- only the upsell UI exists, not actual voice processing.
2. Pipecat costs $0.02/conversation vs Vapi $0.12/conversation -- 6x savings.
3. Pro tier is $49/month -- EXACT price.
4. Voice launches at M9+, not at MVP.
5. "Imogen Heap" is the design persona -- can use as example query subject.
6. Do NOT name specific STT/TTS providers (Whisper, ElevenLabs).
7. The mic animation and example queries are UI MOCKUP elements, not functional.
8. "Defensible against forks" means OSS forks can't offer voice without hosting costs.

## Alt Text

Voice upsell: mic UI mockup, Free to Pro pricing tiers, and voice tier revenue projection.

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "pitch-adv-12",
    "title": "Voice Agent Upsell Path: 3x Pricing, Pro Tier Launch (M9+)",
    "audience": "L1/L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Voice agent as Pro tier upsell -- 3x pricing premium at $49/mo with Pipecat 6x cost savings, defensible against forks.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Voice UI Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Mic button", "PRO badge", "Example queries", "Waveform animation"]
      },
      {
        "name": "Pricing Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Free $0/mo", "Pro $49/mo", "3x premium"]
      },
      {
        "name": "Revenue Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["M9 Launch", "M12 100 users", "M18 ARR contribution"]
      },
      {
        "name": "Pro Tier",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["$49/mo", "Voice + Batch", "Priority support"]
      }
    ],
    "relationships": [
      {
        "from": "Voice UI panel",
        "to": "Pricing panel",
        "type": "solid",
        "label": "voice drives Pro tier"
      },
      {
        "from": "Pricing panel",
        "to": "Revenue panel",
        "type": "solid",
        "label": "Pro tier drives ARR"
      }
    ],
    "callout_boxes": [
      {
        "heading": "COST SAVINGS",
        "body_text": "Pipecat: $0.02/conv vs Vapi $0.12/conv = 6x savings",
        "position": "above-callout-bar"
      },
      {
        "heading": "DEFENSIBILITY",
        "body_text": "Voice requires infrastructure costs = defensible against open-source forks",
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

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Voice upsell: mic UI mockup, Free to Pro pricing tiers, and voice tier revenue projection.](docs/figures/repo-figures/assets/fig-pitch-adv-12-voice-agent-premium-upsell.jpg)

*Voice agent as premium Pro tier upsell: MVP shows aspirational UI (mic animation, example queries), full Pipecat implementation launches at M9+ with 6x cost savings over Vapi, driving 3x pricing premium at $49/month Pro tier -- voice infrastructure costs create a natural moat against open-source forks that cannot replicate the hosted service.*

### From this figure plan (relative)

![Voice upsell: mic UI mockup, Free to Pro pricing tiers, and voice tier revenue projection.](../assets/fig-pitch-adv-12-voice-agent-premium-upsell.jpg)
