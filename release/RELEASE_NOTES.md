# CV v1.3.0 — Release Notes

## Candidate Discovery Interview

Adds a stateful evidence-acquisition interview system designed to gather enough CV evidence without repeatedly asking what the candidate already answered or over-interviewing one topic.

Shipped:
- Master Discovery and Target Delta modes;
- coverage states UNSEEN/DISCOVERED/PARTIAL/CV_USABLE/TARGET_READY/BLOCKED;
- P0-P3 gap priority model;
- semantic intent deduplication;
- bounded probing;
- persistent interview state schema;
- 24 adversarial cases;
- Prompting / Scale / Governor;
- root Skill routing;
- automated audit coverage.

The exact stop states and two-follow-up default are engineering decisions informed by adjacent interview and respondent-burden research, not universal scientific constants.
