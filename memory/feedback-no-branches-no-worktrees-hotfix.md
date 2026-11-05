---
name: feedback-no-branches-no-worktrees-hotfix
description: In hotfix mode no session creates a branch or a worktree; all work is on the default branch in the shared clone (user, 2026-11-05)
metadata:
  type: feedback
---

User, 2026-11-05 (Coordinator-V's chat): every session works in hotfix mode directly on the repo's
default branch (`main`; gemini `dev`) in the shared clone. Never create a new branch (no `wip/*`,
no feature branch) and never a git worktree. Older WIP branches (e.g. `wip/hotfix-python-V`) are
brought onto main and not continued.

**Why:** branches and worktrees split the shared clones and stall deploys; hotfix mode ships from
the default branch at once.
**How to apply:** tell every new or restarted session this in its first prompt; a session that
cannot edit the clone asks the user, it does not switch to a worktree. See
[[reference-start-sessions-bg-remote-control]].
