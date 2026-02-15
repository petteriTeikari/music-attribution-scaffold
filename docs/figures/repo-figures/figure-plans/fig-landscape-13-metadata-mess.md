# fig-landscape-13: The Metadata Mess: 6 Standards That Don't Connect

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-13 |
| **Title** | The Metadata Mess: 6 Standards That Don't Connect |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Visualizes the fragmented landscape of music identity and metadata standards, showing that while six major systems each cover different aspects of music provenance, no single system connects them into a unified chain. Answers: "Why is music metadata still broken despite having six major standards?"

## Key Message

ISRC, ISWC, ISNI, DDEX, MusicBrainz, and C2PA each cover different aspects of music identity -- but no single system connects all six into a unified provenance chain.

## Visual Concept

Hero layout with six standards rendered as separate "islands" arranged in a loose hexagonal pattern on a conceptual ocean. Between the islands, broken bridge fragments (dashed lines) show the missing connections. Each island shows the standard name, what it identifies (recording, composition, person, exchange, community data, provenance), and its scope. The center of the arrangement is deliberately empty -- representing the missing unified layer. This is a deliberately asymmetric editorial composition, not a neat grid.

```
+-----------------------------------------------------------------------+
|  THE METADATA MESS                                                     |
|  ■ 6 Standards That Don't Connect                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|              ┌───────────┐                  ┌───────────┐             |
|              │   ISRC    │- - - - - - - - - │   ISWC    │             |
|              │ Recording │   broken link     │Composition│             |
|              │  level    │                  │  level    │             |
|              └───────────┘                  └───────────┘             |
|                    :                              :                    |
|                    :  broken                      :  broken            |
|                    :                              :                    |
|         ┌───────────┐          (empty)         ┌───────────┐          |
|         │   ISNI    │         NO UNIFIED       │   DDEX    │          |
|         │  Creator  │          LAYER           │  B2B      │          |
|         │  level    │                          │ Exchange  │          |
|         └───────────┘                          └───────────┘          |
|                    :                              :                    |
|                    :  broken                      :  broken            |
|                    :                              :                    |
|              ┌───────────┐                  ┌───────────┐             |
|              │MusicBrainz│- - - - - - - - - │   C2PA    │             |
|              │ Community │   broken link     │Provenance │             |
|              │ Open Data │                  │Authenttic.│             |
|              └───────────┘                  └───────────┘             |
|                                                                        |
|  ■ Entity resolution ACROSS these standards is the unsolved problem    |
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
    bounds: [0, 0, 1920, 100]
    content: "THE METADATA MESS"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "6 Standards That Don't Connect"
    role: subtitle

  - id: hero_area
    bounds: [60, 160, 1800, 800]
    role: content_area
    label: "Standards landscape"

  - id: empty_center
    bounds: [760, 440, 400, 200]
    role: problem_statement
    label: "NO UNIFIED LAYER"

  - id: footer_callout
    bounds: [60, 1000, 1800, 60]
    role: callout_bar
    label: "Entity resolution across standards is the unsolved problem"

anchors:
  - id: island_isrc
    position: [340, 200]
    size: [320, 160]
    role: solution_component
    label: "ISRC"

  - id: island_iswc
    position: [1260, 200]
    size: [320, 160]
    role: solution_component
    label: "ISWC"

  - id: island_isni
    position: [140, 460]
    size: [320, 160]
    role: solution_component
    label: "ISNI"

  - id: island_ddex
    position: [1460, 460]
    size: [320, 160]
    role: solution_component
    label: "DDEX"

  - id: island_musicbrainz
    position: [340, 720]
    size: [320, 160]
    role: solution_component
    label: "MusicBrainz"

  - id: island_c2pa
    position: [1260, 720]
    size: [320, 160]
    role: solution_component
    label: "C2PA"

  - id: broken_isrc_iswc
    from: island_isrc
    to: island_iswc
    type: dashed_line
    label: "broken link"

  - id: broken_isrc_isni
    from: island_isrc
    to: island_isni
    type: dashed_line
    label: "broken link"

  - id: broken_iswc_ddex
    from: island_iswc
    to: island_ddex
    type: dashed_line
    label: "broken link"

  - id: broken_isni_musicbrainz
    from: island_isni
    to: island_musicbrainz
    type: dashed_line
    label: "broken link"

  - id: broken_ddex_c2pa
    from: island_ddex
    to: island_c2pa
    type: dashed_line
    label: "broken link"

  - id: broken_musicbrainz_c2pa
    from: island_musicbrainz
    to: island_c2pa
    type: dashed_line
    label: "broken link"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "THE METADATA MESS" in editorial caps with accent square |
| Subtitle | `label_editorial` | "6 Standards That Don't Connect" |
| ISRC island | `solution_component` | Recording-level identifier, managed by IFPI, assigns unique ID to each recording |
| ISWC island | `solution_component` | Composition-level identifier, managed by CISAC, assigns unique ID to each musical work |
| ISNI island | `solution_component` | Creator-level identifier, ISO 27729, identifies persons and organizations |
| DDEX island | `solution_component` | B2B metadata exchange standard, XML-based, used by labels and distributors |
| MusicBrainz island | `solution_component` | Community-maintained open database, crowd-sourced metadata, MBID identifiers |
| C2PA island | `solution_component` | Content provenance and authenticity standard, cryptographic manifests, Coalition for Content Provenance |
| Empty center | `problem_statement` | Deliberately empty space representing the missing unified layer |
| Broken bridges | `data_flow` | Dashed lines between islands showing non-existent or partial connections |
| Footer callout | `callout_bar` | "Entity resolution ACROSS these standards is the unsolved infrastructure problem" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| ISRC | ISWC | dashed_line | No automatic recording-to-composition link |
| ISRC | ISNI | dashed_line | No automatic recording-to-creator link |
| ISWC | DDEX | dashed_line | Partial: DDEX can carry ISWC but often missing |
| ISNI | MusicBrainz | dashed_line | MusicBrainz has some ISNI links but coverage is sparse |
| DDEX | C2PA | dashed_line | No integration between B2B exchange and provenance |
| MusicBrainz | C2PA | dashed_line | No integration between community data and provenance |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "NO UNIFIED LAYER" | No single system connects recording identity (ISRC) to composition identity (ISWC) to creator identity (ISNI) to provenance (C2PA) -- this is the entity resolution gap | center void |
| "SCOPE MISMATCH" | ISRC/ISWC/ISNI identify entities; DDEX exchanges metadata; MusicBrainz stores data; C2PA proves authenticity -- they solve different problems | right margin |
| "OPEN DATA GAP" | MusicBrainz is the only open, community-maintained standard -- all others are proprietary or consortium-controlled | bottom-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ISRC (Recording)"
- Label 2: "ISWC (Composition)"
- Label 3: "ISNI (Creator)"
- Label 4: "DDEX (B2B Exchange)"
- Label 5: "MusicBrainz (Open Data)"
- Label 6: "C2PA (Provenance)"
- Label 7: "No Unified Layer"
- Label 8: "Broken Link"
- Label 9: "Entity Resolution Gap"
- Label 10: "Recording-Level ID"
- Label 11: "Composition-Level ID"
- Label 12: "Creator-Level ID"

### Caption (for embedding in documentation)

Six major music identity and metadata standards -- ISRC (recording), ISWC (composition), ISNI (creator), DDEX (B2B exchange), MusicBrainz (community open data), and C2PA (content provenance) -- each cover different aspects of the music identity chain but lack interoperability. Entity resolution across these standards remains the unsolved infrastructure problem for music attribution.

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

8. ISRC is managed by IFPI -- do NOT attribute it to another organization.
9. ISWC is managed by CISAC -- do NOT conflate with ISRC.
10. ISNI is ISO 27729 -- do NOT describe it as music-specific (it covers all creative domains).
11. DDEX is XML-based B2B exchange -- do NOT describe it as a database or identifier.
12. MusicBrainz uses MBIDs (MusicBrainz IDs) -- do NOT call them ISRCs.
13. C2PA is the Coalition for Content Provenance and Authenticity -- do NOT confuse with Content ID or watermarking.
14. The "broken bridges" are conceptual -- do NOT claim zero integration exists (some partial links exist, they are just incomplete).
15. Do NOT add Spotify, Apple Music, or streaming platform IDs -- these are proprietary, not standards.
16. Do NOT imply this scaffold solves the metadata mess -- it is a research scaffold, not a standards body.

## Alt Text

Six music identity standards as disconnected islands with broken bridges showing no unified provenance chain exists

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-13",
    "title": "The Metadata Mess: 6 Standards That Don't Connect",
    "audience": "L2",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "Six major standards each cover different aspects of music identity but no system connects them all.",
    "layout_flow": "hexagonal-islands",
    "key_structures": [
      {
        "name": "ISRC",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["ISRC", "Recording-level", "IFPI"]
      },
      {
        "name": "ISWC",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["ISWC", "Composition-level", "CISAC"]
      },
      {
        "name": "ISNI",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["ISNI", "Creator-level", "ISO 27729"]
      },
      {
        "name": "DDEX",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["DDEX", "B2B exchange", "XML-based"]
      },
      {
        "name": "MusicBrainz",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["MusicBrainz", "Community open data", "MBIDs"]
      },
      {
        "name": "C2PA",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["C2PA", "Provenance", "Cryptographic"]
      },
      {
        "name": "Empty Center",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["No unified layer"]
      }
    ],
    "relationships": [
      {
        "from": "ISRC",
        "to": "ISWC",
        "type": "dashed_line",
        "label": "broken link"
      },
      {
        "from": "ISRC",
        "to": "ISNI",
        "type": "dashed_line",
        "label": "broken link"
      },
      {
        "from": "ISWC",
        "to": "DDEX",
        "type": "dashed_line",
        "label": "partial link"
      },
      {
        "from": "ISNI",
        "to": "MusicBrainz",
        "type": "dashed_line",
        "label": "sparse coverage"
      },
      {
        "from": "DDEX",
        "to": "C2PA",
        "type": "dashed_line",
        "label": "no integration"
      },
      {
        "from": "MusicBrainz",
        "to": "C2PA",
        "type": "dashed_line",
        "label": "no integration"
      }
    ],
    "callout_boxes": [
      {
        "heading": "NO UNIFIED LAYER",
        "body_text": "No system connects recording, composition, creator, and provenance identities",
        "position": "center"
      },
      {
        "heading": "ENTITY RESOLUTION GAP",
        "body_text": "Cross-standard entity resolution is the unsolved infrastructure problem",
        "position": "footer"
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
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
