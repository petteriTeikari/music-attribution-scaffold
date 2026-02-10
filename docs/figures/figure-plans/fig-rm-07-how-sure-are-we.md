# fig-rm-07: How Sure Are We?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-07 |
| **Title** | How Sure Are We? |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |
| **Gap Filled** | What does confidence scoring actually mean? |

---

## Content Specification

### Title
HOW SURE ARE WE?

### Subtitle
Confidence Scores Explained

### Main Visual Elements
- Three circular "meter" badges showing different confidence levels
- Each meter shows a fill level (like a fuel gauge)
- Simple explanations under each level
- Real example showing what each level means for a credit

### Layout Pattern
Pattern A: Horizontal Progression (like fig-rm-03)

```
    LOW                    MEDIUM                   HIGH
  ┌─────────┐            ┌─────────┐            ┌─────────┐
  │  ◐      │            │  ◕      │            │  ●      │
  │  0.3    │            │  0.6    │            │  0.95   │
  │         │            │         │            │         │
  │ "Found  │            │"Probably│            │ "We're  │
  │  some-  │            │  right" │            │ certain"│
  │  thing" │            │         │            │         │
  └─────────┘            └─────────┘            └─────────┘
      │                      │                      │
      ▼                      ▼                      ▼
  "One source           "Two sources           "Multiple
   mentions it"          agree"                 sources +
                                                artist confirms"
```

### Labels & Text

**Title & Subtitle:**
- "HOW SURE ARE WE?"
- "Confidence Scores Explained"

**Level 1 - Low (0.3):**
- "0.3"
- "Found something..."
- "One source mentions it"
- Meter: ~30% filled

**Level 2 - Medium (0.6):**
- "0.6"
- "Probably right"
- "Two sources agree"
- Meter: ~60% filled

**Level 3 - High (0.95):**
- "0.95"
- "We're certain"
- "Multiple sources + artist confirms"
- Meter: ~95% filled

**Example box:**
- "EXAMPLE: Producer credit on 'Hide and Seek'"
- "0.3 = Streaming says 'unknown'"
- "0.6 = Discogs + MusicBrainz agree"
- "0.95 = Both databases + Mogen confirms"

**Bottom quote:**
- "Every credit comes with a number. Higher = more trustworthy."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| Low meter | Uncertainty | Pink outline, mostly empty |
| Medium meter | Partial confidence | Pink/teal mix |
| High meter | High confidence | Teal fill, full |
| Arrows | Progression | Black, hand-drawn |
| Example box | Concrete illustration | Black border |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image features three circular meter/gauge badges arranged horizontally, showing increasing confidence levels. LEFT METER: Shows '0.3' with the gauge about 30% filled, labeled 'Found something...' with explanation 'One source mentions it'. MIDDLE METER: Shows '0.6' with the gauge about 60% filled, labeled 'Probably right' with explanation 'Two sources agree'. RIGHT METER: Shows '0.95' with the gauge about 95% filled, labeled 'We're certain' with explanation 'Multiple sources + artist confirms'. Hand-drawn arrows connect the meters showing progression. Below is an example box showing how a producer credit moves from 0.3 to 0.95 as more sources confirm. The title 'HOW SURE ARE WE?' is at the top in a bold, black, hand-printed font, with the subtitle 'Confidence Scores Explained' below it. At the bottom is the quote 'Every credit comes with a number. Higher = more trustworthy.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop.",
  "negative_prompt": "garbled text, illegible glyphs, blurred characters, pseudo-text, corrupted letters, gibberish words, broken typography, visible hex codes, color codes as text, file paths visible, markdown syntax visible, citation brackets, '[cite:' text, '.md' text, internal references as text, yaml syntax, json syntax, technical markup visible, prompt instructions as labels, style keywords visible, rendering keywords as labels, aesthetic descriptors as text, parentheses with style words"
}
```

### ⚠️ Internal Reference Warning

The style guide, color codes, and file references in this document are for **workflow use only**. They must NEVER appear as visible text in the generated image. The negative prompt above helps prevent this.

---

## Why Should I Care?

> "Now you know which credits to trust and which need more verification."

## Explain It to a Label Exec

> "Think of it like a credit score for music credits. 0.95 means we're very confident. 0.3 means we found something but can't verify it yet."

---

## Alt Text

Risograph-style zine page showing three circular meter badges representing confidence scores. Left meter shows 0.3 (low, "Found something"), middle shows 0.6 (medium, "Probably right"), right shows 0.95 (high, "We're certain"). Each meter has increasing fill levels. An example box shows how a producer credit gains confidence as more sources confirm. Title reads "HOW SURE ARE WE?"

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
