---
name: feedback-no-pull-requests
description: Sahand 2026-11-03 08:57 +0100: don't open pull requests; merge locally into dev, test, push; then dev -> main and deploy when OK
metadata:
  type: feedback
---

Sahand (2026-11-03 08:57 +0100, WEBSITE UX I): do not open pull requests "for nothing". Merge the work branch locally into whatever needs it (dev), and if a PR already exists, close it and delete the branch. 08:58: "if it is OK, take it to main yourself and deploy".
**Why:** PRs only add waiting; Sahand trusts local tests + the dev -> main rule.
**How to apply:** branch -> local merge into dev -> `npm run check` / build -> push dev -> fast-forward main -> deploy (frontend/backend deploys run on the NTNU Dell via the app thread BACKEND I, see run-services.md). No PRs. Related: [[repo-and-code-preferences]], [[hosting]].

**Changed 2026-11-04 (evening):** this holds in development and hotfix mode only. In production mode, dev reaches main only through a pull request a person approves on GitHub. See [[feedback-development-modes]].
