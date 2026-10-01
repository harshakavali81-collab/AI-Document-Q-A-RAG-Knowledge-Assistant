# Data dictionary and metric definitions

| Artifact/field | Type | Meaning |
|---|---|---|
| Chunk.id | string | Stable content/location-based hash within the current document version |
| Chunk.source | string | Original document filename |
| Chunk.location | string | PDF page, DOCX paragraph/table or TXT section |
| Chunk.text | string | Cleaned passage used for retrieval |
| question | string | Standalone evaluation question |
| source | string or null | Expected source; null means unsupported question |
| evidence | string or null | Annotated phrase that must appear in retrieved evidence |
| evidence_hit_at_3 | boolean or null | Expected source and evidence phrase found within top 3; null for unsupported questions |
| abstained | boolean | No chunk met retrieval threshold; not a measured LLM refusal |
| milliseconds | number | Retrieval-only elapsed time on the original small-corpus run |

**Evidence hit rate at 3** = answerable questions with matching evidence / all answerable questions. Recorded result: 23 / 25 = 92%.

**Unsupported-question abstention rate** = unsupported questions returning no chunks / all unsupported questions. Recorded result: 3 / 5 = 60%.

Both use an authored development fixture, not a held-out production benchmark. Neither is generated answer accuracy. Sample policies and product facts are invented for testing.
