# Normalization Specification

This specification defines how raw scoring signals are normalized into a
consistent numeric range.

## Purpose

Normalization ensures that capability scores are comparable across different jobs
and are bounded within predictable ranges.

## Normalization Rules

- All capability scores MUST be normalized to the range **[0.0, 1.0]**.
- Any missing or invalid numeric values MUST be treated as **0.0**.
- NaN values MUST be normalized to **0.0**.

## Scaling

When transforming counts or signal strengths into normalized scores:

1. Determine the raw signal magnitude per dimension (e.g., keyword matches).
2. Optionally scale the raw value relative to a known maximum.
3. Clamp the resulting value to `[0.0, 1.0]`.

The implementation provides helper functions in:

- `src/engine/normalization.py`

## Implementation Notes

The current implementation uses a simple max-based normalization strategy:

- Each dimension score is divided by the largest dimension score in the same job.
- If all signals are absent, the resulting profile is a zero vector.

This approach preserves relative signal strength while enforcing the required range.
