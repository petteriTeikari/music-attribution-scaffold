"""Initial schema — boundary object tables.

Revision ID: 001
Revises: None
Create Date: 2026-02-10
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "normalized_records",
        sa.Column("record_id", sa.Uuid(), primary_key=True),
        sa.Column("schema_version", sa.String(20), server_default="1.0.0"),
        sa.Column("source", sa.String(50), nullable=False),
        sa.Column("source_id", sa.String(255), nullable=False),
        sa.Column("entity_type", sa.String(50), nullable=False),
        sa.Column("canonical_name", sa.Text(), nullable=False),
        sa.Column("alternative_names", postgresql.JSONB(), server_default="[]"),
        sa.Column("identifiers", postgresql.JSONB(), server_default="{}"),
        sa.Column("metadata", postgresql.JSONB(), server_default="{}"),
        sa.Column("relationships", postgresql.JSONB(), server_default="[]"),
        sa.Column("fetch_timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("source_confidence", sa.Float(), nullable=False),
        sa.Column("raw_payload", postgresql.JSONB(), nullable=True),
    )

    op.create_table(
        "resolved_entities",
        sa.Column("entity_id", sa.Uuid(), primary_key=True),
        sa.Column("schema_version", sa.String(20), server_default="1.0.0"),
        sa.Column("entity_type", sa.String(50), nullable=False),
        sa.Column("canonical_name", sa.Text(), nullable=False),
        sa.Column("alternative_names", postgresql.JSONB(), server_default="[]"),
        sa.Column("identifiers", postgresql.JSONB(), server_default="{}"),
        sa.Column("source_records", postgresql.JSONB(), nullable=False),
        sa.Column("resolution_method", sa.String(50), nullable=False),
        sa.Column("resolution_confidence", sa.Float(), nullable=False),
        sa.Column("resolution_details", postgresql.JSONB(), server_default="{}"),
        sa.Column("assurance_level", sa.String(20), nullable=False),
        sa.Column("relationships", postgresql.JSONB(), server_default="[]"),
        sa.Column("conflicts", postgresql.JSONB(), server_default="[]"),
        sa.Column("needs_review", sa.Boolean(), server_default="false"),
        sa.Column("review_reason", sa.Text(), nullable=True),
        sa.Column("merged_from", postgresql.JSONB(), nullable=True),
        sa.Column("resolved_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        "attribution_records",
        sa.Column("attribution_id", sa.Uuid(), primary_key=True),
        sa.Column("schema_version", sa.String(20), server_default="1.0.0"),
        sa.Column("work_entity_id", sa.Uuid(), nullable=False),
        sa.Column("credits", postgresql.JSONB(), nullable=False),
        sa.Column("assurance_level", sa.String(20), nullable=False),
        sa.Column("confidence_score", sa.Float(), nullable=False),
        sa.Column("conformal_set", postgresql.JSONB(), nullable=False),
        sa.Column("source_agreement", sa.Float(), nullable=False),
        sa.Column("provenance_chain", postgresql.JSONB(), server_default="[]"),
        sa.Column("needs_review", sa.Boolean(), server_default="false"),
        sa.Column("review_priority", sa.Float(), server_default="0.0"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False, server_default="1"),
    )

    # Indexes for common queries
    op.create_index("ix_normalized_records_source", "normalized_records", ["source"])
    op.create_index("ix_normalized_records_entity_type", "normalized_records", ["entity_type"])
    op.create_index("ix_normalized_records_source_id", "normalized_records", ["source", "source_id"])
    op.create_index("ix_resolved_entities_entity_type", "resolved_entities", ["entity_type"])
    op.create_index("ix_resolved_entities_assurance_level", "resolved_entities", ["assurance_level"])
    op.create_index("ix_attribution_records_work_entity_id", "attribution_records", ["work_entity_id"])


def downgrade() -> None:
    op.drop_table("attribution_records")
    op.drop_table("resolved_entities")
    op.drop_table("normalized_records")
