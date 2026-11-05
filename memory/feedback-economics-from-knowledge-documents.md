---
name: feedback-economics-from-knowledge-documents
description: case lead may recommend economics from any sourced Knowledge document; an assumptions document covering the case comes first
metadata:
  type: feedback
---

User decision (2026-11-05 ~10:08 UTC, via Coordinator-III): in `ask_economics` the case lead may
recommend a value from ANY Knowledge document that states it with a source (an assumptions file
the user put in Knowledge), not only cost-sources catalogue rows: `{key, value, unit, source}`
citing the document. An assumptions document that covers the case comes first, so the economics
match it in one question. Keys neither the files nor Knowledge give (for example
`opex.per_energy.*`, `revenue.subsidy.*`) go to `open`, never invented. Keep the prompts general,
not hackathon-specific.

**Why:** the hackathon case guide and assumptions file give the sample's economics; catalogue-only
recommendations made the economics differ from gemini's sample and its rankings.

**How to apply:** geomind 0.4.80 `prompts/case/lead.md` (economics section, per-energy rule);
the handbook `documents/project/quality-assurance/inputs/handbook-case-definition.md` (chapter 12,
the hackathon example) must agree
with the prompt.
