# Job Representation Specification

This spec defines the structured internal representation used by the engine to describe jobs and candidates.

## Job Description Model

The engine consumes job data and produces a `JobDescription` object.

### Required fields

- `title` (string): The role title.
- `company` (string): The hiring organization name.

### Optional fields

- `location` (string): Primary location of the role.
- `source` (string): Link or reference where the job description was obtained.
- `description` (string): Full free-text job description.
- `responsibilities` (string): Key responsibilities or tasks.
- `requirements` (string): Required skills, experience, or qualifications.

### Additional fields

Any additional fields are preserved in an `additional` map and can be used by
custom scoring logic.

### Implementation

- Model defined in: `src/engine/job_representation.py`
- Parsing of raw inputs to this model is implemented in: `src/engine/job_parser.py`

---

## Candidate Profile Model

The candidate profile provides the reference point for alignment analysis.

### Required fields

- `profile_id` (string): Identifier used in outputs to link back to the candidate.

### Optional fields

- `capability_profile` (object): Explicit capability vector with the same dimensions as the job capability profile.
- `weight_profiles` (object): Optional weighting preferences used to adjust evaluation.
- `raw_text` (string): Free-form text describing the candidate's background.

### Implementation

- Model defined in: `src/engine/job_representation.py`
- Parsing of raw inputs to this model is implemented in: `src/engine/job_parser.py`

---

## Capability Profile

A capability profile is a normalized vector of scores describing a role's demands across dimensions.

- Dimensions are: `reasoning`, `planning`, `creativity`, `operational_complexity`, `coordination`.
- Scores are floats in [0.0, 1.0].

Implementation is in: `src/engine/job_representation.py`.
