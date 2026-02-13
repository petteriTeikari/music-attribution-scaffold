"""Tests for commercial landscape enums (Tasks B1, B2).

Validates that future-readiness enums for TDA, rights, media, certification,
watermarks, and revenue models exist with correct values, and that
PermissionTypeEnum has fine-grained AI training permissions.
"""

from __future__ import annotations

from enum import StrEnum

from music_attribution.schemas.enums import (
    AssuranceLevelEnum,
    AttributionMethodEnum,
    CalibrationStatusEnum,
    CertificationTypeEnum,
    ConfidenceMethodEnum,
    ConfidenceTrendEnum,
    ConflictSeverityEnum,
    CreditRoleEnum,
    DelegationRoleEnum,
    EntityTypeEnum,
    EvidenceTypeEnum,
    MediaTypeEnum,
    PermissionScopeEnum,
    PermissionTypeEnum,
    PermissionValueEnum,
    PipelineFeedbackTypeEnum,
    ProvenanceEventTypeEnum,
    RelationshipTypeEnum,
    ResolutionMethodEnum,
    RevenueModelEnum,
    ReviewerRoleEnum,
    RightsTypeEnum,
    SourceEnum,
    UncertaintyDimensionEnum,
    UncertaintySourceEnum,
    WatermarkTypeEnum,
)


class TestAttributionMethodEnum:
    """Tests for AttributionMethodEnum (Task B1)."""

    def test_attribution_method_enum_values(self) -> None:
        """Verify all TDA method values exist."""
        expected = {
            "TRAINING_TIME_INFLUENCE",
            "UNLEARNING_BASED",
            "INFLUENCE_FUNCTIONS",
            "EMBEDDING_SIMILARITY",
            "WATERMARK_DETECTION",
            "INFERENCE_TIME_CONDITIONING",
        }
        actual = {e.value for e in AttributionMethodEnum}
        assert expected <= actual, f"Missing values: {expected - actual}"


class TestRightsTypeEnum:
    """Tests for RightsTypeEnum (Task B1)."""

    def test_rights_type_enum_values(self) -> None:
        """Verify all rights type values exist."""
        expected = {
            "MASTER_RECORDING",
            "COMPOSITION_PUBLISHING",
            "PERFORMANCE",
            "MECHANICAL",
            "SYNC",
        }
        actual = {e.value for e in RightsTypeEnum}
        assert expected <= actual, f"Missing values: {expected - actual}"


class TestMediaTypeEnum:
    """Tests for MediaTypeEnum (Task B1)."""

    def test_media_type_enum_values(self) -> None:
        """Verify all media type values exist."""
        expected = {
            "AUDIO",
            "IMAGE",
            "VIDEO",
            "TEXT",
            "SYMBOLIC_MUSIC",
            "MULTIMODAL",
        }
        actual = {e.value for e in MediaTypeEnum}
        assert expected <= actual, f"Missing values: {expected - actual}"


class TestCertificationTypeEnum:
    """Tests for CertificationTypeEnum (Task B1)."""

    def test_certification_type_enum_values(self) -> None:
        """Verify all certification type values exist."""
        expected = {
            "FAIRLY_TRAINED_LICENSED",
            "C2PA_PROVENANCE",
            "EU_AI_ACT_COMPLIANT",
            "CMO_APPROVED",
        }
        actual = {e.value for e in CertificationTypeEnum}
        assert expected <= actual, f"Missing values: {expected - actual}"


class TestWatermarkTypeEnum:
    """Tests for WatermarkTypeEnum (Task B1)."""

    def test_watermark_type_enum_values(self) -> None:
        """Verify all watermark type values exist."""
        expected = {
            "SYNTHID",
            "AUDIOSEAL",
            "WAVMARK",
            "DIGIMARC",
        }
        actual = {e.value for e in WatermarkTypeEnum}
        assert expected <= actual, f"Missing values: {expected - actual}"


class TestRevenueModelEnum:
    """Tests for RevenueModelEnum (Task B1)."""

    def test_revenue_model_enum_values(self) -> None:
        """Verify all revenue model values exist."""
        expected = {
            "FLAT_FEE_UPFRONT",
            "PRO_RATA_MONTHLY",
            "PER_GENERATION",
            "INFLUENCE_BASED",
        }
        actual = {e.value for e in RevenueModelEnum}
        assert expected <= actual, f"Missing values: {expected - actual}"


class TestAllNewEnumsAreStrEnum:
    """Verify all 6 new enums inherit from StrEnum (Task B1)."""

    def test_all_new_enums_are_str_enum(self) -> None:
        """All 6 new enums must be StrEnum subclasses."""
        new_enums = [
            AttributionMethodEnum,
            RightsTypeEnum,
            MediaTypeEnum,
            CertificationTypeEnum,
            WatermarkTypeEnum,
            RevenueModelEnum,
        ]
        for enum_cls in new_enums:
            assert issubclass(enum_cls, StrEnum), f"{enum_cls.__name__} is not a StrEnum"


class TestExistingEnumsUnchanged:
    """Verify existing enums retain their original values (Task B1)."""

    def test_existing_enums_unchanged(self) -> None:
        """Existing enums must still have original values."""
        assert "MUSICBRAINZ" in {e.value for e in SourceEnum}
        assert "RECORDING" in {e.value for e in EntityTypeEnum}
        assert "PERFORMED" in {e.value for e in RelationshipTypeEnum}
        assert "EXACT_ID" in {e.value for e in ResolutionMethodEnum}
        assert "LEVEL_0" in {e.value for e in AssuranceLevelEnum}
        assert "LOW" in {e.value for e in ConflictSeverityEnum}
        assert "PERFORMER" in {e.value for e in CreditRoleEnum}
        assert "FETCH" in {e.value for e in ProvenanceEventTypeEnum}
        assert "ARTIST" in {e.value for e in ReviewerRoleEnum}
        assert "LINER_NOTES" in {e.value for e in EvidenceTypeEnum}
        assert "STREAM" in {e.value for e in PermissionTypeEnum}
        assert "ALLOW" in {e.value for e in PermissionValueEnum}
        assert "CATALOG" in {e.value for e in PermissionScopeEnum}
        assert "OWNER" in {e.value for e in DelegationRoleEnum}
        assert "REFETCH" in {e.value for e in PipelineFeedbackTypeEnum}
        assert "INTRINSIC" in {e.value for e in UncertaintySourceEnum}
        assert "INPUT" in {e.value for e in UncertaintyDimensionEnum}
        assert "SELF_REPORT" in {e.value for e in ConfidenceMethodEnum}
        assert "CALIBRATED" in {e.value for e in CalibrationStatusEnum}
        assert "INCREASING" in {e.value for e in ConfidenceTrendEnum}


class TestPermissionTypeFinegrainedAI:
    """Tests for PermissionTypeEnum fine-grained AI training (Task B2)."""

    def test_permission_type_has_fine_grained_ai(self) -> None:
        """Verify 4 new fine-grained AI training permissions exist."""
        values = {e.value for e in PermissionTypeEnum}
        assert "AI_TRAINING_COMPOSITION" in values
        assert "AI_TRAINING_RECORDING" in values
        assert "AI_TRAINING_STYLE" in values
        assert "DATASET_INCLUSION" in values

    def test_permission_type_keeps_original(self) -> None:
        """Verify original PermissionTypeEnum values still exist."""
        values = {e.value for e in PermissionTypeEnum}
        original = {
            "STREAM",
            "DOWNLOAD",
            "SYNC_LICENSE",
            "AI_TRAINING",
            "VOICE_CLONING",
            "STYLE_LEARNING",
            "LYRICS_IN_CHATBOTS",
            "COVER_VERSIONS",
            "REMIX",
            "SAMPLE",
            "DERIVATIVE_WORK",
        }
        assert original <= values, f"Missing original values: {original - values}"
