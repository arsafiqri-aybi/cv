# Architecture v0.1 — CV as a Screening Representation

## 1. Why the architecture changed

An earlier concept proposed seven "scientific cores" such as personnel selection, psychometrics, signaling, cognition, communication, and ATS.

After adversarial review, that framing was rejected because it mixed:

- academic disciplines;
- process stages;
- evaluation methods;
- technologies;
- and document properties

at the same abstraction level.

The replacement architecture separates:

1. **real-world states**;
2. **CV transformation stages**;
3. **interpretation systems**;
4. **scientific lenses**;
5. **evaluation criteria**.

This is more defensible and easier to extend.

---

## 2. Umbrella domain

The broad scientific home is:

**Recruitment + Personnel Selection + Staffing**

CVs sit between applicant self-presentation and organizational screening.

Personnel selection is central, but recruitment science matters because the applicant is an active participant producing signals, not a passive test subject.

---

## 3. Canonical process model

```text
┌───────────────────────────────┐
│ A. WORK / ROLE REALITY        │
│ tasks, outputs, context,      │
│ KSAOs, constraints, level     │
└───────────────┬───────────────┘
                │ relevance target
                ▼
┌───────────────────────────────┐
│ B. CANDIDATE REALITY          │
│ history, skills, education,   │
│ projects, outcomes, context   │
└───────────────┬───────────────┘
                │ observable support
                ▼
┌───────────────────────────────┐
│ C. EVIDENCE MODEL             │
│ facts → evidence → claims     │
│ provenance + uncertainty      │
└───────────────┬───────────────┘
                │ selection
                ▼
┌───────────────────────────────┐
│ D. SIGNAL MODEL               │
│ what to foreground, omit,     │
│ compare, quantify, qualify    │
└───────────────┬───────────────┘
                │ encoding
                ▼
┌───────────────────────────────┐
│ E. DOCUMENT REPRESENTATION    │
│ sections, bullets, language,  │
│ hierarchy, typography, format │
└───────┬─────────────────┬─────┘
        │                 │
        ▼                 ▼
┌───────────────┐  ┌─────────────────┐
│ F1. HUMAN     │  │ F2. MACHINE     │
│ INTERPRETATION│  │ INTERPRETATION  │
│ attention,    │  │ parsing, search,│
│ inference, fit│  │ ranking, NLP    │
└───────┬───────┘  └────────┬────────┘
        └──────────┬────────┘
                   ▼
┌───────────────────────────────┐
│ G. SCREENING OUTCOME          │
│ rejection / review / interview│
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│ H. FEEDBACK                   │
│ observed funnel outcomes,     │
│ uncertainty-aware learning    │
└───────────────────────────────┘
```

This is a dependency model, not a claim that every employer follows the sequence exactly.

---

## 4. Layer A — Work / Role Reality

### Scientific basis

- work analysis;
- job analysis;
- competency modeling;
- task analysis;
- KSAO frameworks;
- occupational context.

### Core question

**What does successful work actually require?**

### Important correction

A job description is not treated as complete ground truth.

Target-role modeling may use:

- job posting;
- occupational data;
- team/company context;
- role family;
- seniority expectations;
- tools and domain;
- outputs and responsibilities;
- explicit must-have constraints.

### Failure modes

- copying keywords without understanding the work;
- treating every listed qualification as equally important;
- ignoring context and seniority;
- confusing credential requirements with actual work outputs;
- using obsolete role taxonomies.

---

## 5. Layer B — Candidate Reality

This layer stores what actually happened.

Possible evidence sources:

- employment;
- projects;
- education;
- certifications;
- volunteer work;
- coursework;
- products;
- code;
- publications;
- awards;
- measured outcomes;
- responsibilities;
- artifacts.

### Boundary

Candidate reality is **not yet CV copy**.

It should be represented before compression so that wording choices cannot silently mutate facts.

---

## 6. Layer C — Evidence Model

### Purpose

Convert candidate history into inspectable evidence units.

Canonical structure:

```text
FACT
→ CONTEXT
→ ACTION / CONTRIBUTION
→ OUTPUT
→ OUTCOME
→ SCOPE
→ SUPPORT
→ UNCERTAINTY
```

Not every evidence unit has every field.

### Why this exists

Prehire work-experience quantity has weak criterion-related validity in meta-analysis. Therefore the architecture must not equate duration with performance evidence.

### Claim classes

- directly observed fact;
- candidate-reported fact;
- externally verifiable credential;
- measured result;
- bounded inference;
- unsupported claim.

Unsupported material claims must not be promoted into final copy.

---

## 7. Layer D — Signal Model

### Scientific basis

Personnel selection can be modeled as a signaling game under information asymmetry.

The applicant decides which truthful information to make salient. The organization interprets signals while knowing applicants have incentives to self-present favorably.

### Design objective

**High-information, high-relevance, low-distortion signaling.**

### Signal properties

- relevance;
- specificity;
- credibility;
- diagnosticity;
- verifiability;
- distinctiveness;
- costliness / difficulty to fake;
- ambiguity;
- redundancy.

### Important correction

Persuasiveness is not equivalent to evidentiary strength.

---

## 8. Layer E — Document Representation

### Components

- section selection;
- ordering;
- bullet construction;
- sentence structure;
- terminology;
- detail;
- clarity;
- information density;
- white space;
- typography;
- alignment;
- file structure.

### Evidence status

A 2025 field study found that greater detail, clarity, and structure in resumes/cover letters was associated with more interviews and faster job attainment even after controls for experience and achievement.

This supports document communication as consequential.

It does **not** prove that polished writing predicts job performance.

### Architecture consequence

Document quality is optimized for **transmission and screening**, not treated as evidence of candidate capability.

---

## 9. Layer F1 — Human Interpretation

### Relevant sciences

- judgment and decision making;
- attention and cognitive load;
- impression formation;
- person–job fit perceptions;
- person–organization fit perceptions;
- heuristics;
- stereotyping and discrimination;
- source credibility.

### Key distinction

**Perceived fit ≠ objective fit.**

Recruiter fit perceptions can mediate hiring recommendations, but perceptions may contain noise or bias.

### Guardrail

Do not optimize a CV for vague "culture fit" mimicry.

Prioritize demonstrable work relevance and role alignment.

---

## 10. Layer F2 — Machine Interpretation

### Relevant sciences / technologies

- information retrieval;
- NLP;
- entity extraction;
- semantic matching;
- ranking;
- classification;
- recommender systems;
- LLM-based screening;
- algorithmic fairness.

### Important correction

"ATS" is not one algorithm.

Different systems may:

- store applications;
- parse documents;
- enable recruiter search;
- apply knockout rules;
- rank candidates;
- integrate external assessments;
- provide AI recommendations;
- do none of the above.

### Guardrail

The system must never claim a universal ATS score or universal keyword formula without evidence about the actual system.

---

## 11. Layer G — Screening Outcome

Possible outcomes:

- parsed successfully;
- failed minimum requirement;
- surfaced in recruiter search;
- recruiter review;
- shortlist;
- interview;
- rejection;
- unknown.

### Critical distinction

**Screening success ≠ job performance validity.**

A CV can be excellent at securing interviews and still be a poor instrument for predicting future performance.

The architecture must track both concepts separately.

---

## 12. Layer H — Feedback

Application outcomes are noisy.

A rejection may result from:

- stronger candidates;
- internal candidate;
- headcount change;
- location/visa constraints;
- compensation mismatch;
- recruiter judgment;
- algorithmic screening;
- timing;
- bias;
- random variation;
- weak CV.

Therefore:

```text
OBSERVED OUTCOME
≠
DIRECT PROOF OF A CV MECHANISM
```

Feedback may update tactical hypotheses, not automatically rewrite scientific rules.

---

## 13. Cross-cutting scientific lenses

### X1 — Measurement, validity, and reliability

Use psychometric concepts to ask:

- what construct is being inferred?
- what outcome is being predicted?
- is the inference reliable?
- is there criterion-related evidence?
- what is measurement error?
- is a proxy being mistaken for the target construct?

Psychometrics is a **cross-cutting evaluation lens**, not a CV content core.

### X2 — Fairness, discrimination, and ethics

Apply across every layer:

- role criteria;
- evidence selection;
- sensitive attributes;
- human inference;
- algorithmic processing;
- feedback interpretation.

Resume audit literature shows that otherwise equivalent applications can receive different outcomes based on demographic signals.

### X3 — Provenance and uncertainty

Every material rule or claim should record:

- source;
- evidence type;
- context;
- date;
- confidence;
- limitations;
- contradictions.

### X4 — Legal / policy context

Legal rules vary by jurisdiction and time.

Never universalize one country's law into a scientific law of CV construction.

---

## 14. Scientific map — many-to-many

The project will use a graph, not a rigid tree.

Example:

```text
WORK ANALYSIS
  → relevance model
  → evidence selection
  → terminology
  → minimum requirements
  → machine matching
  → fairness / job-relatedness

SIGNALING
  → evidence salience
  → self-presentation
  → credibility
  → omission decisions
  → recruiter inference

HUMAN JUDGMENT
  → perceived fit
  → attention
  → heuristics
  → screening decision
  → discrimination risk

DOCUMENT COMMUNICATION
  → clarity
  → structure
  → information density
  → human comprehension
  → parseability

ALGORITHMIC HIRING
  → parsing
  → ranking
  → retrieval
  → bias
  → explainability
```

---

## 15. Provisional quality function

Do not reduce quality to one magic score.

Evaluate separately:

```text
Factual Fidelity
Job Relevance
Evidence Strength
Claim Calibration
Information Clarity
Human Readability
Machine Parseability
Credibility
Fairness Risk
Consistency
Constraint Compliance
```

A CV should not gain points in one dimension by silently destroying another.

---

## 16. Architecture status

### Accepted now

- CV as screening representation / interface;
- recruitment + selection umbrella;
- process-layer architecture;
- human and machine interpretation split;
- validity and fairness as cross-cutting;
- fact/evidence/claim separation;
- callback vs performance distinction.

### Not yet frozen

- number of modules;
- number of neurons;
- exact scoring weights;
- universal bullet formulas;
- universal ATS rules;
- universal page-length rule;
- universal template;
- exact role-fit algorithm.

These must emerge from evidence and testing.
