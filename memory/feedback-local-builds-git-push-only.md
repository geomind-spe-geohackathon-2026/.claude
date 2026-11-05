---
name: feedback-local-builds-git-push-only
description: Never wait for a GitHub release or build; push every change, build wheels and deploy locally
metadata:
  type: feedback
---

Sahand, 2026-11-05 16:54 UTC (hotfix-python thread): never wait for a release or a package build
on GitHub. Push every change, then go on locally: build the wheels on the Dell
(`backend/.tmp/hotfix-wheels/`, `pip wheel ../geomind` / `../gemini`) and deploy from them. Git
is only for pushing code, never for building packages. A pushed commit (and its tag) is enough
to deploy; do not wait on GitHub Actions or a GitHub release asset.

**Why:** waiting on GitHub releases held fixes back from production.

**How to apply:** in every mode and for every repo (geomind, gemini, backend, frontend): commit,
push, build locally, deploy at once by the mode's deploy steps.

Sahand, 2026-11-05 16:54 UTC: releases and deploys need no OK from him any more (every package,
gemini included): release, push, build locally and deploy at once.
