# .claude Directory

This directory contains Claude Code configuration and context files for AI-assisted development.

## Structure

```
.claude/
├── CLAUDE.md              # Main behavior contract
├── auto-context.yaml      # Automatic context loading rules
├── golden-paths.md        # Approved implementation patterns
├── GUARDRAILS.md          # Safety guardrails
├── settings.json          # Hook configuration
├── template-sync.yaml     # Template sync rules
├── config/
│   └── modes.yaml         # Adaptive mode definitions
├── rules/
│   ├── 00-project-context.md
│   ├── 01-code-analysis-ban.md
│   └── 05-source-of-truth.md
├── domains/
│   ├── testing.md
│   └── configuration.md
├── skills/
│   └── commit/SKILL.md
├── sessions/
│   ├── current-session.md
│   └── archive/
├── institutional-knowledge/
└── planning/
```

## Purpose

- **CLAUDE.md**: Main behavior contract defining what AI can/cannot do
- **auto-context.yaml**: Rules for automatically loading context based on file patterns
- **rules/**: Domain-specific rules that get injected based on context
- **domains/**: Technical domain documentation
- **skills/**: Reusable skill definitions for common tasks
- **sessions/**: Session tracking for continuity across conversations
