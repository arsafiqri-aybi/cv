---
name: cv-candidate-discovery
description: Interview a candidate to build or update the Master Candidate Evidence Base used for CV/resume creation. Use when the user wants to be interviewed for their CV, provide career/project history conversationally, fill missing CV data, or gather reusable evidence before targeting applications. Ask adaptively but minimally: never knowingly repeat answered information, stop probing once evidence is CV-usable, and use target-specific follow-up only for material gaps.
---

# CV Candidate Discovery

Build reusable candidate evidence through a stateful, bounded interview.

## 1. Load before asking

Retrieve existing candidate evidence, prior interview state, known episodes, asked/answered intents, contradictions, interview preferences, and target application if one exists.

Never start from zero when usable evidence already exists.

## 2. Two modes

Master Discovery collects reusable candidate evidence broadly.

Target Delta asks only missing target-specific information.

Do not repeat Master Discovery for each company.

## 3. Discover broadly first

Read `references/INTERVIEW_FLOW.md`.

Start with a timeline/episode sweep. Do not spend too long on the first project/job before discovering the rest.

## 4. Extract after every answer

Before asking again:
- normalize facts;
- update evidence items;
- update coverage state;
- mark answered intents;
- identify contradictions;
- calculate the next material gap.

## 5. Ask only useful new intents

Read `references/QUESTION_POLICY.md` and `references/INTERVIEW_MEMORY.md`.

Default to one primary question per turn, with at most one tightly related sub-question.

Never knowingly ask the same semantic intent twice.

## 6. Stop at sufficiency

Read `references/COVERAGE_AND_SUFFICIENCY.md`.

Move on when an episode is CV_USABLE and no material blocker remains.

Do not require metrics, leadership stories, or exhaustive tool lists.

## 7. Prioritize

P0 integrity blocker -> P1 CV usability -> P2 target-specific material gap -> STOP.

P3 optional enrichment is deferred by default.

## 8. Bounded probing

Engineering default: initial answer plus up to two follow-up rounds per topic.

Exceed only for unresolved factual-integrity/CV-usability blockers or a material target-specific gap.

## 9. Preserve root rules

Evidence must comply with:
- `candidate_evidence/MODEL.md`
- `standards/DATE_STANDARD.md`
- `standards/CONSISTENCY_STANDARD.md`

Never invent metrics, dates, scope, outcomes, ownership, tools, or credentials.

## 10. Target integration

For a concrete application, use `skills/cv-application-targeting/SKILL.md`.

Targeting may identify a missing P2 detail. It may not force re-asking information already sufficient in the Master Candidate Evidence Base.

## 11. Research discipline

Read `references/RESEARCH_BASE.md`.

This subsystem adapts structured-interview and respondent-burden research. Its exact stop states, P0-P3 priorities, and probe budget are engineering decisions.

## 12. Output

Follow `references/OUTPUT_CONTRACT.md`.

Persist state so future sessions continue from the last-known-good evidence base.

## Completion

Complete enough means major history is mapped, material episodes are CV-usable, no P0 blocker remains, and target deltas are answered or explicitly unresolved.

Do not interview for depth after sufficiency has been reached.
