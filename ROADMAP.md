# Roadmap

## Stage 0 — Architecture red-team

Status: **COMPLETE v0.1**

Outputs:
- process-layer model;
- umbrella-domain correction;
- psychometrics reclassified as cross-cutting;
- ATS reclassified as machine mediation;
- resume-validity caveat;
- callback vs performance separation;
- evidence policy.

## Stage 1 — Literature discovery

Status: **BREADTH PASS v0.1 COMPLETE**

Goal:
Build the research map before forcing module counts.

Research clusters covered in first pass:

1. recruitment + staffing;
2. personnel selection;
3. work / role analysis;
4. résumé screening;
5. signaling + self-presentation;
6. person–job / person–organization fit;
7. recruiter judgment + cognition;
8. résumé content;
9. work-experience validity;
10. biodata;
11. skills signaling;
12. writing quality + communication;
13. information architecture + document design;
14. résumé aesthetics/layout;
15. recruiter attention;
16. personality inference;
17. machine parsing;
18. digital selection;
19. information retrieval + ranking;
20. algorithmic hiring;
21. fairness + discrimination;
22. applicant reactions;
23. generative AI and résumé signaling;
24. feedback / application outcomes.

Still under-covered:
- cross-cultural conventions;
- occupation-specific moderation;
- executive/academic CV distinctions;
- legal regimes;
- production ATS behavior.

Deliverables:
- `research/LITERATURE_DISCOVERY_V0_1.md`
- source-registry supplement;
- explicit research gaps.

## Stage 2 — Claim / contradiction / uncertainty registry

Status: **BOOTSTRAPPED v0.1**

Created:
- `research/CLAIM_REGISTRY_V0_1.md`
- `research/CONTRADICTION_REGISTRY_V0_1.md`
- `research/UNCERTAINTY_REGISTRY_V0_1.md`

Next:
- expand source coverage for each material claim;
- attach outcome + context + boundary metadata;
- promote/demote claims based on contradiction search.

## Stage 3 — Construct decomposition

Status: **STARTED / PROVISIONAL**

Current artifact:
- `research/CONSTRUCT_CANDIDATES_V0_1.md`

Do not begin with a target module count.

For each construct:

- canonical definition;
- neighboring constructs;
- aliases;
- non-equivalences;
- evidence status;
- outcome relation;
- context;
- measurement;
- failure modes.

Then cluster into modules.

## Stage 4 — Graph architecture

Status: NOT STARTED

Build:

- nodes;
- primary memberships;
- secondary memberships;
- evidence-backed edges;
- contradictions;
- non-edges;
- boundary conditions.

Every edge must state the relationship type.

Possible edge types:

- prerequisite;
- moderates;
- mediates;
- predicts;
- associated-with;
- constrains;
- transforms;
- interpreted-by;
- measured-by;
- conflicts-with.

## Stage 5 — Candidate evidence model

Status: NOT STARTED

Create a structured schema for candidate history before writing.

Candidate data must support:

- chronology;
- role;
- task;
- contribution;
- output;
- outcome;
- scope;
- tools;
- collaborators;
- evidence source;
- confidence;
- sensitivity.

## Stage 6 — Target role model

Status: NOT STARTED

Combine:

- job posting;
- role family;
- work activities;
- KSAOs;
- context;
- seniority;
- hard constraints;
- occupational terminology;
- evidence of importance.

Avoid treating all JD bullets equally.

## Stage 7 — Reasoning engine

Status: NOT STARTED

Reasoning route:

```text
TARGET ROLE
→ CANDIDATE REALITY
→ EVIDENCE INVENTORY
→ RELEVANCE MAP
→ CLAIM CALIBRATION
→ SIGNAL SELECTION
→ INFORMATION PRIORITY
→ DOCUMENT STRUCTURE
→ LANGUAGE
→ HUMAN SCREENING AUDIT
→ MACHINE INTERPRETATION AUDIT
→ FACTUAL / FAIRNESS AUDIT
→ FINAL CV
```

## Stage 8 — Evaluation system

Status: NOT STARTED

Separate scorecards:

- factual fidelity;
- relevance;
- evidence quality;
- claim calibration;
- clarity;
- structure;
- redundancy;
- human readability;
- machine parseability;
- sensitive-data exposure;
- bias/fairness risk;
- consistency.

Do not combine into one score unless the weighting has an explicit use case.

## Stage 9 — Behavioral tests

Status: NOT STARTED

Test at least:

- strong candidate / clear job;
- weakly matched candidate;
- career changer;
- student / minimal experience;
- fragmented employment;
- project-heavy candidate;
- technical role;
- creative role;
- academic CV edge case;
- multilingual CV;
- conflicting dates;
- unverifiable metrics;
- ATS-hostile source document;
- misleading job description;
- sensitive demographic information;
- user asks to exaggerate;
- user asks to keyword-stuff;
- user gives no target role.

## Stage 10 — Runtime Skill

Status: NOT STARTED

Only after the domain architecture is stable:

- build `SKILL.md`;
- retrieval map;
- references;
- deterministic validators where useful;
- trigger tests;
- behavioral tests;
- packaging;
- release gates.

## Stage 11 — Feedback learning

Status: NOT STARTED

Observed application outcomes may update:

- target-role hypotheses;
- wording hypotheses;
- section-order hypotheses;
- context-specific heuristics.

They may **not** directly rewrite:

- scientific source claims;
- validity conclusions;
- universal architecture.

Those require research evidence.
