# Lattice Scoring Model Specification

## Purpose

The lattice scoring model provides a structured framework for evaluating job roles across multiple capability dimensions.

Instead of reducing a role to a single score, the system evaluates roles within a **multidimensional capability space**.  
Each dimension represents a type of cognitive or operational demand required by the role.

The resulting representation forms a **capability profile** that can be used for comparison, benchmarking, and analysis.

## Capability Dimensions

The lattice model evaluates roles across a predefined set of dimensions.

Examples of capability dimensions include:

- reasoning complexity
- planning and coordination demands
- creativity and problem solving
- operational execution complexity
- task structure and variability

Each dimension captures a different type of requirement present in the job description.

In this repository, the lattice scoring logic is implemented in the engine layer to keep the evaluation pipeline simple and deterministic.

Current implementation details:

- Scoring dimensions are defined in the evaluation engine.
- The scoring logic is implemented in `src/engine/evaluator.py`.
- Normalization is applied in `src/engine/normalization.py`.

### Normalization

Dimension scores are normalized to allow comparison across different job descriptions.

Normalization ensures that:

- scores remain within a consistent scale
- extreme values do not dominate the evaluation
- different job types remain comparable

### Capability Profile

The final evaluation produces a **capability vector** representing the job's position in the capability space.

Example conceptual form:

- Reasoning: 0.72
- Planning: 0.65
- Creativity: 0.48
- Operational Complexity: 0.55
- Coordination: 0.60

This vector represents the role’s location within the multidimensional capability space.

### Downstream Usage

The capability profile can be used for several purposes:

- job comparison
- role benchmarking
- candidate-role matching
- capability gap analysis

### Integration with Evaluation Layer

Capability vectors produced by the lattice model are consumed by the evaluation subsystem.

The evaluation layer performs:

- comparisons across roles
- gap analysis against candidate abilities

Relevant specification:

- specs/evaluation/evaluation-framework.md

### Design Principles

**Multidimensional Evaluation**
Roles are represented as vectors rather than single scores.

**Comparability**
Scores are normalized to support cross-role comparison.

**Determinism**
The scoring logic is deterministic and based on explicit signals.

**Interpretability**
Capability profiles remain human-readable and explainable.
