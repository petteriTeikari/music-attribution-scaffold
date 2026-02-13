# fig-repo-07: Pre-commit Quality Gates

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-07 |
| **Title** | Pre-commit Quality Gates: Seven Hooks, Zero Exceptions |
| **Audience** | Technical (contributors) |
| **Complexity** | L2 (workflow) |
| **Location** | CONTRIBUTING.md, docs/architecture/quality.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Every commit passes through seven pre-commit hooks before it can land. This figure shows the sequential chain of quality gates, what each hook catches, and the tools behind them. It reinforces the project's "quality is non-negotiable" stance and helps contributors understand what will block their commits.

The key message is: "Seven automated quality gates run on every commit -- from trailing whitespace to secret detection. No exceptions, no bypasses."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  PRE-COMMIT QUALITY GATES                                              |
|  ■ Seven Hooks, Zero Exceptions                                        |
+-----------------------------------------------------------------------+
|                                                                        |
|  git commit ──▶                                                        |
|                                                                        |
|  I          II          III         IV          V          VI    VII   |
|  ┌────┐    ┌────┐     ┌────┐     ┌────┐     ┌────┐     ┌────┐ ┌────┐|
|  │TRIM│───▶│YAML│───▶ │ UV │───▶ │RUFF│───▶ │RUFF│───▶ │MYPY│─│SECS│|
|  │SPACE│    │TOML│     │LOCK│     │LINT│     │ FMT│     │TYPE│ │SCAN│|
|  └────┘    └────┘     └────┘     └────┘     └────┘     └────┘ └────┘|
|    │          │          │          │          │          │       │    |
|  trailing  config     lockfile   style +    format    static  detect |
|  white-    validity   in sync    rules      check     types   secrets|
|  space     check      with deps  fix                  check         |
|  + EOF                                                               |
|                                                                        |
|  ─────────────────────────────────────────────────────────────────    |
|                                                                        |
|  ALSO CHECKED:                                                         |
|  ■ Large files (>1MB blocked, except docs/figures/generated/)          |
|  ■ Merge conflict markers                                              |
|  ■ Private key detection                                               |
|  ■ CSS token lint (frontend .tsx files only)                           |
|                                                                        |
|  ANY HOOK FAILS ──▶ COMMIT BLOCKED ──▶ FIX + RETRY                   |
|                                                                        |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "PRE-COMMIT QUALITY GATES" Instrument Serif ALL-CAPS |
| Hook chain (I-VII) | `pipeline_stage` | Seven connected boxes in horizontal flow |
| Roman numerals | `section_numeral` | Above each hook box |
| Hook names | `data_mono` | IBM Plex Mono inside each box |
| Description labels | `label_editorial` | Plus Jakarta Sans below each box |
| Flow arrows | `primary_pathway` | Coral arrows connecting hooks left-to-right |
| "git commit" trigger | `data_mono` | Entry point on the left |
| "Also Checked" list | `supplementary_list` | Additional hooks with accent square bullets |
| Failure flow | `error_pathway` | "ANY HOOK FAILS" to "COMMIT BLOCKED" to "FIX + RETRY" |
| Accent line divider | `accent_line` | Separating main chain from supplementary info |

## Anti-Hallucination Rules

1. The pre-commit config has these hook groups: pre-commit-hooks (trailing-whitespace, end-of-file-fixer, check-yaml, check-toml, check-added-large-files, check-merge-conflict, detect-private-key), uv-lock, ruff (local), ruff-format (local), mypy (local), css-token-lint (local), detect-secrets.
2. Ruff hooks use `repo: local` with `uv run ruff` -- NOT a pinned remote repo version.
3. The large file limit is 1000KB (1MB), with `docs/figures/generated/` excluded.
4. detect-secrets uses a `.secrets.baseline` file and excludes `uv.lock` and `.cruft.json`.
5. mypy runs on `src/` only (not tests), with `pass_filenames: false`.
6. css-token-lint runs `scripts/css-token-lint.sh` on frontend `.tsx` files only.
7. There is NO black, isort, or flake8 hook -- ruff handles all linting and formatting.
8. The hooks are configured for both pre-commit and commit-msg hook types.

## Alt Text

Horizontal chain of seven pre-commit hooks: whitespace, YAML/TOML, uv lock, ruff lint, ruff format, mypy types, detect-secrets. Any failure blocks the commit.
