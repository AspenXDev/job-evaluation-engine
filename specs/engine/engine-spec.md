# Engine Specification

## Purpose

The Engine subsystem is responsible for transforming job descriptions and candidate profiles into structured representations that can be evaluated by the lattice scoring model.

It acts as the entry point of the evaluation pipeline and prepares the data required for downstream scoring and comparison.

## Inputs

The engine accepts two primary inputs.

### Job Description

A job description may be provided as:

- raw text
- semi-structured text
- structured data

Typical contents include:

- role responsibilities
- required skills
- experience expectations
- organizational context

### Candidate Profile

A structured representation of an individual’s capabilities and background.
Typical elements include:

- skills and competencies
- experience history
- education
- domain expertise

## Processing Stages

The engine performs a sequence of transformations to convert raw inputs into structured representations.

### 1. Job Parsing

The job description is parsed to identify:

- tasks
- responsibilities
- required capabilities
- coordination requirements

Relevant implementation modules:
src/engine/job_parser.py

### 2. Job Representation Construction

Parsed job information is converted into a structured internal representation.
This representation captures:

- task categories
- capability signals
- complexity indicators
- coordination demands

Relevant implementation modules:
src/engine/job_representation.py

### 3. Normalization

Extracted signals are normalized to ensure consistency across job descriptions.
Normalization may include:

- scale adjustments
- signal aggregation
- categorical standardization

Relevant implementation modules:
src/engine/normalization.py

## Intermediate Output

The result of engine processing is a **structured job representation**.
This representation serves as the input to the lattice scoring model.

Key characteristics:

- structured capability signals
- normalized indicators
- standardized format

## Downstream Integration

The structured job representation is passed to the lattice scoring subsystem.
Relevant specification:
specs/lattice/lattice_scoring_model.md

## Final Output

After downstream processing, the system produces a structured evaluation report conforming to the defined output schema.
Relevant specification:
specs/output-schema.md
