# Red-Team Audit — Why This CV Concept, and What Could Falsify It?

This document records attacks against the architecture so the project does not preserve an elegant but false model.

## Attack 1 — "A CV is evidence of future performance"

### Objection

That claim is too strong.

A 2025 Academy of Management Proceedings study reported low point estimates of criterion-related validity for holistic resume assessments in two samples and found no significant relation with performance or turnover. The public record is an abstract/proceedings contribution, so it should be treated as important but not definitive.

A 2019 meta-analysis also found that common measures of prehire work experience were weak predictors of subsequent performance and turnover.

### Decision

Reject:

> CV = validated performance predictor.

Retain:

> CV = screening representation containing candidate-relevant signals, some of which may or may not be valid indicators of future performance.

### Consequence

The system separates:

- **screening effectiveness**;
- **evidence quality**;
- **predictive validity**.

They are not interchangeable.

---

## Attack 2 — "Personnel Selection is the entire scientific foundation"

### Objection

Too narrow.

Recruitment research studies the applicant side, recruitment messages, methods, attraction, and prehire processes. CVs are produced by applicants and interpreted by organizations.

### Decision

Use **Recruitment + Personnel Selection / Staffing** as the broad umbrella.

Personnel selection remains central for screening validity and decision quality.

---

## Attack 3 — "Psychometrics should be a CV core"

### Objection

Category error.

Psychometrics concerns measurement quality, reliability, validity, construct inference, and assessment. A normal CV is not a standardized psychometric instrument.

### Decision

Move psychometrics to a cross-cutting **Measurement & Validity Lens**.

Use it to audit inferences such as:

- "years of experience = competence";
- "degree = ability";
- "keyword count = fit";
- "polished writing = performance."

---

## Attack 4 — "Work experience is the strongest evidence"

### Objection

The quantity or duration of prehire experience has shown weak criterion-related validity for job performance in meta-analysis.

### Decision

Do not optimize for experience volume.

Model evidence quality using:

- role relevance;
- task specificity;
- contribution;
- output;
- outcome;
- scope;
- recency;
- support;
- uncertainty.

No rule says all achievements must contain a number.

---

## Attack 5 — "Person–job fit is objective truth"

### Objection

Recruiters form fit perceptions, and those perceptions can predict hiring recommendations, but perceived fit remains a judgment.

Person–organization fit can especially blur into subjective "fitting in" decisions.

### Decision

Distinguish:

- objective requirement match;
- evidence-supported role relevance;
- recruiter-perceived P–J fit;
- recruiter-perceived P–O fit.

Do not optimize for cultural mimicry.

---

## Attack 6 — "Signaling means persuasive self-marketing"

### Objection

Signaling theory includes information asymmetry and strategic self-presentation, but a signal can be misleading, inflated, cheap, or easily copied.

### Decision

Use **calibrated signaling**:

```text
truthful
+ relevant
+ specific
+ interpretable
+ credible
+ proportionate to evidence
```

Persuasion without support is a failure.

---

## Attack 7 — "Better writing proves a better candidate"

### Objection

A 2025 field study found that detail, clarity, and structure predicted interview success after controls. But the authors explicitly note that such compositional qualities can now be generated or improved by technologies such as ChatGPT.

Therefore writing quality may influence screening without being a stable indicator of worker capability.

### Decision

Treat writing quality as a **communication advantage**, not a performance construct.

---

## Attack 8 — "ATS optimization is the main CV science"

### Objection

Algorithmic hiring is heterogeneous.

Modern recruitment technology spans parsing, retrieval, ranking, recommendation, assessments, LLMs, and human-in-the-loop systems. Research also shows unresolved fairness and validity challenges.

### Decision

ATS / AI screening becomes a machine-interpretation branch.

Rules must specify the assumed system behavior.

No universal ATS score.

---

## Attack 9 — "One clean visual format is scientifically best"

### Objection

Resume aesthetics can influence judgments, but evidence does not establish one universal layout as optimal across roles, countries, screening systems, and applicant pools.

Industry observational data in 2026 also found no consistent winning template across a large self-reported application dataset, though such evidence is not equivalent to randomized peer-reviewed research.

### Decision

Optimize for:

- legibility;
- hierarchy;
- semantic clarity;
- consistent structure;
- export integrity;
- parseability;
- context fit.

Do not freeze a universal visual template.

---

## Attack 10 — "More keywords = more ATS success"

### Objection

This assumes a specific retrieval/ranking mechanism that may not exist.

Keyword repetition can also reduce human quality and distort meaning.

### Decision

Prefer semantic role alignment and correct terminology.

Keyword usage must be natural, evidence-backed, and job-relevant.

---

## Attack 11 — "The job description is the ground truth"

### Objection

Job postings can be incomplete, aspirational, templated, inconsistent, or outdated.

Work-analysis research distinguishes work activities, worker attributes, and work context.

### Decision

Use a **Target Role Model**, not a raw JD copy.

The JD is one input.

---

## Attack 12 — "Maximize interview rate at all costs"

### Objection

A CV optimized purely for callbacks can reward exaggeration, generic polish, identity masking, or overfitting.

### Decision

Optimization is constrained:

```text
maximize screening usefulness
subject to
truthfulness
+ evidence calibration
+ role relevance
+ fairness-aware practice
+ long-term consistency
```

---

## Attack 13 — "A very large neural graph means the project is better"

### Objection

Node count is not scientific coverage.

Premature decomposition creates ontology debt and false precision.

### Decision

No neuron/module count will be frozen until:

1. construct discovery;
2. literature clustering;
3. boundary analysis;
4. duplicate-resolution;
5. evidence mapping;
6. cross-core edge audit.

Architecture should grow only when new distinctions improve reasoning or retrieval.

---

## Current conclusion

The strongest defensible concept is not:

> CV = marketing document.

Not:

> CV = ATS keyword file.

Not:

> CV = proof of job performance.

Instead:

> **A CV is a strategically constructed but evidence-constrained representation of a candidate, used as one input in a socio-technical recruitment and selection system under uncertainty.**

This statement is provisional and should be revised if stronger evidence contradicts it.
