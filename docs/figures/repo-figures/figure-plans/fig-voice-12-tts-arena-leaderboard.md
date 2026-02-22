# fig-voice-12: TTS Arena Leaderboard (Feb 2026)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-12 |
| **Title** | TTS Arena Leaderboard (Feb 2026) |
| **Audience** | L2 (Technical Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Visualize the current TTS Arena blind preference leaderboard, showing how the competitive landscape has shifted away from ElevenLabs dominance. Answers: "Which TTS models rank highest in blind human preference tests as of Feb 2026, and what does the reshuffling mean for voice attribution agents?"

## Key Message

The TTS Arena leaderboard as of Feb 2026 shows ElevenLabs Flash at 7th place (Elo 1547), displaced by specialized models: Vocu V3.0 (1613), Inworld (1578), CastleFlow (1575), Inworld MAX (1572), Papla (1563), and Hume Octave (1559) -- demonstrating that the market has fragmented beyond any single leader.

## Visual Concept

Horizontal bar chart (Template B adapted as single-panel chart). Seven horizontal bars ranked by Elo score, longest at top. Each bar labeled with model name on the left and Elo score on the right. Bar lengths proportional to Elo rating. ElevenLabs Flash at position 7 is visually marked with an accent indicator to draw attention to its fall from dominance. Bottom callout delivers the market-shift insight.

```
+-------------------------------------------------------------------+
|  TTS ARENA LEADERBOARD (FEB 2026)                          [sq]   |
|                                                                    |
|  Rank  Model                    Elo                                |
|                                                                    |
|  1.    Vocu V3.0          ████████████████████████████  1613       |
|  2.    Inworld            ██████████████████████████░░  1578       |
|  3.    CastleFlow         █████████████████████████░░░  1575       |
|  4.    Inworld MAX        █████████████████████████░░░  1572       |
|  5.    Papla              ████████████████████████░░░░  1563       |
|  6.    Hume Octave        ███████████████████████░░░░░  1559       |
|  7.    ElevenLabs Flash   ██████████████████████░░░░░░  1547  ◄   |
|                                                                    |
|  +-----------------------------------------------------+          |
|  | "ELEVENLABS IS NO LONGER #1 -- Specialized models   |          |
|  |  surpass former leader in blind preference"          |          |
|  +-----------------------------------------------------+  [line] |
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
    content: "TTS ARENA LEADERBOARD (FEB 2026)"
    role: title

  - id: chart_zone
    bounds: [80, 160, 1760, 660]
    role: content_area

  - id: callout_zone
    bounds: [80, 860, 1760, 180]
    content: "ELEVENLABS IS NO LONGER #1"
    role: callout_box

anchors:
  - id: bar_vocu
    position: [400, 200]
    size: [1200, 70]
    role: data_bar
    label: "Vocu V3.0 -- 1613"

  - id: bar_inworld
    position: [400, 290]
    size: [1140, 70]
    role: data_bar
    label: "Inworld -- 1578"

  - id: bar_castleflow
    position: [400, 380]
    size: [1134, 70]
    role: data_bar
    label: "CastleFlow -- 1575"

  - id: bar_inworld_max
    position: [400, 470]
    size: [1128, 70]
    role: data_bar
    label: "Inworld MAX -- 1572"

  - id: bar_papla
    position: [400, 560]
    size: [1110, 70]
    role: data_bar
    label: "Papla -- 1563"

  - id: bar_hume
    position: [400, 650]
    size: [1102, 70]
    role: data_bar
    label: "Hume Octave -- 1559"

  - id: bar_elevenlabs
    position: [400, 740]
    size: [1078, 70]
    role: data_bar
    label: "ElevenLabs Flash -- 1547"

  - id: elevenlabs_marker
    position: [1520, 740]
    size: [40, 70]
    role: accent_indicator
    label: "former #1"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Vocu V3.0 | `data_bar` | Rank 1, Elo 1613, top-ranked TTS in blind preference |
| Inworld | `data_bar` | Rank 2, Elo 1578, game/entertainment specialist |
| CastleFlow | `data_bar` | Rank 3, Elo 1575, emerging specialized TTS |
| Inworld MAX | `data_bar` | Rank 4, Elo 1572, premium Inworld tier |
| Papla | `data_bar` | Rank 5, Elo 1563, newer entrant |
| Hume Octave | `data_bar` | Rank 6, Elo 1559, emotion-focused TTS from Hume AI |
| ElevenLabs Flash | `data_bar` | Rank 7, Elo 1547, former market leader now displaced |
| ElevenLabs Marker | `accent_indicator` | Visual accent marking the fall from #1 position |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Vocu V3.0 | ElevenLabs Flash | dashed | "66 Elo gap" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELEVENLABS IS NO LONGER #1" | Specialized models surpass the former leader in blind human preference tests. The TTS market has fragmented -- no single provider dominates. For voice attribution agents, this means more choices and negotiating leverage. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Vocu V3.0"
- Label 2: "Inworld"
- Label 3: "CastleFlow"
- Label 4: "Inworld MAX"
- Label 5: "Papla"
- Label 6: "Hume Octave"
- Label 7: "ElevenLabs Flash"
- Label 8: "1613"
- Label 9: "1578"
- Label 10: "1575"
- Label 11: "1572"
- Label 12: "1563"
- Label 13: "1559"
- Label 14: "1547"
- Label 15: "Elo Rating"
- Label 16: "Rank"

### Caption (for embedding in documentation)

Horizontal bar chart of TTS Arena blind preference leaderboard as of February 2026, showing Vocu V3.0 at #1 (Elo 1613) and ElevenLabs Flash displaced to #7 (Elo 1547) by specialized competitors.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `data_bar`, `accent_indicator`, etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Elo scores are from the TTS Arena (HuggingFace community) as of approximately Feb 2026. These are community-voted blind preference scores, not objective benchmarks.
10. The exact Elo values are: Vocu V3.0 (1613), Inworld (1578), CastleFlow (1575), Inworld MAX (1572), Papla (1563), Hume Octave (1559), ElevenLabs Flash (1547). Do NOT alter these values.
11. Only show these 7 models -- the full leaderboard has more entries but these are the top 7 as specified.
12. ElevenLabs Flash is specifically the Flash variant, not Multilingual v2 or other ElevenLabs models that may rank differently.
13. Bar lengths must be proportional to Elo scores (the visual difference between 1613 and 1547 is only ~4%, so bars should be similar length with the difference visible at the right edge).
14. The leaderboard changes frequently -- this is a snapshot, not a permanent ranking. The "(Feb 2026)" qualifier in the title is essential.
15. The accent marker on ElevenLabs Flash should visually convey "former #1 displaced" without negative connotation -- it is a factual observation.

## Alt Text

Horizontal bar chart of TTS Arena blind preference leaderboard (Feb 2026) ranking seven speech synthesis models by Elo score, with Vocu V3.0 at #1 (1613) and ElevenLabs Flash displaced to #7 (1547), showing market fragmentation in text-to-speech quality.

## Image Embed

![Horizontal bar chart of TTS Arena blind preference leaderboard (Feb 2026) ranking seven speech synthesis models by Elo score, with Vocu V3.0 at #1 (1613) and ElevenLabs Flash displaced to #7 (1547), showing market fragmentation in text-to-speech quality.](docs/figures/repo-figures/assets/fig-voice-12-tts-arena-leaderboard.jpg)

*Horizontal bar chart of TTS Arena blind preference leaderboard as of February 2026, showing Vocu V3.0 at #1 (Elo 1613) and ElevenLabs Flash displaced to #7 (Elo 1547) by specialized competitors.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-12",
    "title": "TTS Arena Leaderboard (Feb 2026)",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "ElevenLabs Flash dropped to #7 in blind preference, displaced by specialized models led by Vocu V3.0 at Elo 1613.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Vocu V3.0",
        "role": "data_bar",
        "is_highlighted": true,
        "labels": ["Vocu V3.0", "1613"]
      },
      {
        "name": "Inworld",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["Inworld", "1578"]
      },
      {
        "name": "CastleFlow",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["CastleFlow", "1575"]
      },
      {
        "name": "Inworld MAX",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["Inworld MAX", "1572"]
      },
      {
        "name": "Papla",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["Papla", "1563"]
      },
      {
        "name": "Hume Octave",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["Hume Octave", "1559"]
      },
      {
        "name": "ElevenLabs Flash",
        "role": "data_bar",
        "is_highlighted": true,
        "labels": ["ElevenLabs Flash", "1547"]
      }
    ],
    "relationships": [
      {
        "from": "Vocu V3.0",
        "to": "ElevenLabs Flash",
        "type": "dashed",
        "label": "66 Elo gap"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ELEVENLABS IS NO LONGER #1",
        "body_text": "Specialized models surpass former leader in blind preference tests.",
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
