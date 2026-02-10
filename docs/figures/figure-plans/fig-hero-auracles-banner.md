# Figure Content Specification: Music Attribution Hero Banner

**Version:** 1.0 (Gemini-optimized with Spatial Anchors)
**See STYLE-GUIDE.md for base specifications; this figure uses artistic overrides below.**

---

## Meta

```json
{
  "figure_id": "hero-banner",
  "title": "the system: Music Attribution with Transparent Confidence",
  "type": "hero banner / conceptual illustration",
  "section": "README.md (top)",
  "priority": "high",
  "aspect_ratio": "16:9 (1920×1080 or 1600×900)"
}
```

---

## Artistic Style Override

**This figure departs from the Herman Miller infographic style** to use a more artistic, editorial illustration aesthetic suitable for a hero banner.

### Visual Direction
- **Primary inspiration**: Vintage anatomical diagrams meets music iconography
- **Secondary inspiration**: Hsiao-Ron Cheng folk art, Japanese Showa-era educational posters
- **Texture**: Hand-painted, slightly textured paper feel
- **Color mood**: Warm cream base, dusty pastels, muted metallics
- **NOT**: Corporate, sterile, purely technical, sci-fi glowing effects

### Color Palette (Artistic Override)

| Semantic Role | Hex | Swatch | Usage |
|---------------|-----|--------|-------|
| `background_paper` | #FCF5E5 | 🟨 | Warm cream paper texture |
| `accent_problem` | #D4A5A5 | 🩷 | Dusty rose - chaos/disorder |
| `accent_solution` | #A3B899 | 🟩 | Sage green - trust/harmony |
| `accent_gold` | #D4A03C | 🟡 | Muted gold - verification/reward |
| `deep_contrast` | #1E3A5F | 🔵 | Navy - outlines, text |
| `human_warmth` | #E8A598 | 🧡 | Soft coral - figures/humanity |
| `trust_teal` | #2E7D7B | 🩵 | Verdigris - confidence/verified |

---

## Content Architecture

### Primary Message
> The system transforms chaotic, fragmented music attribution data into unified, confidence-scored records that empower artists.

### Supporting Messages
1. Music metadata is fragmented across siloed databases (the problem)
2. Entity resolution unifies disparate sources (the process)
3. Confidence scoring provides transparency (the trust layer)
4. Artists regain control of their credits (the outcome)

### Layout Flow
```
16:9 panoramic composition with central figure + side panels

LEFT SIDE (Problem/Input):
- Fragmented vinyl records, tangled data streams
- Question marks, scattered papers
- Muted, cooler tones

CENTER (The Attribution Engine):
- Humanoid figure OR stylized machine as "music keeper"
- Internal anatomy: database heart, resolution maze brain
- Receiving data flows from left, outputting clarity to right

RIGHT SIDE (Solution/Output):
- Complete golden record, unified data
- Checkmarks, confidence meters
- Warm, brighter tones

BOTTOM:
- "ATTRIBUTION" typography banner
- Decorative musical motifs
```

### Spatial Anchors (v1.0)
```yaml
spatial_anchors:
  left_chaos:
    x: 0.15
    y: 0.5
    content: "Fragmented data silos"
  center_figure:
    x: 0.5
    y: 0.45
    content: "the attribution engine"
  right_harmony:
    x: 0.85
    y: 0.5
    content: "Unified, confidence-scored output"
  title_banner:
    x: 0.5
    y: 0.92
    content: "ATTRIBUTION typography"
  top_flow:
    x: 0.5
    y: 0.15
    content: "Data flow arrows/ribbons"
```

---

## Key Structures

| Structure | Role | Semantic Tag | Labels |
|-----------|------|--------------|--------|
| Broken vinyl records | Data silos | `warning_caution` | "Labels", "Streaming", "Rights Orgs" |
| Tangled threads | Messy metadata | `pathological_critical` | "40%+ errors" |
| Central figure | The System engine | `source_system` | "Entity Resolution" |
| Database heart | Unified storage | `healthy_normal` | "PostgreSQL + pgvector" |
| Maze brain | Resolution logic | `source_system` | "Fuzzy matching" |
| Golden record | Verified output | `verified_gold` | "A3 Verified" |
| Confidence meter | Trust display | `healthy_normal` | "0.0 → 1.0" |
| Checkmarks | Verification | `healthy_normal` | "Provenance" |
| Small human figures | Artists | `neutral_standard` | "Artists empowered" |

---

## Signal Pathways

| From | To | Type | Semantic Tag |
|------|-----|------|--------------|
| Discogs | Central Figure | Data ingest | `secondary_pathway` |
| MusicBrainz | Central Figure | Data ingest | `secondary_pathway` |
| User Input | Central Figure | Artist claims | `primary_pathway` |
| Central Figure | Unified Database | Resolution | `primary_pathway` |
| Database | Golden Record | Verified output | `healthy_normal` |
| Database | MCP API | AI access | `secondary_pathway` |

---

## Numerical Annotations

```yaml
- error_rate: "40%+ music metadata is wrong"
- unclaimed_royalties: "$2.5B+ annually"
- data_sources: "3+ sources aggregated"
- confidence_range: "0.0 to 1.0 per field"
- trust_levels: "A0 → A1 → A2 → A3"
- attribution_crisis: "No single source of truth"
```

---

## Callout Boxes (Visual Panels)

### Panel 1: THE PROBLEM (Left)
```yaml
visual_elements:
  - "Cracked/broken vinyl record"
  - "Sheet music torn into pieces"
  - "Question marks floating"
  - "Small worried figures"
semantic_tag: "warning_caution"
mood: "Frustration, chaos, loss"
```

### Panel 2: THE ENGINE (Center)
```yaml
visual_elements:
  - "Humanoid/mechanical figure with transparent internals"
  - "Heart = glowing database"
  - "Brain = maze being solved"
  - "Arms/veins = data flow ribbons"
semantic_tag: "source_system"
mood: "Calm, trustworthy, processing"
```

### Panel 3: THE SOLUTION (Right)
```yaml
visual_elements:
  - "Complete golden vinyl record"
  - "Checkmarks and trust badges"
  - "Confidence dial pointing high"
  - "Small celebrating figures"
semantic_tag: "healthy_normal"
mood: "Clarity, joy, empowerment"
```

### Panel 4: TITLE BANNER (Bottom)
```yaml
typography: "ATTRIBUTION"
style: "Vintage display type, musical decorations"
tagline: "Music attribution with transparent confidence"
decorations: "G-clefs, musical notes, flowing ribbons"
```

---

## Caption / Alt Text

```
The system hero banner: A vintage-style illustration depicting
the transformation of chaotic music attribution data (left:
broken records, tangled metadata) through the system engine
(center: entity resolution and confidence scoring) into unified,
verified attribution records (right: golden record, checkmarks).
The warm, hand-painted aesthetic emphasizes human artistry and
trust over cold technology.
```

---

## Verification Checklist

- [x] Primary message clear in one sentence
- [x] 12+ content elements defined
- [x] Layout flow specified (panoramic with center focus)
- [x] Spatial anchors defined (5 key positions)
- [x] Semantic tags used for all structures
- [x] Color palette defined (artistic override)
- [x] Signal pathways show data flow
- [x] Callout boxes describe visual panels
- [x] **Artistic direction explicit** (not corporate infographic)

---

## JSON Export (for Gemini/Nano Banana Pro)

```json
{
  "meta": {
    "figure_id": "hero-banner",
    "title": "the system: Music Attribution with Transparent Confidence",
    "aspect_ratio": "16:9",
    "style": "vintage illustration, hand-painted texture, Hsiao-Ron Cheng aesthetic"
  },
  "content_architecture": {
    "primary_message": "The system transforms fragmented music metadata into unified, confidence-scored attribution records.",
    "layout_flow": "Panoramic: chaos (left) → processing (center) → harmony (right) + title banner (bottom)",
    "spatial_anchors": {
      "left_chaos": {"x": 0.15, "y": 0.5, "content": "Broken records, tangled data"},
      "center_figure": {"x": 0.5, "y": 0.45, "content": "the system engine figure"},
      "right_harmony": {"x": 0.85, "y": 0.5, "content": "Golden record, checkmarks"},
      "title_banner": {"x": 0.5, "y": 0.92, "content": "ATTRIBUTION typography"}
    },
    "key_structures": [
      {
        "name": "Broken Vinyl Records",
        "description": "Fragmented data silos (Labels, Streaming, Rights Orgs)",
        "semantic_tag": "warning_caution",
        "position": "left"
      },
      {
        "name": "Attribution Engine Figure",
        "description": "Central humanoid/machine with database heart, maze brain",
        "semantic_tag": "source_system",
        "position": "center"
      },
      {
        "name": "Golden Record",
        "description": "Verified, unified attribution output",
        "semantic_tag": "healthy_normal",
        "position": "right"
      },
      {
        "name": "Confidence Meter",
        "description": "Dial showing trust level (0.0 → 1.0)",
        "semantic_tag": "healthy_normal",
        "position": "right"
      }
    ],
    "signal_pathways": [
      {"from": "Data Sources", "to": "Engine", "type": "ingest"},
      {"from": "Engine", "to": "Golden Record", "type": "resolution"},
      {"from": "Engine", "to": "MCP API", "type": "access"}
    ],
    "visual_style": {
      "texture": "Hand-painted, textured paper",
      "colors": "Warm cream, dusty rose, sage green, muted gold",
      "mood": "Warm, trustworthy, artistic, human-centered",
      "inspiration": "Hsiao-Ron Cheng, Showa-era educational posters, anatomical diagrams"
    }
  }
}
```

---

## Generation Prompt (Nano Banana Pro / DALL-E / Midjourney)

### Full Prompt
```
Create a 16:9 hero banner illustration for "the system" - a music attribution platform.

STYLE: Vintage editorial illustration, hand-painted texture, inspired by Hsiao-Ron Cheng folk art and Showa-era Japanese educational posters. Warm cream paper background. NOT corporate, NOT sci-fi, NOT photorealistic.

COLOR PALETTE: Dusty rose (#D4A5A5), sage green (#A3B899), muted gold (#D4A03C), navy outlines (#1E3A5F), soft coral for figures (#E8A598).

COMPOSITION (Left to Right):
- LEFT (The Problem): Broken vinyl records, tangled thread/data streams, scattered sheet music, question marks, small worried human figures. Muted, cooler tones.
- CENTER (The Engine): Stylized humanoid figure with transparent internals showing: glowing database as heart, maze as brain, data ribbons as veins. Calm, trustworthy expression. Receiving chaotic inputs from left, outputting clarity to right.
- RIGHT (The Solution): Complete golden vinyl record, checkmarks/badges, confidence meter dial pointing high, flowing musical notation, small celebrating human figures. Warm, brighter tones.
- BOTTOM: "ATTRIBUTION" in vintage display typography with musical note decorations. Optional tagline: "Music attribution with transparent confidence"

MOOD: Warm, hopeful, human-centered, artistic, empowering. The illustration should appeal to creative professionals (musicians, artists) while conveying trust and technology.
```

### Simplified Prompt
```
Vintage folk art illustration, 16:9 hero banner. Warm cream background. Left side: broken vinyl records, tangled wires, chaos. Center: humanoid figure with database-heart and maze-brain, processing data. Right side: golden record, checkmarks, harmony. Bottom: "ATTRIBUTION" typography. Style: Hsiao-Ron Cheng, hand-painted, dusty pastels (rose, sage, gold). NOT corporate, NOT photorealistic.
```

---

## Integration

### README.md Placement
```markdown
# Music Attribution

[![Python 3.13](badges...)]

![Music Attribution Hero Banner](docs/figures/assets/fig-hero-auracles-banner.jpg)

**Music attribution with transparent confidence.**
```

### File Specs
- **Output**: JPEG, optimized (~200-300KB)
- **Dimensions**: 1920×1080 or 1600×900
- **Filename**: `fig-hero-auracles-banner.jpg`
