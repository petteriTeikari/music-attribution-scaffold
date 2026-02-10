# fig-rm-09: What You Get

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-09 |
| **Title** | What You Get |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |
| **Gap Filled** | Tangible artist benefits |

---

## Content Specification

### Title
WHAT YOU GET

### Subtitle
From Chaos to Clarity

### Main Visual Elements
- LEFT side: "BEFORE" - chaotic, problematic state (pink/negative)
- RIGHT side: "AFTER" - organized, empowered state (teal/positive)
- Hand-drawn arrow showing transformation
- Mogen appears on the "AFTER" side, empowered

### Layout Pattern
Pattern D: Before/After comparison

```
         BEFORE                          AFTER
    ┌─────────────┐                ┌─────────────┐
    │             │                │             │
    │  ❌ Lost    │                │  ✓ Verified │
    │   royalties │                │   credits   │
    │             │                │             │
    │  ❌ Wrong   │    ───────▶   │  ✓ Tracked  │
    │   credits   │                │   usage     │
    │             │                │             │
    │  ❌ No AI   │                │  ✓ You      │
    │   control   │                │   decide    │
    │             │                │             │
    │  😰        │                │  😊 MOGEN   │
    └─────────────┘                └─────────────┘
```

### Labels & Text

**Title & Subtitle:**
- "WHAT YOU GET"
- "From Chaos to Clarity"

**BEFORE column (problems):**
- "BEFORE"
- "❌ Lost royalties"
- "❌ Wrong credits"
- "❌ No control over AI"
- "❌ Invisible to the industry"

**AFTER column (benefits):**
- "AFTER"
- "✓ Verified credits"
- "✓ Tracked usage"
- "✓ You decide on AI"
- "✓ Findable and credited"

**Arrow:**
- "ATTRIBUTION" (on the transformation arrow)

**Bottom quote:**
- "From invisible to verified. From chaos to control."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| BEFORE column | Problems | Pink accents, X marks |
| AFTER column | Benefits | Teal accents, checkmarks |
| Transformation arrow | The System solution | Black with label |
| Mogen in AFTER | Empowered artist | Teal highlight |
| X marks | Negatives | Pink |
| Checkmarks | Positives | Teal |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image shows a before/after comparison with two rectangular panels side by side. LEFT PANEL labeled 'BEFORE' with pink accents: Lists problems with X marks - 'Lost royalties', 'Wrong credits', 'No control over AI', 'Invisible to the industry'. Shows a frustrated/sad simple face icon. RIGHT PANEL labeled 'AFTER' with teal accents: Lists benefits with checkmarks - 'Verified credits', 'Tracked usage', 'You decide on AI', 'Findable and credited'. Shows a stylized female figure with blonde ponytail and rectangular glasses (Mogen) looking confident. A large hand-drawn arrow connects the two panels with 'ATTRIBUTION' written on it. The title 'WHAT YOU GET' is at the top in a bold, black, hand-printed font, with the subtitle 'From Chaos to Clarity' below it. At the bottom is the quote 'From invisible to verified. From chaos to control.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop.",
  "negative_prompt": "garbled text, illegible glyphs, blurred characters, pseudo-text, corrupted letters, gibberish words, broken typography, visible hex codes, color codes as text, file paths visible, markdown syntax visible, citation brackets, '[cite:' text, '.md' text, internal references as text, yaml syntax, json syntax, technical markup visible, prompt instructions as labels, style keywords visible, rendering keywords as labels, aesthetic descriptors as text, parentheses with style words"
}
```

### ⚠️ Internal Reference Warning

The style guide, color codes, and file references in this document are for **workflow use only**. They must NEVER appear as visible text in the generated image. The negative prompt above helps prevent this.

---

## Why Should I Care?

> "This is the payoff. This is why the system matters to YOU."

## Explain It to a Label Exec

> "Before the system: lost money, wrong credits, no say in AI training. After the system: verified credits, tracked usage, artist in control. Simple as that."

---

## Alt Text

Risograph-style zine page showing before/after comparison. Left panel "BEFORE" (pink) lists problems with X marks: lost royalties, wrong credits, no AI control, invisible. Right panel "AFTER" (teal) lists benefits with checkmarks: verified credits, tracked usage, you decide on AI, findable. Mogen appears confident in the AFTER panel. A large arrow labeled "ATTRIBUTION" connects them. Title reads "WHAT YOU GET."

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
