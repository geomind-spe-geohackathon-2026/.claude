---
name: feedback-development-modes
description: Three modes (development, production, hotfix) decide branch, tests, the way to main and deploys; ask the mode at every session start; always commit and push
metadata:
  type: feedback
---

Sahand, 2026-11-04 (evening): every piece of work runs in one of three modes. At the start of EVERY session, ask the user which mode this session is in; change nothing until they answer. Full text: `documents/project/ops/development-modes.md` in the project root.

- Development: work on the second branch (`dev`); run every automated test that needs no LLM; the agent fast-forwards `main`, tags, deploys.
- Production: work on `dev`; the same tests; `dev` reaches `main` only through a GitHub pull request a person approves and merges; the agent never merges locally. This replaces the old "no pull requests" rule ([[feedback-no-pull-requests]]) in this mode only.
- Hotfix (the name is just "hotfix", not "QA"): work directly on the default branch (`main`; for gemini it is `dev`, so push gemini only to `dev`); run NO test, lint or check of any kind; tag, push, deploy only that service at once; check again on the live site and go on.
- One clone per repo, no git worktrees (Sahand, 2026-11-04 evening).
- Hotfix, more (Fatemeh, 2026-11-04 20:05 UTC): fix each bug in the repo it really belongs in; when 50/50 between frontend/backend and a Python package, fix it in frontend/backend. Packages need no GitHub build: build the wheel locally into `backend/.tmp/hotfix-wheels/` and `backend/scripts/hotfix_deploy.sh` installs it on top of the image (`Dockerfile.hotfix`); compose never builds. Raise the version in every touched project; put the bug id and title in every commit. Fastest path to production.
- Always: commit and push everything left when a piece of work ends; nothing stays only on the Dell.

**Why:** fast fix-deploy-check loops on the live site, full automated tests for normal work, and a person's review for risky changes.

**How to apply:** first message of a session: ask "development, production or hotfix?"; then follow that mode's column until the user changes it.
