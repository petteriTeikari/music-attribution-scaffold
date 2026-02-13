# fig-choice-12: Why Alembic for Migrations?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-12 |
| **Title** | Why Alembic for Migrations? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/planning/ |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the database migration strategy. The scaffold uses Alembic (SQLAlchemy-native) because it integrates directly with the SQLAlchemy models used for data access. This avoids the impedance mismatch of Django migrations (which require Django ORM) or manual SQL scripts (which have no version tracking).

The key message is: "Alembic provides SQLAlchemy-native migration management -- the same model definitions drive both data access and schema evolution."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY ALEMBIC FOR MIGRATIONS?                                   |
|  ■ SQLAlchemy-Native Schema Evolution                          |
+---------------------------------------------------------------+
|                                                                |
|  MODEL-MIGRATION ALIGNMENT                                     |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  SQLAlchemy Model ──── autogenerate ────> Alembic       │   |
|  │  (class Attribution)    alembic revision    Migration    │   |
|  │                         --autogenerate      (version)    │   |
|  │                                                         │   |
|  │  Same model definition drives BOTH:                     │   |
|  │  1. Runtime data access (queries, inserts)              │   |
|  │  2. Schema migrations (ALTER TABLE, CREATE INDEX)       │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ ALEMBIC      │ │ DJANGO       │ │ MANUAL SQL   │          |
|  │ ■ SELECTED   │ │ MIGRATIONS   │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ SQLAlchemy-  │ │ Django ORM   │ │ No ORM       │          |
|  │ native       │ │ required     │ │ dependency   │          |
|  │              │ │              │ │              │          |
|  │ Autogenerate │ │ Auto-detect  │ │ Manual diff  │          |
|  │ from models  │ │ from models  │ │              │          |
|  │              │ │              │ │              │          |
|  │ Version      │ │ Version      │ │ No version   │          |
|  │ chain        │ │ numbering    │ │ tracking     │          |
|  │              │ │              │ │              │          |
|  │ Up + Down    │ │ Up + Down    │ │ Up only      │          |
|  │ migrations   │ │ (sometimes)  │ │ (usually)    │          |
|  │              │ │              │ │              │          |
|  │ Works with   │ │ Requires     │ │ Any database │          |
|  │ FastAPI      │ │ Django       │ │              │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Directory: alembic/ (versions tracked in git)                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY ALEMBIC FOR MIGRATIONS?" with coral accent square |
| Model-migration alignment diagram | `data_flow` | SQLAlchemy model to Alembic migration autogeneration |
| Alembic card | `selected_option` | SQLAlchemy-native, autogenerate, version chain, up+down |
| Django Migrations card | `deferred_option` | Requires Django ORM, not compatible with FastAPI |
| Manual SQL card | `deferred_option` | No version tracking, no autogeneration |
| Directory footer | `callout_bar` | alembic/ directory location |

## Anti-Hallucination Rules

1. The scaffold uses Alembic for database migrations -- the `alembic/` directory exists in the project.
2. Alembic autogeneration compares SQLAlchemy model definitions to the current database schema.
3. The scaffold uses SQLAlchemy (not Django ORM) for data access.
4. Alembic migrations are version-controlled in git.
5. Django migrations are NOT compatible with FastAPI without the full Django framework.
6. The scaffold uses FastAPI, not Django -- this is why Alembic (not Django migrations) is the natural choice.
7. Do NOT modify migration files after they have been applied -- per CLAUDE.md rules.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Migration tool comparison showing Alembic selected for SQLAlchemy-native autogeneration, versus Django migrations requiring Django ORM and manual SQL with no versioning.
