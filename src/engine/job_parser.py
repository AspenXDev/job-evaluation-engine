"""Parsers for job descriptions and candidate profiles."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from .job_representation import CandidateProfile, JobDescription


def parse_job_description(raw: Any) -> JobDescription:
    """Parse a raw job description into a structured JobDescription.

    Accepted input types:
    - dict (preferred): expected keys include title, company, location, source,
      description, responsibilities, requirements.
    - string: treated as the full job text (title/company will be set to 'UNKNOWN').
    """
    if isinstance(raw, JobDescription):
        return raw

    if isinstance(raw, str):
        return JobDescription(title="UNKNOWN", company="UNKNOWN", description=raw)

    if isinstance(raw, dict):
        title = raw.get("title") or raw.get("job_title") or "UNKNOWN"
        company = raw.get("company") or raw.get("employer") or "UNKNOWN"
        return JobDescription(
            title=title,
            company=company,
            location=raw.get("location"),
            source=raw.get("source"),
            description=raw.get("description"),
            responsibilities=raw.get("responsibilities"),
            requirements=raw.get("requirements"),
            additional={k: v for k, v in raw.items() if k not in {
                "title",
                "job_title",
                "company",
                "employer",
                "location",
                "source",
                "description",
                "responsibilities",
                "requirements",
            }},
        )

    raise ValueError(f"Unsupported job description type: {type(raw)}")


def parse_candidate_profile(raw: Any) -> CandidateProfile:
    """Parse raw candidate profile data into a CandidateProfile."""
    if isinstance(raw, CandidateProfile):
        return raw

    if isinstance(raw, str):
        # Assume free-form text
        return CandidateProfile(profile_id="UNKNOWN", raw_text=raw)

    if isinstance(raw, dict):
        profile_id = raw.get("profile_id") or raw.get("id") or "UNKNOWN"
        return CandidateProfile(
            profile_id=profile_id,
            capability_profile=raw.get("capability_profile"),
            weight_profiles=raw.get("weight_profiles"),
            raw_text=raw.get("raw_text") or raw.get("bio") or raw.get("summary"),
        )

    raise ValueError(f"Unsupported candidate profile type: {type(raw)}")


def load_json(path: str) -> Any:
    """Load JSON from a file path."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_job_from_file(path: str) -> JobDescription:
    return parse_job_description(load_json(path))


def load_candidate_from_file(path: str) -> CandidateProfile:
    return parse_candidate_profile(load_json(path))
