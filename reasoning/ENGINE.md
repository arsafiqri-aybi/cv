# CV Reasoning Engine v1

## Objective

Transform real candidate evidence into a target-specific CV while preserving truth, calibration, and interpretability.

## Canonical reasoning route

```text
1. INGEST TARGET ROLE
2. INGEST CANDIDATE REALITY
3. NORMALIZE EVIDENCE
4. MAP EVIDENCE ↔ REQUIREMENTS
5. IDENTIFY GAPS
6. CALIBRATE CLAIMS
7. SELECT SIGNALS
8. PRIORITIZE INFORMATION
9. CHOOSE SECTION ARCHITECTURE
10. WRITE
11. HUMAN SCREENING AUDIT
12. MACHINE INTERPRETATION AUDIT
13. FACTUAL / FAIRNESS AUDIT
14. FINALIZE
```

No downstream stage may invent upstream evidence.

## Decision hierarchy

When two goals conflict, preserve in this order:

1. factual fidelity;
2. material constraints / eligibility;
3. evidence calibration;
4. role relevance;
5. clarity / interpretability;
6. machine compatibility where relevant;
7. persuasion;
8. aesthetics.

## Step 1 — Target role

Build the Target Role Model.

If no target role exists:
- construct a general-purpose CV only if the user requests it;
- explicitly reduce tailoring claims;
- do not pretend to optimize for an unknown job.

## Step 2 — Candidate reality

Build evidence records.

Separate:
- supplied facts;
- externally checked facts;
- inferences;
- missing information.

## Step 3 — Normalize evidence

Resolve:
- duplicate episodes;
- inconsistent dates;
- ambiguous ownership;
- aliases;
- metric meaning;
- tool/domain naming.

If conflict cannot be resolved, preserve it as an open issue.

## Step 4 — Requirement mapping

For each important requirement:
- find direct evidence;
- find adjacent/transferable evidence;
- record no-match where appropriate.

Do not force a match.

## Step 5 — Gap diagnosis

Classify:
- hard constraint gap;
- evidence gap;
- wording gap;
- provenance gap;
- transferability gap;
- recency gap;
- unknown.

A wording gap can be fixed by writing.
An evidence gap cannot.

## Step 6 — Claim calibration

Determine the strongest justified statement.

```text
EVIDENCE STRONG + ATTRIBUTION CLEAR
→ direct claim

EVIDENCE PARTIAL / TEAM CONTEXT
→ bounded claim

FACT TRUE BUT DIAGNOSTICITY LOW
→ descriptive fact if useful

MATERIAL CLAIM UNSUPPORTED
→ omit / ask / mark gap
```

## Step 7 — Signal selection

Prefer signals that are:
- relevant;
- specific;
- credible;
- diagnostic;
- interpretable;
- non-redundant.

Distinctive but irrelevant signals do not automatically deserve space.

## Step 8 — Priority

Prioritize by:
- target importance;
- evidence relevance;
- evidence strength;
- transferability;
- recency/context;
- scarcity of document space.

No pseudo-precise global score is required.

## Step 9 — Section architecture

Choose sections based on:
- career stage;
- evidence distribution;
- role type;
- regional convention;
- reader needs;
- machine constraints.

Never force a fixed section order.

## Step 10 — Writing

Write from evidence records.

Each material bullet should answer enough of:
- what;
- how;
- contribution;
- output;
- outcome;
- scale;
- relevance.

Not every bullet requires every component.

## Step 11 — Human audit

Test:
- first-pass clarity;
- hierarchy;
- ambiguity;
- credibility;
- cognitive load;
- irrelevant demographic cues;
- unsupported impression-management tactics.

## Step 12 — Machine audit

Test assumptions explicitly:
- text extraction;
- section recognition;
- date/role parsing;
- entity clarity;
- table/column hazards;
- semantic/lexical alignment.

Do not claim a universal ATS result.

## Step 13 — Integrity + fairness

Check:
- facts unchanged;
- no invented metrics;
- ownership accurate;
- no hidden contradictions;
- sensitive data justified;
- protected/non-job-relevant cues reviewed;
- legal claims jurisdiction-scoped.

## Step 14 — Finalize

A CV can be finalized when:
- required facts are stable enough;
- high-priority requirements are represented where evidence exists;
- material gaps are not disguised;
- document is readable;
- machine assumptions are reasonable for the chosen format;
- no critical integrity failure remains.

## Failure statuses

- `EVIDENCE_GAP`
- `ROLE_AMBIGUITY`
- `FACT_CONFLICT`
- `UNSUPPORTED_CLAIM`
- `HARD_CONSTRAINT_GAP`
- `PARSE_RISK`
- `FAIRNESS_RISK`
- `CONTEXT_UNCERTAINTY`

These statuses trigger repair, not fabrication.
