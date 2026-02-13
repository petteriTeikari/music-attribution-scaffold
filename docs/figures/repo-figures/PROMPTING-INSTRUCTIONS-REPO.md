# Nano Banana Pro -- Repository Figure Prompting Instructions

**Version:** 1.0.0
**Scope:** Repository documentation figures (architecture, pipelines, decisions, comparisons)
**Adapted from:** `docs/figures/frontend-figures/PROMPTING-INSTRUCTIONS.md`
**Generator:** Gemini (Nano Banana Pro)

---

## Workflow

Every repo documentation figure follows this five-step workflow. Do not skip steps.

### Step 1: Read the Figure Plan

Open the figure plan from `docs/figures/repo-figures/figure-plans/fig-repo-{NN}-{name}.md`.

Confirm:
- [ ] Metadata is complete (ID, audience level, layout template, aspect ratio)
- [ ] Key message is a single sentence
- [ ] Spatial anchors are defined in YAML
- [ ] Anti-hallucination rules are listed
- [ ] JSON export block is present

### Step 2: Read the Style Guide

Open `docs/figures/repo-figures/STYLE-GUIDE-REPO.md`.

Confirm the figure plan's semantic tags map to valid palette entries:
- Pipeline stages: `etl_extract`, `entity_resolve`, `source_corroborate`, `final_score`
- Confidence tiers: `confidence_high`, `confidence_medium`, `confidence_low`
- Assurance levels: `assurance_a0` through `assurance_a3`
- Data sources: `source_musicbrainz`, `source_discogs`, `source_acoustid`, `source_file`, `source_artist`

### Step 3: Compose the Two-Part Prompt

Build the prompt from two sections: Style + Content.

### Step 4: Generate in Nano Banana Pro

- Upload the composed prompt to Gemini
- Generate the image
- If the figure plan includes visual reference images, upload those alongside the prompt

### Step 5: Verify and Save

- Run the quality checklist (17/20 threshold)
- Save raw PNG to `docs/figures/repo-figures/generated/`
- Run conversion script for web-optimized JPEG to `docs/figures/repo-figures/assets/`
- Embed JPEG in documentation

---

## Master Prompt Template

Use this template for every repo figure. Replace bracketed sections with content from the figure plan.

```
STYLE:
Warm cream background (#f6f3e6). Warp Records editorial aesthetic meets
constructivist data visualization. Coral red (#E84C4F) as primary graphic
accent -- accent squares, thin accent lines, stage markers. Deep navy
(#1E3A5F) for structural elements and module boundaries. Teal (#2E7D7B)
for technology/innovation and feedback loops. Matte finish, halftone
grain texture. Asymmetric composition with generous negative space (30%+).
Sharp geometric edges, no rounded corners, no drop shadows. Instrument
Serif-style display headings in ALL-CAPS with letter tracking. Sans-serif
labels. Monospace for numbers and data.

[IF APPLICABLE -- add layout-specific style notes:]
[For Template A (Hero): Bold display type as primary visual element]
[For Template B (Multi-Panel): Thin coral dividers between panels]
[For Template C (Flowchart): Solid lines for selected paths, dashed for alternatives]
[For Template D (Split-Panel): Muted palette on left, full palette on right]
[For Template E (Steps): Vertical signal chain, coral squares as stage markers]

CONTENT:
[Paste the visual concept description from the figure plan]
[Paste the spatial anchors summary -- translate YAML to natural language]
[Describe each primary structure with its visual role, NOT its semantic tag]
[Describe relationships/flows as visual connections]
[Include callout text if present]

DIMENSIONS: [width]x[height] pixels, [aspect ratio]

NEGATIVE:
--no stock photography, generic AI art, corporate gradient, neon glow,
sci-fi futuristic, dark background, symmetric layout, rounded pill shapes,
glossy finish, 3D render, photorealistic, detailed faces, text-heavy,
PowerPoint style, flowchart software, Lucidchart, Miro, drop shadows,
thick block arrows, centered composition, dense dashboard, clip art,
holographic, plasma effects, oversaturated colors, pure white background,
visible hex codes, semantic tag names, prompt keywords visible,
garbled text, illegible glyphs, pseudo-text, font names as labels
```

---

## Prompt Translation Rules

The following terms appear in figure plans but must be translated before prompting. Nano Banana Pro should never see raw semantic tags.

### Pipeline Stages

| In Figure Plan | In Prompt |
|----------------|-----------|
| `etl_extract` | "data ingestion zone with chaotic lines becoming orderly" |
| `entity_resolve` | "matching zone with overlapping clusters merging into single nodes" |
| `source_corroborate` | "voting zone with multiple colored lines converging and being weighed" |
| `final_score` | "output zone with confidence gauge/spectrum and calibrated result" |

### Confidence Tiers

| In Figure Plan | In Prompt |
|----------------|-----------|
| `confidence_high` | "green-tinted element indicating high trust" |
| `confidence_medium` | "amber-tinted element indicating partial trust" |
| `confidence_low` | "red-tinted element indicating low trust or flagged" |

### Assurance Levels

| In Figure Plan | In Prompt |
|----------------|-----------|
| `assurance_a0` | "gray marker labeled A0 (no data)" |
| `assurance_a1` | "amber marker labeled A1 (single source)" |
| `assurance_a2` | "blue marker labeled A2 (multiple sources)" |
| `assurance_a3` | "green marker labeled A3 (artist-verified)" |

### Data Sources

| In Figure Plan | In Prompt |
|----------------|-----------|
| `source_musicbrainz` | "purple-tinted source node" |
| `source_discogs` | "dark gray source node" |
| `source_acoustid` | "teal-tinted source node" |
| `source_file` | "warm gray source node" |
| `source_artist` | "gold source node, slightly larger/emphasized (highest authority)" |

### Scaffold Concepts

| In Figure Plan | In Prompt |
|----------------|-----------|
| `selected_option` | "solid line path" |
| `deferred_option` | "dashed line path (alternative, not chosen)" |
| `branching_path` | "fork in the flow where two paths diverge" |
| `archetype_overlay` | "tinted overlay zone showing team-specific configuration" |

---

## Prompt Examples by Layout Template

### Template A (Hero Overview) -- Example Prompt

```
STYLE:
[Standard style block from master template]
Bold display type as primary visual element. Large title takes 30% of canvas.

CONTENT:
A landscape hero image (1920x1080) showing the Music Attribution Scaffold
as an abstract signal chain. The title "ATTRIBUTION BY DESIGN" appears in
large serif display type across the top third, ALL-CAPS with generous
letter spacing. A coral accent square sits to the left of the subtitle
"TRANSPARENT CONFIDENCE SCORING FOR MUSIC CREDITS". Below the title zone,
an abstract constructivist composition shows five colored signal dots
(purple, dark gray, teal, warm gray, gold) with thin lines flowing through
four processing bands (navy at varying opacity), emerging as a single
unified output with a small green confidence gauge motif. A thin teal
feedback arc curves along the right edge. The bottom-right corner has
an editorial caps label reading "SCAFFOLD v2.0" with a thin coral accent
line beneath it. Generous negative space throughout.

DIMENSIONS: 1920x1080, 16:9
NEGATIVE: [Standard negative block]
```

### Template B (Multi-Panel) -- Example Prompt

```
STYLE:
[Standard style block from master template]
Thin coral dividers between panels. Roman numerals I-V as panel markers.

CONTENT:
A landscape multi-panel diagram (1920x1080) showing five pipeline stages
side by side. The title "FIVE-STAGE ATTRIBUTION PIPELINE" appears at the
top left in serif display type with a coral accent square. Five vertical
panels separated by thin coral accent lines. Panel I (ETL) shows abstract
chaotic lines entering and orderly lines exiting. Panel II (Resolution)
shows overlapping circles merging. Panel III (Corroboration) shows multiple
colored lines being weighed on a balance motif. Panel IV (Scoring) shows
a confidence spectrum from red through amber to green. Panel V (Output)
shows a single clean unified record. Thin navy arrows connect panels
left to right. Roman numerals I through V appear as faint labels above
each panel. Bottom callout reads "CONFIDENCE = AGREEMENT x AUTHORITY"
in monospace. Background is warm cream throughout.

DIMENSIONS: 1920x1080, 16:9
NEGATIVE: [Standard negative block]
```

### Template D (Split-Panel) -- Example Prompt

```
STYLE:
[Standard style block from master template]
Left panel uses muted, desaturated colors. Right panel uses full palette.

CONTENT:
A landscape split-panel comparison (1920x1080). Title "FROM CHAOS TO
CONFIDENCE" spans the top. Left panel titled "BEFORE" (in editorial caps)
shows a grey, fragmented mess of disconnected data nodes -- scattered
boxes with question marks, broken links, faded red warning indicators.
Right panel titled "AFTER" shows the same data flowing through clean
pipeline stages in full color -- purple, gray, teal, warm gray, and gold
source nodes converge through navy processing stages into a unified output
with a green confidence gauge reading 0.92. A coral accent line divides
the two panels vertically. Bottom callout spanning full width reads
"40% OF MUSIC METADATA IS WRONG -- ATTRIBUTION BY DESIGN FIXES THIS"
in editorial caps with a thin coral underline.

DIMENSIONS: 1920x1080, 16:9
NEGATIVE: [Standard negative block]
```

---

## Quality Checklist (Pre-Accept)

Run this checklist after every generation. The figure must score 17/20 or higher (see STYLE-GUIDE-REPO.md for the full 20-item checklist).

### Quick Pass/Fail (reject immediately if any fail)

- [ ] Background IS warm cream (#f6f3e6), not white, gray, or yellow
- [ ] NO neon, glow, or sci-fi aesthetic anywhere
- [ ] NO garbled, illegible, or pseudo-text
- [ ] NO semantic tags, hex codes, or font names rendered as visible text

### Full Checklist (score 1/0 each, accept if >= 17/20)

**Palette (5):**
1. Cream background
2. Coral red accent present
3. Deep navy structural elements
4. No unauthorized colors
5. Correct confidence tier colors (if applicable)

**Typography (4):**
6. Serif display headings
7. ALL-CAPS sans labels with tracking
8. No garbled text
9. Readable at 50% zoom

**Composition (5):**
10. Asymmetric layout
11. 30%+ negative space
12. No drop shadows or gloss
13. Matte finish
14. Clear information hierarchy

**Domain (4):**
15. Technical accuracy (correct pipeline order, correct thresholds)
16. No internal terms as visible text
17. Warp Records aesthetic achieved
18. Target audience would understand

**Production (2):**
19. Correct aspect ratio
20. Sufficient resolution (>= 1200px wide)

---

## Output Paths

| Type | Path | Git Status |
|------|------|------------|
| Raw PNG (Nano Banana Pro output) | `docs/figures/repo-figures/generated/fig-repo-{NN}-{name}.png` | Gitignored |
| Web-optimized JPEG | `docs/figures/repo-figures/assets/fig-repo-{NN}-{name}.jpg` | Tracked |
| Figure plan | `docs/figures/repo-figures/figure-plans/fig-repo-{NN}-{name}.md` | Tracked |

### Conversion

Use the existing conversion script:

```bash
uv run python docs/figures/scripts/resize_and_convert.py \
  --input docs/figures/repo-figures/generated/ \
  --output docs/figures/repo-figures/assets/ \
  --width 1600
```

If the script does not support custom input/output directories, copy PNGs to `docs/figures/generated/`, run the script, then move the resulting JPEGs to `docs/figures/repo-figures/assets/`.

---

## Anti-Hallucination Protocol

Nano Banana Pro will sometimes render internal instructions as visible text in the image. This protocol prevents that.

### Before Prompting

1. **Scrub the prompt** of all semantic tag names (`etl_extract`, `confidence_high`, etc.)
2. **Scrub the prompt** of all hex codes -- use natural color names ("coral red", "deep navy")
3. **Scrub the prompt** of all font family names -- use descriptive terms ("serif display type", "sans-serif labels", "monospace for numbers")
4. **Scrub the prompt** of framework/library names unless the figure is L3/L4 audience
5. **Add explicit ban** to the negative prompt: `--no visible hex codes, no semantic tag names, no font names as labels, no prompt keywords visible`

### After Generation -- Text Audit

Zoom to 100% and scan every text element in the image:

1. Does any text read "etl_extract", "source_corroborate", "confidence_high", or similar? **REJECT.**
2. Does any text read "#E84C4F", "#1E3A5F", "#2E7D7B", or any hex code? **REJECT.**
3. Does any text read "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono"? **REJECT.**
4. Does any text read "Nano Banana", "Gemini", "prompt:", "STYLE:", or "NEGATIVE:"? **REJECT.**
5. Does any text read "Pydantic", "FastAPI", "Splink" when the audience is L1 or L2? **REJECT.**
6. Is there any garbled, pseudo-text, or lorem-ipsum-like gibberish? **REJECT.**

If any check fails, do NOT attempt to fix with inpainting. Re-prompt from scratch with stronger negative instructions.

---

## Iteration Protocol for Failures

When a generated figure fails the quality checklist (score < 17/20), follow this protocol.

### Failure Category: Wrong Background Color

**Symptom:** Background is white, gray, pure cream, or has a gradient.
**Fix:** Add to the start of the content prompt: "The entire background MUST be warm cream color (#f6f3e6). No pure white, no gray, no gradient."
**Also add to negative:** `--no white background, no gray background, no gradient background`

### Failure Category: Sci-Fi / Corporate Aesthetic

**Symptom:** Glowing elements, neon highlights, corporate gradients, glossy surfaces.
**Fix:** Strengthen negative prompt with: `--no glowing, no neon, no gradient, no glossy, no sci-fi, no corporate, no futuristic`
**Also add to style:** "This MUST look like a Warp Records album insert or a vintage recording studio wall chart, NOT a tech startup pitch deck."

### Failure Category: Garbled Text

**Symptom:** Text elements contain random characters, overlapping glyphs, or unreadable labels.
**Fix:** Reduce the number of text elements. Nano Banana Pro handles fewer, larger text elements better than many small ones. Consider removing labels and adding them post-generation in an image editor.
**Rule of thumb:** Maximum 8 distinct text elements per figure.

### Failure Category: Symmetric / Centered Layout

**Symptom:** Everything is perfectly centered, balanced, or on a regular grid.
**Fix:** Add to style prompt: "Deliberately asymmetric composition. The main visual element should be offset to the left or right, NOT centered. Negative space should be uneven -- more on one side than the other."

### Failure Category: Too Dense / No Breathing Room

**Symptom:** Elements fill the entire canvas with no negative space.
**Fix:** Remove 30% of the content elements. Start with the least essential labels and annotations. Negative space is not wasted space -- it is a design element.
**Add to style:** "At least 30% of the canvas MUST be empty warm cream background with no elements."

### Failure Category: Rendered Internal Terms

**Symptom:** Semantic tags, hex codes, or font names appear as visible text.
**Fix:** Re-prompt from scratch. Completely remove all internal terms from the prompt and replace with natural language descriptions. See the Anti-Hallucination Protocol above.

### General Iteration Rule

- **Maximum 3 attempts** per figure before stepping back to revise the figure plan itself
- If 3 attempts all fail the same check, the figure plan is too complex -- simplify the content elements
- Document each attempt with the score and the specific failures in the figure plan's Status section

---

## Checklist: Complete Workflow

Use this checklist to track each figure through the full workflow.

- [ ] **Plan**: Figure plan created in `figure-plans/fig-repo-{NN}-{name}.md`
- [ ] **Review**: Content spec reviewed (all 10 items in CONTENT-TEMPLATE-REPO.md checklist pass)
- [ ] **Translate**: Semantic tags translated to natural language for prompt
- [ ] **Compose**: Two-part prompt (Style + Content) written using master template
- [ ] **Generate**: Image generated in Nano Banana Pro
- [ ] **Audit**: Anti-hallucination text audit passed (0 internal terms visible)
- [ ] **Score**: Quality checklist scored >= 17/20
- [ ] **Save**: Raw PNG saved to `generated/`
- [ ] **Convert**: Web-optimized JPEG saved to `assets/`
- [ ] **Embed**: JPEG linked from target documentation file
- [ ] **Status**: Figure plan Status section updated to reflect completion

---

*Music Attribution Scaffold -- Repository Documentation Prompting Instructions v1.0.0*
