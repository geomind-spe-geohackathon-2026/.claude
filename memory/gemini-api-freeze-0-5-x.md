---
name: gemini-api-freeze-0-5-x
description: "Sahand's rule: no change to gemini APIs already given to others; version stays 0.5.x; next focus after fixes is speed"
metadata:
  type: project
---

Sahand, 2026-11-03: gemini's APIs given to others do not change. The version stays 0.5.x (patch may go as high as 0.5.100) and the minor never rises. After open problems are fixed, the next priority is making the package run faster.

**Why:** other projects depend on the API, and no API change is planned for now.

**How to apply:** speed work must keep every public name, signature and output; check `test_api_compatibility` and `test_competition_surface`. See [[package-release-plan]] and [[gemini-workspace]].
