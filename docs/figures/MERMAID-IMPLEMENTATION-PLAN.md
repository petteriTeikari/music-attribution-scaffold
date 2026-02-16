# Mermaid Diagram Implementation Plan

## Overview

Systematic addition of Mermaid diagrams across documentation, from domain (L2) to implementation (L4).

## Diagram Inventory

### L2: Solution Overview (PRDs)

| ID | Document | Diagram | Type | Status |
|----|----------|---------|------|--------|
| L2-01 | vision-v1.md | User Persona Flow | flowchart | Planned |
| L2-02 | vision-v1.md | Platform Ecosystem | flowchart | Planned |
| L2-03 | attribution-engine-prd.md | Pipeline Overview | flowchart | Replace ASCII |
| L2-04 | mcp-server-prd.md | Trust Tier Model | flowchart | Planned |
| L2-05 | mcp-server-prd.md | Tool Architecture | flowchart | Planned |
| L2-06 | chat-interface-prd.md | Conversation Flow | flowchart | Replace ASCII |

### L3: Technical Architecture (docs/architecture/)

| ID | Document | Diagram | Type | Status |
|----|----------|---------|------|--------|
| L3-01 | README.md | System Architecture | flowchart | Exists (update styling) |
| L3-02 | README.md | Entity Resolution Sequence | sequence | Planned |
| L3-03 | README.md | Database Schema | erDiagram | Planned |
| L3-04 | README.md | MCP Request Flow | sequence | Planned |

### L4: Implementation Details (docs/architecture/)

| ID | Document | Diagram | Type | Status |
|----|----------|---------|------|--------|
| L4-01 | README.md | Confidence Scoring Algorithm | flowchart | Planned |
| L4-02 | README.md | Attribution Level Transitions | stateDiagram | Planned |

## Implementation Order

1. **Phase 1**: PRD diagrams (L2-01 to L2-06)
2. **Phase 2**: Architecture diagrams (L3-01 to L3-04)
3. **Phase 3**: Implementation diagrams (L4-01 to L4-02)

## Standard Init Block

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'background': '#fcfaf5',
    'primaryColor': '#1E3A5F',
    'primaryTextColor': '#ffffff',
    'primaryBorderColor': '#1E3A5F',
    'secondaryColor': '#2E7D7B',
    'tertiaryColor': '#D4A03C',
    'lineColor': '#333333',
    'textColor': '#2C2C2C'
  }
}}%%
```
