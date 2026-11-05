---
name: feedback-no-tests-now
description: Since 2026-11-05 16:55 UTC no session runs any test (unit, live check, browser, LLM run) until the user says otherwise
metadata:
  type: feedback
---

User, Coordinator-IV's chat, 2026-11-05 16:55 UTC: neither the coordinator nor any session runs
any test for now: no unit or integration test runs, no live checks on geomind.team, no browser
checks, no LLM runs (the timed case run approved at 16:35 UTC is withdrawn).

**Why:** the user's call (usage and focus).

**How to apply:** hotfix sessions fix, release and deploy only; Manual QA passes findings but runs
nothing; successors inherit this until the user lifts it, then delete this file.
