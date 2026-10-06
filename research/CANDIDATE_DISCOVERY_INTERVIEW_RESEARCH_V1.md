# Candidate Discovery Interview Research v1.0

## Research question

How should a CV-building interview collect enough candidate evidence without repeatedly asking what is already known or over-interviewing one topic?

## Evidence boundary

There is no large direct literature validating a distinct "CV evidence-acquisition interview" method. This subsystem therefore adapts adjacent evidence from structured interviewing and respondent-burden research, while labeling its stop rules and probe limits as engineering decisions.

## Structured coverage

Structured interview research shows benefits from job-related question design, consistent coverage, explicit evaluation criteria, and controlled probing. Relevant sources include Campion, Pursell, & Brown (1988), Campion, Palmer, & Campion (1997), and Levashina et al. (2014).

Sources:
- DOI 10.1111/j.1744-6570.1988.tb00630.x
- DOI 10.1111/j.1744-6570.1997.tb00709.x
- DOI 10.1111/peps.12052

Operational adaptation:
- structure the evidence fields;
- adapt follow-up questions to actual gaps;
- do not force an exhaustive fixed questionnaire.

## Probing

Patel et al. (2025) found benefits from structured probing in asynchronous interviews.

Source:
- DOI 10.1111/ijsa.12514

Operational adaptation:
- use a follow-up only when it resolves a defined evidence gap;
- do not probe automatically after every answer.

## Respondent burden

Krosnick (1991) describes satisficing under cognitive demand. Yan & Williams (2022) model response burden as cumulative throughout an interview/survey process.

Sources:
- DOI 10.1002/acp.2350050305
- DOI 10.2478/jos-2022-0041

Operational adaptation:
- do not repeat answered questions;
- stop after evidence becomes usable;
- prefer delta questions to restarting a topic.

Rolstad, Adler, & Rydén (2011) found longer questionnaires were associated with lower response rates overall, while emphasizing that content matters and shorter is not automatically better.

Source:
- DOI 10.1016/j.jval.2011.06.003

## Runtime synthesis

The interview should be:

STRUCTURED IN COVERAGE
+ ADAPTIVE IN PROBING
+ STATEFUL IN MEMORY
+ BOUNDED BY SUFFICIENCY

The exact coverage states, P0-P3 priorities, and default probe budget are project engineering decisions, not scientific constants.
