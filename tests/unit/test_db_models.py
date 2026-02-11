"""Tests for ORM models: existing + new tables (permissions, feedback, edges, embeddings, audit)."""

from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class TestAllModelsShareBase:
    """Verify all models inherit from the same Base."""

    def test_all_models_share_base(self) -> None:
        """Every ORM model inherits from db.models.Base."""
        from music_attribution.db.models import (
            AttributionRecordModel,
            AuditLogModel,
            Base,
            EdgeModel,
            EntityEmbeddingModel,
            FeedbackCardModel,
            NormalizedRecordModel,
            PermissionBundleModel,
            ResolvedEntityModel,
        )

        models = [
            NormalizedRecordModel,
            ResolvedEntityModel,
            AttributionRecordModel,
            PermissionBundleModel,
            FeedbackCardModel,
            EdgeModel,
            EntityEmbeddingModel,
            AuditLogModel,
        ]

        for model in models:
            assert issubclass(model, Base), f"{model.__name__} does not inherit from Base"
            assert issubclass(model, DeclarativeBase), f"{model.__name__} not a DeclarativeBase"


class TestPermissionBundleModel:
    """Tests for PermissionBundleModel."""

    def test_permission_bundle_model_columns(self) -> None:
        """PermissionBundleModel has all BO-5 fields mapped."""
        from music_attribution.db.models import PermissionBundleModel

        table = PermissionBundleModel.__table__
        column_names = {c.name for c in table.columns}

        expected = {
            "permission_id",
            "entity_id",
            "scope",
            "scope_entity_id",
            "permissions",
            "effective_from",
            "effective_until",
            "delegation_chain",
            "default_permission",
            "created_by",
            "updated_at",
            "version",
        }
        assert expected.issubset(column_names), f"Missing columns: {expected - column_names}"

    def test_permission_bundle_primary_key(self) -> None:
        """Primary key is permission_id."""
        from music_attribution.db.models import PermissionBundleModel

        pk_cols = [c.name for c in PermissionBundleModel.__table__.primary_key.columns]
        assert pk_cols == ["permission_id"]

    def test_permission_bundle_tablename(self) -> None:
        """Table name is permission_bundles."""
        from music_attribution.db.models import PermissionBundleModel

        assert PermissionBundleModel.__tablename__ == "permission_bundles"


class TestFeedbackCardModel:
    """Tests for FeedbackCardModel."""

    def test_feedback_card_model_columns(self) -> None:
        """FeedbackCardModel has all BO-4 fields mapped."""
        from music_attribution.db.models import FeedbackCardModel

        table = FeedbackCardModel.__table__
        column_names = {c.name for c in table.columns}

        expected = {
            "feedback_id",
            "attribution_id",
            "reviewer_id",
            "reviewer_role",
            "attribution_version",
            "corrections",
            "overall_assessment",
            "center_bias_flag",
            "free_text",
            "evidence_type",
            "submitted_at",
        }
        assert expected.issubset(column_names), f"Missing columns: {expected - column_names}"

    def test_feedback_card_primary_key(self) -> None:
        """Primary key is feedback_id."""
        from music_attribution.db.models import FeedbackCardModel

        pk_cols = [c.name for c in FeedbackCardModel.__table__.primary_key.columns]
        assert pk_cols == ["feedback_id"]


class TestEdgeModel:
    """Tests for EdgeModel (graph edges)."""

    def test_edge_model_columns(self) -> None:
        """EdgeModel has from/to entity_id, relationship_type, confidence."""
        from music_attribution.db.models import EdgeModel

        table = EdgeModel.__table__
        column_names = {c.name for c in table.columns}

        expected = {
            "edge_id",
            "from_entity_id",
            "to_entity_id",
            "relationship_type",
            "confidence",
            "metadata",
            "created_at",
        }
        assert expected.issubset(column_names), f"Missing columns: {expected - column_names}"

    def test_edge_unique_constraint(self) -> None:
        """Unique constraint on (from_entity_id, to_entity_id, relationship_type)."""
        from music_attribution.db.models import EdgeModel

        constraints = EdgeModel.__table__.constraints
        unique_constraints = [c for c in constraints if hasattr(c, "columns") and len(c.columns) == 3]
        assert len(unique_constraints) >= 1, "Missing unique constraint on edge triple"


class TestEntityEmbeddingModel:
    """Tests for EntityEmbeddingModel."""

    def test_entity_embedding_model_columns(self) -> None:
        """EntityEmbeddingModel has entity_id, model_name, embedding."""
        from music_attribution.db.models import EntityEmbeddingModel

        table = EntityEmbeddingModel.__table__
        column_names = {c.name for c in table.columns}

        expected = {
            "embedding_id",
            "entity_id",
            "model_name",
            "model_version",
            "embedding",
            "created_at",
        }
        assert expected.issubset(column_names), f"Missing columns: {expected - column_names}"

    def test_entity_embedding_unique_constraint(self) -> None:
        """Unique constraint on (entity_id, model_name)."""
        from music_attribution.db.models import EntityEmbeddingModel

        constraints = EntityEmbeddingModel.__table__.constraints
        unique_constraints = [
            c
            for c in constraints
            if hasattr(c, "columns")
            and len(c.columns) == 2
            and {col.name for col in c.columns} == {"entity_id", "model_name"}
        ]
        assert len(unique_constraints) == 1, "Missing unique constraint on (entity_id, model_name)"


class TestAuditLogModel:
    """Tests for AuditLogModel."""

    def test_audit_log_model_columns(self) -> None:
        """AuditLogModel has requester, result, context."""
        from music_attribution.db.models import AuditLogModel

        table = AuditLogModel.__table__
        column_names = {c.name for c in table.columns}

        expected = {
            "audit_id",
            "permission_id",
            "requester_id",
            "requester_type",
            "permission_type",
            "result",
            "request_context",
            "checked_at",
        }
        assert expected.issubset(column_names), f"Missing columns: {expected - column_names}"
