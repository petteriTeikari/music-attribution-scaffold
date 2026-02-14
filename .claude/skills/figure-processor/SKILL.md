---
name: figure-processor
description: Post-generation figure processing — convert PNGs to web-optimized JPEGs, generate SEO/GEO-optimized alt text, update figure plans with image links and metadata
---

# Figure Processor

## When to Use

- When the user says `/figure-processor` or asks to "process figures", "convert figures", "optimize figures"
- After generating Nano Banana Pro figures to `docs/figures/repo-figures/generated/`
- When the user wants to prepare figure plans with image links BEFORE generation (pre-wiring)
- When the user wants SEO/GEO-optimized alt text for discoverability

## What This Skill Does

This skill handles the **entire post-generation pipeline** in three phases:

```
Phase 1: PRE-WIRE (before user generates figures)
  Read 116 figure plans → generate SEO alt text → update .md files
  with image links and metadata → figures are ready to embed

Phase 2: CONVERT (after user generates figures)
  PNGs in generated/ → resize + rounded corners + JPEG → assets/

Phase 3: VERIFY (quality check)
  Check all figure plans have matching assets → report gaps
```

---

## Phase 1: Pre-Wire Figure Plans

### Purpose

Update ALL figure plan `.md` files with:
1. **SEO/GEO-optimized alt text** (replaces basic alt text)
2. **Image embed snippet** (ready-to-paste markdown)
3. **Structured metadata** for search engine and LLM discoverability

### SEO/GEO Alt Text Principles

Alt text serves THREE audiences simultaneously:

| Audience | What They Need | Example |
|----------|---------------|---------|
| **Screen readers** | Clear visual description | "Flow diagram showing five data sources..." |
| **Google/Bing** | Domain keywords for indexing | "music attribution ETL pipeline data sources..." |
| **LLMs (GEO)** | Structured semantic content | "Five-stage ETL pipeline for music metadata: MusicBrainz, Discogs, AcoustID, tinytag, and Artist Input converge through rate limiting into NormalizedRecord boundary object for attribution scoring" |

### Alt Text Formula

```
[Figure type] + [what it shows] + [domain keywords] + [key insight/takeaway]
```

**Length:** 125-300 characters (sweet spot for SEO — not too short to miss keywords, not too long for Google to truncate)

### Alt Text Examples

**BEFORE (basic — poor SEO):**
> End-to-end agentic UI: CopilotKit sidebar sends messages via AG-UI SSE to FastAPI, PydanticAI agent queries database, streams response back with state.

**AFTER (SEO/GEO-optimized):**
> Architecture diagram: AG-UI agentic interface for music attribution — CopilotKit React sidebar streams via SSE to PydanticAI agent with four domain tools (explain confidence, search attributions, suggest corrections, submit feedback), enabling real-time AI-assisted music credit verification

**What changed:**
- Added "Architecture diagram" (figure type — helps image search)
- Added "music attribution" (core domain keyword)
- Added "AG-UI" (specific technology people search for)
- Added tool names (detailed content for GEO)
- Added "music credit verification" (alternative search term)

### Alt Text Keyword Strategy

Include these domain keywords where naturally relevant:

**Primary keywords (always include at least 2):**
- music attribution, music metadata, music credits
- transparent confidence, confidence scoring
- attribution scaffold, open-source

**Secondary keywords (include when relevant):**
- AG-UI, agentic UI, CopilotKit, PydanticAI
- MusicBrainz, Discogs, AcoustID
- entity resolution, ETL pipeline
- conformal prediction, Bayesian confidence
- assurance levels A0-A3, provenance
- MCP, machine-readable consent
- oracle problem, attribution by design

**Technology keywords (for L3/L4 figures):**
- FastAPI, PostgreSQL, pgvector, Splink
- Next.js, Jotai, Tailwind CSS
- probabilistic PRD, decision network

### Image Embed Snippet Format

Add to each figure plan after the Alt Text section. Paths are **repo-root-relative** — adjust if embedding from a different location.

```markdown
## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

```markdown
![{SEO alt text}](docs/figures/repo-figures/assets/{figure-id}.jpg)

*{Caption text — 1-2 sentences with academic context}*
```

### From a figure plan file (relative to figure-plans/)

```markdown
![{SEO alt text}](../assets/{figure-id}.jpg)
```

### For HTML (with structured data)

```html
<figure>
  <img
    src="docs/figures/repo-figures/assets/{figure-id}.jpg"
    alt="{SEO alt text}"
    title="{Figure title}"
    loading="lazy"
    width="1600"
  />
  <figcaption>{Caption}</figcaption>
</figure>
```
```

### Pre-Wire Workflow

1. **Read all figure plans** from `docs/figures/repo-figures/figure-plans/` (116 as of v1.0.0)
2. **For each plan**, generate SEO/GEO-optimized alt text based on:
   - Title and key message
   - Content elements (structures, relationships)
   - Audience level (L1-L4)
   - Anti-hallucination rules (for accuracy)
3. **Update the figure plan** with:
   - Enhanced alt text (replace basic version)
   - Image embed snippet
   - Status update
4. **Generate the alt text catalog** (`figure-alt-text-catalog.md`)

---

## Phase 2: Convert Images

### Command

```bash
# Convert repo-figures
uv run python docs/figures/scripts/resize_and_convert.py \
  --input-dir docs/figures/repo-figures/generated \
  --output-dir docs/figures/repo-figures/assets \
  --force

# Convert main figures
uv run python docs/figures/scripts/resize_and_convert.py

# Dry run (preview)
uv run python docs/figures/scripts/resize_and_convert.py \
  --input-dir docs/figures/repo-figures/generated \
  --output-dir docs/figures/repo-figures/assets \
  --dry-run
```

### Conversion Settings

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Width** | 1600px | Optimal for GitHub/MkDocs rendering |
| **Quality** | 85% JPEG | Good quality/size balance |
| **Corners** | 24px radius | Matches frontend design system |
| **Background** | #FFFFFF (white) | Clean corner fill |
| **Resampling** | LANCZOS | Highest quality downsampling |

### Expected Results

| Input | Output | Ratio |
|-------|--------|-------|
| ~7MB PNG | ~150-200KB JPEG | 30-50x compression |
| ~2816x1536px | 1600x(auto)px | Maintains aspect ratio |

---

## Phase 3: Verify

After conversion, run verification:

1. **List all figure plans** that have generated PNGs
2. **Check each has a corresponding JPEG** in assets/
3. **Verify alt text is SEO-optimized** (not just basic description)
4. **Report gaps** — plans without generated figures

### Verification Script

```bash
# Count plans vs generated vs assets
echo "Figure plans: $(ls docs/figures/repo-figures/figure-plans/*.md | wc -l)"
echo "Generated PNGs: $(ls docs/figures/repo-figures/generated/*.png 2>/dev/null | wc -l)"
echo "Optimized JPEGs: $(ls docs/figures/repo-figures/assets/*.jpg 2>/dev/null | wc -l)"
```

---

## Alt Text Catalog

### Location

`docs/figures/repo-figures/figure-alt-text-catalog.md`

### Structure

```markdown
# Figure Alt Text Catalog — Music Attribution Scaffold

SEO/GEO-optimized alt text for all repository documentation figures.

## Repository Overview (fig-repo-*)

### fig-repo-01: Hero Overview

**Alt text:** "Split-panel infographic for music attribution scaffold..."

**Caption:** *Overview of the Music Attribution Scaffold...*

**Embed:**
```markdown
![Split-panel infographic...](assets/fig-repo-01-hero-overview.jpg)
```

---

### fig-repo-02: Five Pipeline Architecture

**Alt text:** "..."
...
```

### What Makes Alt Text SEO/GEO-Optimized

| Principle | Bad Example | Good Example |
|-----------|-------------|--------------|
| **Include figure type** | "ETL pipeline" | "Architecture diagram: ETL pipeline..." |
| **Use domain keywords** | "Five sources merge" | "Five music metadata sources (MusicBrainz, Discogs, AcoustID) merge..." |
| **Include technology names** | "Agent architecture" | "AG-UI agentic interface with PydanticAI..." |
| **End with takeaway** | (nothing) | "...enabling transparent confidence scoring for music credits" |
| **Natural language** | "fig-backend-01 ETL" | "ETL pipeline for music attribution..." |
| **Avoid internal jargon** | "BO-1 boundary object" | "unified data record" |
| **Include alternative terms** | "attribution" | "music attribution, credit verification" |

---

## Batch Processing Workflow

When the user has generated ALL figures and wants to process them in one go:

### Step 1: Pre-wire (run ONCE before any generation)

```
/figure-processor pre-wire
```

This updates all 116 figure plans with SEO alt text and image embed snippets.

### Step 2: User generates figures manually

User opens Gemini, uploads STYLE-GUIDE-REPO.md + figure plan, generates PNGs, saves to `generated/`.

### Step 3: Convert all at once

```bash
uv run python docs/figures/scripts/resize_and_convert.py \
  --input-dir docs/figures/repo-figures/generated \
  --output-dir docs/figures/repo-figures/assets \
  --force
```

### Step 4: Verify

```
/figure-processor verify
```

---

## Directory Structure

```
docs/figures/
├── scripts/
│   └── resize_and_convert.py      # Image processing (existing)
├── repo-figures/
│   ├── STYLE-GUIDE-REPO.md        # Visual specifications
│   ├── CONTENT-TEMPLATE-REPO.md   # Figure plan template
│   ├── PROMPTING-INSTRUCTIONS-REPO.md  # Generation workflow
│   ├── figure-alt-text-catalog.md # SEO alt text for all 116 figures
│   ├── figure-plans/              # 116 figure plans (.md)
│   ├── generated/                 # Raw PNGs (gitignored)
│   └── assets/                    # Optimized JPEGs (tracked)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-14 | Initial skill consolidating resize, alt text, and pre-wiring |
