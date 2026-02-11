# Nano Banana Pro — Frontend Figure Prompting Instructions

**Version:** 1.0.0
**Adapted from:** `docs/figures/CONTENT-TEMPLATE.md` (foundation-PLR)

---

## Workflow

1. **Read the figure plan** (e.g., `figure-plans/fig-hero-01-waveform-tapestry.md`)
2. **Read the style guide** (`STYLE-GUIDE-FRONTEND.md`)
3. **Compose two-part prompt:**
   - **Style prompt** → references STYLE-GUIDE-FRONTEND.md palette + aesthetic
   - **Content prompt** → references figure plan spatial anchors + elements
4. **Generate in Nano Banana Pro**
5. **Export at target dimensions** (specified in figure plan)
6. **Save to:** `docs/figures/assets/` (source) and `docs/figures/generated/` (final)

---

## Master Prompt Template

```
STYLE: [Paste relevant section from STYLE-GUIDE-FRONTEND.md]
Background: warm cream #F8F6F0
Primary accent: coral red #E84C4F
Secondary: deep navy #1E3A5F
Texture: subtle grain overlay, matte finish
Composition: asymmetric, editorial, generous whitespace
Typography: Instrument Serif display, Plus Jakarta Sans labels (ALL-CAPS)

CONTENT: [Paste from figure plan]
[Spatial anchors]
[Element descriptions with semantic tags]

NEGATIVE: no stock photography, no corporate gradient, no neon glow,
no symmetric layout, no rounded pills, no glossy finish, no 3D render
```

---

## Quality Checklist

Before accepting a generated image:

- [ ] Background is warm cream (#F8F6F0), not white or gray
- [ ] Coral red accent is present and prominent
- [ ] Composition is asymmetric
- [ ] No sci-fi/neon/corporate aesthetic
- [ ] Typography is editorial (serif display + sans labels)
- [ ] Grain/halftone texture visible at 100% zoom
- [ ] At least 30% negative space
- [ ] Would look at home in a Warp Records catalog
