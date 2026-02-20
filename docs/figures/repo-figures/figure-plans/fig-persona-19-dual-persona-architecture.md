# fig-persona-19: Dual Persona Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-19 |
| **Title** | Dual Persona Architecture: Attribution Agent and Digital Twin |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Reveals the architectural design where two distinct personas -- the Attribution Agent (system voice) and the Digital Twin (artist voice) -- share a common memory system, confidence framework, and cross-channel state, separated by a consent gate. Answers: "How can a system maintain both a reliable attribution voice and an authentic artist voice without conflating them?"

## Key Message

Two personas, one memory system, one confidence framework -- the consent gate between attribution agent and digital twin prevents voice conflation while enabling shared knowledge.

## Visual Concept

Vertical split panel with a shared foundation layer. Left panel shows the Attribution Agent: system voice, factually grounded, RAG-only knowledge, warm but precise. Right panel shows the Digital Twin: artist voice, emotionally expressive, consent-gated, PRAC3-compliant. Between them, a prominent consent gate barrier. Below both, a shared foundation layer shows the memory system, confidence scoring engine, and cross-channel state that both personas access.

```
+-----------------------------------------------------------------------+
|  DUAL PERSONA ARCHITECTURE                                             |
|  -- Attribution Agent and Digital Twin                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌──────────────────┐    CONSENT    ┌──────────────────┐              |
|  │                  │     GATE      │                  │              |
|  │  ATTRIBUTION     │    ┌────┐     │  DIGITAL TWIN    │              |
|  │  AGENT           │    │ ▐▌ │     │                  │              |
|  │  ═══════════════ │    │ ▐▌ │     │  ═══════════════ │              |
|  │                  │    └────┘     │                  │              |
|  │  Voice: System   │              │  Voice: Artist   │              |
|  │  Tone: Precise,  │              │  Tone: Creative, │              |
|  │    warm          │              │    expressive    │              |
|  │                  │              │                  │              |
|  │  Knowledge:      │              │  Knowledge:      │              |
|  │    RAG-only      │              │    Consent-gated │              |
|  │    (verified     │              │    (artist-      │              |
|  │     sources)     │              │     approved     │              |
|  │                  │              │     content)     │              |
|  │  Grounding:      │              │  Grounding:      │              |
|  │    Factual       │              │    Emotional +   │              |
|  │    attribution   │              │    factual       │              |
|  │    data          │              │                  │              |
|  │                  │              │  Compliance:     │              |
|  │  Behavior:       │              │    PRAC3         │              |
|  │    Never         │              │    (all 6 dims)  │              |
|  │    speculates    │              │                  │              |
|  │                  │              │  Behavior:       │              |
|  │                  │              │    May express    │              |
|  │                  │              │    opinions       │              |
|  └────────┬─────────┘              └────────┬─────────┘              |
|           │                                  │                        |
|           └──────────────┬───────────────────┘                        |
|                          │                                            |
|  ┌───────────────────────┴───────────────────────────┐               |
|  │  SHARED FOUNDATION                                 │               |
|  │  ─────────────────                                │               |
|  │                                                    │               |
|  │  ┌──────────┐  ┌──────────────┐  ┌─────────────┐ │               |
|  │  │ Memory   │  │ Confidence   │  │ Cross-      │ │               |
|  │  │ System   │  │ Scoring      │  │ Channel     │ │               |
|  │  │ (shared) │  │ (A0-A3)      │  │ State       │ │               |
|  │  └──────────┘  └──────────────┘  └─────────────┘ │               |
|  └───────────────────────────────────────────────────┘               |
|                                                                        |
|  -- TWO PERSONAS, ONE MEMORY SYSTEM, ONE CONFIDENCE FRAMEWORK          |
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
    content: "DUAL PERSONA ARCHITECTURE"
    role: title

  - id: left_panel
    bounds: [80, 140, 760, 540]
    content: "Attribution Agent"
    role: content_area

  - id: consent_gate
    bounds: [860, 200, 200, 420]
    content: "CONSENT GATE"
    role: security_layer

  - id: right_panel
    bounds: [1080, 140, 760, 540]
    content: "Digital Twin"
    role: content_area

  - id: shared_foundation
    bounds: [80, 720, 1760, 200]
    content: "Shared Foundation"
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "TWO PERSONAS, ONE MEMORY SYSTEM, ONE CONFIDENCE FRAMEWORK"
    role: callout_box

anchors:
  - id: agent_voice
    position: [120, 180]
    size: [680, 100]
    role: processing_stage
    label: "System voice, precise, warm"

  - id: agent_knowledge
    position: [120, 300]
    size: [680, 100]
    role: processing_stage
    label: "RAG-only, verified sources"

  - id: agent_grounding
    position: [120, 420]
    size: [680, 100]
    role: processing_stage
    label: "Factual attribution data"

  - id: agent_behavior
    position: [120, 540]
    size: [680, 80]
    role: processing_stage
    label: "Never speculates"

  - id: gate_barrier
    position: [880, 240]
    size: [160, 360]
    role: security_layer
    label: "CONSENT GATE"

  - id: twin_voice
    position: [1120, 180]
    size: [680, 100]
    role: stakeholder_artist
    label: "Artist voice, creative, expressive"

  - id: twin_knowledge
    position: [1120, 300]
    size: [680, 100]
    role: stakeholder_artist
    label: "Consent-gated, artist-approved"

  - id: twin_grounding
    position: [1120, 420]
    size: [680, 100]
    role: stakeholder_artist
    label: "Emotional + factual"

  - id: twin_compliance
    position: [1120, 540]
    size: [680, 80]
    role: security_layer
    label: "PRAC3 compliant"

  - id: shared_memory
    position: [160, 760]
    size: [480, 120]
    role: storage_layer
    label: "Memory System (shared)"

  - id: shared_confidence
    position: [720, 760]
    size: [480, 120]
    role: final_score
    label: "Confidence Scoring (A0-A3)"

  - id: shared_state
    position: [1280, 760]
    size: [480, 120]
    role: storage_layer
    label: "Cross-Channel State"

  - id: agent_to_foundation
    from: left_panel
    to: shared_foundation
    type: arrow
    label: "reads/writes"

  - id: twin_to_foundation
    from: right_panel
    to: shared_foundation
    type: arrow
    label: "reads/writes"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Attribution Agent panel | `processing_stage` | System voice: precise, warm, factually grounded, RAG-only knowledge, never speculates |
| Consent Gate | `security_layer` | Barrier between agent and twin: requires explicit artist consent to activate twin |
| Digital Twin panel | `stakeholder_artist` | Artist voice: creative, emotionally expressive, consent-gated, PRAC3-compliant |
| Shared Memory System | `storage_layer` | Common memory accessible by both personas |
| Shared Confidence Scoring | `final_score` | A0-A3 assurance levels used by both personas |
| Shared Cross-Channel State | `storage_layer` | Conversation and context state shared across personas |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Attribution Agent | Consent Gate | arrow | "cannot cross without consent" |
| Consent Gate | Digital Twin | arrow | "consent enables twin activation" |
| Attribution Agent | Shared Foundation | arrow | "reads/writes shared state" |
| Digital Twin | Shared Foundation | arrow | "reads/writes shared state" |
| Shared Memory | Both panels | bidirectional | "common knowledge base" |
| Shared Confidence | Both panels | bidirectional | "same scoring framework" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "UNIFIED FOUNDATION" | "TWO PERSONAS, ONE MEMORY SYSTEM, ONE CONFIDENCE FRAMEWORK" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ATTRIBUTION AGENT"
- Label 2: "DIGITAL TWIN"
- Label 3: "CONSENT GATE"
- Label 4: "Voice: System"
- Label 5: "Voice: Artist"
- Label 6: "RAG-only knowledge"
- Label 7: "Consent-gated knowledge"
- Label 8: "Never speculates"
- Label 9: "PRAC3 compliant"
- Label 10: "Memory System (shared)"
- Label 11: "Confidence Scoring (A0-A3)"
- Label 12: "Cross-Channel State"
- Label 13: "SHARED FOUNDATION"

### Caption (for embedding in documentation)

Dual persona architecture showing the Attribution Agent (system voice, factually grounded) and Digital Twin (artist voice, consent-gated) separated by a consent barrier but sharing a common memory system, confidence scoring framework, and cross-channel state.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `security_layer`, `stakeholder_artist` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The Attribution Agent is the SYSTEM voice. It does NOT impersonate the artist. Do NOT blur this distinction.
10. The Digital Twin is the ARTIST voice. It requires explicit consent and PRAC3 compliance. Do NOT show it as always-active.
11. The consent gate is a HARD barrier. The Digital Twin CANNOT activate without consent. Do NOT show a "soft" or "optional" gate.
12. PRAC3 = Privacy, Rights, Authenticity, Compensation, Consent, Control. Do NOT alter.
13. Both personas share the SAME memory system and confidence framework. Do NOT show separate memory or scoring systems.
14. RAG-only means the Attribution Agent ONLY uses retrieved, verified sources. It does NOT generate from its training data.
15. The Digital Twin "may express opinions" but these are consent-gated and PRAC3-compliant, not unconstrained.

## Alt Text

Dual persona architecture diagram showing the Attribution Agent (system voice) and Digital Twin (artist voice) separated by a consent gate barrier, sharing a common memory system, A0-A3 confidence scoring, and cross-channel state for music attribution.

## Image Embed

![Dual persona architecture diagram showing the Attribution Agent (system voice) and Digital Twin (artist voice) separated by a consent gate barrier, sharing a common memory system, A0-A3 confidence scoring, and cross-channel state for music attribution.](docs/figures/repo-figures/assets/fig-persona-19-dual-persona-architecture.jpg)

*Dual persona architecture showing the Attribution Agent (system voice, factually grounded) and Digital Twin (artist voice, consent-gated) separated by a consent barrier but sharing a common memory system, confidence scoring framework, and cross-channel state.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-19",
    "title": "Dual Persona Architecture: Attribution Agent and Digital Twin",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Two personas share one memory system and one confidence framework, separated by a consent gate that prevents voice conflation.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Attribution Agent",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["ATTRIBUTION AGENT", "System voice", "RAG-only", "Never speculates"]
      },
      {
        "name": "Consent Gate",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["CONSENT GATE", "Hard barrier"]
      },
      {
        "name": "Digital Twin",
        "role": "stakeholder_artist",
        "is_highlighted": true,
        "labels": ["DIGITAL TWIN", "Artist voice", "PRAC3 compliant"]
      },
      {
        "name": "Shared Foundation",
        "role": "storage_layer",
        "is_highlighted": false,
        "labels": ["Memory System", "Confidence Scoring", "Cross-Channel State"]
      }
    ],
    "relationships": [
      {
        "from": "Attribution Agent",
        "to": "Consent Gate",
        "type": "arrow",
        "label": "cannot cross without consent"
      },
      {
        "from": "Consent Gate",
        "to": "Digital Twin",
        "type": "arrow",
        "label": "consent enables activation"
      },
      {
        "from": "Both Personas",
        "to": "Shared Foundation",
        "type": "bidirectional",
        "label": "shared memory, scoring, state"
      }
    ],
    "callout_boxes": [
      {
        "heading": "UNIFIED FOUNDATION",
        "body_text": "TWO PERSONAS, ONE MEMORY SYSTEM, ONE CONFIDENCE FRAMEWORK",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
