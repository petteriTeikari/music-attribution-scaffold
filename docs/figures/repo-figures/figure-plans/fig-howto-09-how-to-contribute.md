# fig-howto-09: How to Contribute

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-09 |
| **Title** | How to Contribute |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural mapping) |
| **Location** | CONTRIBUTING.md, docs/guides/contributing.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete contribution workflow from fork to merged PR, with emphasis on the quality gates that every contribution must pass. It highlights the role of CLAUDE.md rules as the behavioral contract for both human and AI contributors. It answers: "I want to contribute -- what is the exact process, and what rules must I follow?"

The key message is: "Every contribution follows a six-step path: fork, branch, code (following CLAUDE.md rules), pass pre-commit hooks, pass tests, and submit a PR. The quality gates are non-negotiable -- ruff, mypy, and pytest must all pass before any PR is reviewed."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO CONTRIBUTE                                             |
|  ■ Fork to Merged PR                                           |
+---------------------------------------------------------------+
|                                                                |
|  I. FORK & CLONE              II. CREATE BRANCH                |
|  ────────────────             ─────────────────                |
|  ┌───────────────────┐       ┌───────────────────┐            |
|  │ gh repo fork       │       │ git checkout -b    │            |
|  │ cd music-          │  ──>  │  feat/my-feature   │            |
|  │  attribution-      │       │                    │            |
|  │  scaffold          │       │ Branch naming:     │            |
|  │ make install-dev   │       │ ■ feat/ fix/ docs/ │            |
|  └───────────────────┘       └─────────┬─────────┘            |
|                                         │                      |
|                                         v                      |
|  III. CODE (FOLLOW THE RULES)                                  |
|  ────────────────────────────                                  |
|  ┌─────────────────────────────────────────────┐              |
|  │ CLAUDE.md Rules (enforced for all contributors):            |
|  │                                              │              |
|  │ ■ uv ONLY (no pip, no conda)                │              |
|  │ ■ AST for code analysis (no grep/sed)        │              |
|  │ ■ encoding='utf-8' for all file ops          │              |
|  │ ■ Path() for all file paths                  │              |
|  │ ■ datetime.now(timezone.utc) always          │              |
|  │ ■ Never modify AIDEV-IMMUTABLE sections      │              |
|  └──────────────────────┬──────────────────────┘              |
|                          v                                      |
|  IV. PRE-COMMIT HOOKS              V. RUN TESTS               |
|  ─────────────────────             ──────────────              |
|  ┌───────────────────┐            ┌───────────────────┐       |
|  │ pre-commit run     │            │ make test          │       |
|  │  --all-files       │     ──>    │                    │       |
|  │                    │            │ All 4 must pass:   │       |
|  │ ■ ruff check       │            │ ■ ruff check       │       |
|  │ ■ ruff format      │            │ ■ ruff format      │       |
|  │ ■ mypy             │            │ ■ mypy             │       |
|  │ ■ detect-secrets   │            │ ■ pytest           │       |
|  └───────────────────┘            └─────────┬─────────┘       |
|                                              │                 |
|                                              v                 |
|  VI. SUBMIT PR                                                 |
|  ─────────────                                                 |
|  ┌─────────────────────────────────────────────┐              |
|  │ git push -u origin feat/my-feature           │              |
|  │ gh pr create --title "feat: description"     │              |
|  │                                              │              |
|  │ CI runs automatically → same 4 checks        │              |
|  │ Reviewer checks → code quality + tests       │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
+---------------------------------------------------------------+
|  ■ CLAUDE.md rules apply to human AND AI contributors alike   |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO CONTRIBUTE" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Fork to Merged PR" in Plus Jakarta Sans caps |
| Step I: Fork & Clone | `processing_stage` | gh repo fork command and make install-dev setup |
| Step II: Create Branch | `processing_stage` | Branch creation with naming convention (feat/, fix/, docs/) |
| Step III: Code with rules | `callout_box` | CLAUDE.md rules highlighted as the behavioral contract |
| Rule items (uv, AST, encoding, etc.) | `security_layer` | Six key rules from CLAUDE.md with coral accent square bullets |
| Step IV: Pre-commit hooks | `processing_stage` | Four hooks: ruff check, ruff format, mypy, detect-secrets |
| Step V: Run tests | `processing_stage` | make test running all four CI checks locally |
| Step VI: Submit PR | `processing_stage` | git push + gh pr create with CI running automatically |
| Flow arrows (I to VI) | `data_flow` | Sequential flow with slight branching at IV-V parallel step |
| Roman numerals I-VI | `section_numeral` | Step headers in editorial style |
| Command text | `data_mono` | IBM Plex Mono for all CLI commands |
| Footer callout | `callout_box` | "CLAUDE.md rules apply to human AND AI contributors alike" |

## Anti-Hallucination Rules

1. The package manager is uv ONLY -- pip and conda are completely banned. This is a hard rule, not a suggestion.
2. Pre-commit hooks run four checks: ruff check, ruff format --check, mypy, detect-secrets -- not just ruff.
3. CI runs the same four checks: ruff check, ruff format --check, mypy, pytest -- all must pass locally before pushing.
4. Branch naming uses conventional prefixes: feat/, fix/, docs/, chore/ -- not arbitrary names.
5. CLAUDE.md is the behavioral contract for BOTH human and AI contributors -- it is not AI-only documentation.
6. The setup command is `make install-dev` -- not `pip install -e .` or `uv install`.
7. AIDEV-IMMUTABLE sections exist and must never be modified -- this is a real constraint.
8. The repo uses `gh` CLI for PR creation -- this is the recommended tool.
9. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

How-to guide: six-step open-source contribution workflow for the music attribution scaffold, from fork and clone through branch creation, coding under CLAUDE.md behavioral rules, pre-commit hook verification, test execution, and pull request submission -- quality gates including ruff, mypy, and pytest are non-negotiable for both human and AI contributors to maintain transparent confidence in music metadata code.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![How-to guide: six-step open-source contribution workflow for the music attribution scaffold, from fork and clone through branch creation, coding under CLAUDE.md behavioral rules, pre-commit hook verification, test execution, and pull request submission -- quality gates including ruff, mypy, and pytest are non-negotiable for both human and AI contributors to maintain transparent confidence in music metadata code.](docs/figures/repo-figures/assets/fig-howto-09-how-to-contribute.jpg)

*Contribution workflow for the Music Attribution Scaffold. The CLAUDE.md behavioral contract governs both human and AI contributors equally, with four mandatory quality gates (ruff check, ruff format, mypy, pytest) ensuring that every pull request meets the project's standards for code quality and attribution correctness (Teikari, 2026).*

### From this figure plan (relative)

![How-to guide: six-step open-source contribution workflow for the music attribution scaffold, from fork and clone through branch creation, coding under CLAUDE.md behavioral rules, pre-commit hook verification, test execution, and pull request submission -- quality gates including ruff, mypy, and pytest are non-negotiable for both human and AI contributors to maintain transparent confidence in music metadata code.](../assets/fig-howto-09-how-to-contribute.jpg)
