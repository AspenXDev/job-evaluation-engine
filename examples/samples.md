# Examples Overview

This folder contains representative examples of inputs, outputs, and user profiles used for testing and demonstration of the Job Evaluation Engine.

All user profile examples are validated against `schemas/user-profile-schema.json`.
This ensures consistency for both default initialization and adaptive interactions.

---

## 1. Candidate Profiles

**File:** `sample-candidate-profile.md`

- Illustrates a structured candidate profile using the template in `inputs/candidate-profile-template.md`.
- Includes personal details, career objectives, and prior experience.

**Purpose:** Used as input to the evaluation engine to simulate real candidate data.

---

## 2. Job Descriptions

**File:** `sample-job-description.md`

- Sample job postings structured according to `inputs/job-description-template.md`.
- Contains key fields such as role, responsibilities, scope, and reporting lines.

**Purpose:** Provides standardized job descriptions for testing engine scoring.

---

## 3. Evaluation Outputs

**File:** `sample-output.json` & `sample-output.md`

- `sample-output.json` shows machine-readable evaluation outputs, including dimension scores, composite score, and risk flags.
- `sample-output.md` provides a human-readable summary of the evaluation results.

**Purpose:** Demonstrates how the engine represents evaluation results in different formats.

---

## 4. User Profiles

**File:** `sample-user-profile.json`

- Default-initialized user profile.
- Contains:
  - `career_phase` (stabilization, growth, transition)
  - `weight_profiles` (risk_tolerance, ambiguity_tolerance, compensation_weight, structure_preference, decision_fatigue_index)
  - Empty `interaction_history`

**Purpose:** Provides a starting point for new users; used to initialize the engine before any interaction.

---

## 5. Adaptive Profile / Stateful Interactions

**File:** `sample-user-profile-interactions.json`

- Shows a stateful user profile with populated `interaction_history`.
- Each interaction includes:
  - `timestamp`
  - `prompt` submitted to the engine/LLM
  - `engine_output` (dimension scores, composite score, risk flags, confidence)
  - `user_feedback` (optional reflections)
- `weight_profiles` subtly update over time based on interaction history.

**Purpose:** Demonstrates how the engine adapts to the user’s behavior while remaining compliant with the unified `user-profile-schema.json`.

**Key Concept:**

- Allows the engine to be **stateful** and **adaptive**, not just stateless scoring.
- Supports behavioral reconciliation: subtle calibration of weights based on observed patterns.
- Maintains long-term psychological stability by adapting internally without confronting the user directly.

---

## 6. Notes

- All examples are intended for **demonstration and testing**.
- They reflect typical usage scenarios for the engine, including both human-readable and machine-readable outputs.
- Use these examples to **validate engine behavior** and **train/illustrate adaptive calibration logic**.
