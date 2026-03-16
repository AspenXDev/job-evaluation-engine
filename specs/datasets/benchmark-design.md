# Benchmark Design Specification

This document describes how to design benchmark tasks for evaluating the Job Evaluation Engine.

## Purpose

Benchmarks are used to:

- Validate scoring consistency across diverse job types.
- Detect regressions after code changes.
- Compare performance across different evaluation configurations.

## Benchmark Composition

Each benchmark consists of a set of scenarios, each containing:

1. A job description (input)
2. A candidate profile (input)
3. An expected evaluation output (reference)

Benchmarks should cover a range of roles and difficulty levels, such as:

- Highly structured operational roles
- Strategic planning roles
- Creative/innovative roles
- Cross-functional coordination roles

## Benchmark Format

Benchmarks are stored as JSON objects. Each entry should include:

- `id`: unique identifier for the scenario
- `job`: job description object
- `candidate`: candidate profile object
- `expected_output`: evaluation output conforming to `schemas/evaluation-output.schema.json`

Example structure:

```json
{
  "id": "benchmark-001",
  "job": { ... },
  "candidate": { ... },
  "expected_output": { ... }
}
```

## Writing Good Benchmarks

- Provide clear, realistic job descriptions.
- Include both positive and negative indicators for key dimensions.
- Ensure candidate profiles are plausible and cover a range of capability levels.
- Maintain consistent formatting to reduce noise in evaluation comparisons.

## Execution

Benchmark runners should:

1. Load benchmark scenarios.
2. Run the evaluation engine for each scenario.
3. Compare the produced output to the expected output.
4. Report mismatches and summary statistics.

## Location

Benchmark datasets live under `/datasets/benchmark_tasks`.

## Versioning

Benchmark datasets are treated as part of the test suite and should be updated when:

- Scoring logic is intentionally changed.
- New dimensions or output schema fields are added.
- New role categories are introduced.
