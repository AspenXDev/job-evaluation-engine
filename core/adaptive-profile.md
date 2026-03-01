# Adaptive Profile / Behavioral Reconciliation

## Purpose

Enable the engine to adapt user weights based on observed behavior and interactions
with the LLM, without requiring explicit user input for every adjustment.

## Logic

1. For each dimension in `weight_profiles`, compare:
   - Last `N` evaluations
   - User's expressed feedback
   - Trends in selection or reasoning

2. Adjust weights incrementally (e.g., ±0.02 per interaction) toward the direction implied
   by user behavior.

3. Maintain deterministic scoring for reproducibility:
   - Scoring engine uses **updated** weight_profiles.
   - Interaction history remains fully logged.
