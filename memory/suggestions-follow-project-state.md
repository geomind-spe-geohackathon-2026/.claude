---
name: suggestions-follow-project-state
description: "geomind next-step suggestions must come from the project's current state, never generic"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3aea9698-789f-59b6-93b1-7cd4178ef35d
  modified: 2026-11-04T00:14:09.939Z
---

Next-step suggestions (run.finished.suggestions, gd.suggest) must follow the project's current
state across all its chats (files, case, plant, study, results, report), never generic chips.

**Why:** Sahand (2026-11-03): "suggestions must not be in the air; they must follow the current state".

**How to apply:** stage from `Workspace.project_state` (backend), falling back to the chat's problem state; stale study → "run the study again" first; all done → more studies (sensitivity, evolve, other objectives, other case). See [[ux-direction-agent-first]].
