This directory contains configuration files that control how the
Job Evaluation Engine behaves.

These files allow tuning the system without modifying code.

Contents:

default_config.yaml
Global system settings.

lattice_weights.yaml
Weighting for each dimension in the Lattice scoring model.

benchmark_profiles.yaml
Defines benchmark configurations used during evaluation runs.

Rules:

- Configuration files must be YAML.
- Do not store datasets here.
- Do not store code here.
