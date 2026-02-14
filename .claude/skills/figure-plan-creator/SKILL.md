---
name: figure-plan-creator
description: Create and review Nano Banana Pro figure plans with anti-hallucination guardrails for repository documentation and manuscript figures
---

# Figure Plan Creator

## When to Use

- When the user asks to "create a figure plan", "design a figure", "plan a figure"
- When the user says `/figure-plan-creator`
- When creating new `.md` files in `docs/figures/repo-figures/figure-plans/`
- When creating new `.md` files in the manuscript figures directory

## Scope: Two Figure Systems

This skill handles TWO distinct figure systems:

| System | Location | Style | Use Case |
|--------|----------|-------|----------|
| **Repo Figures** | `docs/figures/repo-figures/figure-plans/` | Warp Records editorial + constructivist | Repository documentation (README, MkDocs) |
| **Manuscript Figures** | `~/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/` | Hybrid Data-Vector Collage | Academic paper (SSRN preprint) |

Both use Nano Banana Pro (Gemini) for generation and share the same anti-hallucination guardrails.

---

## CRITICAL: The Three Nano Banana Artifacts

These are the three most common quality failures. The entire skill exists to prevent them.

### Artifact 1: Hex Codes Rendered as Text

**What happens:** "#E84C4F" or "#1E3A5F" appears as visible text in the generated image.
**Root cause:** Hex codes in the prompt are near content descriptions. Nano Banana Pro treats them as labels.
**Prevention:**
- NEVER include hex codes in the CONTENT section of prompts
- Keep hex codes in the STYLE section only, at the START of the prompt
- Use natural color names: "coral red", "deep navy", "teal", "warm cream"
- Add to negative prompt: `visible hex codes, "#" followed by six characters, color codes as text`

### Artifact 2: Font Names Rendered as Text

**What happens:** "Instrument Serif", "Plus Jakarta Sans", or "IBM Plex Mono" appears as a visible label.
**Root cause:** Font family names in the prompt are interpreted as content.
**Prevention:**
- NEVER use font family names in prompts
- Use descriptive terms: "bold serif display type", "clean sans-serif labels", "monospace digits"
- Add to negative prompt: `font names as labels, "Instrument Serif" text, "Plus Jakarta Sans" text, "IBM Plex Mono" text`

### Artifact 3: Figure Captions Rendered as Text

**What happens:** "Figure 1. ETL Pipeline Overview" or "Fig. 3:" appears as a formal numbered caption.
**Root cause:** Figure numbering from the plan file or convention leaks into the prompt.
**Prevention:**
- NEVER include "Figure X." or "Fig." in prompts
- Editorial display titles ("ETL PIPELINE") are fine -- numbered captions are NOT
- Add to negative prompt: `"Figure 1", "Fig.", figure title, figure number, figure caption, numbered figure label`

### Bonus Artifact: Prompt Leakage

**What happens:** Style keywords like "(matte finish, asymmetric)" or "editorial" appear as visible text.
**Root cause:** Style descriptors placed near element labels, or parenthetical qualifiers used.
**Prevention:**
- ALL style keywords go at the START of the prompt, separated from content
- Never use parenthetical style qualifiers near element names
- Add to negative prompt: `prompt instructions as labels, style keywords visible, aesthetic descriptors as text`

---

## Instructions

### Step 1: Determine Figure System

Ask the user which system the figure is for:

| If for... | Use these references |
|-----------|---------------------|
| **Repository docs** | `docs/figures/repo-figures/STYLE-GUIDE-REPO.md`, `CONTENT-TEMPLATE-REPO.md`, `PROMPTING-INSTRUCTIONS-REPO.md` |
| **Manuscript** | `~/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/STYLE-GUIDE.md` |

### Step 2: Load Context

Read these files before creating any figure plan:

```
REQUIRED CONTEXT (always load):
1. The appropriate STYLE-GUIDE (repo or manuscript)
2. CONTENT-TEMPLATE-REPO.md (for repo figures)
3. PROMPTING-INSTRUCTIONS-REPO.md (for repo figures)
4. At least 2 existing figure plans as format examples
```

### Step 3: Create the Figure Plan

Follow the CONTENT-TEMPLATE format. Key requirements:

1. **Metadata** -- ID, title, audience level, location, priority, aspect ratio, layout template
2. **Purpose** -- 1-2 sentences on WHY this figure exists
3. **Key Message** -- Single sentence takeaway
4. **Visual Concept** -- ASCII mockup of layout
5. **Spatial Anchors** -- YAML coordinates
6. **Content Elements** -- Structures, relationships, callouts with semantic tags
7. **Text Content** -- Labels (max 30 chars) and caption
8. **Anti-Hallucination Rules** -- ALWAYS include default + figure-specific rules
9. **Alt Text** -- 125 chars max
10. **JSON Export Block** -- Machine-readable format

### Step 4: Run Reviewer Agent (MANDATORY)

After creating the figure plan, ALWAYS spawn a reviewer agent to audit it. This is non-negotiable.

**Reviewer Agent Prompt:**

```
You are a Figure Plan Quality Reviewer for Nano Banana Pro generation.

Read the figure plan at [PATH] and audit it against these CRITICAL checks:

## Quick Reject Checks (ANY fail = must fix before proceeding)

1. Does the plan contain ANY hex codes (#XXXXXX) in the Content Elements,
   Visual Concept, or Text Content sections? (Hex codes are ONLY allowed
   in the Palette section if it exists, which maps to the STYLE-GUIDE)

2. Does the plan contain ANY font family names ("Instrument Serif",
   "Plus Jakarta Sans", "IBM Plex Mono") outside of Anti-Hallucination Rules?

3. Does any text label or callout contain a formal figure caption pattern
   like "Figure 1.", "Fig. X:", or "Figure X:"?

4. Does any text label contain a semantic tag name like "etl_extract",
   "confidence_high", "source_musicbrainz"?

5. Does any label exceed 30 characters?

6. Are style/rendering keywords ("matte", "asymmetric", "editorial",
   "constructivist", "halftone") present in content sections?

## Structural Checks

7. Is the Anti-Hallucination Rules section present and does it include
   all 8 default rules?

8. Is the JSON Export Block present and valid JSON?

9. Are spatial anchors defined?

10. Is the key message a single sentence?

## Content Checks

11. Is the audience level (L1-L4) consistent with the vocabulary used?
    - L1/L2 should NOT reference: Pydantic, FastAPI, Splink, pgvector,
      CopilotKit, Docker, pytest
    - L3/L4 CAN reference these

12. Are the content elements technically accurate? (Check pipeline order,
    confidence thresholds, assurance levels, source names)

Report: List each check as PASS or FAIL with specific line references.
If ANY quick reject check fails, provide the exact fix needed.
```

### Step 5: Fix Issues and Re-Review

If the reviewer agent finds issues:
1. Fix ALL quick reject issues immediately
2. Fix structural issues
3. Re-run the reviewer agent to confirm fixes

### Step 6: Update Status

Mark the figure plan status as "Draft created" and "Content reviewed".

---

## Anti-Hallucination Rules: Default Set

Every figure plan MUST include these 8 default anti-hallucination rules (copy from CONTENT-TEMPLATE-REPO.md):

```
1. Font names are INTERNAL -- "Instrument Serif", "Plus Jakarta Sans",
   "IBM Plex Mono" are CSS references. Do NOT render them as labels.
2. Semantic tags are INTERNAL -- etl_extract, entity_resolve,
   source_corroborate, final_score, confidence_high, assurance_a2,
   source_musicbrainz etc. Do NOT render them as visible text.
3. Hex codes are INTERNAL -- #E84C4F, #1E3A5F, #2E7D7B, #f6f3e6 are
   palette references. Do NOT render them.
4. Engineering jargon -- "Pydantic", "FastAPI", "Splink", "pgvector"
   should NOT appear unless the figure is L3/L4 audience.
5. Background MUST be warm cream (#f6f3e6 for repo, #F8F4E8 for
   manuscript) -- exact match. No pure white, no gray, no yellow.
6. No generic flowchart aesthetics -- no thick block arrows, no
   rounded rectangles, no PowerPoint look.
7. No figure captions -- do NOT render "Figure 1.", "Fig.", or any
   numbered academic caption. Editorial display titles are allowed.
8. No prompt leakage -- do NOT render style keywords ("matte",
   "asymmetric", "editorial", "constructivist") as visible text.
```

Plus add figure-specific rules (e.g., exact source count, correct terminology).

---

## Prompt Construction: DO and DON'T

### Content Section

| DO | DON'T |
|----|-------|
| "coral red accent squares" | "#E84C4F accent squares" |
| "deep navy module boundaries" | "#1E3A5F module boundaries" |
| "bold serif display headings" | "Instrument Serif headings" |
| "clean sans-serif labels" | "Plus Jakarta Sans labels" |
| "monospace digits for scores" | "IBM Plex Mono for scores" |
| "ETL PIPELINE" (editorial title) | "Figure 1. ETL Pipeline Overview" |
| "five source nodes converging" | "five source_musicbrainz/source_discogs nodes" |
| "green confidence indicator" | "confidence_high indicator" |

### Style Section

| DO | DON'T |
|----|-------|
| Style keywords at START of prompt | Style keywords mixed with content |
| "Warm cream background" | "Warm cream background (#f6f3e6)" in content |
| Natural color descriptions | Hex codes anywhere near labels |
| Separate STYLE and CONTENT blocks | Single block mixing both |

### Prompt Structure

```
STYLE: [ALL style/aesthetic keywords here -- far from content]

TEXT RENDERING RULES: [Placeholder protocol if needed]

CONTENT: [Pure content descriptions -- no style words, no hex codes,
          no font names, no semantic tags, no figure numbering]

DIMENSIONS: [width x height, aspect ratio]

NEGATIVE: [Full combined negative prompt from STYLE-GUIDE]
```

---

## Nano Banana Pro Quick Reference

### What It Does Well
- Abstract conceptual diagrams
- Pipeline/architecture visualizations
- Multi-panel compositions
- Warm editorial aesthetic
- Geometric elements, accent squares

### What It Does Poorly
- Text rendering (especially small or multi-word labels)
- Mathematical notation
- Precise data plots
- Exact color matching (iterative)

### When NOT to Use Nano Banana Pro

| Figure Type | Better Tool |
|-------------|-------------|
| Precise data plots | R + ggplot2 |
| Flowcharts with many text labels | Mermaid / Graphviz |
| Tables with exact data | Markdown / LaTeX |
| Timelines with dates | R + ggplot2 |

### Text Element Limits

- Maximum **8 distinct text elements** per figure for clean rendering
- For figures needing more text, use the **Placeholder Protocol**: request solid-colored rectangular blocks where text should go, add labels in post-processing
- Single large letters (A, B, C, I, II, III) for panel identification render well

---

## File Naming Conventions

### Repo Figures
```
fig-{category}-{NN}-{short-description}.md

Categories: repo, backend, frontend, theory, howto, prd, choice, agent
Examples:
  fig-repo-01-hero-overview.md
  fig-backend-11-attribution-engine-flow.md
  fig-theory-03-oracle-problem-eli5.md
```

### Manuscript Figures
```
fig{NN}-{short-description}.md

Examples:
  fig03-oracle-problem.md
  fig06-attribution-by-design.md
```

---

## Quality Checklist (Post-Generation)

The generated image must pass the quality checklist in STYLE-GUIDE-REPO.md (v2.0):
- **21/25 minimum score** for repo figures
- **17/20 minimum score** for manuscript figures
- **Quick reject gates** (ANY fail = immediate re-prompt):
  - Background is warm cream
  - No neon/glow/sci-fi
  - No garbled text
  - No hex codes visible
  - No font names visible
  - No "Figure X." caption visible

---

## Examples

### Good Figure Plan (passes all checks)

```markdown
# fig-backend-01: ETL Pipeline Overview

## Anti-Hallucination Rules

1. Font names are INTERNAL...
2. Semantic tags are INTERNAL...
[all 8 defaults]
9. There are exactly 5 sources: MUSICBRAINZ, DISCOGS, ACOUSTID,
   FILE_METADATA (tinytag), ARTIST_INPUT. Do NOT add Spotify or Apple.
10. MusicBrainz rate limit is 1 req/s. These are from the actual code.

## Content Elements

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| MusicBrainz source | `source_musicbrainz` | Purple-tinted source node showing "1 req/s" |

## Text Content

### Labels
- "ETL PIPELINE" (editorial display title -- NOT "Figure 1. ETL Pipeline")
- "MUSICBRAINZ" (source label)
- "1 req/s" (rate limit in monospace)
```

### Bad Figure Plan (would fail review)

```markdown
## Content Elements

| Name | Description |
|------|-------------|
| MusicBrainz | #BA478F colored source node |  ← HEX CODE IN CONTENT
| Title | "Figure 1. ETL Pipeline" in Instrument Serif |  ← FIGURE CAPTION + FONT NAME
| Score | confidence_high indicator |  ← SEMANTIC TAG AS LABEL
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-14 | Initial skill with reviewer agent, anti-hallucination guardrails, dual figure system support |
