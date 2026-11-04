---
name: hosting-package-pinning
description: Prod images must install gemini/geomind as pinned released versions from registries, not -e or local build contexts
metadata:
  type: project
---
Rule from Sahand (2026-11-02 22:44 +0100, project-wide): nobody installs packages with `-e`. Producers build and push releases to a registry; consumers pin released versions. geomind releases come from branch main (dev holds changes headed for main); gemini releases come from branch dev.

geomind: history rewritten 2026-11-03 (main d9a0aaf, tag v0.4.2=2512cb4, c9a5c1c unchanged); 0.4.3 released (tag v0.4.3=6c7bb46, wheel sha256 836f343b..., private repo -> local wheel pinned by hash); prod waits for BACKEND I pins, then needs GEOMIND_CONTEXT_WINDOW=128000.
Morning deploy waiting for Sahand: /mnt/project-files/notes/prod-morning-deploy-2026-11-03.md (migration 0010, geomind 0.4.13 (NEVER 0.4.12), GEOMIND_GEMINI_THREADS unset, MALLOC_ARENA_MAX=2 via Dockerfile ENV).
Prod since 2026-11-03 02:31 (backend 5ce532c): gemini 0.5.5 and geomind 0.4.3 both installed from hash-pinned wheels; no -e and no build contexts. DONE.

**Why:** reproducible, pinned deploys; no drift from local checkouts.
**How to apply:** once gemini 0.5.4 and a geomind release are published and the backend Dockerfile/requirements pin them, rebuild prod from those pins only and drop the build contexts. Do not do a prod deploy that reintroduces local/editable installs. See [[hosting]].

Worktree rule (Sahand 2026-11-03 01:03 +0100): all git worktrees and build trees only under the repo's own `.tmp/` (git-ignored). Prod deploy build trees go in `<repo>/.tmp/deploy-<commit>/`, removed after the build.

Branch rule (Sahand 2026-11-03 01:31 +0100, all repos incl. infrastructure): new work on dev, main stays stable; only dev and main survive (delete or tag merged branches). Test locally on a local server, merge dev->main when tests pass, deploy prod ONLY from main (backend and frontend). Hosting: before each deploy, verify the pin is on origin/main. infrastructure dev created at 9af0ef5.
