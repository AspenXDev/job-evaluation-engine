# Evaluation Output Schema

This document defines the structured output produced by the Job Evaluation Engine.

The output format is defined by the JSON schema:

- `schemas/evaluation-output.schema.json`

All evaluation runs MUST produce JSON that conforms to this schema.

---

# Design Goals

The schema exists to guarantee:

- Consistent machine-readable evaluation outputs
- Deterministic downstream processing
- Reliable report generation
- Versioned evaluation reproducibility

Outputs must be stable across runs and easy to validate.

---

# High-Level Structure

Each evaluation output contains the following top-level sections:

| Section             | Purpose                                                       |
| ------------------- | ------------------------------------------------------------- |
| `job`               | Information about the evaluated job                           |
| `candidate`         | Candidate profile identifier used in evaluation               |
| `capability_profile`| Capability vector derived from the job description            |
| `evaluation`        | Alignment, gap analysis, and confidence scores                |
| `summary`           | Human-readable evaluation summary                             |
| `metadata`          | Versioning and evaluation runtime metadata                    |

---

# Job Object

Describes the job being evaluated.

Required fields:

- `title` (string)
- `company` (string)

Optional fields:

- `location` (string or null)
- `source` (string or null)

Example:

```json
"job": {
  "title": "Sales Support Executive",
  "company": "Example Trading Pte Ltd",
  "location": "Singapore",
  "source": "https://example.com/job/123"
}
```

---

# Candidate Object

Identifies the candidate profile used during evaluation.

Only the profile identifier is captured in the evaluation output.

Example:

```json
"candidate": {
  "profile_id": "candidate-profile-v1"
}
```

---

# Capability Profile

The capability profile is a multidimensional vector representing the job's demands.

Each dimension is a normalized score between 0.0 and 1.0.

Current dimensions:

- `reasoning`
- `planning`
- `creativity`
- `operational_complexity`
- `coordination`

Example:

```json
"capability_profile": {
  "reasoning": 0.72,
  "planning": 0.65,
  "creativity": 0.48,
  "operational_complexity": 0.55,
  "coordination": 0.60
}
```

---

# Evaluation

The `evaluation` object provides alignment metrics between the job and a candidate profile.

Fields:

- `alignment_score` (0.0–1.0): overall alignment between job demands and candidate capabilities.
- `gap_analysis`: per-dimension difference between job and candidate capability scores.
- `confidence`: evaluation confidence level (`LOW`, `MEDIUM`, `HIGH`).

Example:

```json
"evaluation": {
  "alignment_score": 0.82,
  "gap_analysis": {
    "reasoning": 0.10,
    "planning": -0.05,
    "creativity": 0.12,
    "operational_complexity": 0.00,
    "coordination": -0.08
  },
  "confidence": "HIGH"
}
```

---

# Summary

A concise human-readable interpretation of the evaluation.

The summary should:

- synthesize the scoring results
- highlight risks and strengths
- remain under 2000 characters

---

# Metadata

Metadata enables evaluation reproducibility.

Required fields:

- `evaluation_version`: Version of the scoring model
- `timestamp`: Evaluation runtime timestamp (ISO 8601)

Optional fields:

- `model`: LLM or engine used
- `config_profile`: Configuration profile used

Example:

```json
"metadata": {
  "evaluation_version": "1.0.0",
  "timestamp": "2026-02-28T21:00:00Z",
  "model": "gpt-5.2"
}
```

---

# Schema Governance

Any schema modification must follow:

1. Version bump in `evaluation_version`
2. Schema update
3. Updated example output
4. Updated report generator

This prevents engine outputs from drifting out of compatibility with downstream tools.
