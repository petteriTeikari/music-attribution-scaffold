# fig-ecosystem-06: Content ID System Comparison

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-06 |
| **Title** | Content ID System Comparison |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Compares fingerprinting vs watermark detection vs embedding similarity for content identification. Answers: "Which content identification approach serves which Oracle Problem confidence level?"

## Key Message

Three content identification approaches serve different Oracle Problem confidence levels -- fingerprinting works on distributed copies, watermarks require embedding at creation, embeddings handle transformations.

## Visual Concept

Three columns, each representing a content identification approach. Each column contains the approach name, mechanism description, when it works, limitations, and a confidence level indicator. Fingerprinting (post-hoc, works on copies), Watermark Detection (attribution-by-design, requires embedding at creation, C2PA), Embedding Similarity (handles transformations, lower precision).

```
+-----------------------------------------------------------------------+
|  CONTENT ID SYSTEM COMPARISON                                          |
|  ■ Three Approaches to the Oracle Problem                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. FINGERPRINTING          II. WATERMARK              III. EMBEDDING  |
|  Audio Signature Match       DETECTION                  SIMILARITY     |
|  ═══════════════════         Imperceptible Markers      Vector Distance |
|                              ═══════════════════        ═══════════════ |
|                                                                        |
|  ┌───────────────────┐      ┌───────────────────┐     ┌──────────────┐ |
|  │                   │      │                   │     │              │ |
|  │  MECHANISM        │      │  MECHANISM        │     │  MECHANISM   │ |
|  │  ──────────       │      │  ──────────       │     │  ──────────  │ |
|  │  Spectral hash    │      │  Imperceptible    │     │  Audio       │ |
|  │  of audio signal  │      │  signal embedded  │     │  embeddings  │ |
|  │                   │      │  at creation time │     │  in vector   │ |
|  │                   │      │                   │     │  space       │ |
|  │  WORKS ON         │      │  WORKS ON         │     │              │ |
|  │  ─────────        │      │  ─────────        │     │  WORKS ON    │ |
|  │  Exact copies     │      │  Any copy if      │     │  ─────────   │ |
|  │  Minor edits      │      │  watermark        │     │  Transform-  │ |
|  │  Distribution     │      │  survives         │     │  ations      │ |
|  │  tracking         │      │  processing       │     │  Remixes     │ |
|  │                   │      │                   │     │  Covers      │ |
|  │  LIMITATIONS      │      │  LIMITATIONS      │     │              │ |
|  │  ──────────       │      │  ──────────       │     │  LIMITATIONS │ |
|  │  Fails on heavy   │      │  Must embed at    │     │  ──────────  │ |
|  │  transformations  │      │  creation (not    │     │  Lower       │ |
|  │  Post-hoc only    │      │  retroactive)     │     │  precision   │ |
|  │                   │      │  C2PA standard    │     │  Approximate │ |
|  │                   │      │                   │     │  matches     │ |
|  │  ──────────────── │      │  ──────────────── │     │              │ |
|  │  ORACLE LEVEL:    │      │  ORACLE LEVEL:    │     │  ─────────── │ |
|  │  Post-hoc         │      │  Attribution-     │     │  ORACLE:     │ |
|  │  verification     │      │  by-design        │     │  Similarity  │ |
|  │                   │      │                   │     │  estimation  │ |
|  └───────────────────┘      └───────────────────┘     └──────────────┘ |
|                                                                        |
|  ◄── Exact match ───── Designed provenance ───── Fuzzy match ────►    |
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
    content: "CONTENT ID SYSTEM COMPARISON"
    role: title

  - id: fingerprint_panel
    bounds: [60, 160, 560, 760]
    role: content_area
    label: "I. FINGERPRINTING"

  - id: watermark_panel
    bounds: [680, 160, 560, 760]
    role: content_area
    label: "II. WATERMARK DETECTION"

  - id: embedding_panel
    bounds: [1300, 160, 560, 760]
    role: content_area
    label: "III. EMBEDDING SIMILARITY"

  - id: spectrum_axis
    bounds: [60, 960, 1800, 80]
    role: callout_bar
    label: "Exact match to fuzzy match spectrum"

anchors:
  - id: fingerprint_mechanism
    position: [120, 240]
    size: [440, 120]
    role: processing_stage
    label: "Spectral hash of audio signal"

  - id: fingerprint_works
    position: [120, 380]
    size: [440, 120]
    role: processing_stage
    label: "Exact copies, minor edits"

  - id: fingerprint_limits
    position: [120, 520]
    size: [440, 100]
    role: callout_bar
    label: "Fails on heavy transformations"

  - id: fingerprint_oracle
    position: [120, 640]
    size: [440, 60]
    role: data_mono
    label: "Post-hoc verification"

  - id: watermark_mechanism
    position: [740, 240]
    size: [440, 120]
    role: processing_stage
    label: "Imperceptible signal at creation"

  - id: watermark_works
    position: [740, 380]
    size: [440, 120]
    role: processing_stage
    label: "Any copy if watermark survives"

  - id: watermark_limits
    position: [740, 520]
    size: [440, 100]
    role: callout_bar
    label: "Must embed at creation, C2PA"

  - id: watermark_oracle
    position: [740, 640]
    size: [440, 60]
    role: data_mono
    label: "Attribution-by-design"

  - id: embedding_mechanism
    position: [1360, 240]
    size: [440, 120]
    role: processing_stage
    label: "Audio embeddings in vector space"

  - id: embedding_works
    position: [1360, 380]
    size: [440, 120]
    role: processing_stage
    label: "Transformations, remixes, covers"

  - id: embedding_limits
    position: [1360, 520]
    size: [440, 100]
    role: callout_bar
    label: "Lower precision, approximate"

  - id: embedding_oracle
    position: [1360, 640]
    size: [440, 60]
    role: data_mono
    label: "Similarity estimation"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Fingerprinting panel | `content_area` | Spectral hash matching for exact copies and minor edits |
| Watermark Detection panel | `content_area` | Imperceptible markers embedded at creation time (C2PA) |
| Embedding Similarity panel | `content_area` | Vector distance in embedding space for transformations |
| Mechanism blocks | `processing_stage` | Technical description of each approach |
| Works-on blocks | `processing_stage` | Use cases where each approach succeeds |
| Limitation blocks | `callout_bar` | Where each approach fails or has constraints |
| Oracle level indicators | `data_mono` | Post-hoc / Attribution-by-design / Similarity estimation |
| Match spectrum axis | `data_flow` | Exact match to fuzzy match continuum |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Fingerprinting | Match spectrum (left) | arrow | "exact match" |
| Watermark | Match spectrum (center) | arrow | "designed provenance" |
| Embedding | Match spectrum (right) | arrow | "fuzzy match" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ORACLE PROBLEM" | Each approach addresses a different aspect of the Oracle Problem -- digital systems cannot fully verify physical/training reality | top-right |
| "C2PA" | Coalition for Content Provenance and Authenticity -- industry standard for watermark-based provenance | inset in watermark panel |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Fingerprinting"
- Label 2: "Watermark Detection"
- Label 3: "Embedding Similarity"
- Label 4: "Post-hoc verification"
- Label 5: "Attribution-by-design"
- Label 6: "Similarity estimation"
- Label 7: "C2PA standard"

### Caption (for embedding in documentation)

Three content identification approaches address different aspects of the Oracle Problem: fingerprinting verifies exact copies post-hoc, watermark detection requires attribution-by-design at creation, and embedding similarity handles transformations with approximate matching.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `content_area`, `data_mono` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" may appear as this is L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD nodes: content_id_system, watermark_detection, provenance_verification. provenance_strategy -> watermark_detection (moderate). data_model_complexity -> content_id_system (weak).
10. C2PA is Coalition for Content Provenance and Authenticity. Do NOT expand the acronym incorrectly.
11. Fingerprinting is post-hoc; watermarking is attribution-by-design. Do NOT conflate these two design philosophies.
12. Do NOT claim specific accuracy numbers for any of these three approaches -- the comparison is qualitative.
13. Embedding similarity handles transformations (remixes, covers) but with lower precision than exact-match approaches.

## Alt Text

Content ID comparison: fingerprinting vs watermark detection vs embedding similarity

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-06",
    "title": "Content ID System Comparison",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Three content ID approaches serve different Oracle Problem confidence levels.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Fingerprinting Panel",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Fingerprinting", "Spectral hash", "Post-hoc"]
      },
      {
        "name": "Watermark Detection Panel",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["Watermark Detection", "C2PA", "Attribution-by-design"]
      },
      {
        "name": "Embedding Similarity Panel",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Embedding Similarity", "Vector distance", "Fuzzy match"]
      }
    ],
    "relationships": [
      {
        "from": "Fingerprinting",
        "to": "Exact Match End",
        "type": "arrow",
        "label": "exact copies and minor edits"
      },
      {
        "from": "Watermark Detection",
        "to": "Designed Provenance",
        "type": "arrow",
        "label": "embedded at creation, survives processing"
      },
      {
        "from": "Embedding Similarity",
        "to": "Fuzzy Match End",
        "type": "arrow",
        "label": "transformations, remixes, covers"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ORACLE PROBLEM",
        "body_text": "Each approach addresses a different aspect -- digital systems cannot fully verify physical/training reality",
        "position": "top-right"
      },
      {
        "heading": "C2PA",
        "body_text": "Coalition for Content Provenance and Authenticity -- industry standard for watermark-based provenance",
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
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
