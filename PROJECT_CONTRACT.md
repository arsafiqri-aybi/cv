# Project Contract — CV

## Mission

Build a rigorous knowledge and reasoning system that explains **why CVs work or fail**, then uses that understanding to construct and evaluate CVs without inventing candidate facts.

The project is about the science and operational logic behind CVs first. Portfolio, LinkedIn, GitHub, interview coaching, and broader career branding are outside the active scope unless later authorized.

## Core question

> Given a real target role and a real candidate history, how should relevant information be selected, represented, structured, and verified so that it is accurately and efficiently interpreted during screening?

## Non-goals

This project will not assume that:

- CVs are strong predictors of job performance;
- more experience automatically means stronger evidence;
- ATS systems behave identically;
- keyword matching is the central mechanism;
- one template is universally optimal;
- recruiter perceptions are always accurate or fair;
- person–organization fit is inherently objective;
- persuasive wording can substitute for evidence;
- metrics should be invented when unavailable.

## Protected invariants

1. Candidate facts remain authoritative over generated wording.
2. Claims must not exceed available evidence.
3. Callback probability and job-performance validity are separate outcomes.
4. Human and machine screening are separate interpretation paths.
5. Job descriptions are evidence about a role, not complete ground truth.
6. Cross-context rules require evidence; local heuristics remain local.
7. Fairness and bias are not downstream cosmetic checks.
8. Scientific uncertainty must be represented explicitly.
9. Architecture complexity must be earned by evidence and task needs.
10. A clean result is preferred over maximal module count.

## Acceptance targets

The mature system should be able to:

- model target work and role requirements;
- inventory candidate evidence;
- distinguish fact, inference, claim, and wording;
- map evidence to role relevance;
- identify weak, ambiguous, unsupported, or redundant claims;
- construct a CV with clear information hierarchy;
- preserve machine-readable structure where appropriate;
- evaluate likely human screening interpretation;
- flag fairness, bias, and sensitive-attribute risks;
- maintain provenance for material claims;
- compare CV variants without pretending causal certainty;
- learn from application outcomes without rewriting scientific truth from noisy feedback.

## Evidence hierarchy

Prefer, approximately:

1. systematic reviews / meta-analyses;
2. high-quality review articles;
3. field experiments and longitudinal field studies;
4. preregistered experiments;
5. well-designed observational studies;
6. technical evaluations / audits;
7. official professional or regulatory standards;
8. industry datasets with transparent methodology;
9. expert practice guidance;
10. anecdote.

Evidence level does not replace relevance, recency, design quality, or boundary conditions.

## Completion rule

Do not call the project scientifically complete merely because:

- every folder has content;
- a large node graph exists;
- a Skill package validates;
- test prompts pass;
- a CV looks polished.

Completion requires separate evidence for:

- scientific coverage;
- operational coherence;
- factual integrity;
- retrieval quality;
- reasoning behavior;
- document output quality;
- adversarial robustness;
- machine-readability checks;
- human-readability checks;
- known limitations.
