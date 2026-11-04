---
name: feedback-session-models
description: Only hotfix sessions may run on Opus; every other Claude Code session (QA, coordinator, helpers) runs on Sonnet (Sahand, 2026-11-04 23:45 UTC)
metadata:
  type: feedback
---

Sahand, 2026-11-04 ~23:45 UTC: only the hotfix sessions may run on Opus (claude-opus-5-5). Every
other Claude Code session of the project (QA, coordinator, helpers) runs on Sonnet
(claude-sonnet-5-5). A successor at handover keeps this rule: pass `model` to `create_session`.
This is about the development sessions only; the geomind agents in the app never use any Claude
model ([[feedback-llm-model]]).

**Why:** usage runs out fast; fixing code needs the strongest model, testing and coordinating less.
**How to apply:** every `create_session` names the model; see [[feedback-qa-round-2]],
[[feedback-session-refresh]].
