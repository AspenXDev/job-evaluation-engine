# Lattice Scoring Model Specification

## 1. Purpose

The Lattice Scoring Model evaluates job roles across multiple capability
dimensions relevant to modern human–AI collaborative work environments.

Each job is represented as a vector in a multi-dimensional capability space.
Dimensions capture distinct aspects of work such as reasoning complexity,
physical demands, or social interaction.

The model produces:

1. A capability vector
2. Family-level scores
3. A global composite score

---

# 2. Formal Model

Let:

J = job description

D = set of capability dimensions

D = {d1, d2, … d10}

Each dimension produces a score:

si ∈ [0,1]

The job capability vector is:

S(J) = [s1, s2, … s10]

---

# 3. Capability Dimensions

## Cognitive

### Reasoning Complexity

Degree of multi-step logical reasoning and abstraction required.

Examples:

- strategic planning
- complex diagnostics
- system modeling

Range:
0.0 = minimal reasoning  
1.0 = extremely complex reasoning

---

### Creativity Requirement

Extent to which the role requires novel thinking, innovation,
or idea generation.

Range:
0.0 = routine tasks  
1.0 = highly creative work

---

### Knowledge Breadth

Breadth of domain knowledge required to perform the job effectively.

Range:
0.0 = narrow domain  
1.0 = broad interdisciplinary knowledge

---

## Decision Environment

### Ambiguity Handling

Degree to which the role requires operating under uncertainty,
incomplete information, or evolving situations.

Range:
0.0 = fully structured environment  
1.0 = highly ambiguous environment

---

### Autonomy Requirement

Level of independent decision-making expected in the role.

Range:
0.0 = tightly supervised  
1.0 = fully autonomous decision authority

---

### Planning Horizon

Time scale of planning and decision impact.

Range:
0.0 = immediate tasks  
1.0 = long-term strategic planning

---

## Operational

### Operational Precision

Degree of accuracy and error sensitivity required.

Range:
0.0 = low precision tolerance  
1.0 = extremely high precision required

---

### Physical Demands

Extent of bodily activity required including lifting, movement,
manual work, or sustained physical effort.

Range:
0.0 = sedentary work  
1.0 = intensive physical labor

---

## Workload

### Cognitive Load

Level of sustained mental effort required.

Includes attention demands, information processing,
and decision intensity.

Range:
0.0 = minimal concentration  
1.0 = extreme sustained mental effort

---

## Social

### Human Interaction Complexity

Degree of interpersonal engagement, negotiation,
or relationship management required.

Range:
0.0 = minimal interaction  
1.0 = highly complex social engagement

---

# 4. Capability Families

Dimensions are grouped into capability families.

Cognitive
Reasoning Complexity
Creativity Requirement
Knowledge Breadth

Decision Environment
Ambiguity Handling
Autonomy Requirement
Planning Horizon

Operational
Operational Precision
Physical Demands

Workload
Cognitive Load

Social
Human Interaction Complexity

---

# 5. Normalization

All dimension scores must fall within the range:

si ∈ [0,1]

Scores outside this range must be normalized:

si_normalized = clamp(si_raw, 0, 1)

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
