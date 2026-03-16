"""API layer for programmatic and LLM-driven access to the evaluation engine."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from engine.evaluator import evaluate_job
from engine.job_parser import parse_candidate_profile, parse_job_description


def evaluate_from_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate a payload containing `job` and `candidate` objects.

    The payload is expected to be a dict with keys:
      - "job": dict or raw string representing the job description
      - "candidate": dict or raw string representing the candidate profile

    Returns:
      A dict matching the evaluation output schema.
    """

    job_raw = payload.get("job")
    candidate_raw = payload.get("candidate")

    if job_raw is None or candidate_raw is None:
        raise ValueError("Payload must include 'job' and 'candidate' fields.")

    job = parse_job_description(job_raw)
    candidate = parse_candidate_profile(candidate_raw)

    result = evaluate_job(job, candidate)
    return result.to_dict()


def evaluate_from_json(json_str: str) -> Dict[str, Any]:
    """Evaluate a JSON string payload and return structured output."""
    payload = json.loads(json_str)
    return evaluate_from_payload(payload)


def format_output_as_json(output: Dict[str, Any], indent: int = 2) -> str:
    return json.dumps(output, ensure_ascii=False, indent=indent)
