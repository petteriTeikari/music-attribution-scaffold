"""Generic pipeline runner for declarative DAGs.

Validates and executes pipeline stages in topological order.
Currently implements sequential execution; the same DAG model
can be executed by Prefect, Dagster, or other orchestrators
via adapter classes.
"""

from __future__ import annotations

import logging

from music_attribution.pipeline.dag import PipelineDAG

logger = logging.getLogger(__name__)


class PipelineRunner:
    """Generic runner that validates and executes a PipelineDAG.

    The runner is intentionally simple — it validates the DAG and
    provides a dry-run mode. Actual stage execution would be wired
    to real implementations when deploying (or to an orchestrator
    like Prefect/Dagster).
    """

    def validate(self, dag: PipelineDAG) -> None:
        """Validate that the DAG is well-formed and acyclic.

        Args:
            dag: Pipeline DAG to validate.

        Raises:
            ValueError: If the DAG contains cycles or invalid references.
        """
        dag.validate_acyclic()
        logger.info("DAG '%s' validated: %d stages, acyclic", dag.name, len(dag.stages))

    def dry_run(self, dag: PipelineDAG) -> list[str]:
        """Return the execution plan without running any stages.

        Args:
            dag: Pipeline DAG to plan.

        Returns:
            List of stage names in execution order.
        """
        self.validate(dag)
        order = dag.topological_sort()
        stage_names = [s.name for s in order]
        logger.info("Dry run plan: %s", " → ".join(stage_names))
        return stage_names
