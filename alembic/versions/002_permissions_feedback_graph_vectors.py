"""Permissions, feedback, graph edges, vector embeddings, audit log.

Revision ID: 002
Revises: 001
Create Date: 2026-02-11
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from pgvector.sqlalchemy import HALFVEC
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "002"
down_revision: str | None = "001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # -- Unique constraint on normalized_records (source, source_id) --
    op.create_unique_constraint(
        "uq_normalized_records_source_source_id",
        "normalized_records",
        ["source", "source_id"],
    )

    # -- Table: permission_bundles (BO-5) --
    op.create_table(
        "permission_bundles",
        sa.Column("permission_id", sa.Uuid(), primary_key=True),
        sa.Column(
            "entity_id",
            sa.Uuid(),
            sa.ForeignKey("resolved_entities.entity_id"),
            nullable=False,
        ),
        sa.Column("scope", sa.String(50), nullable=False),
        sa.Column("scope_entity_id", sa.Uuid(), nullable=True),
        sa.Column("permissions", postgresql.JSONB(), nullable=False),
        sa.Column("effective_from", sa.DateTime(timezone=True), nullable=False),
        sa.Column("effective_until", sa.DateTime(timezone=True), nullable=True),
        sa.Column("delegation_chain", postgresql.JSONB(), server_default="[]"),
        sa.Column("default_permission", sa.String(50), nullable=False),
        sa.Column("created_by", sa.Uuid(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False, server_default="1"),
    )

    # -- Table: feedback_cards (BO-4) --
    op.create_table(
        "feedback_cards",
        sa.Column("feedback_id", sa.Uuid(), primary_key=True),
        sa.Column(
            "attribution_id",
            sa.Uuid(),
            sa.ForeignKey("attribution_records.attribution_id"),
            nullable=False,
        ),
        sa.Column("reviewer_id", sa.String(255), nullable=False),
        sa.Column("reviewer_role", sa.String(50), nullable=False),
        sa.Column("attribution_version", sa.Integer(), nullable=False),
        sa.Column("corrections", postgresql.JSONB(), server_default="[]"),
        sa.Column("overall_assessment", sa.Float(), nullable=False),
        sa.Column("center_bias_flag", sa.Boolean(), server_default="false"),
        sa.Column("free_text", sa.Text(), nullable=True),
        sa.Column("evidence_type", sa.String(50), nullable=False),
        sa.Column("submitted_at", sa.DateTime(timezone=True), nullable=False),
    )

    # -- Table: edges (graph relationships) --
    op.create_table(
        "edges",
        sa.Column("edge_id", sa.Uuid(), primary_key=True),
        sa.Column(
            "from_entity_id",
            sa.Uuid(),
            sa.ForeignKey("resolved_entities.entity_id"),
            nullable=False,
        ),
        sa.Column(
            "to_entity_id",
            sa.Uuid(),
            sa.ForeignKey("resolved_entities.entity_id"),
            nullable=False,
        ),
        sa.Column("relationship_type", sa.String(100), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("metadata", postgresql.JSONB(), server_default="{}"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint(
            "from_entity_id",
            "to_entity_id",
            "relationship_type",
            name="uq_edges_from_to_type",
        ),
    )

    # -- Table: entity_embeddings (pgvector halfvec) --
    op.create_table(
        "entity_embeddings",
        sa.Column("embedding_id", sa.Uuid(), primary_key=True),
        sa.Column(
            "entity_id",
            sa.Uuid(),
            sa.ForeignKey("resolved_entities.entity_id"),
            nullable=False,
        ),
        sa.Column("model_name", sa.String(255), nullable=False),
        sa.Column("model_version", sa.String(100), nullable=False),
        sa.Column("embedding", HALFVEC(768), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint(
            "entity_id",
            "model_name",
            name="uq_entity_embeddings_entity_model",
        ),
    )

    # -- Table: audit_log (permission check trail) --
    op.create_table(
        "audit_log",
        sa.Column("audit_id", sa.Uuid(), primary_key=True),
        sa.Column(
            "permission_id",
            sa.Uuid(),
            sa.ForeignKey("permission_bundles.permission_id"),
            nullable=False,
        ),
        sa.Column("requester_id", sa.String(255), nullable=False),
        sa.Column("requester_type", sa.String(100), nullable=False),
        sa.Column("permission_type", sa.String(50), nullable=False),
        sa.Column("result", sa.String(50), nullable=False),
        sa.Column("request_context", postgresql.JSONB(), server_default="{}"),
        sa.Column("checked_at", sa.DateTime(timezone=True), nullable=False),
    )

    # ── Full-text search indexes (GIN on tsvector) ──
    op.execute(
        "CREATE INDEX ix_normalized_records_fts "
        "ON normalized_records USING gin (to_tsvector('english', canonical_name))"
    )
    op.execute(
        "CREATE INDEX ix_resolved_entities_fts ON resolved_entities USING gin (to_tsvector('english', canonical_name))"
    )

    # ── JSONB GIN indexes ──
    op.create_index(
        "ix_normalized_records_identifiers_gin",
        "normalized_records",
        ["identifiers"],
        postgresql_using="gin",
    )
    op.create_index(
        "ix_normalized_records_metadata_gin",
        "normalized_records",
        ["metadata"],
        postgresql_using="gin",
    )
    op.create_index(
        "ix_resolved_entities_identifiers_gin",
        "resolved_entities",
        ["identifiers"],
        postgresql_using="gin",
    )

    # ── Graph edge indexes ──
    op.create_index(
        "ix_edges_from_type",
        "edges",
        ["from_entity_id", "relationship_type"],
    )
    op.create_index(
        "ix_edges_to_type",
        "edges",
        ["to_entity_id", "relationship_type"],
    )

    # ── Permission + audit indexes ──
    op.create_index(
        "ix_permission_bundles_entity_id",
        "permission_bundles",
        ["entity_id"],
    )
    op.create_index(
        "ix_audit_log_perm_time",
        "audit_log",
        ["permission_id", "checked_at"],
    )

    # ── Feedback index ──
    op.create_index(
        "ix_feedback_cards_attribution_id",
        "feedback_cards",
        ["attribution_id"],
    )

    # ── Attribution query indexes ──
    op.create_index(
        "ix_attribution_records_needs_review",
        "attribution_records",
        ["needs_review"],
    )
    op.create_index(
        "ix_attribution_records_confidence",
        "attribution_records",
        ["confidence_score"],
    )


def downgrade() -> None:
    # Drop indexes first (those on tables we're about to drop are auto-dropped)
    op.drop_index("ix_attribution_records_confidence", table_name="attribution_records")
    op.drop_index("ix_attribution_records_needs_review", table_name="attribution_records")
    op.drop_index("ix_feedback_cards_attribution_id", table_name="feedback_cards")
    op.drop_index("ix_audit_log_perm_time", table_name="audit_log")
    op.drop_index("ix_permission_bundles_entity_id", table_name="permission_bundles")
    op.drop_index("ix_edges_to_type", table_name="edges")
    op.drop_index("ix_edges_from_type", table_name="edges")
    op.drop_index("ix_resolved_entities_identifiers_gin", table_name="resolved_entities")
    op.drop_index("ix_normalized_records_metadata_gin", table_name="normalized_records")
    op.drop_index("ix_normalized_records_identifiers_gin", table_name="normalized_records")
    op.execute("DROP INDEX IF EXISTS ix_resolved_entities_fts")
    op.execute("DROP INDEX IF EXISTS ix_normalized_records_fts")

    # Drop new tables in reverse FK order
    op.drop_table("audit_log")
    op.drop_table("entity_embeddings")
    op.drop_table("edges")
    op.drop_table("feedback_cards")
    op.drop_table("permission_bundles")

    # Remove unique constraint added to normalized_records
    op.drop_constraint(
        "uq_normalized_records_source_source_id",
        "normalized_records",
        type_="unique",
    )
