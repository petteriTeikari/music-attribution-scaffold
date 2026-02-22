# fig-voice-46: Test Architecture Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-46 |
| **Title** | Test Architecture Map |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, new subsection |
| **Priority** | P2 (Nice-to-have) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show 4 test files with their coverage areas and mock boundaries. Prose lists test counts but cannot convey the spatial relationship between test files, source modules, and mock boundaries. Answers: "What does each test file cover, and where are the mock seams?"

## Key Message

The voice module has 54 tests across 4 files, testing config validation (17), persona building (14), drift detection (15), and demo script structure (8). All tests run without Pipecat installed by mocking at precise boundaries.

## Visual Concept

Multi-panel (Template B). Four columns, one per test file. Each column shows: file name at top, test count badge, coverage area as a shaded overlay on the source module, and mock boundary markers shown as dashed lines. Below: coverage summary bar showing 54 total tests. Mock boundaries (sentence-transformers, Pipecat) shown as dashed cut-lines crossing between test and source layers.

```
+-----------------------------------------------------------------------+
|  TEST ARCHITECTURE MAP                                           [sq]  |
|  -- 54 Tests Across 4 Files, Zero Network Calls                       |
+-----------------------------------------------------------------------+
|                                                                        |
|  test_voice_      test_voice_      test_voice_      test_demo_         |
|  config.py        persona.py       drift.py         script.py          |
|  [17 tests]       [14 tests]       [15 tests]       [8 tests]          |
|  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐         |
|  │ VoiceConfig│    │ build_     │    │ DriftDet  │    │ Demo CLI  │         |
|  │ validation │    │ system_    │    │ scoring   │    │ structure │         |
|  │ enum types │    │ prompt     │    │ EWMA      │    │ AST-based │         |
|  │ defaults   │    │ 5 dims     │    │ state     │    │ analysis  │         |
|  │ env vars   │    │ reinforce  │    │ Jaccard   │    │ argparse  │         |
|  └─ ─ ─ ─ ─ ┘    └─ ─ ─ ─ ─ ┘    └─ ─ ─ ─ ─ ┘    └─ ─ ─ ─ ─ ┘         |
|       │                │                │                │              |
|  - - -│- - MOCK - - - -│- - - - - - - - │- - - - - - - -│- - - -      |
|       │                │                │                │              |
|       ▼                ▼                ▼                ▼              |
|  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐         |
|  │ config.py │    │persona.py│    │ drift.py  │    │demo_voice│         |
|  │           │    │          │    │           │    │ _agent.py│         |
|  └──────────┘    └──────────┘    └──────────┘    └──────────┘         |
|                                                                        |
|  MOCK BOUNDARIES: sentence-transformers (drift), Pipecat (all)        |
|  ═══════════════════════════════════════════════════                   |
|  TOTAL: 54 tests | 0 network calls | 0 API keys required              |
+-----------------------------------------------------------------------+
|  ELI5: Like a sound check before a gig -- each test file checks  [sq]  |
|  a different part of the PA without needing the actual speakers.       |
+-----------------------------------------------------------------------+
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
    content: "TEST ARCHITECTURE MAP"
    role: title

  - id: test_panels_zone
    bounds: [40, 140, 1840, 340]
    role: content_area

  - id: mock_boundary_zone
    bounds: [40, 500, 1840, 40]
    role: accent_line

  - id: source_panels_zone
    bounds: [40, 560, 1840, 200]
    role: content_area

  - id: summary_zone
    bounds: [40, 800, 1840, 100]
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "ELI5: Like a sound check before a gig"
    role: callout_box

anchors:
  - id: panel_config
    position: [140, 280]
    size: [380, 260]
    role: processing_stage
    label: "test_voice_config.py"

  - id: panel_persona
    position: [580, 280]
    size: [380, 260]
    role: processing_stage
    label: "test_voice_persona.py"

  - id: panel_drift
    position: [1020, 280]
    size: [380, 260]
    role: processing_stage
    label: "test_voice_drift.py"

  - id: panel_demo
    position: [1460, 280]
    size: [380, 260]
    role: processing_stage
    label: "test_demo_script.py"

  - id: mock_line
    position: [40, 520]
    size: [1840, 2]
    role: accent_line
    label: "MOCK BOUNDARY"

  - id: source_config
    position: [140, 620]
    size: [380, 120]
    role: data_flow
    label: "config.py"

  - id: source_persona
    position: [580, 620]
    size: [380, 120]
    role: data_flow
    label: "persona.py"

  - id: source_drift
    position: [1020, 620]
    size: [380, 120]
    role: data_flow
    label: "drift.py"

  - id: source_demo
    position: [1460, 620]
    size: [380, 120]
    role: data_flow
    label: "demo_voice_agent.py"

  - id: config_coverage
    from: panel_config
    to: source_config
    type: dashed_arrow
    label: "covers"

  - id: persona_coverage
    from: panel_persona
    to: source_persona
    type: dashed_arrow
    label: "covers"

  - id: drift_coverage
    from: panel_drift
    to: source_drift
    type: dashed_arrow
    label: "covers"

  - id: demo_coverage
    from: panel_demo
    to: source_demo
    type: dashed_arrow
    label: "covers"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "TEST ARCHITECTURE MAP" with coral accent square |
| Config test panel | `processing_stage` | test_voice_config.py -- 17 tests covering VoiceConfig validation, enum types, defaults, env var parsing |
| Persona test panel | `processing_stage` | test_voice_persona.py -- 14 tests covering build_system_prompt, persona dimensions, reinforcement intervals |
| Drift test panel | `processing_stage` | test_voice_drift.py -- 15 tests covering DriftDetector scoring, EWMA, state transitions, Jaccard fallback |
| Demo test panel | `processing_stage` | test_demo_script.py -- 8 tests covering demo script structure, CLI argument parsing, AST-based analysis |
| Mock boundary line | `accent_line` | Dashed line separating test layer from source layer |
| Source modules | `data_flow` | config.py, persona.py, drift.py, demo_voice_agent.py |
| Summary bar | `data_mono` | "54 tests, 0 network calls, 0 API keys required" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| test_voice_config.py | config.py | dashed_arrow | "covers" |
| test_voice_persona.py | persona.py | dashed_arrow | "covers" |
| test_voice_drift.py | drift.py | dashed_arrow | "covers" |
| test_demo_script.py | demo_voice_agent.py | dashed_arrow | "covers" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of the test suite like a sound check before a gig: each test file checks a different part of the PA system -- the mixer (config), the EQ presets (persona), the feedback eliminator (drift), and the overall signal chain (demo script) -- all without needing the actual speakers connected. | bottom-center |
| "MOCK BOUNDARIES" | sentence-transformers mocked in drift tests, Pipecat mocked everywhere (PIPECAT_AVAILABLE=False path), no network calls in any test | center-divider |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "test_voice_config.py"
- Label 2: "test_voice_persona.py"
- Label 3: "test_voice_drift.py"
- Label 4: "test_demo_script.py"
- Label 5: "17 tests"
- Label 6: "14 tests"
- Label 7: "15 tests"
- Label 8: "8 tests"
- Label 9: "VoiceConfig validation"
- Label 10: "build_system_prompt"
- Label 11: "DriftDetector scoring"
- Label 12: "Demo CLI structure"
- Label 13: "MOCK BOUNDARY"
- Label 14: "54 tests total"
- Label 15: "0 network calls"
- Label 16: "0 API keys required"

### Caption (for embedding in documentation)

Test architecture map showing 54 voice module tests across 4 files -- config validation (17), persona building (14), drift detection (15), and demo structure (8) -- with mock boundaries at sentence-transformers and Pipecat, requiring zero network calls or API keys.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- "EWMA", "Pipecat", "Jaccard", "AST" are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Test counts (17, 14, 15, 8) must match stated values and sum to 54.
10. Test file names must exactly match actual test files in tests/unit/.
11. Mock boundaries must be shown as dashed lines crossing from test to source layer.
12. Do NOT show individual test function names -- show coverage areas only.

## Alt Text

Four-panel test architecture: 54 voice tests across config, persona, drift, and demo files with mock boundaries at Pipecat and transformers.

## Image Embed

![Four-panel test architecture: 54 voice tests across config, persona, drift, and demo files with mock boundaries at Pipecat and transformers.](docs/figures/repo-figures/assets/fig-voice-46-test-architecture-map.jpg)

*Test architecture map showing 54 voice module tests across 4 files -- config validation (17), persona building (14), drift detection (15), and demo structure (8) -- with mock boundaries at sentence-transformers and Pipecat, requiring zero network calls or API keys.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-46",
    "title": "Test Architecture Map",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The voice module has 54 tests across 4 files, testing config (17), persona (14), drift (15), and demo (8), all running without Pipecat by mocking at precise boundaries.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "test_voice_config.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["test_voice_config.py", "17 tests", "VoiceConfig validation"]
      },
      {
        "name": "test_voice_persona.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["test_voice_persona.py", "14 tests", "build_system_prompt"]
      },
      {
        "name": "test_voice_drift.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["test_voice_drift.py", "15 tests", "DriftDetector scoring"]
      },
      {
        "name": "test_demo_script.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["test_demo_script.py", "8 tests", "Demo CLI structure"]
      },
      {
        "name": "Mock Boundary",
        "role": "accent_line",
        "is_highlighted": false,
        "labels": ["MOCK BOUNDARY", "sentence-transformers", "Pipecat"]
      }
    ],
    "relationships": [
      {"from": "test_voice_config.py", "to": "config.py", "type": "dashed_arrow", "label": "covers"},
      {"from": "test_voice_persona.py", "to": "persona.py", "type": "dashed_arrow", "label": "covers"},
      {"from": "test_voice_drift.py", "to": "drift.py", "type": "dashed_arrow", "label": "covers"},
      {"from": "test_demo_script.py", "to": "demo_voice_agent.py", "type": "dashed_arrow", "label": "covers"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Think of the test suite like a sound check before a gig: each test file checks a different part of the PA system -- the mixer (config), the EQ presets (persona), the feedback eliminator (drift), and the overall signal chain (demo script) -- all without needing the actual speakers connected.",
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
- [x] Anti-hallucination rules listed (8 default + 4 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
