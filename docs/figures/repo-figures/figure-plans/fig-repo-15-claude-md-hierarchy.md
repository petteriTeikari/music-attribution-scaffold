# fig-repo-15: CLAUDE.md Hierarchy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-15 |
| **Title** | CLAUDE.md Hierarchy: AI-Assisted Development Configuration Tree |
| **Audience** | All (contributors using AI assistants) |
| **Complexity** | L2 (configuration) |
| **Location** | README.md, CONTRIBUTING.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This project uses an extensive AI assistant configuration system with multiple layers of rules, skills, golden paths, and domain-specific guidance. This figure maps the `.claude/` directory tree, showing how configuration cascades from root CLAUDE.md through rules, domains, skills, and memory files. It helps contributors understand how AI behavior is governed and where to add new rules.

The key message is: "AI assistant behavior is governed by a layered configuration system -- root CLAUDE.md sets the contract, rules/ adds domain specifics, skills/ provides reusable workflows, and memory/ captures project-specific learnings."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  CLAUDE.MD HIERARCHY                                                   |
|  ■ AI-Assisted Development Configuration Tree                          |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. ROOT LEVEL (always loaded)                                         |
|  ─────────────────────────────                                         |
|                                                                        |
|  CLAUDE.md  ◄── Quick reference, critical rules, forbidden actions     |
|       │                                                                |
|       ▼                                                                |
|  .claude/CLAUDE.md  ◄── Full behavior contract, templates, modes       |
|       │                                                                |
|       ├── golden-paths.md  ◄── Approved patterns + anti-patterns       |
|       │                                                                |
|  II. DOMAIN RULES (loaded by file trigger)                             |
|  ─────────────────────────────────────────                             |
|       │                                                                |
|       ├── rules/                                                       |
|       │   ├── 00-project-context.md      Project info + structure      |
|       │   ├── 01-code-analysis-ban.md    AST only, grep banned         |
|       │   ├── 05-source-of-truth.md      Config authority map          |
|       │   ├── 10-frontend-design-system.md  ■ Color + typography       |
|       │   └── 11-ux-first-philosophy.md  ■ UX principles              |
|       │                                                                |
|  III. SKILLS (invokable workflows)                                     |
|  ─────────────────────────────────                                     |
|       │                                                                |
|       ├── skills/                                                      |
|       │   └── self-learning-iterative-coder/                           |
|       │       └── SKILL.md               TDD loop with self-correction |
|       │                                                                |
|  IV. INSTITUTIONAL KNOWLEDGE                                           |
|  ─────────────────────────────                                         |
|       │                                                                |
|       ├── memory/                        Persistent failure patterns    |
|       ├── institutional-knowledge/       Domain expertise cache         |
|       ├── sessions/                      Session-specific context       |
|       └── meta-learning/                 Learning from past mistakes    |
|                                                                        |
|  ─────────────────────────────────────────────────────────             |
|  CONTEXT LOADING TRIGGERS:                                             |
|  ■ tests/** ──▶ loads domains/testing.md                               |
|  ■ pyproject.toml ──▶ loads domains/configuration.md                   |
|  ■ frontend/** ──▶ loads rules/10-* + rules/11-*                       |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "CLAUDE.MD HIERARCHY" Instrument Serif ALL-CAPS |
| Root level section | `config_tier` | CLAUDE.md and .claude/CLAUDE.md |
| Domain rules section | `config_tier` | Five rule files with numbered prefixes |
| Skills section | `config_tier` | Invokable workflow skills |
| Knowledge section | `config_tier` | Memory, institutional knowledge, sessions |
| File tree | `data_mono` | IBM Plex Mono tree structure |
| File descriptions | `label_editorial` | Plus Jakarta Sans, right-aligned annotations |
| Context triggers | `trigger_map` | File pattern to loaded config mapping |
| Roman numerals I-IV | `section_numeral` | Tier identifiers |
| Accent squares on frontend rules | `accent_square` | Highlighting design system rules |
| Cascade arrows | `primary_pathway` | Showing config inheritance flow |
| Footer trigger map | `callout_tip` | Three trigger patterns |

## Anti-Hallucination Rules

1. There are exactly TWO CLAUDE.md files: root `CLAUDE.md` and `.claude/CLAUDE.md`.
2. Rule files are numbered: 00, 01, 05, 10, 11 -- these are the actual filenames.
3. The `.claude/` directory contains: auto-context.yaml, CLAUDE.md, config, domains, golden-paths.md, GUARDRAILS.md, institutional-knowledge, memory, meta-learning, planning, README.md, rules, sessions, settings.json, skills, template-sync.yaml.
4. The skill is "self-learning-iterative-coder" -- a TDD loop skill, not a code generation skill.
5. Context loading triggers are defined in `.claude/CLAUDE.md` in the Context Loading table.
6. Frontend files trigger loading of rules/10-frontend-design-system.md AND rules/11-ux-first-philosophy.md.
7. The mode system has three modes: creation, maintenance, debug -- with different risk tolerances.
8. Current mode is "maintenance" (low risk, max 3 files, max 200 lines).
9. Do NOT show rules that don't exist (no 02, 03, 04, 06, 07, 08, 09 files).
10. The GUARDRAILS.md file exists at `.claude/GUARDRAILS.md` -- include it in the tree.

## Alt Text

Configuration tree showing CLAUDE.md hierarchy: root contract, five numbered domain rules, skills directory, and institutional knowledge layers with context loading triggers.
