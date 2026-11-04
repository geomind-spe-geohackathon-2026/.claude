---
name: feedback-no-live-runs
description: Sahand rule 2026-11-02 21:50: for now NO live LLM runs anywhere (no tokens, no OpenRouter calls); fix bugs only, verify offline
metadata:
  type: feedback
  modified: 2026-11-02T20:50:36.276Z
---

Sahand (2026-11-02 21:50 local, geomind thread): "no more live runs; only fix the bugs; run nothing; use no tokens for now; tell everyone this for now".
**Why:** live tests spent money (and ran on Sonnet by accident, see [[feedback-no-anthropic-models]]).
**How to apply:** every prompt/thread until Sahand lifts it: no live run, no live eval/recording, no network check-live, no app rerun on a real model; unset OPENROUTER_API_KEY; verify with fake/scripted providers only; list skipped live steps in reports. Do not suggest live runs to Fatemeh. Added to /mnt/project-files/prompts/geomind-live-run-fixes.md rules; coordinator asked to tell all threads.
2026-11-03 00:44 Sahand (app thread decision card): exception approved — ONE full live DeepSeek test after geomind 0.4.2 is final and wired in the app, cap 1 USD total, on dev with a copy of the competition project (not prod). Otherwise the rule still holds.
