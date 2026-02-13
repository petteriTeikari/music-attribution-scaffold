# fig-theory-21: Consent Infrastructure Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-21 |
| **Title** | Consent Infrastructure Architecture |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (code terms, architecture diagram, module references) |
| **Location** | docs/theory/mcp-consent.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the full architecture of the consent infrastructure: how permissions are stored, managed, and queried through the MCP server and FastAPI routes. It answers: "What is the technical architecture for storing and serving consent permissions?"

The key message is: "Consent infrastructure has three layers: the MCP server for machine-to-machine queries, the FastAPI API for human management, and PostgreSQL for durable storage -- all wrapped in the music_attribution package."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  CONSENT INFRASTRUCTURE                                        |
|  ■ Architecture: Store, Manage, Query                          |
+---------------------------------------------------------------+
|                                                                |
|  EXTERNAL CONSUMERS                                            |
|  ──────────────────                                            |
|                                                                |
|  ┌──────────┐  ┌──────────┐  ┌──────────┐                    |
|  │ AI Agent │  │ AI Agent │  │ Web UI   │                    |
|  │ (MCP)    │  │ (MCP)    │  │ (Human)  │                    |
|  └────┬─────┘  └────┬─────┘  └────┬─────┘                    |
|       │              │              │                          |
|       └──────┬───────┘              │                          |
|              │                      │                          |
|              ▼                      ▼                          |
|  ┌──────────────────┐  ┌──────────────────────┐              |
|  │  MCP SERVER       │  │  FASTAPI REST API     │              |
|  │  ─────────        │  │  ─────────────────    │              |
|  │                   │  │                       │              |
|  │  music_attribution│  │  /api/v1/permissions  │              |
|  │  /mcp/server.py   │  │  /api/v1/permissions  │              |
|  │                   │  │    /{work_id}          │              |
|  │  Tools:           │  │                       │              |
|  │  • check_         │  │  Methods:             │              |
|  │    permission     │  │  • GET (read)         │              |
|  │  • list_          │  │  • POST (create)      │              |
|  │    permissions    │  │  • PUT (update)       │              |
|  │  • get_           │  │  • DELETE (revoke)    │              |
|  │    attribution    │  │                       │              |
|  └────────┬─────────┘  └──────────┬────────────┘              |
|           │                       │                            |
|           └───────────┬───────────┘                            |
|                       │                                        |
|                       ▼                                        |
|  ┌─────────────────────────────────────────┐                  |
|  │  PERMISSION STORE                        │                  |
|  │  ────────────────                        │                  |
|  │                                          │                  |
|  │  ┌────────────────┐  ┌───────────────┐  │                  |
|  │  │ permissions     │  │ audit_log      │  │                  |
|  │  │ ──────────     │  │ ─────────     │  │                  |
|  │  │ work_id (ISRC) │  │ timestamp     │  │                  |
|  │  │ use_type       │  │ action        │  │                  |
|  │  │ status         │  │ actor         │  │                  |
|  │  │ conditions     │  │ permission_id │  │                  |
|  │  │ granted_by     │  │ old_value     │  │                  |
|  │  │ expires_at     │  │ new_value     │  │                  |
|  │  └────────────────┘  └───────────────┘  │                  |
|  │                                          │                  |
|  │  PostgreSQL + pgvector                   │                  |
|  └─────────────────────────────────────────┘                  |
|                                                                |
+---------------------------------------------------------------+
|  ■ Two interfaces, one truth: MCP for machines, REST for       |
|    humans, PostgreSQL for durable storage with full audit log. |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "CONSENT INFRASTRUCTURE" with coral accent square |
| Subtitle | `label_editorial` | "Architecture: Store, Manage, Query" |
| AI Agent boxes | `stakeholder_platform` | Two MCP-consuming AI agents |
| Web UI box | `stakeholder_artist` | Human-facing management interface |
| MCP Server module | `api_endpoint` | music_attribution/mcp/server.py with tool names |
| FastAPI REST API | `api_endpoint` | /api/v1/permissions endpoints with HTTP methods |
| MCP tools list | `data_mono` | check_permission, list_permissions, get_attribution |
| REST methods list | `data_mono` | GET, POST, PUT, DELETE |
| Permission Store | `storage_layer` | PostgreSQL database with two tables |
| permissions table | `storage_layer` | Schema: work_id, use_type, status, conditions, granted_by, expires_at |
| audit_log table | `storage_layer` | Schema: timestamp, action, actor, permission_id, old_value, new_value |
| Flow arrows (agents to MCP) | `data_flow` | AI agents connecting to MCP server |
| Flow arrow (UI to REST) | `data_flow` | Web UI connecting to FastAPI |
| Flow arrows (servers to store) | `data_flow` | Both servers connecting to PostgreSQL |
| Footer callout | `callout_box` | "Two interfaces, one truth" -- MCP for machines, REST for humans |

## Anti-Hallucination Rules

1. The MCP server module path is `music_attribution/mcp/server.py` -- do NOT change.
2. The REST API path prefix is `/api/v1/permissions` -- do NOT use a different prefix.
3. MCP tools: check_permission, list_permissions, get_attribution. Do NOT add or rename.
4. REST methods: GET, POST, PUT, DELETE. Standard CRUD. Do NOT add PATCH.
5. Permission table fields: work_id, use_type, status, conditions, granted_by, expires_at. Do NOT add fields.
6. Audit log exists -- every permission change is logged with old and new values.
7. The database is PostgreSQL + pgvector -- do NOT substitute SQLite or other databases.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Architecture diagram with MCP server and FastAPI REST API as two interfaces, both connecting to PostgreSQL permission store with permissions and audit log tables.
