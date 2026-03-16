# Lattice Scoring Model Specification

## 1. Purpose

The Lattice Scoring Model produces a structured capability profile for a job role.
It is designed to quantify a job's demands across a small set of interpretable dimensions.

The output is a vector of normalized scores that can be used for:

- role comparison
- candidate-job alignment analysis
- benchmark evaluation

---

## 2. Formal Model

Let:

- **J** be a job description.
- **D** be the set of evaluated capability dimensions.

Each dimension produces a score:

s_i ∈ [0, 1]

The job capability profile is:

S(J) = [s_reasoning, s_planning, s_creativity, s_operational_complexity, s_coordination]

---

## 3. Capability Dimensions

The current implementation evaluates the following dimensions.

### Reasoning

Degree of multi-step analytical reasoning and decision complexity required.

- Signals: strategic framing, diagnostics, modeling, analysis.
- High values indicate roles that require significant cognitive abstraction.

### Planning

Extent of longer-horizon planning, roadmapping, and coordination of multi-step efforts.

- Signals: roadmaps, timelines, strategic plans, cross-functional sequencing.
- High values indicate roles that involve future-focused planning.

### Creativity

Need for idea generation, innovation, and novel problem solving.

- Signals: design, innovation, ideation, experimentation.
- High values indicate roles with open-ended or exploratory work.

### Operational Complexity

Degree of process execution complexity, precision requirements, and operational scale.

- Signals: operations, workflows, logistics, execution, implementation.
- High values indicate roles with complex operational coordination.

### Coordination

Level of interpersonal collaboration and stakeholder management required.

- Signals: cross-functional collaboration, stakeholder engagement, meetings, alignment.
- High values indicate roles with significant social coordination.

---

## 4. Normalization

All scores must be normalized into the range [0.0, 1.0].

In practice, the engine computes a raw signal strength per dimension and normalizes
it to ensure comparability across job descriptions.

Normalization is implemented in:

- `src/engine/normalization.py`

---

## 5. Implementation Mapping

The lattice scoring logic is implemented in:

- `src/engine/evaluator.py` (keyword-based scoring)

This is intentionally lightweight and deterministic, allowing the model to remain
transparent and easy to validate.

---

## 6. Future Extensions

Future iterations may incorporate:

- machine-learned signal extraction
- configurable dimension weights
- multi-source evidence aggregation
- richer job ontology mapping

---

# 6. Family Aggregation

Each family score is calculated as the weighted average
of its dimensions.

Example:

CognitiveScore =
Σ (dimension_score × dimension_weight)

Dimension weights within a family must sum to 1.

---

# 7. Global Aggregation

The overall job capability score is computed as:

GlobalScore =
Σ (family_score × family_weight)

Family weights must sum to 1.

---

# 8. Output Representation

The evaluation engine produces:

- dimension scores
- family scores
- global score

Example structure:

{
"dimension_scores": {...},
"family_scores": {...},
"global_score": 0.62
}

---

# 9. Extensibility

New dimensions may be added if they satisfy:

- conceptual independence
- clear scoring rubric
- bounded score range
- defined family placement

All additions must update:

config/lattice_weights.yaml
schemas/evaluation-output.schema.json
