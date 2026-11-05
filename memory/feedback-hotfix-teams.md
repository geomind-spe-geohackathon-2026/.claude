---
name: feedback-hotfix-teams
description: Hotfix work runs as three teams (python, back, front), each one lead + 3 members; members only edit files, the lead splits work, commits, pushes and deploys
metadata:
  type: feedback
---

Sahand, 2026-11-05 18:37 Trondheim (Coordinator-V's thread): to fix bugs in parallel, each hotfix
area is a team: `hotfix-<area>-lead` and `hotfix-<area>-member-<id>-<gen>` (area python, back,
front; id 1-3; gen roman numeral of the session generation), e.g. hotfix-python-member-2-I.

Rules:
- The lead claims bugs with qa.py, splits them into tasks and gives each member a task with an
  explicit list of files it owns. No two members ever own the same file at the same time.
- Members only edit their own files in the shared clone (hotfix mode: no branch, no worktree),
  run quick checks that need no LLM, and report to the lead: what changed, which files, how to check.
  Members never git add/commit/push, never deploy, never run qa.py set.
- The lead reviews, stages by path, commits per bug, pushes, deploys with hotfix_deploy.sh
  (local build, no GitHub wait), and sets the bug fixed with qa.py.
- Leads coordinate across teams through Coordinator-V (shared files, contracts).
- CPU: ≤ ~24 cores in total on the Dell; members nice long jobs.

**Why:** one hotfix thread per area could not keep up with the QA threads (~70 bugs in an hour).
**How to apply:** route bugs to the team lead of the area; the lead does the rest.
