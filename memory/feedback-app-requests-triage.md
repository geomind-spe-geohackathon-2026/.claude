---
name: feedback-app-requests-triage
description: Sahand rule 2026-11-02 20:30 (+0100) on how gemini handles requests from frontend/backend/geomind
metadata:
  type: feedback
---

Sahand (2026-11-02 19:30 UTC): when the frontend (or other consumers) asks gemini for something:
- a NEW FEATURE it needs, or a BUG report that shows a real error in gemini's calculation logic -> fix it in gemini.
- anything that is really a refactor/workaround on their side or a misuse -> do NOT change gemini; tell them the correct way to use gemini, in their own thread (via coordinator).
**Why:** gemini is the source of truth ([[feedback-contribution-gemini-source-of-truth]]) and is backward compatible from 0.5.0 ([[feedback-gemini-api-freeze]]); consumers adapt to it.
Same day: Sahand agreed `range` on a case value is meaningless (case = outside world; search space = plant range/options; outside variation = uncertainty). Decision: keep reading it (compat), check() warns it has no effect, docs mark it deprecated.
