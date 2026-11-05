---
name: feedback-local-builds-git-push-only
description: Never wait for a GitHub release or build; push every change, build wheels and deploy locally
metadata:
  type: feedback
---

Sahand, 2026-11-05 16:54 UTC (hotfix-python thread): never wait for a release or a package build
on GitHub. Push every change, then go on locally (no wheels by hand any more, see the end). Git
is only for pushing code, never for building packages. A pushed commit (and its tag) is enough
to deploy; do not wait on GitHub Actions or a GitHub release asset.

**Why:** waiting on GitHub releases held fixes back from production.

**How to apply:** in every mode and for every repo (geomind, gemini, backend, frontend): commit,
push, build locally, deploy at once by the mode's deploy steps.

Sahand, 2026-11-05 16:54 UTC: releases and deploys need no OK from him any more (every package,
gemini included): release, push, build locally and deploy at once.

Sahand, 2026-11-05 16:55 UTC: a package session (geomind, gemini) does NOT build wheels either:
the backend builds geomind and gemini itself from the pushed code (hotfix-back-VI sets this up).
A package session only commits and pushes; the backend side builds and deploys.

LIVE since backend 1.1.104 (hotfix-back-VI, 2026-11-05): `backend/scripts/hotfix_deploy.sh` checks
that the gemini (`dev`) and geomind (`main`) clones are committed and pushed, `git archive`s their
HEAD and builds both into the image (`backend/Dockerfile.hotfix`). To ship a geomind or gemini fix:
commit and push it, then a backend session bumps the backend version and runs the script.
`.tmp/hotfix-wheels` is no longer read.
