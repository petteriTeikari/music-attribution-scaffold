"""Tests for declarative pipeline DAG (P2-1).

Validates the 5-stage pipeline architecture is represented as a
declarative Pydantic model with dependency validation, topological
sort, and acyclicity checking.
"""

from __future__ import annotations

import pytest


class TestPipelineDAGModel:
    """Tests for the declarative pipeline DAG definition."""

    def test_dag_model_has_five_stages(self) -> None:
        """The attribution pipeline DAG defines exactly 5 stages."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        assert len(ATTRIBUTION_DAG.stages) == 5

    def test_dag_stage_names(self) -> None:
        """The 5 stages match the documented pipeline architecture."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        names = {s.name for s in ATTRIBUTION_DAG.stages}
        expected = {"etl", "entity_resolution", "attribution", "api", "chat"}
        assert names == expected

    def test_dag_is_acyclic(self) -> None:
        """The DAG passes acyclicity validation."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        # Should not raise
        ATTRIBUTION_DAG.validate_acyclic()

    def test_dag_stages_have_correct_dependencies(self) -> None:
        """Each stage declares its upstream dependencies."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        stage_map = {s.name: s for s in ATTRIBUTION_DAG.stages}

        # ETL has no dependencies (entry point)
        assert stage_map["etl"].depends_on == []

        # Entity resolution depends on ETL
        assert "etl" in stage_map["entity_resolution"].depends_on

        # Attribution depends on entity resolution
        assert "entity_resolution" in stage_map["attribution"].depends_on

        # API depends on attribution
        assert "attribution" in stage_map["api"].depends_on

        # Chat depends on API (agent uses API endpoints)
        assert "api" in stage_map["chat"].depends_on

    def test_dag_topological_sort_order(self) -> None:
        """Topological sort respects dependency ordering."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        order = ATTRIBUTION_DAG.topological_sort()
        names = [s.name for s in order]

        # ETL must come before entity_resolution
        assert names.index("etl") < names.index("entity_resolution")
        # Entity resolution must come before attribution
        assert names.index("entity_resolution") < names.index("attribution")
        # Attribution must come before API
        assert names.index("attribution") < names.index("api")
        # API must come before chat
        assert names.index("api") < names.index("chat")

    def test_dag_stage_io_types_defined(self) -> None:
        """Each stage declares input/output type names for documentation."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        for stage in ATTRIBUTION_DAG.stages:
            assert stage.output_type is not None, f"Stage {stage.name} missing output_type"

    def test_dag_cycle_detection_raises(self) -> None:
        """A DAG with a cycle raises ValueError on validation."""
        from music_attribution.pipeline.dag import PipelineDAG, PipelineStage

        cyclic = PipelineDAG(
            name="cyclic_test",
            stages=[
                PipelineStage(
                    name="a",
                    description="Stage A",
                    depends_on=["b"],
                    module_path="x",
                    output_type="X",
                ),
                PipelineStage(
                    name="b",
                    description="Stage B",
                    depends_on=["a"],
                    module_path="y",
                    output_type="Y",
                ),
            ],
        )
        with pytest.raises(ValueError, match="cycle"):
            cyclic.validate_acyclic()


class TestPipelineRunner:
    """Tests for the generic DAG runner."""

    def test_runner_validates_acyclicity(self) -> None:
        """Runner validates DAG is acyclic before execution."""
        from music_attribution.pipeline.runner import PipelineRunner

        runner = PipelineRunner()
        # Should not raise for the valid attribution DAG
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG

        runner.validate(ATTRIBUTION_DAG)

    def test_runner_dry_run_returns_stage_order(self) -> None:
        """Dry run returns the execution plan without running stages."""
        from music_attribution.pipeline.dag import ATTRIBUTION_DAG
        from music_attribution.pipeline.runner import PipelineRunner

        runner = PipelineRunner()
        plan = runner.dry_run(ATTRIBUTION_DAG)
        assert len(plan) == 5
        assert plan[0] == "etl"
        assert plan[-1] == "chat"
