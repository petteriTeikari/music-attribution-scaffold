# STYLE GUIDE v2.0 - The system Documentation Infographics

## Unified Risograph/Zine Aesthetic

**Version:** 2.0
**Scope:** All repository documentation figures
**Target:** DIY indie zine aesthetic with professional clarity
**Generator:** Gemini (Nano Banana Pro)

---

## DESIGN PHILOSOPHY

### Why Risograph/Zine?

This aesthetic was chosen because it:
- Resonates with **independent music industry** professionals (our audience)
- Feels **grassroots and artist-empowering**, not corporate
- Has **intentional imperfection** that feels human and approachable
- Uses **limited spot colors** that create visual cohesion across all figures
- Evokes **DIY culture** central to Imogen Heap's ethos and indie artists

### Core Principles

1. **Unified style** - All figures share the same visual language
2. **Content/style decoupling** - This guide defines style; content specs define what to show
3. **Clarity over cleverness** - Information must be readable despite the artistic aesthetic
4. **Authentic imperfection** - Misregistration and texture are features, not bugs

---

## MANDATORY SPECIFICATIONS

### Background Color (NON-NEGOTIABLE)

| Element | Hex | RGB | Description |
|---------|-----|-----|-------------|
| **Primary Background** | `#fcfbf4` | 252, 251, 244 | Very light off-white, NOT yellow |

**Critical:** This is a clean, bright off-white—lighter and less warm than typical cream/parchment. It makes the spot colors pop without feeling yellowed or aged.

### Spot Color Palette (3 colors only)

| Color | Hex | Usage |
|-------|-----|-------|
| **Fluorescent Pink/Magenta** | `#E91E8C` | Primary accent, highlights, emphasis |
| **Teal** | `#00B4B4` | Secondary accent, progress indicators, success states |
| **Black** | `#1A1A1A` | Text, outlines, primary structural elements |

**Rules:**
- Maximum 3 spot colors per figure (plus background)
- Visible **misregistration** between color layers (slight offset, 2-4px)
- Colors should feel like screen-printed ink, not digital fills

### Typography

| Element | Style | Notes |
|---------|-------|-------|
| **Titles** | Bold condensed sans-serif, hand-printed feel | ALL CAPS with letter spacing |
| **Subtitles** | Regular weight, sentence case | Below title |
| **Labels** | Mix of bold sans and hand-drawn | Inside or near elements |
| **Body text** | Typewriter or clean sans-serif | For explanatory text boxes |
| **Quotes** | Italic or script, handwritten feel | Empowering statements |

**Critical:** All text must be **crisp and legible** despite the zine aesthetic.

### Visual Elements

| Element | Treatment |
|---------|-----------|
| **Badges/Stamps** | Circular with hand-drawn borders, filled or outlined |
| **Arrows** | Hand-drawn, organic curves, NOT straight lines |
| **Progress indicators** | Simple rectangular blocks filling up |
| **Containers/Boxes** | Hand-drawn borders with slight wobble |
| **Icons** | Simple, bold shapes (not detailed illustrations) |

### Texture

- Visible **paper grain** (subtle, not overwhelming)
- **Screen-print texture** on colored areas
- **Ink spread** at edges of shapes
- **Misregistration** between color layers

---

## GEMINI PROMPT TEMPLATE

### Optimized Base Prompt Structure

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. [CONTENT DESCRIPTION]. The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop."
}
```

### Prompt Components

**Opening (always include):**
```
A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish.
```

**Content section (customize per figure):**
```
The image features [MAIN VISUAL ELEMENTS]. The title '[TITLE]' is at the top in a bold, black, hand-printed font, with the subtitle '[SUBTITLE]' below it.
```

**Closing (always include):**
```
The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop.
```

### Example Complete Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image features four circular badges in a horizontal progression, connected by hand-drawn arrows. Each badge contains a label (A0, A1, A2, A3) and a progress bar showing increasing fill levels. Below the badges are brief explanatory labels. An example box in the lower portion shows a specific use case. The title 'FROM UNKNOWN TO VERIFIED' is at the top in a bold, black, hand-printed font, with the subtitle 'The Trust Progression' below it. The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop."
}
```

---

## CONTENT SPECIFICATION TEMPLATE

Each figure's content spec should include:

### Required Sections

```markdown
## Figure: [ID]

### Title
[Main title in ALL CAPS]

### Subtitle
[Explanatory subtitle]

### Main Visual Elements
[Describe the primary graphic elements: badges, flowcharts, diagrams, etc.]

### Labels & Text
- [List all text that should appear in the figure]
- [Include any quotes or callouts]

### Layout Description
[How elements are arranged: horizontal progression, vertical stack, radial, etc.]

### Key Semantic Roles
| Element | Role | Color Treatment |
|---------|------|-----------------|
| [Element] | [What it represents] | [Pink/Teal/Black] |
```

### Do NOT Include in Content Specs

- Style descriptions (handled by this guide)
- Color hex codes (use semantic names: "pink accent", "teal fill")
- Typography specifications (handled by this guide)
- Texture instructions (handled by this guide)

---

## LAYOUT PATTERNS

### Pattern A: Horizontal Progression
Best for: State transitions, workflows, timelines

```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE                                                          │
│  Subtitle                                                       │
│                                                                 │
│   ○──────→ ○──────→ ○──────→ ○                                │
│  Step 1    Step 2    Step 3    Step 4                          │
│                                                                 │
│  [Example box or explanatory text]                              │
│                                                                 │
│  "Empowering quote or key message"                              │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern B: Central Hub
Best for: Data aggregation, entity relationships

```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE                                                          │
│  Subtitle                                                       │
│                                                                 │
│       ○                                                         │
│        ╲                                                        │
│   ○ ───→ ◉ ←─── ○                                              │
│        ╱                                                        │
│       ○                                                         │
│                                                                 │
│  [Labels around central element]                                │
│                                                                 │
│  "Key message"                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern C: Tiered Stack
Best for: Access levels, hierarchies

```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE                                                          │
│  Subtitle                                                       │
│                                                                 │
│  ┌─────────────────────────────────────────┐                   │
│  │  TIER 1 (most access)                   │                   │
│  ├─────────────────────────────────────────┤                   │
│  │  TIER 2 (medium access)                 │                   │
│  ├─────────────────────────────────────────┤                   │
│  │  TIER 3 (limited access)                │                   │
│  └─────────────────────────────────────────┘                   │
│                                                                 │
│  "Key message"                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern D: Before/After
Best for: Problem/solution, transformation

```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE                                                          │
│  Subtitle                                                       │
│                                                                 │
│  ┌──────────────┐          ┌──────────────┐                    │
│  │   BEFORE     │   ───→   │    AFTER     │                    │
│  │   (problem)  │          │  (solution)  │                    │
│  └──────────────┘          └──────────────┘                    │
│                                                                 │
│  [Explanatory text or details]                                  │
│                                                                 │
│  "Key message"                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern E: User Journey
Best for: Day-in-the-life, process flows with personas

```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE                                                          │
│  Subtitle                                                       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  STEP 1: [Action]                                        │   │
│  │  [Visual + description]                                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                        ↓                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  STEP 2: [Action]                                        │   │
│  │  [Visual + description]                                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                        ↓                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  STEP 3: [Action]                                        │   │
│  │  [Visual + description]                                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  "Key message"                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## COLOR SEMANTICS

When writing content specs, use these semantic color assignments:

| Semantic Role | Color | Usage |
|---------------|-------|-------|
| **Emphasis/Highlight** | Pink | Key terms, important states, call-to-action |
| **Success/Progress** | Teal | Verified status, filled progress, positive outcomes |
| **Structure/Text** | Black | Titles, labels, borders, arrows |
| **Warning/Problem** | Pink (faded/outlined) | Issues, unverified states |
| **Neutral/Background** | Off-white | Paper background, empty states |

---

## NEGATIVE PROMPT (Include with all generations)

```
corporate design, clean modern aesthetic, gradient fills,
photorealistic, 3D rendering, perfect alignment, sharp edges,
sci-fi aesthetic, glowing effects, neon, cyberpunk,
polished professional finish, stock imagery, generic icons,
tech startup visual language, flowchart software style,
pure white background, glossy finish, drop shadows,
single solid color fills without texture,
yellow or cream background (use #fcfbf4 off-white),
digital/vector perfection, smooth gradients
```

---

## QUALITY CHECKLIST

### Before Prompting

- [ ] Background specified as `#fcfbf4` (very light off-white)
- [ ] Only 3 spot colors used (pink, teal, black)
- [ ] Content description is clear and specific
- [ ] Layout pattern identified
- [ ] All text content listed
- [ ] Negative prompt included

### After Generation

- [ ] Background IS very light off-white (not yellow/cream)
- [ ] Visible misregistration between color layers
- [ ] Hand-drawn/organic feel to elements
- [ ] All text is crisp and legible
- [ ] Feels like indie zine, NOT corporate infographic
- [ ] Information hierarchy is clear despite artistic style

---

## MOGEN & ANDY PERSONALIZATION

For figures requiring persona personalization:

### Mogen (Imogen Heap) - CHARACTER DESCRIPTION

**Use this description for any female character or non-Andy character in figures:**

```
A woman with light blonde/platinum hair pulled back in a casual ponytail,
wearing rectangular dark-framed glasses, dressed in black clothing.
She has a creative, thoughtful expression. Style her in the risograph
aesthetic with pink and teal accents.
```

**Additional context:**
- Reference her songs: "Hide and Seek", "Tiny Human"
- Artist ID: AURA01JE38RP4ES
- Associated imagery: Mi.Mu gloves (gesture-control wearable tech), waveforms, electronic music
- Often shown at laptop, in studio, or gesturing with hands (referencing Mi.Mu gloves)

**Prompt snippet for figures with Mogen:**
```
Include a stylized female figure representing "Mogen" - a woman with light
blonde hair in a ponytail, rectangular dark-framed glasses, wearing black
clothing, rendered in the risograph ink style.
```

### Andy (Andy Carne) - CHARACTER DESCRIPTION

**Use this description when Andy appears:**

```
A man with a bald/shaved head, salt-and-pepper beard stubble, wearing
distinctive round black-framed glasses, dressed in dark/black clothing.
He has a creative, artistic presence. Style him in the risograph
aesthetic with pink and teal accents.
```

**Prompt snippet for figures with Andy:**
```
Include a stylized male figure representing "Andy" - a bald man with
a gray beard stubble, round black-framed glasses, wearing dark clothing,
rendered in the risograph ink style.
```

**Additional context:**
- Reference his role: Art Director, Special Projects Lead, 25+ years in music visuals
- Artist ID: AURA01JE38RRG1T

### When to Include Characters

| Figure Type | Character Inclusion |
|-------------|---------------------|
| User journey figures | Include Mogen and/or Andy as protagonists |
| Dashboard/interface examples | Show Mogen interacting with the system |
| Persona galleries | Both Mogen and Andy with supporting personas |
| Abstract concept figures | No characters needed (badges, diagrams, flows) |
| Problem statement figures | Can show Mogen as affected artist |

---

## FILE NAMING CONVENTION

```
fig-[location]-[number]-[short-description].png
```

Examples:
- `fig-rm-01-where-credits-go-to-die.png` (README figure 1)
- `fig-arch-02-entity-resolution.png` (Architecture figure 2)
- `fig-mcp-01-three-tier-access.png` (MCP PRD figure 1)

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-04 | Initial multi-style approach |
| 2.0 | 2026-02-04 | Unified risograph/zine aesthetic, style/content decoupling |

---

*This style guide ensures visual consistency while allowing content flexibility. All figures should feel like they came from the same indie zine about music attribution.*
