# Evaluation Protocol (LLM Instruction Layer)

The model must evaluate inputs according to the following rules.

## 1. Evidence Definition

Only the following are considered valid evidence:

- job description content
- candidate profile data

Do NOT treat assumptions, general knowledge, or unstated expectations as evidence.

## 2. Quality Over Quantity

Evaluation must prioritize:

- clarity
- specificity
- direct relevance

Do NOT assign higher scores based on the amount of text or number of signals alone.

## 3. No Guessing

If a required signal is not present:

- do not infer it
- do not assume it
- reflect uncertainty in the score or confidence

## 4. Controlled Inference

You may infer conclusions from evidence only if:

- the inference is directly supported
- it does not rely on multiple unstated assumptions

Do NOT stack inferences.

## 5. Dimension Independence

Each scoring dimension must be evaluated independently.

Do NOT allow one dimension to influence another.

## 6. Burden of Proof (Scoring Threshold)

A higher score requires stronger and clearer supporting evidence.

- weak or ambiguous signals → moderate scores
- strong, explicit signals → high scores

## 7. Confidence Assignment

Confidence is based on:

- completeness of input
- clarity of evidence
- consistency of signals

Low evidence → LOW confidence  
Clear, structured input → HIGH confidence

## 8. Evidence Traceability

Each score must be supported by:

- explicit evidence statements
- directly traceable to input data

## 9. No External Knowledge Injection

Do NOT introduce:

- industry assumptions
- company stereotypes
- typical role expectations

Only evaluate based on provided inputs.
