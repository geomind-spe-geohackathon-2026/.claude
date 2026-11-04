---
name: feedback-worktrees-under-tmp
description: Sahand rule 2026-11-03 01:03 +0100: every git worktree lives only under its repo's own .tmp/ folder; .tmp ignored in every repo
metadata:
  type: feedback
---

Sahand (2026-11-03 01:03 +0100, project-wide, "tell everyone"): anyone who needs a git worktree creates it under the repo's own `.tmp/` (e.g. `<repo>/.tmp/<name>`), nowhere else (no sibling ../repo-x folders). `.tmp` must be in .gitignore in every repo; geomind's committed `.tmp/live` must be purged from git history (geomind thread).
**Why:** stray worktrees and sibling folders cluttered the machines, and `.tmp/live` got committed to geomind.
**How to apply:** `git worktree add .tmp/<name> <branch>`; check .gitignore has `.tmp/` before creating; remove worktrees when done. Related: [[local-layout]], [[repo-and-code-preferences]].

**Replaced 2026-11-04 (evening):** no git worktrees any more. Each repo has one clone in the project root; work in it on the branch the mode names ([[feedback-development-modes]]).
