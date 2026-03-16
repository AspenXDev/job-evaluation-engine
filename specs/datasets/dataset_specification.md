# Dataset Specification

This document defines the structure and expectations for datasets used by the Job Evaluation Engine.

## Dataset Purpose

Datasets provide standardized input and output examples for:

- benchmarking evaluation quality
- validating scoring consistency
- regression testing

## Expected Dataset Components

A dataset may contain one or more of the following:

- **Job descriptions**: structured or semi-structured job postings.
- **Candidate profiles**: profiles representing hypothetical or real candidates.
- **Expected evaluation outputs**: reference outputs to validate evaluation results.

## Format

Datasets are stored in JSON format for machine consumption.

### Job Descriptions

Each job entry should include, at minimum:

- `title`
- `company`

Optional fields can include:

- `location`
- `source`
- `description`
- `responsibilities`
- `requirements`

### Candidate Profiles

Each candidate entry should include, at minimum:

- `profile_id`

Optional fields can include:

- `capability_profile` (object with the same dimensions as the evaluation output)
- `raw_text` (free-form resume/biography text)

### Reference Evaluations

Some datasets may include expected evaluation outputs to serve as ground truth.
These outputs should conform to `schemas/evaluation-output.schema.json`.

## Location

Datasets are organized under `/datasets`.

## Usage

The evaluation harness (e.g., scripts or benchmark runners) can read datasets, run
the evaluation engine for each item, and compare results to expected outputs.
