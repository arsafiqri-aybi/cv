# Evaluation Plan v1

## Evidence classes

Keep separate:

1. static repository validation;
2. schema/JSON validation;
3. reasoning behavioral tests;
4. artifact/document tests;
5. scientific claim audit;
6. installation/runtime verification.

Passing one class does not imply another.

## Behavioral evaluation

Use `cases.json`.

For each test:
- provide only the case input + relevant candidate/role data to the runtime;
- do not leak expected answer wording;
- score against `rubric.json`;
- record critical failures separately from style quality.

## Artifact evaluation

When a real CV file is produced, check:
- visual readability;
- text extraction;
- reading order;
- link integrity;
- page breaks;
- headings;
- dates;
- duplicate/hidden text;
- document metadata if relevant.

## Scientific evaluation

For every promoted scientific rule:
- source exists;
- outcome matches claim;
- causal language is justified;
- context is recorded;
- contradiction search was performed;
- uncertainty is explicit.

## Release threshold

A release may be operationally complete without claiming scientific saturation if:
- required architecture exists;
- critical behavioral invariants are covered;
- known limitations are disclosed;
- scientific uncertainty is not hidden;
- runtime behavior is testable.
