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

Sizing (Sahand approved 2026-11-05 18:38 Trondheim): members only where the queue needs them. Now:
python team = lead + 8 members (Sahand 2026-11-05 19:26 Trondheim, queue ~48); back and front = lead + 2 members each (Sahand 19:28 Trondheim); every lead only assigns, collects, commits, pushes, deploys. Add members to a team when its open
queue passes ~8 bugs; drop idle members.

Lead does no fix work (Sahand, 2026-11-05 19:26 Trondheim): a team lead never works on a bug or
task itself. It only claims, splits, assigns, reviews, commits, pushes, deploys and updates qa.py.
Every bug, even a blocker, goes to a member.

CHANGE (Sahand approved 2026-11-05 20:52 Trondheim), replaces "members never commit" and
"lead assigns every task":
1. Members commit and push their OWN fixes: `git add <their files>` by path only, one commit per
   bug, `git pull --rebase` then push. Still no deploy by members. The lead keeps a table
   member -> bug -> files (in its checklist) so no two members own the same file.
2. Members pull their next bug themselves: `qa.py next --area <area> --fixer <member name>` and take
   it only if its files are inside their own area (python: m-case/economics, m-design, m-gemini,
   m-studies ... as the lead set); otherwise leave it and take the next. They tell the lead in one line.
3. Triage: blockers and majors first, especially anything that changes the numbers or the
   competition answer; minor and cosmetic bugs wait until the major queue is empty.
The lead: assigns areas, resolves file conflicts, deploys in batches (~every 10 min), sets
qa.py fixed with the deployed version, and asks QA threads to retest right after each deploy.
