#!/usr/bin/env bash
# Pre-commit hook: catch broken Tailwind v4 text-[var(--text-*)] patterns.
# These generate color declarations instead of font-size in Tailwind v4.
# See .claude/memory/css-tailwind-v4-pitfalls.md

set -euo pipefail

if grep -rl 'text-\[var(--text-' frontend/src/ --include="*.tsx" --include="*.ts" --exclude-dir=__tests__ 2>/dev/null; then
  echo "ERROR: Found text-[var(--text-*)] — use Tailwind utilities (text-xl, text-2xl) instead."
  echo "See .claude/memory/css-tailwind-v4-pitfalls.md"
  exit 1
fi
