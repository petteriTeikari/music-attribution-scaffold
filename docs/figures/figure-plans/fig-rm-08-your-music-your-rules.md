# fig-rm-08: Your Music, Your Rules

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-08 |
| **Title** | Your Music, Your Rules |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |
| **Gap Filled** | How do artists control permissions? |

---

## Content Specification

### Title
YOUR MUSIC, YOUR RULES

### Subtitle
Control Who Accesses Your Data

### Main Visual Elements
- Mogen at center as the controller
- Three toggle switches/permission controls stacked vertically
- Each toggle shows a different access type with ON/OFF state
- Visual emphasis on artist being in control

### Layout Pattern
Pattern C: Tiered Stack (control panel style)

```
                    MOGEN
                   ┌─────┐
                   │ 👤  │
                   │ YOU │
                   └──┬──┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │ VERIFIED│   │ UNKNOWN │   │ RIGHTS  │
   │ AI      │   │ CRAWLERS│   │ ORGS    │
   │         │   │         │   │         │
   │ [ON] ✓  │   │ [OFF] ✗ │   │ [ON] ✓  │
   │         │   │         │   │         │
   │JenMusic │   │ Blocked │   │ ASCAP   │
   └─────────┘   └─────────┘   └─────────┘
```

### Labels & Text

**Title & Subtitle:**
- "YOUR MUSIC, YOUR RULES"
- "Control Who Accesses Your Data"

**Center (Mogen):**
- "YOU DECIDE"
- Mogen icon/figure

**Toggle 1 - Verified AI Partners:**
- "VERIFIED AI PARTNERS"
- "[ON] ✓"
- "JenMusic, ethical AI"
- Teal (approved)

**Toggle 2 - Unknown Crawlers:**
- "UNKNOWN CRAWLERS"
- "[OFF] ✗"
- "Blocked by default"
- Pink (denied)

**Toggle 3 - Rights Organizations:**
- "RIGHTS ORGANIZATIONS"
- "[ON] ✓"
- "ASCAP, BMI, etc."
- Teal (approved)

**Bottom quote:**
- "Turn access on or off. It's your call."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| Mogen | Controller | Pink accents |
| ON toggles | Approved access | Teal fill |
| OFF toggles | Denied access | Pink outline |
| Toggle labels | Access types | Black text |
| Arrows from Mogen | Control flow | Black, hand-drawn |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image shows a stylized female figure with blonde ponytail and rectangular glasses (Mogen) at the top center, labeled 'YOU DECIDE'. Below her, three hand-drawn arrows point down to three toggle switch panels arranged horizontally. LEFT TOGGLE: 'VERIFIED AI PARTNERS' with switch ON (checkmark, teal), showing 'JenMusic' as example. MIDDLE TOGGLE: 'UNKNOWN CRAWLERS' with switch OFF (X mark, pink), showing 'Blocked by default'. RIGHT TOGGLE: 'RIGHTS ORGANIZATIONS' with switch ON (checkmark, teal), showing 'ASCAP, BMI'. Each toggle looks like a hand-drawn control panel or switch. The title 'YOUR MUSIC, YOUR RULES' is at the top in a bold, black, hand-printed font, with the subtitle 'Control Who Accesses Your Data' below it. At the bottom is the quote 'Turn access on or off. It's your call.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop.",
  "negative_prompt": "garbled text, illegible glyphs, blurred characters, pseudo-text, corrupted letters, gibberish words, broken typography, visible hex codes, color codes as text, file paths visible, markdown syntax visible, citation brackets, '[cite:' text, '.md' text, internal references as text, yaml syntax, json syntax, technical markup visible, prompt instructions as labels, style keywords visible, rendering keywords as labels, aesthetic descriptors as text, parentheses with style words"
}
```

### ⚠️ Internal Reference Warning

The style guide, color codes, and file references in this document are for **workflow use only**. They must NEVER appear as visible text in the generated image. The negative prompt above helps prevent this.

---

## Why Should I Care?

> "You're not giving up control—you're setting the rules."

## Explain It to a Label Exec

> "Artists get a simple control panel. Verified partners can be approved, unknown crawlers blocked by default, rights orgs can be granted access. The artist flips the switches."

---

## Alt Text

Risograph-style zine page showing Mogen at top center with "YOU DECIDE" label. Below her, three toggle switch panels: "Verified AI Partners" (ON, teal checkmark, JenMusic example), "Unknown Crawlers" (OFF, pink X, blocked), and "Rights Organizations" (ON, teal checkmark, ASCAP/BMI). Title reads "YOUR MUSIC, YOUR RULES."

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
