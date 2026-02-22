# fig-persona-20: Multi-Agent Attribution Orchestra

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-20 |
| **Title** | Multi-Agent Attribution: Specialized Agents, Unified Voice |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows a multi-agent architecture where a central orchestrator routes attribution queries to four specialized agents (Metadata, AudioFingerprint, Rights, Provenance), then a meta-agent synthesizes results under a unified persona voice. User type detection feeds the routing logic. Answers: "How can multiple specialized agents collaborate while maintaining a single coherent persona for the user?"

## Key Message

Specialized agents handle distinct attribution domains while a meta-agent synthesizes their outputs under a unified persona voice -- the attribution orchestra pattern.

## Visual Concept

Radial flowchart with the orchestrator at center. Four specialized agents arranged around the orchestrator like instruments in an orchestra. User input enters from the top, passes through a user type detector, into the orchestrator, which routes to the appropriate agents. Agent outputs converge at a meta-agent synthesis node below the orchestrator, which produces the unified persona response at the bottom. Flow lines show the routing and synthesis pattern.

```
+-----------------------------------------------------------------------+
|  MULTI-AGENT ATTRIBUTION                                               |
|  -- Specialized Agents, Unified Voice                                  |
+-----------------------------------------------------------------------+
|                                                                        |
|                     ┌──────────────────┐                               |
|                     │  USER QUERY       │                               |
|                     └────────┬─────────┘                               |
|                              │                                         |
|                              ▼                                         |
|                     ┌──────────────────┐                               |
|                     │  USER TYPE        │                               |
|                     │  DETECTION        │                               |
|                     │  (artist/label/   │                               |
|                     │   researcher)     │                               |
|                     └────────┬─────────┘                               |
|                              │                                         |
|                              ▼                                         |
|                     ┌──────────────────┐                               |
|                     │                  │                               |
|                     │   ORCHESTRATOR   │                               |
|                     │   (routing +     │                               |
|                     │    priority)     │                               |
|                     │                  │                               |
|                     └─┬──────┬─────┬──┘                               |
|                       │      │     │                                   |
|           ┌───────────┘  ┌───┘ ┌───┘──────────┐                       |
|           │              │     │               │                       |
|           ▼              ▼     ▼               ▼                       |
|  ┌──────────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐         |
|  │ METADATA     │ │ AUDIO    │ │ RIGHTS   │ │ PROVENANCE   │         |
|  │ AGENT        │ │ FINGER-  │ │ AGENT    │ │ AGENT        │         |
|  │              │ │ PRINT    │ │          │ │              │         |
|  │ ISRC/ISWC    │ │ AGENT    │ │ MCP      │ │ A0-A3        │         |
|  │ lookup       │ │          │ │ consent  │ │ assurance    │         |
|  │              │ │ AcoustID │ │ queries  │ │ scoring      │         |
|  └──────┬───────┘ │ matching │ │          │ │              │         |
|         │         └─────┬────┘ └────┬─────┘ └──────┬───────┘         |
|         │               │          │               │                  |
|         └───────────┬───┴──────────┴───────────────┘                  |
|                     │                                                  |
|                     ▼                                                  |
|            ┌──────────────────┐                                       |
|            │  META-AGENT       │                                       |
|            │  SYNTHESIS        │                                       |
|            │                   │                                       |
|            │  Combines results │                                       |
|            │  under unified    │                                       |
|            │  persona voice    │                                       |
|            └────────┬─────────┘                                       |
|                     │                                                  |
|                     ▼                                                  |
|            ┌──────────────────┐                                       |
|            │  UNIFIED PERSONA  │                                       |
|            │  RESPONSE         │                                       |
|            └──────────────────┘                                       |
|                                                                        |
|  -- SPECIALIZED AGENTS, UNIFIED VOICE -- THE ATTRIBUTION ORCHESTRA     |
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
    content: "MULTI-AGENT ATTRIBUTION"
    role: title

  - id: input_zone
    bounds: [660, 120, 600, 120]
    content: "User query and type detection"
    role: content_area

  - id: orchestrator_zone
    bounds: [660, 260, 600, 140]
    content: "Central orchestrator"
    role: content_area

  - id: agents_zone
    bounds: [80, 420, 1760, 220]
    content: "Four specialized agents"
    role: content_area

  - id: synthesis_zone
    bounds: [560, 660, 800, 200]
    content: "Meta-agent synthesis"
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "SPECIALIZED AGENTS, UNIFIED VOICE -- THE ATTRIBUTION ORCHESTRA"
    role: callout_box

anchors:
  - id: user_query
    position: [760, 130]
    size: [400, 60]
    role: api_endpoint
    label: "USER QUERY"

  - id: user_type_detector
    position: [710, 200]
    size: [500, 80]
    role: processing_stage
    label: "USER TYPE DETECTION"

  - id: orchestrator
    position: [710, 300]
    size: [500, 100]
    role: processing_stage
    label: "ORCHESTRATOR"

  - id: metadata_agent
    position: [100, 440]
    size: [380, 180]
    role: source_musicbrainz
    label: "METADATA AGENT"

  - id: fingerprint_agent
    position: [520, 440]
    size: [380, 180]
    role: source_acoustid
    label: "AUDIO FINGERPRINT AGENT"

  - id: rights_agent
    position: [940, 440]
    size: [380, 180]
    role: security_layer
    label: "RIGHTS AGENT"

  - id: provenance_agent
    position: [1360, 440]
    size: [380, 180]
    role: final_score
    label: "PROVENANCE AGENT"

  - id: meta_agent
    position: [610, 680]
    size: [700, 120]
    role: processing_stage
    label: "META-AGENT SYNTHESIS"

  - id: unified_response
    position: [710, 820]
    size: [500, 80]
    role: stakeholder_artist
    label: "UNIFIED PERSONA RESPONSE"

  - id: query_to_detector
    from: user_query
    to: user_type_detector
    type: arrow
    label: "classify user"

  - id: detector_to_orchestrator
    from: user_type_detector
    to: orchestrator
    type: arrow
    label: "routing context"

  - id: orchestrator_to_metadata
    from: orchestrator
    to: metadata_agent
    type: arrow
    label: "ISRC/ISWC queries"

  - id: orchestrator_to_fingerprint
    from: orchestrator
    to: fingerprint_agent
    type: arrow
    label: "audio matching"

  - id: orchestrator_to_rights
    from: orchestrator
    to: rights_agent
    type: arrow
    label: "consent queries"

  - id: orchestrator_to_provenance
    from: orchestrator
    to: provenance_agent
    type: arrow
    label: "assurance scoring"

  - id: agents_to_synthesis
    from: agents_zone
    to: meta_agent
    type: arrow
    label: "agent results"

  - id: synthesis_to_response
    from: meta_agent
    to: unified_response
    type: arrow
    label: "unified voice"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| User Query input | `api_endpoint` | Incoming attribution query from user |
| User Type Detection | `processing_stage` | Classifies user as artist, label, researcher to inform routing priority |
| Orchestrator | `processing_stage` | Central routing and priority logic, dispatches to specialized agents |
| MetadataAgent | `source_musicbrainz` | ISRC/ISWC identifier lookup against music registries |
| AudioFingerprintAgent | `source_acoustid` | AcoustID-based audio matching and fingerprint comparison |
| RightsAgent | `security_layer` | MCP consent queries, training permission verification |
| ProvenanceAgent | `final_score` | A0-A3 assurance level scoring and provenance chain assembly |
| Meta-Agent Synthesis | `processing_stage` | Combines outputs from all agents under unified persona voice |
| Unified Persona Response | `stakeholder_artist` | Final response delivered in consistent persona tone |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| User Query | User Type Detection | arrow | "classify user" |
| User Type Detection | Orchestrator | arrow | "routing context" |
| Orchestrator | MetadataAgent | arrow | "ISRC/ISWC queries" |
| Orchestrator | AudioFingerprintAgent | arrow | "audio matching" |
| Orchestrator | RightsAgent | arrow | "consent queries" |
| Orchestrator | ProvenanceAgent | arrow | "assurance scoring" |
| MetadataAgent | Meta-Agent Synthesis | arrow | "metadata results" |
| AudioFingerprintAgent | Meta-Agent Synthesis | arrow | "fingerprint results" |
| RightsAgent | Meta-Agent Synthesis | arrow | "rights status" |
| ProvenanceAgent | Meta-Agent Synthesis | arrow | "provenance chain" |
| Meta-Agent Synthesis | Unified Response | arrow | "unified persona voice" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE ATTRIBUTION ORCHESTRA" | "SPECIALIZED AGENTS, UNIFIED VOICE -- THE ATTRIBUTION ORCHESTRA" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "USER QUERY"
- Label 2: "USER TYPE DETECTION"
- Label 3: "ORCHESTRATOR"
- Label 4: "METADATA AGENT"
- Label 5: "AUDIO FINGERPRINT AGENT"
- Label 6: "RIGHTS AGENT"
- Label 7: "PROVENANCE AGENT"
- Label 8: "META-AGENT SYNTHESIS"
- Label 9: "UNIFIED PERSONA RESPONSE"
- Label 10: "ISRC/ISWC lookup"
- Label 11: "AcoustID matching"
- Label 12: "MCP consent queries"
- Label 13: "A0-A3 assurance scoring"

### Caption (for embedding in documentation)

Multi-agent attribution architecture with central orchestrator routing queries to four specialized agents (Metadata, AudioFingerprint, Rights, Provenance), user type detection feeding routing priority, and meta-agent synthesis producing a unified persona voice response.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `source_musicbrainz`, `source_acoustid`, `security_layer`, `final_score` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- Module names and protocol references are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. There are exactly FOUR specialized agents: MetadataAgent, AudioFingerprintAgent, RightsAgent, ProvenanceAgent. Do NOT add or remove agents.
10. The MetadataAgent handles ISRC (International Standard Recording Code) and ISWC (International Standard Musical Work Code). Do NOT confuse these identifiers.
11. The AudioFingerprintAgent uses AcoustID specifically. Do NOT substitute other fingerprinting services.
12. The RightsAgent uses MCP (Model Context Protocol) for consent queries. Do NOT use generic "permissions" language.
13. The ProvenanceAgent scores A0-A3 assurance levels. Do NOT use confidence percentages as its primary output.
14. The meta-agent SYNTHESIZES -- it does not merely concatenate agent outputs. It resolves conflicts and presents unified results.
15. User type detection classifies into artist, label, or researcher. Do NOT add additional user types.
16. This is an architectural aspiration. The current scaffold has a single PydanticAI agent with 4 tools, not 4 separate agents.

## Alt Text

Multi-agent attribution architecture flowchart with central orchestrator routing queries to four specialized agents -- Metadata, AudioFingerprint, Rights, and Provenance -- then meta-agent synthesis producing a unified persona voice for transparent confidence in music attribution.

## Image Embed

![Multi-agent attribution architecture flowchart with central orchestrator routing queries to four specialized agents -- Metadata, AudioFingerprint, Rights, and Provenance -- then meta-agent synthesis producing a unified persona voice for transparent confidence in music attribution.](docs/figures/repo-figures/assets/fig-persona-20-multi-agent-attribution.jpg)

*Multi-agent attribution architecture with central orchestrator routing queries to four specialized agents (Metadata, AudioFingerprint, Rights, Provenance), user type detection feeding routing priority, and meta-agent synthesis producing a unified persona voice response.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-20",
    "title": "Multi-Agent Attribution: Specialized Agents, Unified Voice",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Specialized agents handle distinct attribution domains while a meta-agent synthesizes their outputs under a unified persona voice.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "User Type Detection",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["USER TYPE DETECTION", "artist/label/researcher"]
      },
      {
        "name": "Orchestrator",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["ORCHESTRATOR", "Routing + priority"]
      },
      {
        "name": "MetadataAgent",
        "role": "source_musicbrainz",
        "is_highlighted": true,
        "labels": ["METADATA AGENT", "ISRC/ISWC lookup"]
      },
      {
        "name": "AudioFingerprintAgent",
        "role": "source_acoustid",
        "is_highlighted": true,
        "labels": ["AUDIO FINGERPRINT AGENT", "AcoustID matching"]
      },
      {
        "name": "RightsAgent",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["RIGHTS AGENT", "MCP consent queries"]
      },
      {
        "name": "ProvenanceAgent",
        "role": "final_score",
        "is_highlighted": true,
        "labels": ["PROVENANCE AGENT", "A0-A3 assurance scoring"]
      },
      {
        "name": "Meta-Agent Synthesis",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["META-AGENT SYNTHESIS", "Unified persona voice"]
      }
    ],
    "relationships": [
      {
        "from": "User Query",
        "to": "Orchestrator",
        "type": "arrow",
        "label": "user type informs routing"
      },
      {
        "from": "Orchestrator",
        "to": "Four Agents",
        "type": "arrow",
        "label": "parallel dispatch"
      },
      {
        "from": "Four Agents",
        "to": "Meta-Agent",
        "type": "arrow",
        "label": "domain-specific results"
      },
      {
        "from": "Meta-Agent",
        "to": "Unified Response",
        "type": "arrow",
        "label": "synthesized under persona voice"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE ATTRIBUTION ORCHESTRA",
        "body_text": "SPECIALIZED AGENTS, UNIFIED VOICE -- THE ATTRIBUTION ORCHESTRA",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
