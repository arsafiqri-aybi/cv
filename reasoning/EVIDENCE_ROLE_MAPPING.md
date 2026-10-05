# Evidence ↔ Role Mapping v1

## Mapping record

For every material target requirement, create zero or more candidate evidence links.

Each link should record:

```text
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

A practical priority is based on multiple dimensions, not a single magic score:

```text
role importance
× evidence relevance
× evidence strength
× transferability
× recency/context fit
```

This expression is conceptual. Do not multiply arbitrary pseudo-precise numbers unless a validated scoring scheme is later defined.

## Gap types

- hard-constraint gap;
- evidence gap;
- wording gap;
- provenance gap;
- transferability gap;
- recency gap;
- unknown.

## Construction consequence

High-priority, well-supported evidence should generally receive more document salience.

But section order remains context-dependent and must also respect:
- career stage;
- occupation;
- document conventions;
- reader needs;
- machine parseability.
