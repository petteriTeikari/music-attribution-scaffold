# Skills Index

This directory contains skill definitions for common development tasks.

## Available Skills

| Skill | Description | Location |
|-------|-------------|----------|
| commit | Create well-formatted git commits | `commit/SKILL.md` |
| code-review | Review code changes | `code-review/SKILL.md` |
| self-learning-iterative-coder | Self-correcting TDD loop for plan-driven code implementation | `self-learning-iterative-coder/SKILL.md` |
| integrate-prd-research | Integrate research findings into the probabilistic PRD decision network | `integrate-prd-research/SKILL.md` |
| figure-plan-creator | Create and review Nano Banana Pro figure plans with anti-hallucination guardrails | `figure-plan-creator/SKILL.md` |
| figure-processor | Post-generation figure processing — convert PNGs to web-optimized JPEGs, SEO/GEO alt text, pre-wire figure plans | `figure-processor/SKILL.md` |

## Skill Structure

Each skill follows this structure:

```markdown
---
name: skill-name
description: What the skill does
---

# Skill Name

## When to Use
- Use case 1
- Use case 2

## Instructions
Step-by-step instructions for the skill.

## Examples
Concrete examples of the skill in action.

## Guidelines
Best practices and rules to follow.
```

## Creating New Skills

1. Create a new directory under `.claude/skills/`
2. Add a `SKILL.md` file following the template
3. Document when to use the skill
4. Provide concrete examples
