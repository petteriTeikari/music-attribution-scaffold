# mcp -- MCP Permission Patchbay Server

The MCP (Model Context Protocol) server implements the "Permission Patchbay" from the manuscript. It provides machine-readable permission queries that AI platforms can use to determine training rights and attribution requirements for musical works.

## Files

| File | Purpose |
|---|---|
| `server.py` | MCP server with 3 tools for attribution and permission queries |

## Purpose

When an AI platform wants to use a musical work for training, it needs to know:
- Who created this work? (attribution query)
- May I use it for AI training? (permission check)
- What conditions apply? (royalty rate, attribution requirement, territory)

The MCP server answers these questions via structured tool calls, making permission queries as simple as API calls.

## Tools

The `MCPAttributionServer` registers 3 tools via FastMCP:

| Tool | Input | Output | Purpose |
|---|---|---|---|
| `query_attribution` | work_id (UUID string) | AttributionRecord as dict | Look up who created a work, with confidence scores and provenance |
| `check_permission` | entity_id, permission_type | Permission value + conditions | Check if a specific use (AI_TRAINING, VOICE_CLONING, etc.) is allowed |
| `list_permissions` | entity_id | Full permission bundle | List all permissions for an entity (catalog/release/recording/work scope) |

## Permission Types

The server supports 15 permission types from `PermissionTypeEnum`:

- **AI-specific**: AI_TRAINING, AI_TRAINING_COMPOSITION, AI_TRAINING_RECORDING, AI_TRAINING_STYLE, VOICE_CLONING, STYLE_LEARNING, LYRICS_IN_CHATBOTS, DATASET_INCLUSION
- **Traditional**: STREAM, DOWNLOAD, SYNC_LICENSE, COVER_VERSIONS, REMIX, SAMPLE, DERIVATIVE_WORK

## Permission Values

Each permission resolves to one of:

| Value | Meaning |
|---|---|
| `ALLOW` | Permitted without conditions |
| `DENY` | Not permitted |
| `ASK` | Must contact rights holder |
| `ALLOW_WITH_ATTRIBUTION` | Permitted if proper attribution is provided |
| `ALLOW_WITH_ROYALTY` | Permitted with specified royalty rate |

## Usage

```python
from music_attribution.mcp.server import create_mcp_server

server = create_mcp_server()

# Query attribution
result = await server._query_attribution("work-uuid-here")

# Check permission
result = await server._check_permission("entity-uuid", "AI_TRAINING")

# List all permissions
result = await server._list_permissions("entity-uuid")
```

The server can be run as a standalone MCP server or integrated into the FastAPI app. In the current scaffold, attribution and permission data are stored in-memory dictionaries. Production deployments would back these with PostgreSQL via the async repositories.

## Key Design Decisions

- **Machine-readable responses**: All responses are structured dictionaries, not free text. AI platforms can parse responses programmatically.
- **Delegation chains**: `PermissionBundle` includes a `delegation_chain` tracking who granted the permission (owner, manager, label, distributor).
- **Scope levels**: Permissions can be set at CATALOG (all works), RELEASE, RECORDING, or WORK granularity.
- **Temporal validity**: Each permission bundle has `effective_from` and optional `effective_until` dates.
- **TDM reservation**: The system supports `TdmReservationMethodEnum` for EU DSM Directive Art. 4 compliance, including robots.txt, llms.txt, and MCP-native permission queries.

## Connection to Adjacent Pipelines

- **Upstream**: Reads `AttributionRecord` and `PermissionBundle` objects.
- **Complement to REST API**: The MCP server and REST API expose the same data -- MCP for AI platform integration (machine-to-machine), REST for web clients (human-facing).
- **Audit trail**: Permission checks can be logged for compliance (see `permissions/persistence.py`).

## Full API Documentation

See the [API Reference: MCP Server](https://petteriTeikari.github.io/music-attribution-scaffold/api-reference/mcp/) on the documentation site.

## Visual Documentation

![MCP permission patchbay showing machine-readable permission queries for AI training rights](../../../docs/figures/repo-figures/assets/fig-choice-11-mcp-permissions.jpg)
*MCP Permission Patchbay -- machine-readable consent queries for AI training, voice cloning, and derivative works.*
