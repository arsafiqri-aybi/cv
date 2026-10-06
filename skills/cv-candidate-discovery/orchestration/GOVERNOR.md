# Candidate Discovery Governor

## Objective

Maximize useful candidate evidence per unit of interview burden.

## Before asking

Classify the question reason:
- P0 integrity blocker;
- P1 CV-usability gap;
- P2 target-specific material gap;
- P3 optional enrichment.

Do not ask P3 by default.

## Repetition control

Check known facts, asked intents, answered intents, and required precision before asking.

If already sufficient, skip.

## Topic stopping

Stop when CV_USABLE, no P0/P1 gap remains, and no material target P2 gap remains.

## Session stopping

Stop when major history is mapped and remaining questions are optional enrichment.

## Burden response

If the candidate signals fatigue or answers become increasingly low-effort, finish only the current material blocker, defer enrichment, summarize state, and stop.

## Reuse

Future applications retrieve prior evidence first. New questions are delta-only.
