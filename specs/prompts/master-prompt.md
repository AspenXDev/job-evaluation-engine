# Master Prompt for Job Evaluation

This prompt orchestrates the modular prompt components in this folder.  
It enforces deterministic, traceable evaluation following a "jury instruction" style: evidence drives scoring, each dimension is independent, and output is fully structured.

---

## 1. Load Modular Prompts

At runtime, include the content of these files:

- `system-role.md` → defines AI persona and behavior
- `evaluation-criteria.md` → specifies scoring dimensions and evaluation factors
- `scoring-model.md` → scoring rules, weights, and computation
- `input-instructions.md` → how to read and interpret input data
- `evaluation-protocol.md` → procedural rules (burden of proof, independent deliberation)
- `recruiter-intelligence-prompt.md` → domain-specific context guidance
- `api-calling-template.md` → if interacting with APIs (optional for automation)
- `run-manual.md` → operational instructions for evaluation runs

> The AI **must apply all guidance from these modules**.

---

## 2. Inputs

- `job` → title, company, location, source, etc.
- `candidate` → structured profile, ID, relevant history

> Only use provided inputs. No assumptions or external knowledge.

---

## 3. Dimension Evaluation

Evaluate each dimension **independently**:

1. Scope Clarity
2. Psychological Load Risk
3. Technical Match
4. Operational Structure

For each dimension:

- Apply **burden of proof** (preponderance / clear & convincing evidence where specified).
- Weigh **quality of evidence over quantity**.
- Provide **1–5 traceable evidence statements** justifying the score.
- Assign score (0–5) and confidence (LOW / MEDIUM / HIGH).
- Maintain **separate reasoning per dimension**, no cross-contamination.

---

## 4. Summarize Reasoning

- Combine all dimension reasoning into a concise summary (100–2000 chars).
- Highlight gaps, strengths, and risks.
- Summary should reflect evidence-based conclusions, not assumptions.

---

## 5. Output Generation

- Output must **strictly conform to `evaluation-output.schema.json`**.
- Required fields:

```text
job
candidate
scores (dimension → 0–5)
confidence (LOW / MEDIUM / HIGH)
evidence (dimension → array of strings)
summary
metadata (evaluation_version, timestamp, model)
```
