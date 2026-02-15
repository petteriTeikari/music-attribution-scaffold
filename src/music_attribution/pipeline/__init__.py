"""Pipeline orchestration: declarative DAG and generic runner.

Defines the 5-stage attribution pipeline as a Pydantic model (the DAG
is *data*, not imperative code) with a generic runner that validates
and executes stages in topological order.

The separation of "what" (DAG definition) from "how" (execution engine)
enables the same pipeline definition to be executed by a simple
sequential runner, Prefect, Dagster, or any future orchestrator.

Submodules
----------
dag
    ``PipelineStage`` and ``PipelineDAG`` Pydantic models, plus the
    canonical ``ATTRIBUTION_DAG`` instance defining the 5-stage
    pipeline: ETL -> Entity Resolution -> Attribution -> API/MCP -> Chat.
runner
    ``PipelineRunner`` with ``validate()`` and ``dry_run()`` methods.

See Also
--------
music_attribution.pipeline.dag.ATTRIBUTION_DAG : Canonical pipeline definition.
"""

from __future__ import annotations
