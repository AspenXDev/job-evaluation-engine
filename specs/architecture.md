# System Architecture (High Level)

This specification describes the high-level architecture of the Job Evaluation Engine.

## Architectural Principles

- **Spec-Driven Development**: All behavior is defined in `/specs`. Implementation must conform to these specifications.
- **Modular Layers**: The system separates concerns across clearly defined layers: input parsing, representation, scoring, evaluation, and output.
- **Determinism**: Evaluation results must be repeatable given the same inputs.
- **Schema Compliance**: All inputs and outputs must conform to JSON schema definitions in `/schemas`.

## Core Components

### Input Layer (Engine)

- Responsible for ingesting and normalizing job descriptions and candidate profiles.
- Produces structured representations used by the scoring subsystem.
- Implemented in: `src/engine/`

### Scoring Layer (Lattice)

- Applies the lattice scoring model to compute a capability profile for a job.
- Produces a normalized vector of dimension scores.
- Implemented in: `src/engine/evaluator.py` (current implementation)

### Evaluation Layer

- Compares job capability profiles against candidate profiles.
- Produces alignment metrics, gap analysis, and confidence estimates.
- Implemented in: `src/evaluation/` (future work) and integrated in the engine pipeline.

### Output Layer

- Formats evaluation results as JSON conforming to `schemas/evaluation-output.schema.json`.
- Provides CLI entrypoints and example outputs.
- Implemented in: `scripts/run_evaluation.py` and `examples/`.

## Execution Flow

1. Inputs are loaded (job + candidate).
2. Engine parses inputs into structured objects.
3. Scoring layer computes a capability profile for the job.
4. Evaluation layer computes alignment, gaps, and confidence.
5. Output is produced in the standardized JSON schema.

## Extension Points

- New scoring dimensions can be added by extending the capability profile and updating the scoring logic.
- Alternate parsing strategies can be added by enhancing `src/engine/job_parser.py`.
- Additional output formats (e.g., CSV, markdown reports) can be built on top of the evaluation output.
