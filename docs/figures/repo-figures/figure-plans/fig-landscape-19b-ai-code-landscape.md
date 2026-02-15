# fig-landscape-19b: AI Attribution Trust Stacks: Music vs Code

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-19b |
| **Title** | AI Attribution Trust Stacks: Music vs Code |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

This figure exposes the structural isomorphism between music attribution (A0-A3 assurance levels) and code attribution (unknown/ai/mixed/human from Cursor's Agent Trace spec). It demonstrates that the same trust-stack architecture applies to both domains: graduated confidence, the Oracle Problem, and EU AI Act pressure. This is a companion to fig-landscape-19 (Ethical Certification) and extends the cross-domain method transfer pattern from fig-landscape-26. The audience is software engineers who need an introduction to why music attribution patterns apply directly to their codebase.

## Key Message

Music attribution's A0-A3 assurance levels map exactly to code attribution's unknown/ai/mixed/human classification -- both face the Oracle Problem, both need graduated confidence, and both face EU AI Act pressure -- making Agent Trace the code equivalent of ISRC provenance.

## Visual Concept

Split-panel layout with music attribution on the left and code attribution on the right. Each side shows a four-tier trust stack (A0-A3 / unknown-human) with verification methods at each level. The center column highlights three shared challenges that connect both domains. A bottom bar draws the cross-domain analogy to food safety (extending fig-landscape-19's pattern). An inset diagram shows Agent Trace's architecture flow.

```
+---------------------------------------------------------------+
|  AI ATTRIBUTION TRUST STACKS                                   |
|  ■ Music vs Code: Structural Isomorphism                       |
+---------------------------------------------------------------+
|                         |                |                      |
|  MUSIC ATTRIBUTION      |   SHARED       |  CODE ATTRIBUTION    |
|                         |   CHALLENGES   |                      |
|  ┌─────────────────┐    |                |  ┌─────────────────┐ |
|  │ A3 Artist-       │    │ Oracle        │  │ human Developer- │ |
|  │    verified       │    │ Problem       │  │       attested   │ |
|  │ (ISRC+artist     │    │               │  │ (signed commits  │ |
|  │  attestation)    │    │ Cannot fully  │  │  + attestation)  │ |
|  ├─────────────────┤    │ verify claims │  ├─────────────────┤ |
|  │ A2 Multiple      │    │               │  │ mixed Human+AI   │ |
|  │    sources agree  │    ├──────────────┤  │       iterative  │ |
|  │ (MusicBrainz +   │    │ Graduated    │  │ (trace records   │ |
|  │  Discogs match)  │    │ Confidence   │  │  + git blame)    │ |
|  ├─────────────────┤    │               │  ├─────────────────┤ |
|  │ A1 Single source  │    │ Not binary   │  │ ai  Single LLM   │ |
|  │    claims         │    │ yes/no       │  │     generated    │ |
|  │ (file metadata   │    │              │  │ (Agent Trace     │ |
|  │  only)           │    ├──────────────┤  │  record)         │ |
|  ├─────────────────┤    │ EU AI Act    │  ├─────────────────┤ |
|  │ A0 No data        │    │ Art. 50      │  │ unknown No trace │ |
|  │                   │    │              │  │                  │ |
|  │ (no provenance   │    │ AI-generated │  │ (standard git    │ |
|  │  at all)         │    │ content law  │  │  only)           │ |
|  └─────────────────┘    └──────────────┘  └─────────────────┘ |
|                                                                |
|  CROSS-DOMAIN ANALOGY                                           |
|  ═══════════════════                                            |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         |
|  │ Agent Trace  │  │ git-blame +  │  │ EU AI Act    │         |
|  │ = HACCP      │  │ Co-Authored  │  │ Art. 50      │         |
|  │ (process     │  │ = health     │  │ = FDA        │         |
|  │ provenance)  │  │ grade        │  │ (mandate)    │         |
|  └──────────────┘  └──────────────┘  └──────────────┘         |
|                                                                |
|  ┌─ AGENT TRACE ARCHITECTURE (inset) ──────────────────────┐  |
|  │ Coding Agents → Traces → Storage → IDE / Analytics / Audit│ |
|  └─────────────────────────────────────────────────────────┘  |
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
      text: "AI ATTRIBUTION TRUST STACKS"
    - type: label_editorial
      text: "Music vs Code: Structural Isomorphism"

panel_music:
  position: [60, 140]
  width: 640
  height: 520
  label: "MUSIC ATTRIBUTION"
  tiers:
    - { level: "A3", name: "Artist-verified", method: "ISRC + artist attestation", color_semantic: confidence_high }
    - { level: "A2", name: "Multiple sources agree", method: "MusicBrainz + Discogs match", color_semantic: confidence_medium }
    - { level: "A1", name: "Single source claims", method: "File metadata only", color_semantic: confidence_low }
    - { level: "A0", name: "No data", method: "No provenance at all", color_semantic: assurance_a0 }

panel_shared:
  position: [720, 140]
  width: 360
  height: 520
  label: "SHARED CHALLENGES"
  challenges:
    - { name: "Oracle Problem", description: "Cannot fully verify authorship claims — design for deterrence, not detection" }
    - { name: "Graduated Confidence", description: "Not binary yes/no — continuous spectrum of trust levels" }
    - { name: "EU AI Act Art. 50", description: "AI-generated content transparency obligations — scope expanding" }

panel_code:
  position: [1100, 140]
  width: 640
  height: 520
  label: "CODE ATTRIBUTION"
  tiers:
    - { level: "human", name: "Developer-attested", method: "Signed commits + attestation", color_semantic: confidence_high }
    - { level: "mixed", name: "Human + AI iterative", method: "Trace records + git blame", color_semantic: confidence_medium }
    - { level: "ai", name: "Single LLM generated", method: "Agent Trace record", color_semantic: confidence_low }
    - { level: "unknown", name: "No trace", method: "Standard git only", color_semantic: assurance_a0 }

analogy_bar:
  position: [60, 700]
  width: 1800
  height: 160
  elements:
    - type: label_editorial
      text: "CROSS-DOMAIN ANALOGY"
    - type: solution_component
      mappings:
        - { code: "Agent Trace", food: "HACCP", role: "Process provenance" }
        - { code: "git-blame + Co-Authored-By", food: "Health grade", role: "Visible score" }
        - { code: "EU AI Act Art. 50", food: "FDA", role: "Federal mandate" }

inset_architecture:
  position: [60, 880]
  width: 1800
  height: 120
  label: "AGENT TRACE ARCHITECTURE"
  flow:
    - "Coding Agents"
    - "Structured Traces"
    - "Trace Storage"
    - "IDE Display / Analytics Dashboards / Compliance Audit"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "AI ATTRIBUTION TRUST STACKS" with coral accent square |
| Subtitle | `label_editorial` | "Music vs Code: Structural Isomorphism" |
| Music panel | `solution_component` | Four-tier A0-A3 trust stack with verification methods |
| Code panel | `solution_component` | Four-tier unknown/ai/mixed/human trust stack with trace methods |
| Shared challenges | `callout_bar` | Three shared challenges connecting both domains |
| Oracle Problem | `callout_bar` | "Cannot fully verify authorship claims" |
| Graduated Confidence | `callout_bar` | "Not binary yes/no — continuous spectrum" |
| EU AI Act Art. 50 | `callout_bar` | "AI-generated content transparency obligations" |
| Cross-domain analogy | `archetype_overlay` | Agent Trace/git-blame/EU AI Act mapped to HACCP/health grade/FDA |
| Agent Trace inset | `data_mono` | Architecture flow: Agents → Traces → Storage → IDE/Analytics/Audit |
| Tier labels | `data_mono` | Level identifiers (A0-A3 / unknown-human) |
| Isomorphism arrows | `branching_path` | Horizontal mapping lines connecting corresponding tiers |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| A0 tier | unknown tier | structural_isomorphism | "No provenance data" |
| A1 tier | ai tier | structural_isomorphism | "Single source claim" |
| A2 tier | mixed tier | structural_isomorphism | "Multiple sources/agents" |
| A3 tier | human tier | structural_isomorphism | "Verified attestation" |
| Music panel | Shared challenges | convergence | "Same trust problems" |
| Code panel | Shared challenges | convergence | "Same trust problems" |
| Agent Trace | HACCP | analogy | "Process provenance" |
| git-blame | Health grade | analogy | "Visible score" |
| EU AI Act | FDA | analogy | "Federal mandate" |
| fig-landscape-19 | This figure | companion | "Extends ethical certification to code domain" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Isomorphism | "A0↔unknown, A1↔ai, A2↔mixed, A3↔human — EXACT mapping, not analogy" | Center between panels |
| Oracle Problem | "Neither domain can fully verify authorship — design for deterrence" | Shared challenges panel |
| Agent Trace | "Cursor open spec (Jan 2026) for structured AI code provenance" | Inset architecture box |
| Companion | "See fig-landscape-19 for Fairly Trained / A0-A3 / EU AI Act trust layers" | Top-right corner |

## Text Content

### Labels (Max 30 chars each)

- AI ATTRIBUTION TRUST STACKS
- Music vs Code Isomorphism
- MUSIC ATTRIBUTION
- CODE ATTRIBUTION
- SHARED CHALLENGES
- A3 Artist-verified
- A2 Multiple sources agree
- A1 Single source claims
- A0 No data
- human Developer-attested
- mixed Human + AI iterative
- ai Single LLM generated
- unknown No trace
- Oracle Problem
- Graduated Confidence
- EU AI Act Art. 50
- Agent Trace = HACCP
- git-blame = health grade
- EU AI Act = FDA
- AGENT TRACE ARCHITECTURE
- CROSS-DOMAIN ANALOGY

### Caption (for embedding in documentation)

Music attribution's A0-A3 assurance levels map exactly to code attribution's unknown/ai/mixed/human classification (Cursor Agent Trace, Jan 2026): A0 (no data) maps to unknown (no trace), A1 (single source) maps to ai (single LLM), A2 (multiple sources) maps to mixed (human + AI iterative), and A3 (artist-verified) maps to human (developer-attested). Both domains face the Oracle Problem (cannot fully verify authorship), need graduated confidence over binary certification, and face EU AI Act Article 50 pressure on AI-generated content transparency.

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

1. Agent Trace is from Cursor (Jan 2026) -- it is an OPEN spec, not proprietary. Do NOT describe it as closed or Cursor-only.
2. A0-A3 maps to unknown/ai/mixed/human -- this is the EXACT mapping. Do NOT reorder levels or invent alternative mappings.
3. The Oracle Problem applies IDENTICALLY to both domains -- do NOT suggest one domain has solved it.
4. EU AI Act Art. 50 targets "AI-generated content" broadly -- it does NOT explicitly cover source code yet. Do NOT state that code is covered.
5. AIDEV-* patterns (AIDEV-NOTE, AIDEV-IMMUTABLE, AIDEV-GENERATED) are COMMUNITY conventions, not formal standards. Do NOT describe them as standards.
6. This is a COMPANION to fig-landscape-19 (Ethical Certification) -- reference it, do NOT duplicate its content.
7. The split-panel layout must show BOTH stacks at equal visual weight -- do NOT make one side larger than the other.
8. The inset architecture diagram shows Agent Trace flow only -- do NOT expand it into a full system architecture.
9. The cross-domain analogy bar extends fig-landscape-19's food safety pattern -- maintain consistency with HACCP/health grade/FDA mapping.
10. Do NOT imply that Agent Trace is widely adopted -- it is nascent (Jan 2026). The spec exists; adoption is early.

## Alt Text

Split panel: music A0-A3 assurance and code unknown/ai/mixed/human attribution stacks with shared Oracle Problem.

## JSON Export Block

```json
{
  "id": "fig-landscape-19b",
  "title": "AI Attribution Trust Stacks: Music vs Code",
  "audience": "L3",
  "priority": "P1",
  "layout": "D",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "novelty": 4,
  "companion_to": "fig-landscape-19",
  "cross_domain_isomorphism": {
    "music_stack": [
      { "level": "A0", "name": "No data", "method": "No provenance" },
      { "level": "A1", "name": "Single source claims", "method": "File metadata only" },
      { "level": "A2", "name": "Multiple sources agree", "method": "MusicBrainz + Discogs" },
      { "level": "A3", "name": "Artist-verified", "method": "ISRC + artist attestation" }
    ],
    "code_stack": [
      { "level": "unknown", "name": "No trace", "method": "Standard git only" },
      { "level": "ai", "name": "Single LLM generated", "method": "Agent Trace record" },
      { "level": "mixed", "name": "Human + AI iterative", "method": "Trace records + git blame" },
      { "level": "human", "name": "Developer-attested", "method": "Signed commits + attestation" }
    ],
    "shared_challenges": ["Oracle Problem", "Graduated Confidence", "EU AI Act Art. 50"]
  },
  "cross_domain_analogy": {
    "domain": "food_safety",
    "mappings": [
      { "code": "Agent Trace", "food": "HACCP", "role": "Process provenance" },
      { "code": "git-blame + Co-Authored-By", "food": "Health grade", "role": "Visible score" },
      { "code": "EU AI Act Art. 50", "food": "FDA", "role": "Federal mandate" }
    ]
  },
  "agent_trace_architecture": ["Coding Agents", "Structured Traces", "Trace Storage", "IDE / Analytics / Audit"],
  "references": [
    "Cursor Agent Trace (Jan 2026)",
    "EU AI Act Art. 50",
    "SSRN 6109087"
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component", "archetype_overlay",
    "callout_bar", "data_mono", "branching_path"
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
