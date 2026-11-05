---
name: feedback-gemini-changes-allowed
description: Hotfix sessions may change gemini without asking for permission first (user, 2026-11-05); replaces the old "ask Sahand before any gemini change" rule
metadata:
  type: feedback
---

User, in Coordinator-III's chat, 2026-11-05 11:00 UTC: "for gemini you no longer need to ask
permission; make the change". Hotfix sessions change gemini (on its default branch `dev`), release
patch versions and deploy them at the half-hour windows like the other repos, with tests for the
change. The older rules [[gemini-requests-need-approval]] and the AGENTS.md line "Nobody asks
gemini for anything without Sahand's permission" are superseded for this QA/hotfix round.

Every gemini commit message says what changed and why (bug id), so the pull request to GEMINI's
development branch can list our gemini fixes. The gemini API freeze stays: public APIs do not change.

**Why:** gemini fixes were blocking the QA round (QA-104, QA-107).
**How to apply:** fix gemini directly when the cause is there; tell the coordinator the version.
