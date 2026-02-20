# fig-voice-21: Build vs Buy: Voice Agent Decision Matrix

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-21 |
| **Title** | Build vs Buy: Voice Agent Decision Matrix |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Present a structured comparison matrix across four deployment approaches (Managed Platforms, Framework + APIs, Self-Hosted, Hybrid) evaluating cost, time to market, customization, scalability, vendor lock-in, and DevOps burden. Answers: "Which deployment approach fits my team's constraints across the six key dimensions?"

## Key Message

Start with Framework + APIs (the sweet spot column) for flexibility and speed, then migrate individual components to self-hosted as call volume grows and team DevOps capacity increases.

## Visual Concept

Four-column comparison (Template B) with six evaluation rows. Column I: Managed Platforms (Retell, Vapi). Column II: Framework + APIs (Pipecat/LiveKit + cloud services) -- highlighted as sweet spot. Column III: Self-Hosted (open-source stack on own infra). Column IV: Hybrid (cloud LLM + on-device STT/TTS). Rows: Cost/min, Time to market, Customization, Scalability, Vendor lock-in, DevOps burden. Traffic-light indicators (green/amber/red semantic tags) for quick scanning.

```
+-------------------------------------------------------------------+
|  BUILD VS BUY                                              [sq]   |
|  VOICE AGENT DECISION MATRIX                                      |
+-------------------------------------------------------------------+
|              | I MANAGED   | II FRAMEWORK | III SELF-  | IV HYBRID |
|              | PLATFORMS   | + APIs ■     | HOSTED     |           |
+--------------+-------------+--------------+------------+-----------+
| Cost/min     | $0.07-0.14  | $0.05-0.10   | $0.01-0.02 | Variable  |
|              | (HIGH)      | (MEDIUM)     | (LOW)      | (LOW@scale)|
+--------------+-------------+--------------+------------+-----------+
| Time to      | Days        | Weeks        | Months     | Months    |
| market       | (FAST)      | (MODERATE)   | (SLOW)     | (SLOW)    |
+--------------+-------------+--------------+------------+-----------+
| Customiz-    | Limited     | High         | Full       | High      |
| ation        | (LOW)       | (HIGH)       | (FULL)     | (HIGH)    |
+--------------+-------------+--------------+------------+-----------+
| Scalability  | Auto        | API-limited  | Self-      | Mixed     |
|              | (HIGH)      | (HIGH)       | managed    |           |
|              |             |              | (MEDIUM)   | (MEDIUM)  |
+--------------+-------------+--------------+------------+-----------+
| Vendor       | HIGH        | MODERATE     | NONE       | LOW       |
| lock-in      | (platform)  | (APIs swap)  | (own stack)| (LLM only)|
+--------------+-------------+--------------+------------+-----------+
| DevOps       | NONE        | LOW          | HIGH       | HIGH      |
| burden       |             |              | (GPUs, etc)| (edge+cloud)|
+--------------+-------------+--------------+------------+-----------+
|  "START WITH FRAMEWORK + APIs, MIGRATE TO SELF-HOSTED            |
|   AS VOLUME GROWS"                                  [accent line] |
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
    content: "BUILD VS BUY"
    role: title

  - id: matrix_zone
    bounds: [40, 140, 1840, 760]
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "START WITH FRAMEWORK + APIs"
    role: callout_box

anchors:
  - id: col_header_row
    position: [280, 150]
    size: [1600, 60]
    role: annotation
    label: "Column headers"

  - id: col_i_managed
    position: [280, 220]
    size: [380, 700]
    role: branching_path
    label: "I MANAGED PLATFORMS"

  - id: col_ii_framework
    position: [680, 220]
    size: [380, 700]
    role: selected_option
    label: "II FRAMEWORK + APIs"

  - id: col_iii_selfhosted
    position: [1080, 220]
    size: [380, 700]
    role: branching_path
    label: "III SELF-HOSTED"

  - id: col_iv_hybrid
    position: [1480, 220]
    size: [380, 700]
    role: branching_path
    label: "IV HYBRID"

  - id: row_labels
    position: [40, 220]
    size: [220, 700]
    role: annotation
    label: "Row labels"

  - id: row_cost
    position: [40, 220]
    size: [1840, 100]
    role: data_row
    label: "Cost/min"

  - id: row_time
    position: [40, 330]
    size: [1840, 100]
    role: data_row
    label: "Time to market"

  - id: row_custom
    position: [40, 440]
    size: [1840, 100]
    role: data_row
    label: "Customization"

  - id: row_scale
    position: [40, 550]
    size: [1840, 100]
    role: data_row
    label: "Scalability"

  - id: row_lockin
    position: [40, 660]
    size: [1840, 100]
    role: data_row
    label: "Vendor lock-in"

  - id: row_devops
    position: [40, 770]
    size: [1840, 100]
    role: data_row
    label: "DevOps burden"

  - id: sweet_spot_highlight
    from: col_ii_framework
    to: callout_zone
    type: arrow
    label: "recommended"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Column I: Managed Platforms | `branching_path` | Retell, Vapi, Bland -- fully outsourced, fastest to market, highest cost and lock-in |
| Column II: Framework + APIs | `selected_option` | Pipecat/LiveKit + Deepgram/ElevenLabs -- highlighted sweet spot, moderate cost, high flexibility |
| Column III: Self-Hosted | `branching_path` | Open-source stack on own GPUs -- lowest cost, full control, highest DevOps burden |
| Column IV: Hybrid | `branching_path` | Cloud LLM + on-device STT/TTS -- edge deployment, complex setup, lowest cost at scale |
| Cost Row | `data_row` | Per-minute cost comparison across all four approaches |
| Time to Market Row | `data_row` | Development timeline from days to months |
| Customization Row | `data_row` | Degree of pipeline customization available |
| Scalability Row | `data_row` | Auto-scaling capability of each approach |
| Vendor Lock-in Row | `data_row` | Degree of platform dependency |
| DevOps Burden Row | `data_row` | Infrastructure management requirements |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Column II: Framework + APIs | Column III: Self-Hosted | dashed | "migrate as volume grows" |
| Sweet Spot Highlight | Column II: Framework + APIs | arrow | "recommended starting point" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "START WITH FRAMEWORK + APIs, MIGRATE TO SELF-HOSTED AS VOLUME GROWS" | Begin with Pipecat or LiveKit + cloud STT/TTS APIs for fast iteration and moderate cost. As call volume exceeds 10K minutes/month, migrate STT and TTS to self-hosted (faster-whisper, Orpheus) for 5-10x cost reduction. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I MANAGED PLATFORMS"
- Label 2: "II FRAMEWORK + APIs"
- Label 3: "III SELF-HOSTED"
- Label 4: "IV HYBRID"
- Label 5: "Cost/min"
- Label 6: "Time to market"
- Label 7: "Customization"
- Label 8: "Scalability"
- Label 9: "Vendor lock-in"
- Label 10: "DevOps burden"
- Label 11: "$0.07-0.14/min"
- Label 12: "$0.05-0.10/min"
- Label 13: "$0.01-0.02/min"
- Label 14: "Days"
- Label 15: "Weeks"
- Label 16: "Months"
- Label 17: "SWEET SPOT"

### Caption (for embedding in documentation)

Four-column decision matrix comparing managed platforms, framework + APIs (sweet spot), self-hosted, and hybrid voice agent deployment approaches across cost, time to market, customization, scalability, vendor lock-in, and DevOps burden.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `branching_path`, `selected_option`, `data_row` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Cost ranges are approximate industry averages as of early 2026. These are estimates, not exact pricing. Do NOT present as guaranteed quotes.
10. Column II (Framework + APIs) must be visually highlighted as the "sweet spot" -- use accent treatment or border emphasis.
11. The migration arrow from Column II to Column III is essential -- it shows the intended progression path.
12. Time to market estimates: Managed = days, Framework = weeks, Self-Hosted = months, Hybrid = months. These reflect realistic engineering timelines.
13. Do NOT frame any column as "wrong" -- each is appropriate for different team constraints and scale.
14. The 10K minutes/month threshold for migrating to self-hosted is an approximate crossover point, not a hard rule.
15. Roman numerals I-IV must be used for column headers.
16. Vendor lock-in for Framework + APIs is "moderate" because cloud APIs (Deepgram, ElevenLabs) can be swapped via the framework abstraction layer.

## Alt Text

Four-column decision matrix comparing voice agent deployment approaches (managed platforms, framework + APIs, self-hosted, hybrid) across six dimensions: cost per minute, time to market, customization, scalability, vendor lock-in, and DevOps burden, with framework + APIs highlighted as the recommended sweet spot.

## Image Embed

![Four-column decision matrix comparing voice agent deployment approaches (managed platforms, framework + APIs, self-hosted, hybrid) across six dimensions: cost per minute, time to market, customization, scalability, vendor lock-in, and DevOps burden, with framework + APIs highlighted as the recommended sweet spot.](docs/figures/repo-figures/assets/fig-voice-21-managed-vs-self-hosted-decision.jpg)

*Four-column decision matrix comparing managed platforms, framework + APIs (sweet spot), self-hosted, and hybrid voice agent deployment approaches across cost, time to market, customization, scalability, vendor lock-in, and DevOps burden.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-21",
    "title": "Build vs Buy: Voice Agent Decision Matrix",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Start with Framework + APIs (the sweet spot) for flexibility and speed, then migrate to self-hosted as volume grows.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Column I: Managed Platforms",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["I MANAGED PLATFORMS", "Retell / Vapi", "$0.07-0.14/min", "Days to market"]
      },
      {
        "name": "Column II: Framework + APIs",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["II FRAMEWORK + APIs", "Pipecat / LiveKit", "$0.05-0.10/min", "SWEET SPOT"]
      },
      {
        "name": "Column III: Self-Hosted",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["III SELF-HOSTED", "faster-whisper / Orpheus", "$0.01-0.02/min", "Months to market"]
      },
      {
        "name": "Column IV: Hybrid",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["IV HYBRID", "Cloud LLM + on-device", "variable cost", "Months to market"]
      }
    ],
    "relationships": [
      {
        "from": "Column II: Framework + APIs",
        "to": "Column III: Self-Hosted",
        "type": "dashed",
        "label": "migrate as volume grows"
      }
    ],
    "callout_boxes": [
      {
        "heading": "START WITH FRAMEWORK + APIs, MIGRATE TO SELF-HOSTED AS VOLUME GROWS",
        "body_text": "Begin with Pipecat/LiveKit + cloud APIs for fast iteration. Migrate to self-hosted at 10K+ minutes/month for 5-10x cost reduction.",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors, hex codes, or font names in content spec)
- [ ] ASCII layout sketched
- [ ] Spatial anchors defined in YAML
- [ ] Labels under 30 characters
- [ ] Anti-hallucination rules listed
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L2)
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
