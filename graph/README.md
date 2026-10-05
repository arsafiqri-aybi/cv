# CV Knowledge Graph v1

The graph is many-to-many.

Files:
- `nodes.json` — operational constructs
- `edges.json` — directional typed relationships
- `non_edges.json` — distinctions that must not be collapsed

## Relationship types

- requires
- produces
- supports
- associated_with
- scoped_by
- constrains
- instantiates
- reduces
- evaluated_by
- influences
- threatens
- drives
- implements
- precedes
- biases
- enables
- feeds
- may_influence
- evaluates_against
- evaluates
- related_to
- not_equivalent

## Graph rule

An edge is not a causal claim unless its relationship type and evidence explicitly justify causality.

The runtime reasoning engine may use the graph to retrieve relevant neighboring constructs, but it must preserve:
- evidence status;
- context boundary;
- contradictions;
- protected non-edges.
