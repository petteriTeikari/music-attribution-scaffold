# ADR-0002: Pure Markdown Documentation

## Status

Accepted

## Context

Documentation format choice impacts:
- Claude Code's ability to read and update docs
- Developer experience when writing and reviewing
- Rendering across different platforms (GitHub, IDEs, docs sites)

Options considered:
1. **LaTeX**: Rich formatting, academic standard
2. **reStructuredText**: Python ecosystem standard
3. **Markdown**: Simple, universal support

## Decision

Use pure Markdown (GitHub-flavored) for all documentation. No LaTeX.

## Consequences

### Positive

- **Claude Code native**: Direct consumption without parsing
- **Simple tooling**: No compilation step required
- **Universal rendering**: GitHub, VS Code, any markdown viewer
- **Diff-friendly**: Meaningful version control diffs
- **RAG-optimized**: Clean text for embedding and retrieval

### Negative

- **Limited math notation**: Must use code blocks or Unicode for formulas
- **No complex layouts**: Tables and diagrams are basic

### Mitigations

- Use Mermaid diagrams (GitHub-rendered) for visual documentation
- Use code blocks for mathematical expressions where needed
- Complex visualizations can link to external images
