#!/usr/bin/env python3
"""Run the attribution pipeline DAG.

Usage:
    # Dry run — show execution plan without running stages
    uv run python scripts/run-pipeline.py --dry-run

    # Run a specific stage (future: with orchestrator integration)
    uv run python scripts/run-pipeline.py --stage etl

    # Show DAG as JSON
    uv run python scripts/run-pipeline.py --show-dag
"""

from __future__ import annotations

import argparse
import json
import sys

from music_attribution.pipeline.dag import ATTRIBUTION_DAG
from music_attribution.pipeline.runner import PipelineRunner


def main() -> None:
    """Entry point for pipeline execution."""
    parser = argparse.ArgumentParser(description="Music Attribution Pipeline Runner")
    parser.add_argument("--dry-run", action="store_true", help="Show execution plan without running")
    parser.add_argument("--show-dag", action="store_true", help="Print DAG definition as JSON")
    parser.add_argument("--stage", type=str, help="Run a specific stage (future)")
    args = parser.parse_args()

    runner = PipelineRunner()

    if args.show_dag:
        print(json.dumps(ATTRIBUTION_DAG.model_dump(), indent=2))  # noqa: T201
        return

    if args.dry_run or args.stage is None:
        plan = runner.dry_run(ATTRIBUTION_DAG)
        print(f"Pipeline: {ATTRIBUTION_DAG.name}")  # noqa: T201
        print(f"Stages ({len(plan)}):")  # noqa: T201
        for i, name in enumerate(plan, 1):
            stage = next(s for s in ATTRIBUTION_DAG.stages if s.name == name)
            deps = ", ".join(stage.depends_on) if stage.depends_on else "(entry point)"
            print(f"  {i}. {name} [{stage.module_path}] ← {deps}")  # noqa: T201
            print(f"     {stage.input_type or '∅'} → {stage.output_type}")  # noqa: T201
        return

    if args.stage:
        stage_names = {s.name for s in ATTRIBUTION_DAG.stages}
        if args.stage not in stage_names:
            print(f"Unknown stage: {args.stage}. Available: {', '.join(sorted(stage_names))}")  # noqa: T201
            sys.exit(1)
        print("Stage execution not yet implemented. Use --dry-run to see the plan.")  # noqa: T201
        sys.exit(0)


if __name__ == "__main__":
    main()
