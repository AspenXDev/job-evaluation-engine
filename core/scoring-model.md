# Scoring Model

Each evaluation dimension receives:

- A raw score (0–100)
- A weight (defined in config/default-weights.yaml)

## Final Score Calculation

Final Score = Sum (dimension_score × weight)

Weights must sum to 1.0.

The scoring model is designed to be modular and extensible.
