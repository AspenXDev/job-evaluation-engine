# LLM Prompt Template — Call the Evaluation API

Use this template when you want an LLM to call the local evaluation API (or the `evaluate_from_payload` function) to score a job against a candidate profile.

## Option A — Call the Local HTTP API

> **Precondition:** The API server is running (e.g., `python scripts/api_server.py --host 0.0.0.0 --port 8000`).

Prompt to send as a tool call or in a tool-enabled environment (with an `http.post` tool):

```text
POST http://localhost:8000/evaluate
Content-Type: application/json

{
  "job": {
    "title": "<JOB TITLE>",
    "company": "<COMPANY>",
    "description": "<FULL JOB DESCRIPTION TEXT>"
  },
  "candidate": {
    "profile_id": "<CANDIDATE ID>",
    "raw_text": "<CANDIDATE RESUME OR BACKGROUND TEXT>"
  }
}
```

The response will be a JSON object matching `schemas/evaluation-output.schema.json`.

---

## Option B — Call the Python API Function

If the LLM can execute Python code (e.g., in a notebook or a python tool), use the `evaluate_from_payload` helper.

```python
from api import evaluate_from_payload

payload = {
  "job": {
    "title": "<JOB TITLE>",
    "company": "<COMPANY>",
    "description": "<FULL JOB DESCRIPTION TEXT>"
  },
  "candidate": {
    "profile_id": "<CANDIDATE ID>",
    "raw_text": "<CANDIDATE RESUME OR BACKGROUND TEXT>"
  }
}

result = evaluate_from_payload(payload)
print(result)
```

---

### Notes

- The engine is deterministic; identical inputs produce identical outputs.
- Output conforms to: `schemas/evaluation-output.schema.json`.
