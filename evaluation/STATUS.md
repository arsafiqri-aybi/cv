# Evaluation Status — v1.0

## Static verification

Status: **PASS**

Checks:
- required release components exist;
- graph JSON parses;
- node IDs unique;
- all edge source/target IDs resolve;
- all protected non-edge IDs resolve;
- declared counts match;
- evaluation-case count matches;
- factual_fidelity is critical;
- claim_calibration is critical;
- fairness_privacy is critical;
- consistency is critical;
- scientific saturation is not claimed.

Snapshot:
- nodes: 77
- edges: 70
- non-edges: 12
- adversarial cases: 18
- rubric dimensions: 10

## GitHub Actions

Status: **INSTALLED_AND_PASSING**

Workflow:
`.github/workflows/validate.yml`

First run:
- run ID: 37392045537
- job ID: 112039162963
- conclusion: **success**

Validated steps:
1. checkout repository;
2. set up Python 3.12;
3. compile both validator scripts;
4. run repository static audit.

## Behavioral evaluation

18 adversarial test definitions cover:
- weak match;
- career change;
- student/no experience;
- team attribution;
- absent metrics;
- conflicting facts;
- keyword stuffing;
- unsupported skills;
- creative layout;
- academic CV;
- sensitive data;
- unknown ATS;
- hard constraints;
- AI-polished prose;
- noisy rejection feedback;
- LLM screening;
- no-target-role conditions.

Independent recruiter/model pass-rate is **NOT_CLAIMED**.
