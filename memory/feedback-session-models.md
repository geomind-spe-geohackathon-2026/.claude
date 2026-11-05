---
name: feedback-session-models
description: Only hotfix sessions and the coordinator run on Opus; QA and every other Claude Code session runs on Sonnet (Sahand, 2026-11-04 23:45-23:55 UTC)
metadata:
  type: feedback
---

Sahand, 2026-11-04 ~23:45 UTC: only the hotfix sessions may run on Opus (claude-opus-5-5). At
~23:55 UTC he added: the coordinator stays on Opus too (core work). Every other Claude Code
session of the project (QA, helpers) runs on Sonnet (claude-sonnet-5-5). A successor at handover keeps this rule: pass `model` to `create_session`.
This is about the development sessions only; the geomind agents in the app never use any Claude
model ([[feedback-llm-model]]).

**Why:** usage runs out fast; fixing code needs the strongest model, testing and coordinating less.
**How to apply:** every `create_session` names the model; see [[feedback-qa-round-2]],
[[feedback-session-refresh]].

**Change, 2026-11-05 16:50 UTC (user, Coordinator-IV's chat):** the backend and frontend hotfix
sessions (hotfix-back-*, hotfix-front-*) run on Sonnet (claude-sonnet-5-5). hotfix-python-* and
the coordinator stay on Opus.
