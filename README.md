# **User Story**

**Role:** Job seeker
**Situation:** Receives a job intro from a recruiter via email
**Goal:** Get consistent clarity and advice from your LLM so you can decide whether to pursue the application
**Constraint:** No friction — you don’t want to manually reformat emails, copy JSON, or wrestle with a separate tool

---

# Breaking Down the Flow

### 1. Input acquisition

- **Current reality:** Job description is in email text.
- **Friction point:** Parsing unstructured email → structured engine input.
  **Solution:**
- ChatGPT (or another LLM) acts as a **parser/translator**:
  - User forwards job description (or copy-pastes email).
  - LLM extracts relevant fields: title, responsibilities, reporting lines, scope, ambiguity, compensation indicators.
  - Produces JSON or structured prompt for engine.

---

### 2️. Engine evaluation

- Engine uses **current user profile** (`weight_profiles` + `interaction_history`) to score the job.
- Provides **dimension scores, composite score, and risk flags**.
  **Output example:**

```text
Composite score: 61/100
Key alignment:
- Structure: 0.78 → high
- Risk: 0.58 → moderate
- Ambiguity: 0.68 → slightly high
Risk flags:
- Undefined reporting lines
- Ambiguous scope
```

---

### 3. Human-readable advice

- ChatGPT translates engine output into **natural-language advice**: - Highlights trade-offs - Contextualizes risk vs your past behavior - Suggests focus areas if you pursue further exploration
  Example:
  > “This role is moderately risky due to undefined reporting lines and some ambiguity. Your preference for structure is high, so you might experience decision fatigue if you pursue this. Consider whether the learning opportunity outweighs these challenges before applying.”

---

### 4️. Feedback loop

- User responds with feedback (short, natural sentence):
  - “Feels too chaotic”
  - “I like the challenge, worth exploring”
- Engine logs this in `interaction_history`.
- Subtle **weight calibration** updates risk tolerance, ambiguity tolerance, etc., for future evaluations.

---

### 5️. Consistency and automation

- After this setup, the workflow is **repeatable for every new job introduction**: 1. Forward / copy-paste job description 2. Ask your LLM for evaluation 3. Receive clear, structured advice aligned with your profile 4. Optionally provide feedback to adapt future evaluations
  No JSON tinkering, no separate CLI — just a **conversational interface with consistent structured evaluation behind the scenes**.

---

# Key Design Implications

1. **Engine must be stateless in isolation but stateful with profile**
   - It doesn’t care about the human narrative directly, only about interaction patterns and feedback.
2. **LLM acts as the interface layer**
   - Converts human input → structured engine input
   - Converts engine output → natural advice
3. **Persistent profile storage**
   - Could be local or cloud-based
   - Holds `weight_profiles` + `interaction_history`
4. **Minimal friction** = product success
   - User doesn’t need to touch JSON
   - Everything happens as part of **conversation + evaluation**

---

# Job Evaluation Engine

A structured decision engine for evaluating job opportunities through stability, scope clarity, and cognitive sustainability.

This repository currently represents Phase 1 of a multi-stage evolution toward a generalized structured evaluation engine.

---

## Purpose

The Job Evaluation Engine provides:

- Structured analysis of job descriptions
- Weighted scoring across defined dimensions
- Standardized output schema for decision clarity
- Modular design for future CLI and API integration

This is not a job search assistant. It is an evaluation engine.

---

## Design Philosophy

This engine by default does not optimize for:

- Prestige
- Title acceleration
- Compensation maximization
- Ego validation

It prioritizes:

- Defined scope
- Clear reporting lines
- Structured environments
- Sustainable workload
- Long-term psychological stability

The goal is not prediction.
The goal is clarity of trade-offs.
The engine adapts weight calibration based on behavioral patterns while preserving user agency.

Engine is API-first, stateful, and adaptive.

---

## When This Engine Is Not Appropriate

- High-risk founder decisions
- Aggressive career acceleration strategies
- Pure compensation optimization
- Situations requiring intuition over structure

---

## Evolution Roadmap

- Phase 1 — Prompt Architecture (Completed)
- Phase 2 — Wrapped Execution (In Progress)
- Phase 3 — Programmatic Scoring Engine (Will leverage adaptive profiles and stateful behavior)
  Phase 4 — Recruiter Intelligence Layer
  Phase 5 — Comparative Portfolio Evaluation

---

## Current Architecture

core/ -> Evaluation logic and scoring specifications

prompts/ -> LLM interaction layer

config/ -> Weight configuration

inputs/ -> Structured templates

examples/ -> Reference usage

src/ -> Reserved for CLI and API implementation

---

## Future Direction

- CLI interface for local execution
- REST API for integration
- Modular scoring engine
- Pluggable evaluation dimensions
- Abstracted evaluation core reusable beyond job contexts

---

## Examples

The `/examples` folder contains representative inputs, outputs, and user profiles used for demonstration and testing of the Job Evaluation Engine.

- **Candidate Profiles:** `sample-candidate-profile.md`
- **Job Descriptions:** `sample-job-description.md`
- **Evaluation Outputs:** `sample-output.json` (machine-readable) and `sample-output.md` (human-readable)
- **Default User Profile:** `sample-user-profile.json` — starter profile for new users
- **Adaptive User Profile:** `sample-user-profile-interactions.json` — demonstrates how `weight_profiles` evolve through interactions, supporting the stateful, adaptive behavior layer.

**Purpose of the Adaptive Profile:**  
The adaptive profile allows the engine to calibrate decision weights over time based on the user’s interaction history with the engine/LLM. This supports **personalized recommendations** while preserving long-term psychological stability and providing clarity on trade-offs.

---

## Sample Run (Adaptive Workflow)

1. **Initialize user** → load `sample-user-profile.json`
2. **Run evaluation** → provide job description + current profile to the engine
3. **Log interaction** → append prompt, engine output, user feedback to `interaction_history`
4. **Adaptive calibration** → subtly adjust `weight_profiles` based on interaction patterns
5. **Save updated profile** → ready for next evaluation

---

## Status

Early architecture foundation (Phase 1).
