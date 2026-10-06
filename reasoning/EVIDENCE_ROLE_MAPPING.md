# Evidence ↔ Role / Application Mapping v1.1

## Mapping record

For every material target requirement, create zero or more candidate evidence links:

```text
application_id
requirement_id
evidence_id
match_type
relevance
transferability
evidence_strength
confidence
notes
```

## Match types

- direct;
- adjacent;
- transferable;
- credential-only;
- weak;
- none.

## Priority logic

Conceptually consider:

```text
role importance
× evidence relevance
× evidence strength
× transferability
× recency/context fit
```

Do not turn this into arbitrary pseudo-precision.

## Application context

Company/vacancy context may change:
- requirement importance;
- terminology;
- transferability interpretation;
- evidence salience.

It may not change:
- candidate facts;
- ownership;
- unsupported skill status;
- claim ceiling.

## Gap types

- hard-constraint gap;
- evidence gap;
- wording/terminology gap;
- provenance gap;
- transferability gap;
- recency gap;
- freshness gap;
- unknown.

## Construction consequence

High-priority supported evidence should receive more salience.

Use `reasoning/APPLICATION_TARGETING.md` for variant decisions.
