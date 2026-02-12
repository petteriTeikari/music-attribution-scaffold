"""Add work_title, artist_name display field columns to attribution_records.

Revision ID: 004
Revises: 003
Create Date: 2026-02-12
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "004"
down_revision: str | None = "003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "attribution_records",
        sa.Column("work_title", sa.String(500), server_default="", nullable=False),
    )
    op.add_column(
        "attribution_records",
        sa.Column("artist_name", sa.String(500), server_default="", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("attribution_records", "artist_name")
    op.drop_column("attribution_records", "work_title")
