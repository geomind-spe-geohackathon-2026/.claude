---
name: feedback-hotfix-build-local
description: In hotfix mode the backend image builds gemini and geomind from the local clones (Dockerfile.hotfix); never wait for GitHub releases or package builds
metadata:
  type: feedback
---

Sahand, 2026-11-05 18:19 Trondheim (Coordinator-V's thread): in hotfix mode nobody waits for a
GitHub release, a GitHub Actions run or a published package. The backend builds itself with
`backend/Dockerfile.hotfix`, taking gemini and geomind straight from the local clones on the Dell
(backend 1.1.104+), and `hotfix_deploy.sh` deploys at once.

**Why:** GitHub release and package pipelines are slow; hotfix mode exists to ship fixes at once.

**How to apply:** fix -> commit and push (for history) -> tag if the mode says so -> run
`hotfix_deploy.sh` with the hotfix Dockerfile right away. Do not block on GitHub release jobs, wheel
uploads or CI. Related: [[feedback-development-modes]], [[feedback-hotfix-deploy-every-half-hour]].
