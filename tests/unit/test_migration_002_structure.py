"""Structural tests for migration 002 — verifiable without a database."""

from __future__ import annotations

import ast
import importlib.util
from pathlib import Path


def _load_migration():
    """Load migration 002 as a module from file path."""
    migration_path = Path("alembic/versions/002_permissions_feedback_graph_vectors.py")
    spec = importlib.util.spec_from_file_location("m002", migration_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestMigration002Structure:
    """Verify migration 002 file structure and revision chain."""

    def test_migration_002_importable(self) -> None:
        """Migration 002 module can be imported and has upgrade/downgrade."""
        m002 = _load_migration()
        assert hasattr(m002, "upgrade")
        assert hasattr(m002, "downgrade")
        assert callable(m002.upgrade)
        assert callable(m002.downgrade)

    def test_migration_002_revision_chain(self) -> None:
        """Migration 002 depends on 001."""
        m002 = _load_migration()
        assert m002.revision == "002"
        assert m002.down_revision == "001"

    def test_migration_002_has_table_operations(self) -> None:
        """Migration 002 creates permission_bundles, feedback_cards, edges, entity_embeddings, audit_log."""
        migration_path = Path("alembic/versions/002_permissions_feedback_graph_vectors.py")
        assert migration_path.exists(), "Migration file does not exist"

        source = migration_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        # Find all string literals that are table names in create_table calls
        table_names_in_source = set()
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and node.value in {"permission_bundles", "feedback_cards", "edges", "entity_embeddings", "audit_log"}
            ):
                table_names_in_source.add(node.value)

        expected = {"permission_bundles", "feedback_cards", "edges", "entity_embeddings", "audit_log"}
        assert expected == table_names_in_source, f"Missing tables: {expected - table_names_in_source}"

    def test_migration_002_creates_indexes(self) -> None:
        """Migration 002 creates all required indexes."""
        migration_path = Path("alembic/versions/002_permissions_feedback_graph_vectors.py")
        source = migration_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        expected_indexes = {
            "ix_normalized_records_fts",
            "ix_resolved_entities_fts",
            "ix_normalized_records_identifiers_gin",
            "ix_normalized_records_metadata_gin",
            "ix_resolved_entities_identifiers_gin",
            "ix_edges_from_type",
            "ix_edges_to_type",
            "ix_permission_bundles_entity_id",
            "ix_audit_log_perm_time",
            "ix_feedback_cards_attribution_id",
            "ix_attribution_records_needs_review",
            "ix_attribution_records_confidence",
        }

        # Find all string literals that contain index names (standalone or in SQL)
        index_names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                val = node.value
                if val.startswith("ix_"):
                    index_names.add(val)
                # Also check for index names embedded in raw SQL strings
                for expected_ix in expected_indexes:
                    if expected_ix in val:
                        index_names.add(expected_ix)

        missing = expected_indexes - index_names
        assert not missing, f"Missing indexes in migration: {missing}"

    def test_migration_002_uses_halfvec(self) -> None:
        """Migration 002 uses pgvector halfvec for embeddings."""
        import ast

        migration_path = Path("alembic/versions/002_permissions_feedback_graph_vectors.py")
        source = migration_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        halfvec_found = any(isinstance(node, ast.Name) and node.id == "HALFVEC" for node in ast.walk(tree))
        assert halfvec_found, "No HALFVEC reference in migration AST"

    def test_alembic_single_head(self) -> None:
        """After adding migration 002, there is still only one head."""
        from alembic.config import Config
        from alembic.script import ScriptDirectory

        cfg = Config()
        cfg.set_main_option("script_location", "alembic")
        script = ScriptDirectory.from_config(cfg)
        heads = script.get_heads()
        assert len(heads) == 1, f"Expected 1 head, got {len(heads)}: {heads}"
