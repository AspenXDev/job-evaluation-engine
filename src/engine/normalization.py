"""Normalization utilities for the evaluation engine."""

from __future__ import annotations

from typing import Dict, Iterable, Optional


def clamp01(value: float) -> float:
    """Clamp a value to the [0.0, 1.0] range."""
    if value is None:
        return 0.0
    try:
        f = float(value)
    except (TypeError, ValueError):
        return 0.0
    if f != f:  # NaN
        return 0.0
    return max(0.0, min(1.0, f))


def normalize_dict_scores(scores: Dict[str, float]) -> Dict[str, float]:
    """Clamp all values in a dict to [0.0, 1.0]."""
    return {k: clamp01(v) for k, v in scores.items()}


def average(values: Iterable[float], default: float = 0.0) -> float:
    """Compute the average of a list of floats, returning default when empty."""
    values_list = [v for v in values if v is not None]
    if not values_list:
        return default
    return sum(values_list) / len(values_list)


def scale_to_01(value: float, min_value: float, max_value: float) -> float:
    """Linearly scale value into [0,1] given an expected min/max range."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return 0.0
    if max_value == min_value:
        return 0.0
    return clamp01((v - min_value) / (max_value - min_value))
