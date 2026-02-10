# Music Attribution Scaffold

Open-source research scaffold for music attribution with transparent confidence scoring.

**Companion code to**: Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Project Type** | library |
| **Language** | Python 3.13 |
| **Package Manager** | uv (ONLY) |
| **Linter/Formatter** | ruff |
| **Type Checker** | mypy |
| **Test Framework** | pytest |

## Critical Rules

1. **uv ONLY** - Never use pip, conda, or requirements.txt
2. **AST ONLY** - For code analysis, use `ast.parse()` not grep/sed/awk/regex
3. **Pre-commit Required** - All changes must pass pre-commit hooks
4. **Encoding** - Always specify `encoding='utf-8'` for file operations
5. **Paths** - Always use `pathlib.Path()` not string concatenation
6. **Timezone** - Always use `datetime.now(timezone.utc)` not `datetime.now()`

## Quick Commands

```bash
# Install dependencies
make install-dev

# Run tests
make test

# Lint and format
make lint
make format

# Type check
make typecheck

# Coverage report
make test-cov
```

## What AI Must NEVER Do

- Modify files marked with `# AIDEV-IMMUTABLE`
- Use pip, conda, or create requirements.txt
- Parse Python code with grep/sed/awk/regex
- Skip pre-commit hooks
- Hardcode file paths
- Use `datetime.now()` without timezone
- Commit secrets or credentials

## Knowledge Base

The `docs/knowledge-base/` directory contains RAG-optimized markdown for LLM consumption.

**Important workflow**:
- Raw sources (PDFs, HTML) go in `raw-sources/` (gitignored)
- Convert to clean markdown before committing
- Use SYNTHESIS.md pattern for aggregation

See [docs/knowledge-base/README.md](docs/knowledge-base/README.md) for details.

## Private Development Context

This scaffold serves dual purposes:

1. **Research companion**: Provides reproducible code for the SSRN preprint on music attribution
2. **CV-driven development**: Demonstrates practical software engineering skills (Python packaging, CI/CD, Docker, testing, documentation architecture) in a domain with genuine research value

The knowledge base, PRDs, and architecture docs showcase the ability to synthesize complex domain knowledge into actionable engineering artifacts. The project structure itself is the deliverable — showing how to scaffold a non-trivial attribution system from research to implementation.

**Remove this section before making the repo public.**

## See Also

- [.claude/CLAUDE.md](.claude/CLAUDE.md) - Detailed behavior contract
- [.claude/golden-paths.md](.claude/golden-paths.md) - Approved patterns
- [.claude/rules/](.claude/rules/) - Domain-specific rules
- [docs/planning/](docs/planning/) - Architecture plans and PRDs
- [SSRN Preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087) - Research paper
