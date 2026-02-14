# Nano Banana Pro -- Repository Figure Prompting Instructions

**Version:** 2.0.0
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

**3a. Translate the ASCII layout to natural language.** Do NOT paste the raw ASCII
block — rewrite it as prose describing the visual composition.

**3b. Scrub internal references** (mandatory before pasting):
- [ ] No color names as labels — use tier/level names ("High", "Low", not "Green", "Red")
- [ ] No CSS class names — use descriptions ("serif display type", "small caps")
- [ ] No font family names — use categories ("serif", "sans-serif", "monospace")
- [ ] No hex codes — use natural color names ("coral red", "deep navy")
- [ ] No semantic tag names — use visual descriptions ("data ingestion zone")
- [ ] No parenthetical style annotations near content labels

**3c. Apply the Master Prompt Template** with the translated, scrubbed content.

### Step 4: Generate in Nano Banana Pro

- Upload the composed prompt to Gemini
- Generate the image
- If the figure plan includes visual reference images, upload those alongside the prompt

### Step 5: Verify and Save

- Run the quality checklist (21/25 threshold)
- Save raw PNG to `docs/figures/repo-figures/generated/`
- Run conversion script for web-optimized JPEG to `docs/figures/repo-figures/assets/`
- Embed JPEG in documentation

---

## Master Prompt Template

Use this template for every repo figure. Replace bracketed sections with content from the figure plan.

**CRITICAL: Style keywords go FIRST, content SECOND. Never put style descriptors near element labels -- this causes prompt leakage where style words appear as visible text.**

```
STYLE:
Warm cream background. Warp Records editorial aesthetic meets
constructivist data visualization. Coral red as primary graphic
accent -- accent squares, thin accent lines, stage markers. Deep navy
for structural elements and module boundaries. Teal for technology
and feedback loops. Matte finish, halftone grain texture. Asymmetric
composition with generous negative space (30%+). Sharp geometric edges,
no rounded corners, no drop shadows. Bold serif display headings in
ALL-CAPS with letter tracking. Clean sans-serif labels. Monospace
typeface for numbers and data.

[IF APPLICABLE -- add layout-specific style notes:]
[For Template A (Hero): Bold display type as primary visual element]
[For Template B (Multi-Panel): Thin coral dividers between panels]
[For Template C (Flowchart): Solid lines for selected paths, dashed for alternatives]
[For Template D (Split-Panel): Muted palette on left, full palette on right]
[For Template E (Steps): Vertical signal chain, coral squares as stage markers]

TEXT RENDERING RULES:
- Render text labels cleanly at large size or use solid-colored
  placeholder blocks where text would go (for post-processing)
- Do NOT attempt to render complex multi-word labels -- use
  placeholder rectangles with colored borders instead
- Maximum 8 distinct text elements per figure
- NO figure numbers, NO "Figure X." captions, NO "Fig." prefix
- The editorial display title IS allowed but must not look like
  a formal academic figure caption

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
garbled text, illegible glyphs, blurred characters, pseudo-text,
corrupted letters, gibberish words, broken typography,
visible hex codes, color codes as text, "#" followed by six characters,
semantic tag names visible, technical markup visible,
font names as labels, "Instrument Serif" text, "Plus Jakarta Sans" text,
prompt instructions as labels, style keywords visible,
rendering keywords as labels, aesthetic descriptors as text,
parentheses with style words, meta-instructions rendered,
"Figure 1", "Fig.", figure title, figure number, figure caption,
numbered figure label, academic figure numbering,
color names as labels, "Green" as label, "Amber" as label, "Red" as label,
CSS class names visible, ".editorial-display" text, ".data-mono" text,
"(editorial-caps)" text, "(editorial-display)" text
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

## ASCII Layout Hygiene (CRITICAL)

The ASCII layout in each figure plan is the primary visual blueprint. Nano Banana Pro
renders EVERYTHING in the ASCII block as visible content. Internal reference information
MUST NOT appear inside the ``` ASCII layout ``` block.

### BANNED inside ASCII layouts:

| Category | Examples | Replace With |
|----------|----------|-------------|
| Color names as labels | "Green", "Amber", "Red" | Tier labels: "High", "Medium", "Low" |
| CSS class annotations | "(editorial-caps)", ".data-mono" | Natural descriptions: "in small caps", "in monospace" |
| Font family names | "(Instrument Serif)", "(IBM Plex Mono)" | "serif display type", "monospace" |
| Hex codes | "#E84C4F", "#f6f3e6" | Never — colors are style, not content |
| Semantic tag names | "etl_extract", "confidence_high" | Natural labels: "ETL", "HIGH" |
| Style annotations | "(matte)", "(asymmetric)" | Never — move to style prompt |

### WHERE to put internal references instead:

- **Content Elements table** — map visible labels to their semantic tags
- **Anti-Hallucination Rules** — document exact values/thresholds
- **Style notes** (outside ASCII block) — font and color specifications

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

Run this checklist after every generation. The figure must score 21/25 or higher (see STYLE-GUIDE-REPO.md v2.0 for the full 25-item checklist).

### Quick Reject (ANY fail = immediate reject)

- [ ] Background IS warm cream (#f6f3e6), not white, gray, or yellow
- [ ] NO neon, glow, or sci-fi aesthetic anywhere
- [ ] NO garbled, illegible, or pseudo-text
- [ ] NO hex codes visible as text ("#E84C4F", "#1E3A5F", etc.)
- [ ] NO semantic tags visible as text ("etl_extract", "confidence_high", etc.)
- [ ] NO font names visible as text ("Instrument Serif", "Plus Jakarta Sans", etc.)
- [ ] NO prompt/style keywords visible as text ("matte", "asymmetric", "editorial", etc.)
- [ ] NO "Figure 1.", "Fig.", or numbered figure caption visible
- [ ] NO color names visible as standalone labels ("Green", "Amber", "Red", "Blue", etc.)
- [ ] NO CSS class names visible (".editorial-display", ".data-mono", etc.)

If any quick reject fails, re-prompt from scratch -- do NOT fix with inpainting.

### Full Checklist (score 1/0 each, accept if >= 21/25, see STYLE-GUIDE-REPO.md v2.0)

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

**Anti-Hallucination (5):**
15. No semantic tag names visible
16. No hex codes visible as text
17. No font names visible as text
18. No prompt keywords visible as text
19. No "Figure X." or "Fig." numbered caption visible

**Domain (4):**
20. Technical accuracy (correct pipeline order, correct thresholds)
21. Warp Records aesthetic achieved
22. Target audience would understand
23. No internal/workflow terms rendered as visible text

**Production (2):**
24. Correct aspect ratio
25. Sufficient resolution (>= 1200px wide)

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

## Anti-Hallucination Protocol (v2.0)

Nano Banana Pro will sometimes render internal instructions as visible text in the image. This is the #1 quality issue and requires aggressive prevention.

### Three Classes of Hallucination

| Class | Example | Severity |
|-------|---------|----------|
| **Technical Markup** | "#E84C4F", "etl_extract", "source_musicbrainz" visible as text | CRITICAL -- immediate reject |
| **Prompt Leakage** | "(matte finish, asymmetric)", "Instrument Serif", "editorial caps" visible | CRITICAL -- immediate reject |
| **Figure Caption** | "Figure 1. ETL Pipeline Overview", "Fig. 3: Oracle Problem" visible | CRITICAL -- immediate reject |
| **Text Garbling** | Random characters, illegible glyphs, pseudo-text | HIGH -- reject unless minimal |

### Before Prompting -- Scrub Checklist

1. **Scrub ALL hex codes** -- use natural color names ("coral red", "deep navy", "teal")
2. **Scrub ALL semantic tag names** (`etl_extract`, `confidence_high`, etc.)
3. **Scrub ALL font family names** -- use descriptive terms ("serif display type", "sans-serif labels", "monospace for numbers")
4. **Scrub ALL framework/library names** unless the figure is L3/L4 audience
5. **Separate style from content** -- style keywords go at the START of the prompt, content descriptions AFTER. Never interleave.
6. **No parenthetical qualifiers near labels** -- write "Five processing stages flowing left to right" not "Five processing stages (matte, asymmetric, editorial)"
7. **No figure numbering** -- do not mention "Figure 1" or "Fig." anywhere in the prompt
8. **Add the full Combined Negative Prompt** from STYLE-GUIDE-REPO.md

### After Generation -- Text Audit (MANDATORY)

Zoom to 100% and scan every text element in the image:

| Check | What to Look For | Action |
|-------|-----------------|--------|
| 1 | Semantic tags: "etl_extract", "source_corroborate", "confidence_high", "primary_outcome", "data_flow" | **REJECT** |
| 2 | Hex codes: "#E84C4F", "#1E3A5F", "#2E7D7B", "#f6f3e6", or any "#XXXXXX" pattern | **REJECT** |
| 3 | Font names: "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" | **REJECT** |
| 4 | Prompt keywords: "Nano Banana", "Gemini", "prompt:", "STYLE:", "NEGATIVE:", "matte", "asymmetric" | **REJECT** |
| 5 | Figure captions: "Figure 1.", "Fig.", "Figure X:", any numbered academic caption | **REJECT** |
| 6 | Framework names (L1/L2 only): "Pydantic", "FastAPI", "Splink", "CopilotKit" | **REJECT** |
| 7 | Style descriptors: "(non-glowing, elegant)", "(editorial)", parenthesized style words | **REJECT** |
| 8 | Garbled text: random characters, illegible glyphs, pseudo-text, lorem ipsum | **REJECT** |
| 9 | Color names as labels: "Green", "Amber", "Red", "Blue", "Gray", "Gold" as standalone text | **REJECT** |
| 10 | CSS class names: ".editorial-display", ".editorial-caps", ".data-mono" | **REJECT** |

**If any check fails, do NOT attempt to fix with inpainting. Re-prompt from scratch with stronger negative instructions and fewer text elements.**

### The Placeholder Protocol (for Text-Heavy Figures)

When a figure requires many text labels, request placeholders instead of rendered text:

```
TEXT RENDERING: For all text labels and callout content, render
clean solid-colored rectangular placeholder blocks (light gray
backgrounds with colored borders) where text would go. Do NOT
attempt to render actual text characters. I will add labels in
post-processing using an image editor. Exception: single large
letters (A, B, C) for panel identification are OK to render.
```

This is the most reliable approach for figures with more than 8 text elements.

---

## Iteration Protocol for Failures

When a generated figure fails the quality checklist (score < 21/25), follow this protocol.

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

### Failure Category: Rendered Internal Terms (Hex Codes, Semantic Tags)

**Symptom:** "#E84C4F", "etl_extract", "source_musicbrainz", or similar internal markup appears as visible text.
**Cause:** Hex codes or semantic tag names were in the prompt near content descriptions.
**Fix:** Re-prompt from scratch. Replace ALL hex codes with natural color names ("coral red", "deep navy"). Replace ALL semantic tags with visual descriptions ("data ingestion zone", "confidence indicator").
**Also add to negative:** the specific strings that leaked (e.g., `"#E84C4F" visible, "etl_extract" text`)

### Failure Category: Font Names as Labels

**Symptom:** "Instrument Serif", "Plus Jakarta Sans", or "IBM Plex Mono" appears as visible text in the image.
**Cause:** Font family names were in the prompt.
**Fix:** Replace all font names with descriptive terms: "bold serif display type", "clean sans-serif labels", "monospace digits".
**Also add to negative:** `"Instrument Serif" text, "Plus Jakarta Sans" text, "IBM Plex Mono" text, font names as labels`

### Failure Category: Figure Caption Rendered

**Symptom:** "Figure 1. ETL Pipeline Overview" or "Fig. 3:" appears as a formal numbered caption in the image.
**Cause:** The figure plan title or numbering leaked into the prompt, or Nano Banana Pro added it autonomously.
**Fix:** Ensure no "Figure X" or "Fig." text appears anywhere in the prompt. The editorial display title ("ETL PIPELINE") is fine, but it must NOT include a figure number prefix.
**Also add to negative:** `"Figure 1", "Fig.", figure title, figure number, figure caption, numbered figure label`

### Failure Category: Prompt Leakage (Style Words as Text)

**Symptom:** Words like "(matte finish)", "asymmetric", "editorial", "constructivist" appear as visible text in the image.
**Cause:** Style descriptors were placed too close to content labels, or parenthetical qualifiers were used.
**Fix:** Restructure the prompt: move ALL style keywords to the very beginning, keep content descriptions plain and factual. Never use parenthetical style qualifiers near element names.

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
- [ ] **Score**: Quality checklist scored >= 21/25
- [ ] **Save**: Raw PNG saved to `generated/`
- [ ] **Convert**: Web-optimized JPEG saved to `assets/`
- [ ] **Embed**: JPEG linked from target documentation file
- [ ] **Status**: Figure plan Status section updated to reflect completion

---

*Music Attribution Scaffold -- Repository Documentation Prompting Instructions v2.0.0*
