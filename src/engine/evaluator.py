"""Evaluation engine that scores job descriptions against a candidate profile."""

from __future__ import annotations

import datetime
import re
from typing import Dict, List, Optional

from .job_representation import (
    CapabilityProfile,
    CandidateProfile,
    EvaluationResult,
    JobDescription,
)
from .normalization import clamp01, normalize_dict_scores, average


_DEFAULT_KEYWORDS = {
    "reasoning": [
        "strateg", "analysis", "complex", "evaluate", "model", "diagnos", "problem",
        "assessment",
    ],
    "planning": [
        "plan", "roadmap", "forecast", "timeline", "strategy", "milestone", "long[- ]term",
    ],
    "creativity": [
        "innovate", "creative", "design", "ideation", "brainstorm", "experiment",
    ],
    "operational_complexity": [
        "process", "operations", "workflow", "execute", "logistics", "implementation",
        "operational", "coordination", "deployment",
    ],
    "coordination": [
        "collaborat", "stakeholder", "cross[- ]functional", "team", "partner", "align",
        "liaison", "communicat", "facilitat",
    ],
}


def _count_keyword_matches(text: str, keywords: List[str]) -> int:
    matches = 0
    lower = text.lower()
    for kw in keywords:
        if re.search(r"\b" + kw + r"\b", lower):
            matches += 1
    return matches


def _score_from_text(text: str, keywords: Dict[str, List[str]]) -> CapabilityProfile:
    """Derive a capability profile from free-form text using keyword heuristics."""
    if not text:
        return CapabilityProfile.zero()

    scores: Dict[str, float] = {}
    total_matches = 0

    for dim, kws in keywords.items():
        count = _count_keyword_matches(text, kws)
        scores[dim] = float(count)
        total_matches += count

    if total_matches == 0:
        return CapabilityProfile.zero()

    # Normalize per-dimension to [0,1] by dividing by max (and clamp)
    max_count = max(scores.values()) or 1
    normalized = {k: clamp01(v / max_count) for k, v in scores.items()}

    return CapabilityProfile(
        reasoning=normalized.get("reasoning", 0.0),
        planning=normalized.get("planning", 0.0),
        creativity=normalized.get("creativity", 0.0),
        operational_complexity=normalized.get("operational_complexity", 0.0),
        coordination=normalized.get("coordination", 0.0),
    )


def _build_job_capability_profile(job: JobDescription) -> CapabilityProfile:
    consolidated = job.consolidated_text()
    return _score_from_text(consolidated, _DEFAULT_KEYWORDS)


def _build_candidate_capability_profile(candidate: CandidateProfile) -> CapabilityProfile:
    if candidate.capability_profile:
        # Accept partial dictionaries; fill missing dims with 0.
        return CapabilityProfile(
            reasoning=clamp01(candidate.capability_profile.get("reasoning", 0.0)),
            planning=clamp01(candidate.capability_profile.get("planning", 0.0)),
            creativity=clamp01(candidate.capability_profile.get("creativity", 0.0)),
            operational_complexity=clamp01(candidate.capability_profile.get("operational_complexity", 0.0)),
            coordination=clamp01(candidate.capability_profile.get("coordination", 0.0)),
        )

    # Fallback: derive from free text in the candidate profile.
    return _score_from_text(candidate.raw_text or "", _DEFAULT_KEYWORDS)


def _compute_gap(job_profile: CapabilityProfile, candidate_profile: CapabilityProfile) -> Dict[str, float]:
    return {
        "reasoning": job_profile.reasoning - candidate_profile.reasoning,
        "planning": job_profile.planning - candidate_profile.planning,
        "creativity": job_profile.creativity - candidate_profile.creativity,
        "operational_complexity": job_profile.operational_complexity - candidate_profile.operational_complexity,
        "coordination": job_profile.coordination - candidate_profile.coordination,
    }


def _compute_alignment_score(gap: Dict[str, float]) -> float:
    # Alignment = 1 - mean(abs(gap))
    abs_gaps = [abs(v) for v in gap.values()]
    return clamp01(1.0 - average(abs_gaps, default=1.0))


def _compute_confidence(job: JobDescription, candidate: CandidateProfile) -> str:
    """Compute a simple confidence level based on input completeness."""
    text = job.consolidated_text()
    length = len(text)
    if length >= 400 and (candidate.capability_profile or (candidate.raw_text and len(candidate.raw_text) > 200)):
        return "HIGH"
    if length >= 200:
        return "MEDIUM"
    return "LOW"


def _generate_summary(
    job: JobDescription,
    job_profile: CapabilityProfile,
    candidate_profile: CapabilityProfile,
    alignment_score: float,
    gap: Dict[str, float],
    confidence: str,
) -> str:
    """Generate a concise summary string describing the evaluation."""
    top_dims = sorted(job_profile.as_dict().items(), key=lambda t: t[1], reverse=True)
    bottom_dims = sorted(job_profile.as_dict().items(), key=lambda t: t[1])

    def dim_list(items):
        return ", ".join([f"{k} ({v:.2f})" for k, v in items[:2]])

    return (
        f"Job capability profile is strongest in {dim_list(top_dims)} and weakest in {dim_list(bottom_dims)}. "
        f"Alignment score is {alignment_score:.2f} (confidence: {confidence}). "
        f"Top gaps: "
        + ", ".join(
            [f"{k}: {v:+.2f}" for k, v in sorted(gap.items(), key=lambda t: abs(t[1]), reverse=True)[:2]]
        )
        + "."
    )


def evaluate_job(job: JobDescription, candidate: CandidateProfile) -> EvaluationResult:
    """Evaluate a job description against a candidate profile."""
    job_profile = _build_job_capability_profile(job)
    candidate_profile = _build_candidate_capability_profile(candidate)

    gap = _compute_gap(job_profile, candidate_profile)
    alignment_score = _compute_alignment_score(gap)
    confidence = _compute_confidence(job, candidate)

    summary = _generate_summary(job, job_profile, candidate_profile, alignment_score, gap, confidence)

    metadata = {
        "evaluation_version": "1.0.0",
        "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "model": None,
        "config_profile": None,
    }

    return EvaluationResult(
        job={
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "source": job.source,
        },
        candidate={
            "profile_id": candidate.profile_id,
        },
        capability_profile=job_profile,
        alignment_score=alignment_score,
        gap_analysis=gap,
        confidence=confidence,
        summary=summary,
        metadata=metadata,
    )
