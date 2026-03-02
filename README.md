# Job Evaluation Engine

A structured decision engine for evaluating job opportunities through stability, scope clarity, and cognitive sustainability.

This repository currently represents Phase 2 of a multi-stage evolution toward a generalized structured evaluation engine integrated and callable through the user's LLM of choice.

---

## Purpose

The Job Evaluation Engine provides:

- Structured analysis of job descriptions
- Weighted scoring across defined dimensions
- Standardized output schema for decision clarity
- Modular design for future CLI and API integration

**Note:** This engine does not search or apply for jobs. It evaluates opportunities based on your profile and interaction history, providing structured clarity for decision-making.

---

---

## Current State

The repository currently provides:

- A deterministic evaluation specification
- A modular scoring model
- JSON schema definitions
- A manual execution interface (`manual-run-v1.md`)

This represents Phase 2 (Wrapped Execution Preparation).

Automation and programmatic scoring will be introduced in later phases.

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

The goal is not prediction. The goal is clarity of trade-offs.  
The engine itself is **stateless**; adaptivity and weight calibration are achieved through the **user profile** and the **LLM interface**, which maintain `interaction_history` and update `weight_profiles` over time while preserving user agency.

The engine is API-first and stateless; adaptivity is achieved through the stateful user profile and LLM interface.

---

## Adaptive Workflow (Corrected)

### 1. Input acquisition

- **Reality:** Job description comes from email.
- **Challenge:** Parsing unstructured email → structured engine input.
- **Solution:**
  - ChatGPT (or another LLM) acts as a parser/translator.
  - User forwards or copy-pastes the job description.
  - LLM extracts key fields: title, responsibilities, reporting lines, scope, ambiguity, compensation indicators.
  - Produces JSON or structured prompt for the engine.

---

### 2. Engine evaluation

- Engine consumes:
  - Job description
  - **Current user profile** (weights + `interaction_history`)
- Outputs **dimension scores, composite score, and risk flags**.

**Example output:**

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

---

## Manual Execution (Phase 1 Engine)

The engine is currently executable in manual mode.

### Steps

1. Open:
   `engine/manual-run-v1.md`

2. Copy the entire file contents.

3. Paste into your LLM (e.g., ChatGPT).

4. Replace:
   - `CANDIDATE PROFILE`
   - `JOB DESCRIPTION`

5. Execute.

The engine will return structured JSON output only.

---

### Important

- The engine is stateless.
- All scoring is rule-based.
- No implicit inference is permitted.
- Heuristics are limited to signal extraction only.

Future phases will provide wrapped execution and programmatic scoring.
