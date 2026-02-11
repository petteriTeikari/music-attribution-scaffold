"""Add uncertainty_summary JSONB column to attribution_records.

Revision ID: 003
Revises: 002
Create Date: 2026-02-11
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "003"
down_revision: str | None = "002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "attribution_records",
        sa.Column("uncertainty_summary", postgresql.JSONB(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("attribution_records", "uncertainty_summary")
