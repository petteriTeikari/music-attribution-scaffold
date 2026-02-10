# fig-arch-02: Entity Resolution as Piano Action

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-arch-02 |
| **Title** | Entity Resolution as Piano Action |
| **Gallery** | Technical Wing (docs/architecture/) |
| **Audience** | Developers and technical partners |
| **Template** | D: Instrument Anatomy |
| **Texture** | Watercolor paper, warm parchment, precise linework |

---

## Narrative Position

**Technical Deep Dive: How Entity Resolution Actually Works**

This figure explains the entity resolution algorithm by mapping it to the mechanism inside a piano—the "action" that translates a key press into a hammer strike. Just as piano action has multiple coordinated parts, entity resolution has stages that work together.

---

## Why Should I Care?

> "This is the machinery that matches 'Imogen Heap' to 'I. Heap' to 'iMi'."

## Explain It to a Label Exec

> "Imagine the mechanism inside a piano—when you press a key, a complex sequence happens before the hammer hits the string. That's what happens when we match artist names across databases."

---

## Mogen/Andy Personalization

**Technical figure with domain grounding:**
- The example data flowing through shows Mogen's variations: "Imogen Heap" → "I. Heap" → "Imogen J. Heap" → "iMi"
- Andy's credit variations also shown: "Andy Carne" → "A. Carne" → "Andrew Carne"
- Output shows unified entity with canonical name + aliases

**Not featuring portraits** (technical diagram), but using their data as examples makes it concrete.

---

## Visual Concept

**Style: Piano action cross-section with data flow annotations**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   ╔══════════════════════════════════════════════════════════════════════╗  │
│   ║    E N T I T Y   R E S O L U T I O N   A S   P I A N O   A C T I O N ║  │
│   ╚══════════════════════════════════════════════════════════════════════╝  │
│                                                                              │
│                    THE GRAND PIANO OF DATA MATCHING                          │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │  INPUT (Raw Records)         MECHANISM              OUTPUT          │   │
│   │                                                                      │   │
│   │  ┌──────────────┐                                  ┌──────────────┐ │   │
│   │  │"Imogen Heap" │──┐                               │              │ │   │
│   │  └──────────────┘  │     ┌───────────────┐        │ UNIFIED      │ │   │
│   │  ┌──────────────┐  ├────▶│  DAMPER       │        │ ENTITY       │ │   │
│   │  │"I. Heap"     │──┤     │  (Blocking)   │        │              │ │   │
│   │  └──────────────┘  │     │  "First pass  │        │ Canonical:   │ │   │
│   │  ┌──────────────┐  │     │   filtering"  │        │ Imogen Heap  │ │   │
│   │  │"Imogen J.    │──┤     └───────┬───────┘        │              │ │   │
│   │  │ Heap"        │  │             │                │ Aliases:     │ │   │
│   │  └──────────────┘  │             ▼                │ • I. Heap    │ │   │
│   │  ┌──────────────┐  │     ┌───────────────┐        │ • iMi        │ │   │
│   │  │"iMi"         │──┘     │  HAMMER       │        │ • Imogen J.  │ │   │
│   │  └──────────────┘        │  (Matching)   │───────▶│              │ │   │
│   │                          │  "Fuzzy       │        │ Confidence:  │ │   │
│   │                          │   similarity" │        │ 0.94         │ │   │
│   │                          └───────┬───────┘        │              │ │   │
│   │                                  │                │ Sources: 4   │ │   │
│   │                                  ▼                │              │ │   │
│   │                          ┌───────────────┐        └──────────────┘ │   │
│   │                          │  STRING       │                         │   │
│   │                          │  (Storage)    │                         │   │
│   │                          │  "Unified     │                         │   │
│   │                          │   record"     │                         │   │
│   │                          └───────────────┘                         │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  STAGE MAPPING:                                                      │   │
│   │  • KEY (Input) → Raw source records with variant names              │   │
│   │  • DAMPER (Blocking) → Filter obvious non-matches early             │   │
│   │  • HAMMER (Matching) → Fuzzy similarity scoring (Jaro-Winkler etc) │   │
│   │  • STRING (Storage) → Unified entity with confidence score          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Content Elements

| Element | Semantic Role | Visual Treatment |
|---------|---------------|------------------|
| Piano action cross-section | Central metaphor | Detailed anatomical drawing style |
| Key (input) | Raw records | Multiple variant names |
| Damper | Blocking stage | First filter |
| Hammer | Matching stage | Similarity algorithms |
| String | Storage | Unified output |
| Data flow arrows | Process direction | Elegant callout lines |
| Stage mapping legend | Technical explanation | Bottom box with bullets |

---

## Text Content (Max 30 chars each)

### Labels
- "INPUT (Raw Records)"
- "MECHANISM"
- "OUTPUT"
- "DAMPER (Blocking)"
- "HAMMER (Matching)"
- "STRING (Storage)"
- "UNIFIED ENTITY"
- "Canonical: Imogen Heap"
- "Aliases: I. Heap, iMi..."
- "Confidence: 0.94"

### Legend
- "KEY → Raw source records"
- "DAMPER → Filter non-matches"
- "HAMMER → Fuzzy similarity"
- "STRING → Unified entity"

### Caption
Entity resolution explained through piano action metaphor: variant artist names (key press) pass through blocking (damper), matching (hammer), and storage (string vibration) stages to produce a unified entity with confidence score.

---

## Style-Specific Prompt

```
Create an anatomical cross-section illustration of piano action mechanism with data flow overlay.

STYLE: Victorian-era instrument patent drawing meets data visualization
- Warm parchment background (#F8F0E0)
- Precise black linework with watercolor fills
- Anatomical cross-section aesthetic
- Numbered callout lines with serif labels
- Technical but beautiful (think Steinway factory diagrams)

COMPOSITION:
- Left side: Multiple input boxes with variant artist names
- Center: Detailed piano action mechanism (key, damper, hammer, string)
- Right side: Output box showing unified entity
- Data flow shown as elegant curved lines through mechanism
- Bottom: Stage mapping legend in boxed format

PIANO ACTION DETAIL:
- Show actual piano action components (felt damper, hammer head, strings)
- Label each part with data processing equivalent
- Make the mechanism clearly visible in cross-section

DATA OVERLAY:
- Input variations: "Imogen Heap", "I. Heap", "Imogen J. Heap", "iMi"
- These flow INTO the mechanism
- Output: unified entity card with canonical name, aliases, confidence

MOOD: Technical precision with warmth. This is engineering made beautiful.

TEXT: Elegant serif typography, clear labels, all text crisp and legible.
```

### Negative Prompt
```
cartoon, simplified diagram, corporate flowchart,
sci-fi aesthetic, glowing effects, digital aesthetic,
cold/clinical, pure white background,
generic icons, stock illustration style,
modern sans-serif only (need serif for technical elegance),
abstract representation (want actual piano mechanism visible)
```

---

## Alt Text

Anatomical cross-section illustration showing piano action mechanism as a metaphor for entity resolution. Left side shows input records with variant artist names ("Imogen Heap", "I. Heap", "iMi"). Center shows detailed piano mechanism with labeled stages: damper (blocking), hammer (matching). Right side shows output: unified entity with canonical name, aliases list, and confidence score 0.94. Bottom legend maps piano components to data processing stages.

---

## Musical/Industry References

- **Instrument**: Grand piano action mechanism (specifically Steinway-style)
- **Era reference**: Victorian patent drawings, 19th-century technical illustration
- **Typography**: Elegant serif (similar to music engraving fonts)
- **Color palette**: Warm parchment, sepia tones, black linework

---

## Visual Diversity Matrix Check

| Dimension | This Figure | Differs From README Figures |
|-----------|-------------|----------------------------|
| Primary Color | Sepia/parchment | All README figures use more vibrant palettes |
| Era Reference | Victorian/19th century | README spans 1920s-contemporary |
| Texture | Watercolor on parchment | Different from all README textures |
| Human Figures | None (instrument focus) | fig-rm-04 has human figures |

---

## Status

- [x] Specification complete
- [ ] Generated via Nano Banana Pro
- [ ] Reviewed for clarity
- [ ] Embedded in architecture docs
