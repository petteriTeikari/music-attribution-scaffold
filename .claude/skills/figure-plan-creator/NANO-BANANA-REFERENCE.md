# Nano Banana Pro Figure Creation Reference

**Contextualized for:** Music Attribution Scaffold
**Source:** `sci-llm-writer/docs/nano-banana-image-creation-tutorial.md` v2.1
**Purpose:** Quick reference for creating figures with Nano Banana Pro (Gemini image generation)

---

## What is Nano Banana Pro?

Nano Banana Pro is Gemini's image generation capability. It creates scientific diagrams from detailed text prompts.

**Strengths:** Rapid iteration, consistent style, complex multi-panel layouts, abstract conceptual diagrams
**Weaknesses:** Text rendering (garbled/misspelled), small text illegible, mathematical notation unreliable

---

## The Two-AI Workflow

```
CLAUDE CODE          NANO BANANA PRO         HUMAN
(The Planner)   -->  (The Artist)       -->  (Quality Control)

- Read codebase      - Generate image         - Add text labels
- Write fig-*.md     - Apply style            - Fix artifacts
- Structure content  - Create visual          - Export 300 DPI
```

---

## Content-Style Decoupling (Core Architecture)

```
STYLE-GUIDE-REPO.md (ONE file)     =  Visual specifications (colors, typography, rendering)
fig-*.md (per-figure file)         =  Pure content (what to show, not how)
Combine at generation time         =  Nano Banana Pro prompt
```

**Why separate?** Changing the aesthetic means editing ONE file, not all 116 figure plans.

### What Goes Where

| Content | Location |
|---------|----------|
| Hex codes, color mappings | STYLE-GUIDE-REPO.md ONLY |
| Font specifications | STYLE-GUIDE-REPO.md ONLY |
| Rendering keywords | STYLE-GUIDE-REPO.md ONLY |
| Negative prompts | STYLE-GUIDE-REPO.md ONLY |
| Element descriptions | fig-*.md |
| Spatial anchors | fig-*.md |
| Labels and callouts | fig-*.md |
| Anti-hallucination rules | fig-*.md |

---

## Quick Start Workflow (5 Steps)

### Step 1: Create Figure Plan (Claude Code)

Create `docs/figures/repo-figures/figure-plans/fig-{category}-{NN}-{name}.md` following the CONTENT-TEMPLATE-REPO.md format.

### Step 2: Run Reviewer Agent (Claude Code)

Use the `/figure-plan-creator` skill's reviewer agent to audit the plan for hallucination triggers.

### Step 3: Generate in Gemini (Human)

1. Open new Gemini chat at gemini.google.com
2. Upload `STYLE-GUIDE-REPO.md` (drag and drop)
3. Upload the figure plan `fig-*.md`
4. Paste the Master Prompt from PROMPTING-INSTRUCTIONS-REPO.md
5. Generate (~30 seconds)

### Step 4: Quality Check (Human)

Run the quality checklist:
- Quick reject gates (hex codes? font names? figure caption? garbled text?)
- Full 25-item checklist (21/25 minimum)

### Step 5: Post-Process (Human)

1. Download generated image
2. Open in Figma/Illustrator/PowerPoint
3. Add text labels from the figure plan
4. Export at 300 DPI as PNG
5. Save to `docs/figures/repo-figures/generated/`
6. Convert to web JPEG in `docs/figures/repo-figures/assets/`

---

## The Three Deadly Artifacts

| Artifact | Example | Prevention |
|----------|---------|------------|
| **Hex codes as text** | "#E84C4F" visible in image | Use "coral red" not "#E84C4F" in prompts |
| **Font names as text** | "Instrument Serif" visible | Use "serif display type" not font names |
| **Figure captions** | "Figure 1. ETL Pipeline" visible | Never include "Figure X." in prompts |

**Bonus:** Prompt leakage -- "(matte finish, asymmetric)" appearing as text. Keep style words at START of prompt, far from content.

---

## Prompt Structure for This Repo

```
STYLE:
Warm cream background. Warp Records editorial aesthetic meets
constructivist data visualization. Coral red as primary graphic
accent. Deep navy for structural elements. Teal for technology.
Matte finish, halftone grain. Asymmetric composition, 30%+
negative space. Sharp geometric edges. Bold serif display headings
in ALL-CAPS. Clean sans-serif labels. Monospace for numbers.

TEXT RENDERING RULES:
[Use Placeholder Protocol for text-heavy figures]

CONTENT:
[Pure content -- no hex codes, no font names, no semantic tags,
 no "Figure X." captions, no style words near labels]

DIMENSIONS: [width]x[height], [aspect ratio]

NEGATIVE:
[Full combined negative prompt from STYLE-GUIDE-REPO.md v2.0]
```

---

## Figure Type Decision Matrix

| Figure Type | Best Tool | Why |
|-------------|-----------|-----|
| Pipeline architecture | **Nano Banana Pro** | Abstract visual metaphors |
| Module relationships | **Nano Banana Pro** | Constructivist composition |
| Before/after comparison | **Nano Banana Pro** | Split-panel editorial |
| PRD decision trees | **Nano Banana Pro** | Branching path visualization |
| Flowcharts with many labels | **Mermaid/Graphviz** | Perfect text rendering |
| Data plots | **R + ggplot2** | Publication-quality axes |
| Precise timelines | **R + ggplot2** | Exact date positioning |
| Tables | **Markdown/LaTeX** | Structured data |

### The Compositing Trick

For figures needing BOTH artistic rendering AND precise text:

1. Generate background art with Nano Banana Pro (request placeholder blocks)
2. Add text labels and data overlays in Figma/Illustrator
3. Export final composite at 300 DPI

---

## Iteration Quick Fixes

| Problem | Fix Prompt |
|---------|------------|
| Wrong background | "Background must be EXACTLY warm cream, not white" |
| Hex codes visible | Re-prompt from scratch, remove ALL hex codes |
| Font names visible | Re-prompt, use "serif display" not font names |
| Figure caption visible | Re-prompt, add "Figure 1" to negative prompt |
| Text garbled | "Remove all text, use placeholder boxes" |
| Too sparse | "Add more visual elements, need 15+ elements" |
| Sci-fi aesthetic | "Matte finish, no glow, no neon. Like a Warp Records insert." |
| Symmetric layout | "Deliberately asymmetric, main element offset left" |
| Style words as text | Re-prompt, move ALL style words to start of prompt |

**Maximum 3 attempts** per figure. If 3 fail on same check, simplify the content.

---

## Domain-Specific Terminology

### Music Attribution Domain (for repo figures)

| Concept | Plain-Language (L1) | Technical (L3+) |
|---------|---------------------|------------------|
| ETL Pipeline | "Data collection from 5 sources" | "ETL extractors with TokenBucketRateLimiter" |
| Entity Resolution | "Matching duplicate records" | "Splink probabilistic linkage with pgvector" |
| Confidence Score | "How sure we are (0-100%)" | "Calibrated probability via conformal prediction" |
| Assurance Level | "A0=unknown, A3=artist-verified" | "Four-tier provenance per ISRC/ISWC/ISNI" |
| NormalizedRecord | "Unified data format" | "Boundary object BO-1 (Pydantic schema)" |
| Oracle Problem | "Can't trace AI training data" | "Post-hoc attribution architecturally impossible" |

### Five Data Sources (exact names)

1. **MusicBrainz** -- open database (1 req/s)
2. **Discogs** -- catalog/vinyl data (60 req/min)
3. **AcoustID** -- audio fingerprint (3 req/s)
4. **tinytag** -- local file metadata (no rate limit)
5. **Artist Input** -- direct artist verification (no rate limit)

**NEVER add:** Spotify, Apple Music, YouTube, SoundCloud, Bandcamp

---

## This Repo's Visual Identity

| Aspect | Specification |
|--------|--------------|
| Background | Warm cream (#f6f3e6) -- matches frontend surface |
| Primary accent | Coral red (#E84C4F) -- accent squares, lines |
| Secondary accent | Deep navy (#1E3A5F) -- structure, boundaries |
| Technology accent | Teal (#2E7D7B) -- feedback, innovation |
| Artist accent | Gold (#D4A03C) -- human elements |
| Typography feel | Warp Records editorial, Bauhaus geometric |
| Layout | Asymmetric, 30%+ negative space, no shadows |
| Finish | Matte, halftone grain texture |

**BANNED:** Corporate SaaS gradients, sci-fi neon, symmetric layouts, rounded pills, glossy effects, dark backgrounds, PowerPoint/Lucidchart defaults

---

## File Locations

| What | Where |
|------|-------|
| Style guide | `docs/figures/repo-figures/STYLE-GUIDE-REPO.md` |
| Content template | `docs/figures/repo-figures/CONTENT-TEMPLATE-REPO.md` |
| Prompting instructions | `docs/figures/repo-figures/PROMPTING-INSTRUCTIONS-REPO.md` |
| Figure plans | `docs/figures/repo-figures/figure-plans/fig-*.md` |
| Raw PNGs (gitignored) | `docs/figures/repo-figures/generated/` |
| Web JPEGs (tracked) | `docs/figures/repo-figures/assets/` |
| This reference | `.claude/skills/figure-plan-creator/NANO-BANANA-REFERENCE.md` |

---

*Adapted from sci-llm-writer/docs/nano-banana-image-creation-tutorial.md v2.1 for Music Attribution Scaffold*
