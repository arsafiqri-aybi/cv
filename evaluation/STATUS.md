# Evaluation Status — v1.0

## Static verification

Status: **PASS**

Executed against persisted repository content.

Checks:
- required release components exist in repository tree;
- graph JSON parses;
- node IDs unique;
- all edge source/target IDs resolve;
- all protected non-edge source/target IDs resolve;
- node/edge/non-edge declared counts match content;
- evaluation-case count matches content;
- factual_fidelity is a critical rubric dimension;
- claim_calibration is a critical rubric dimension;
- fairness_privacy is a critical rubric dimension;
- consistency is a critical rubric dimension;
- release manifest does not claim scientific saturation.

Snapshot:
- nodes: 77
- edges: 70
- non-edges: 12
- adversarial cases: 18
- rubric dimensions: 10

## Behavioral evaluation

### Designed
18 adversarial cases cover:
- weak match;
- career change;
- students;
- team attribution;
- missing metrics;
- fact conflicts;
- keyword stuffing;
- unsupported skills;
- creative layouts;
- academic CVs;
- sensitive personal data;
- unknown ATS;
- knockout constraints;
- AI-polished writing;
- noisy rejection feedback;
- LLM screening;
- no-target-role conditions.

### Not claimed
No independent external model, recruiter panel, or blinded evaluator was run in this release.

Therefore:
- behavioral test **coverage is present**;
- independent behavioral pass-rate is **NOT_CLAIMED**.

## CI

GitHub Actions workflow installation was attempted but the GitHub Operator connection returned:
`workflow_writes_not_enabled`.

Deterministic audit scripts are retained in the repository for execution in another environment.
