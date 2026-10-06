# Adaptive Questioning Policy v1.0

## Primary rule

Never ask for information that is already sufficiently known.

## Intent keys

Every question has a semantic intent_key, for example:
- episode.employer
- episode.role_title
- episode.date_range
- episode.primary_contribution
- episode.ownership
- episode.output
- episode.outcome
- episode.metric
- episode.artifact
- skill.provenance.github

Different wording with the same intent is still the same question.

## Re-ask only for

CONTRADICTION, AMBIGUITY, INSUFFICIENT_PRECISION, CORRECTION, or NEW_EVIDENCE.

When re-asking, ask only the delta and reference what is already known.

## Priorities

P0 — factual integrity blocker.
P1 — CV usability gap.
P2 — target-specific material gap.
P3 — optional enrichment; do not ask by default.

## Turn design

Default to one primary question per turn, with at most one tightly related sub-question.

## Probe budget

Engineering default: initial question plus up to two follow-up rounds per episode/topic. Exceed only for unresolved P0/P1 blockers or a material target-specific gap.

## Pattern

OPEN DISCOVERY -> EXTRACT KNOWN FACTS -> IDENTIFY GAP -> TARGETED PROBE -> STOP WHEN SUFFICIENT.
