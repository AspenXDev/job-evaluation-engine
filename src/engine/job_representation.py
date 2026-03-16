"""Structured representations for job descriptions and candidate profiles."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class JobDescription:
    """Structured view of a job description."""

    title: str
    company: str
    location: Optional[str] = None
    source: Optional[str] = None
    description: Optional[str] = None
    responsibilities: Optional[str] = None
    requirements: Optional[str] = None
    additional: Dict[str, object] = field(default_factory=dict)

    def consolidated_text(self) -> str:
        """Return a single text blob that contains all available job fields."""
        parts = [
            self.title or "",
            self.company or "",
            self.location or "",
            self.source or "",
            self.description or "",
            self.responsibilities or "",
            self.requirements or "",
        ]
        return "\n".join([p.strip() for p in parts if p and p.strip()])


@dataclass
class CandidateProfile:
    """Structured view of a candidate profile."""

    profile_id: str
    capability_profile: Optional[Dict[str, float]] = None
    weight_profiles: Optional[Dict[str, float]] = None
    raw_text: Optional[str] = None


@dataclass
class CapabilityProfile:
    """Capability vector representing a job or candidate."""

    reasoning: float = 0.0
    planning: float = 0.0
    creativity: float = 0.0
    operational_complexity: float = 0.0
    coordination: float = 0.0

    def as_dict(self) -> Dict[str, float]:
        return {
            "reasoning": self.reasoning,
            "planning": self.planning,
            "creativity": self.creativity,
            "operational_complexity": self.operational_complexity,
            "coordination": self.coordination,
        }

    @classmethod
    def zero(cls) -> "CapabilityProfile":
        return cls()


@dataclass
class EvaluationResult:
    """Structured evaluation output that can be serialized to JSON."""

    job: Dict[str, object]
    candidate: Dict[str, object]
    capability_profile: CapabilityProfile
    alignment_score: float
    gap_analysis: Dict[str, float]
    confidence: str
    summary: str
    metadata: Dict[str, object]

    def to_dict(self) -> Dict[str, object]:
        return {
            "job": self.job,
            "candidate": self.candidate,
            "capability_profile": self.capability_profile.as_dict(),
            "evaluation": {
                "alignment_score": self.alignment_score,
                "gap_analysis": self.gap_analysis,
                "confidence": self.confidence,
            },
            "summary": self.summary,
            "metadata": self.metadata,
        }
