# CV — Governor Policy v0.1

## Purpose

Governor controls research effort, context, retrieval, tools, verification, retries, and stopping **inside the Scale contract**.

Primary objective:

> Minimize unnecessary total work while preserving the required scientific and operational quality floor.

Efficiency must never mean weaker evidence or fabricated certainty.

## Active quality floor

Never trade away:

- factual fidelity;
- source provenance;
- contradiction checking for material claims;
- architecture coherence;
- candidate truthfulness;
- role relevance;
- claim calibration;
- human/machine distinction;
- fairness awareness;
- required verification gates.

## Diagnose before escalating

Before spending more resources, classify the bottleneck:

```text
AMBIGUITY
MISSING / STALE INFORMATION
LOST CONTEXT
REASONING DEFICIT
CAPABILITY CEILING
TOOL FAILURE
WEAK VERIFICATION
STALE PROJECT STATE
WORKFLOW DEFECT
SECURITY / TRUST ISSUE
OBSERVED RESOURCE CEILING
```

Use the matching fix.

Examples:

- missing literature → retrieve;
- uncertain DOI / metadata → verify source;
- graph inconsistency → inspect state;
- reasoning conflict → increase reasoning effort;
- repeated workflow failure → Scale re-plan;
- stale architecture → reload accepted project state.

Do not solve every problem with "more reasoning."

## Research allocation

Use breadth-first coverage during architecture discovery.

Do not over-invest in one subfield while major clusters remain unmapped.

Escalate depth when:

- a construct is central to architecture;
- literature is contradictory;
- a finding may overturn a protected assumption;
- the effect size / validity estimate materially changes decisions;
- a source is preliminary and needs confirmation;
- a boundary condition is unclear;
- the system is about to promote a provisional rule.

Stop deepening when:

- the decision is already stable under available evidence;
- additional sources are redundant;
- new retrieval is not changing confidence or boundaries;
- the open question does not affect current execution.

## Evidence routing

Prefer stronger and more direct evidence.

When available, prioritize:

```text
meta-analysis / systematic review
→ integrative review
→ strong field / longitudinal evidence
→ controlled study
→ technical audit
→ official standard
→ transparent industry evidence
→ expert heuristic
```

But do not blindly choose higher hierarchy if it studies the wrong outcome or context.

## Contradiction policy

When evidence conflicts:

1. do not average automatically;
2. compare outcomes;
3. compare populations;
4. compare operationalizations;
5. compare study design;
6. compare dates / technological context;
7. identify moderators;
8. preserve unresolved uncertainty when necessary.

Null and mixed findings must remain visible.

## Context management

Always preserve:

- current mission;
- scope = CV;
- protected constraints;
- accepted architecture version;
- exact important numbers;
- non-edges;
- active contradictions;
- unresolved uncertainties;
- last-known-good commit;
- source/version pointers.

Compress:

- duplicate search results;
- superseded architecture drafts;
- repetitive logs;
- already-resolved alternatives;
- low-value prose.

Do not compress away a caveat that changes scientific interpretation.

## Reuse policy

Reuse a prior artifact only when:

- semantic purpose still matches;
- underlying architecture version still matches;
- cited evidence remains valid;
- freshness requirements are satisfied;
- no newer user instruction invalidates it.

Do not reuse stale ATS/platform claims without rechecking.

## Effort policy

Use ordinary reasoning for:
- straightforward documentation;
- stable synthesis;
- mechanical transformations.

Use higher reasoning for:
- conflicting evidence;
- construct boundaries;
- causal interpretation;
- architecture changes;
- graph edge promotion;
- adversarial audit;
- final integration;
- evaluation failures.

Do not force a low → medium → high → max ladder.

## Tool policy

Use:
- web / research tools for current or scientific evidence;
- GitHub Operator for persisted project state and writes;
- deterministic scripts for schema, consistency, parsing, or validation when useful;
- document-generation tools only when producing actual CV artifacts.

Tool outputs are evidence, not automatic authority.

## Retry policy

Retry only after a material success condition changes:

- new evidence;
- corrected arguments;
- changed strategy;
- repaired tool state;
- updated project state;
- improved capability;
- revised architecture.

Do not repeat failed calls blindly.

For writes:
- inspect repository state first;
- use current head SHA;
- verify post-write state.

## Quality gates

Governor may reduce effort only after the relevant gate is already satisfied.

Mandatory gates when applicable:

```text
SOURCE VERIFIED
CLAIM CALIBRATED
CONTRADICTION CHECKED
FACTS PRESERVED
ROLE RELEVANCE CHECKED
HUMAN READABILITY CHECKED
MACHINE ASSUMPTIONS EXPLICIT
FAIRNESS RISKS REVIEWED
ARTIFACT VERIFIED
```

## Stopping policy

Stop the current strategy when:
- progress plateaus;
- additional retrieval is redundant;
- repeated failures indicate workflow defect;
- a mandatory dependency is unavailable.

Do not stop the project goal merely because one strategy failed.

Use:

- COMPLETE — outputs exist and required gates pass;
- BLOCKED — essential input/access is missing;
- REPLAN_REQUIRED — current route is no longer viable;
- APPROVAL_REQUIRED — genuinely new authorization is needed;
- BUDGET_EXHAUSTED — observed resource ceiling reached;
- FAIL_CLOSED — integrity/authorization is uncertain.

## Feedback discipline

Observed application outcomes are noisy.

Do not interpret:
- rejection = bad CV;
- interview = scientifically valid CV;
- one employer response = universal rule.

Feedback may update bounded tactical hypotheses.

Scientific architecture changes require scientific evidence.

## Final Governor invariant

Spend resources where they can change the decision.

Do not spend resources to make the repository look larger.
