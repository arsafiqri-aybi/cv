# CV

Research-grounded architecture for understanding, constructing, and evaluating CVs/résumés.

## Central position

A CV is **not treated as a psychometric test, a keyword container, or merely persuasive copy**.

The working model is:

> A CV is a constrained representation of candidate-relevant information used inside a recruitment and selection system, where the representation is interpreted by human and/or computational screeners under uncertainty.

This repository studies the full path:

```text
WORK / ROLE REALITY
        ↕
CANDIDATE REALITY
        ↓
EVIDENCE SELECTION
        ↓
SIGNAL CONSTRUCTION
        ↓
DOCUMENT REPRESENTATION
        ↓
HUMAN + MACHINE INTERPRETATION
        ↓
SCREENING DECISION
        ↓
OBSERVED OUTCOMES / FEEDBACK
```

The architecture is intentionally **not frozen into an arbitrary number of scientific cores**. Scientific disciplines and mechanisms may cut across multiple process layers.

## What this project is trying to optimize

A high-quality CV should increase:

- factual fidelity;
- job relevance;
- evidence specificity;
- interpretability;
- credibility;
- information efficiency;
- human readability;
- machine parseability where relevant;
- consistency across claims;
- fairness-aware presentation;
- usefulness for the intended screening context.

It should **not** optimize:

- fabricated achievements;
- inflated claims;
- unsupported causal language;
- keyword stuffing;
- imitation of a target employer's personality;
- gaming an unknown ATS;
- aesthetic complexity for its own sake;
- callback rate at the expense of truth or long-term fit.

## Scientific foundation

Primary scientific areas:

1. Recruitment, staffing, and personnel selection
2. Work / job analysis and competency requirements
3. Signaling and information asymmetry
4. Human judgment, impression formation, and perceived fit
5. Language, information architecture, and document communication

Cross-cutting lenses:

- measurement, validity, and reliability;
- fairness, discrimination, and legal/ethical constraints;
- algorithmic hiring, NLP, information retrieval, and machine screening;
- uncertainty, provenance, contradiction, and evidence quality;
- applicant outcomes and feedback.

## Why this architecture

The repository was deliberately red-teamed before being established.

Important corrections to the initial concept:

- **Personnel Selection alone is too narrow** as the umbrella. CVs sit at the recruitment–selection boundary.
- **A CV is not itself a validated predictor of job performance.** Resume screening may influence hiring outcomes while still having weak criterion validity.
- **Psychometrics is an evaluation lens, not a CV core.**
- **Work experience quantity is not equivalent to capability evidence.**
- **Perceived fit is consequential but not objective truth.**
- **Writing quality can affect interview outcomes even after controlling for experience, which means presentation is consequential but may not be diagnostic of job performance.**
- **ATS is a heterogeneous mediation layer, not the foundation of CV science.**
- **There is no evidence-based universal "best template."**

See `docs/ARCHITECTURE.md` and `research/RED_TEAM.md`.

## Current status

**Architecture stage: v0.1 — research-grounded provisional architecture.**

The process model is accepted as the working scaffold. Module counts, neuron counts, edge counts, and runtime rules are **not frozen** until deeper literature discovery and construct decomposition are completed.

## Repository map

- `PROJECT_CONTRACT.md` — mission, scope, constraints, completion logic
- `docs/ARCHITECTURE.md` — working architecture and layer model
- `research/EVIDENCE_POLICY.md` — source and claim promotion rules
- `research/RED_TEAM.md` — adversarial audit of the concept
- `research/SOURCE_REGISTRY.md` — initial scientific source map
- `ROADMAP.md` — staged build plan
