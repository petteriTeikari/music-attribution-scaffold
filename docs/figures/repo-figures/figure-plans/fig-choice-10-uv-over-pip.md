# fig-choice-10: Why uv over pip/conda?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-10 |
| **Title** | Why uv over pip/conda? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | CLAUDE.md, pyproject.toml |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the package manager decision. The scaffold uses uv exclusively -- pip and conda are completely banned. uv provides fast, deterministic dependency resolution with dependency groups, a single lockfile, and virtual environment management. This is a critical project rule: `uv ONLY` is enforced across all documentation and CI.

The key message is: "uv provides 10-100x faster dependency resolution with deterministic lockfiles and dependency groups -- pip and conda are completely banned."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY UV OVER PIP/CONDA?                                       |
|  ■ Package Manager: uv ONLY                                    |
+---------------------------------------------------------------+
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ UV           │ │ PIP          │ │ CONDA        │          |
|  │ ■ SELECTED   │ │ ■ BANNED     │ │ ■ BANNED     │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │              │ │              │ │              │          |
|  │ SPEED        │ │ SPEED        │ │ SPEED        │          |
|  │ ~100x faster │ │ Baseline     │ │ 2-5x slower  │          |
|  │ (Rust-based) │ │              │ │ than pip     │          |
|  │              │ │              │ │              │          |
|  │ LOCKFILE     │ │ LOCKFILE     │ │ LOCKFILE     │          |
|  │ uv.lock      │ │ pip-compile  │ │ conda-lock   │          |
|  │ (built-in)   │ │ (pip-tools)  │ │ (external)   │          |
|  │              │ │              │ │              │          |
|  │ GROUPS       │ │ GROUPS       │ │ GROUPS       │          |
|  │ [dev], [test]│ │ extras only  │ │ environments │          |
|  │ native       │ │              │ │              │          |
|  │              │ │              │ │              │          |
|  │ VENV         │ │ VENV         │ │ VENV         │          |
|  │ uv venv      │ │ python -m    │ │ conda create │          |
|  │ (integrated) │ │ venv (manual)│ │ (heavy)      │          |
|  │              │ │              │ │              │          |
|  │ CONFIG       │ │ CONFIG       │ │ CONFIG       │          |
|  │ pyproject.   │ │ requirements │ │ environment  │          |
|  │ toml only    │ │ .txt         │ │ .yml         │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
|  COMMANDS                                                      |
|  uv add <pkg>        (NOT pip install)                         |
|  uv sync             (NOT pip install -r)                      |
|  uv run pytest       (NOT python -m pytest)                    |
|                                                                |
+---------------------------------------------------------------+
|  RULE: Never use pip, conda, or create requirements.txt        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY UV OVER PIP/CONDA?" with coral accent square |
| uv card | `selected_option` | Speed, lockfile, groups, venv, config |
| pip card | `deferred_option` | Banned -- with reasons (slow, fragile) |
| conda card | `deferred_option` | Banned -- with reasons (heavy, non-Python) |
| Commands section | `data_mono` | uv add, uv sync, uv run equivalents |
| Ban rule footer | `callout_bar` | "Never use pip, conda, or create requirements.txt" |

## Anti-Hallucination Rules

1. uv is the ONLY allowed package manager -- pip and conda are COMPLETELY BANNED per CLAUDE.md.
2. All dependencies are in pyproject.toml, NEVER in requirements.txt.
3. uv is written in Rust -- this is the source of its speed advantage.
4. The lock file is `uv.lock` -- it is deterministic.
5. Dependency groups ([dev], [test]) are supported natively in pyproject.toml.
6. The commands are `uv add`, `uv sync`, `uv run` -- not pip equivalents.
7. The pre-commit hooks use `uv run` to ensure version consistency.
8. This is a CRITICAL rule -- violations should be caught in code review.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Comparison chart: uv package manager selected exclusively for the music attribution scaffold over banned pip and conda, showing 100x faster Rust-based resolution, deterministic lockfiles, and native dependency groups for open-source music metadata project reproducibility.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Comparison chart: uv package manager selected exclusively for the music attribution scaffold over banned pip and conda, showing 100x faster Rust-based resolution, deterministic lockfiles, and native dependency groups for open-source music metadata project reproducibility.](docs/figures/repo-figures/assets/fig-choice-10-uv-over-pip.jpg)

*The music attribution scaffold enforces uv as the sole package manager, completely banning pip and conda for deterministic, fast dependency resolution via Rust-based tooling and a single `pyproject.toml` source of truth.*

### From this figure plan (relative)

![Comparison chart: uv package manager selected exclusively for the music attribution scaffold over banned pip and conda, showing 100x faster Rust-based resolution, deterministic lockfiles, and native dependency groups for open-source music metadata project reproducibility.](../assets/fig-choice-10-uv-over-pip.jpg)
