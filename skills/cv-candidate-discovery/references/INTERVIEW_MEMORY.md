# Interview State and Memory v1.0

Update state after every answer before generating the next question.

Persist:
- known_facts
- evidence_items
- episodes
- asked_intents
- answered_intents
- open_gaps
- contradictions
- deferred_optional
- candidate_preferences
- optional target_application

Before asking:
question -> derive intent_key -> check known facts -> check answered intents -> check asked intents -> check contradictions/open gaps -> ASK / DELTA / SKIP.

Once a fact exists in the Master Candidate Evidence Base, future application interviews should retrieve it rather than ask again.

Do not silently erase corrections. Preserve old value, new value, source, preferred interpretation, and confidence.

Do not ask for reconfirmation after every answer. Use checkpoints only after major timeline blocks, when contradictions exist, or before finalization.
