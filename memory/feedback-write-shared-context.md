---
name: feedback-write-shared-context
description: Write what every session needs into the root .claude at once (memory for rules, STATUS.md for state, QA for bugs); tell running sessions
metadata:
  type: feedback
---

Fatemeh, 2026-11-04 (evening): every important thing all sessions need must always be written into the project root's `.claude/` so every session reads it quickly; tell the sessions so.

**Why:** many parallel Claude Code sessions work on the same clones; a fact kept in one chat or one private memory is lost to the others.

**How to apply:** the moment you learn it: a user rule or decision -> `.claude/memory/<file>.md` + one line in `MEMORY.md`; a change of state (deploy, version, branch, blocker, open decision) -> `.claude/STATUS.md` with the UTC time; a bug -> `documents/project/quality-assurance/`. Read `STATUS.md` first in every session. See [[feedback-docs-vs-claude-layout]], [[feedback-development-modes]].
