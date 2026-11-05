---
name: feedback-no-tests-now
description: Since 2026-11-05 16:55 UTC no session runs QA tests (live checks on geomind.team, browser checks, LLM/agent runs, QA scenarios) until the user says otherwise; unit tests stay allowed
metadata:
  type: feedback
---

User, Coordinator-IV's chat, 2026-11-05 16:55 UTC, clarified 17:00 UTC ("I mean QA tests"): no
session runs QA tests for now: no live checks or retests on geomind.team, no browser checks, no
agent/LLM runs, no QA scenarios (the timed case run approved at 16:35 UTC is withdrawn). Unit and
code tests that need no LLM stay allowed for the hotfix sessions.

**Why:** the user's call (usage and focus).

**How to apply:** hotfix sessions fix, run their usual offline tests, release and deploy, but do
not verify live; Manual QA passes findings but runs nothing; successors inherit this until the
user lifts it, then delete this file.
