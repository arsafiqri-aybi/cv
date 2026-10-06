# Output Contract — CV Document Structure Skill v1.1

For a full document-structure task, produce:

## 1. Structure diagnosis
- candidate context;
- target role;
- evidence distribution;
- machine pathway;
- constraints.

## 2. Section architecture
Use canonical section IDs plus intended display labels.

## 3. Page architecture
- target page count range;
- single-column/multi-column decision;
- page-break strategy;
- information-density strategy.

## 4. Hierarchy specification
Use exact canonical IDs:
- H0 candidate name;
- H1 section heading;
- H2 entry title;
- M1 organization/institution;
- M2 dates/location/metadata;
- B1 evidence bullet;
- B2 supporting detail.

## 5. Entry templates
At minimum when applicable:
- Experience;
- Projects;
- Education.

## 6. Date and chronology specification
State:
- normalized internal precision;
- output language/locale;
- display date pattern;
- ongoing-work token;
- range separator;
- chronology rule.

Use `DATE_STANDARD.md`.

## 7. Typography/layout specification
Clearly distinguish:
- research-backed principles;
- engineering defaults.

## 8. Machine/accessibility specification
- extraction order;
- section semantics;
- PDF rules;
- parser test requirements.

## 9. Editorial consistency specification
Check:
- section naming;
- date format;
- location format;
- technology casing;
- metrics;
- bullet grammar/punctuation;
- link style.

Use `CONSISTENCY_STANDARD.md`.

## 10. QA gates
- human scan;
- text extraction;
- reading order;
- entity/date association;
- PDF integrity;
- editorial consistency;
- factual integrity.

## Completion condition

Do not mark complete until the final exported document has been checked when the artifact exists.
