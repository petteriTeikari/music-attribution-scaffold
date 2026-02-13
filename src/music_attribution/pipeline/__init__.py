"""Pipeline orchestration: declarative DAG and generic runner.

Defines the 5-stage attribution pipeline as a Pydantic model
(data, not code) with a generic runner that validates and executes
stages in topological order.
"""
