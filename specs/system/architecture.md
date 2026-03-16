# System Architecture

## Architectural Philosophy

The Job Evaluation Engine follows a **Spec-Driven Development (SDD)** architecture.

System behaviour is defined in the `/specs` directory.  
Implementation modules in `/src` are expected to conform to these specifications.

This separation ensures that:

- system behaviour is explicitly documented
- implementation logic can evolve without changing system design
- both humans and AI tools can reason about the system structure

## Architectural Layers

The system is organized into five primary layers.
Specifications → Schemas → Configuration → Implementation → Evaluation

Each layer has a specific responsibility.

### 1. Specification Layer

Location:
/specs

Defines the **intended behaviour of the system**.

This includes:

- system architecture
- engine design
- lattice scoring model
- evaluation protocols
- dataset specifications
- output definitions

Specifications are the **canonical design reference** for the system.

---

### 2. Schema Layer

Location:
/schemas

Defines the **structured formats used within the system**.
Schemas enforce consistency between:

- inputs
- internal representations
- evaluation outputs

Example schemas include:

- user profile schema
- evaluation output schema

Schemas allow automated validation during execution.

---

### 3. Configuration Layer

Location:
/config

Defines **parameterized behaviour** of the system.
Examples include:

- lattice dimension weights
- benchmark profiles
- evaluation defaults

This layer allows system behaviour to be adjusted without modifying implementation code.

---

### 4. Implementation Layer

Location:
/src

Contains the modules that implement the behaviour defined in the specifications.
The implementation is organized into subsystem modules:
src/engine
src/lattice
src/evaluation
src/benchmarks
src/utils

Responsibilities:

| Module     | Responsibility                                                  |
| ---------- | --------------------------------------------------------------- |
| engine     | parse job descriptions and construct structured representations |
| lattice    | apply multidimensional capability scoring                       |
| evaluation | compute evaluation metrics and comparisons                      |
| benchmarks | run benchmark task suites                                       |
| utils      | shared utilities such as validation and file handling           |

Implementation modules should remain consistent with the specifications in `/specs`.

---

### 5. Execution and Experimentation Layer

Locations:
/scripts
/experiments
/examples

These directories provide runnable workflows and demonstrations.

- `/scripts` contains execution pipelines
- `/experiments` contains experimental evaluations
- `/examples` provides reference inputs and outputs

These components allow the system to be exercised without modifying core modules.

---

## Data Flow

The high-level execution flow of the system is:
Inputs
↓
Engine Parsing
↓
Structured Job Representation
↓
Capability Extraction
↓
Lattice Scoring
↓
Evaluation Metrics
↓
Structured Output

Each stage corresponds to a subsystem module.

| Stage                        | Implementation    |
| ---------------------------- | ----------------- |
| Input parsing                | src/engine        |
| Representation normalization | src/engine        |
| Capability scoring           | src/lattice       |
| Evaluation metrics           | src/evaluation    |
| Output generation            | scripts / reports |

---

## Dataset Integration

Benchmark datasets are used to evaluate system behaviour.
Datasets are organized in:
/datasets

Dataset structures are defined in:
/specs/datasets

This separation allows datasets to evolve while preserving dataset specifications.

---

## Output Generation

Evaluation outputs follow structured formats defined by schemas.

Typical outputs include:

- capability profiles
- evaluation scores
- benchmark comparison results

Outputs are written to:
/outputs

Report generation scripts may transform raw outputs into human-readable reports.

---

## Implementation Alignment

The architecture assumes the following mapping between specifications and implementation:

| Specification          | Implementation            |
| ---------------------- | ------------------------- |
| engine specification   | src/engine                |
| lattice scoring model  | src/lattice               |
| evaluation framework   | src/evaluation            |
| dataset specifications | datasets + src/benchmarks |
| output schema          | schemas + scripts         |

Maintaining alignment between these layers is essential for system consistency.

---

## Design Principles

The system follows several design principles:

**Specification First**
System behaviour must be defined in `/specs` before implementation changes.

**Modular Subsystems**
Each subsystem has a clear responsibility and minimal coupling.

**Structured Data Flow**
Inputs, intermediate states, and outputs use structured formats wherever possible.

**Reproducible Evaluation**
Benchmark datasets and evaluation protocols allow consistent system evaluation.
