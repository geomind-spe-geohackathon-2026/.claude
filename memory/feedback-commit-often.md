---
name: feedback-commit-often
description: Every session commits and pushes as often as it can, one change per commit, with messages that say what and why, so any change can be reverted later (Sahand, 2026-11-05)
metadata:
  type: feedback
---

Sahand, 2026-11-05 ~02:00 UTC: every session commits and pushes as often as it can, in every
repo it touches (code, `.claude`, `documents`), so he can follow the work on GitHub and revert a
change when needed.

- One change per commit: one bug fix, one feature step, one role's prompt, one doc update. Never
  mix two fixes in one commit.
- The message says what changed and why, with the ids: e.g. "QA-071: web_search sends
  language=en and refuses queries over 8 words", "feature evolve-structures: structure plant
  endpoint (GET/POST)". Not "fix", "update", "wip".
- Push right after each commit (stage by path; shared clones).
- A release or deploy names its version in the tag and the message.

**Why:** a clean, small history makes `git revert <commit>` safe when a hotfix goes wrong.
**How to apply:** also in `notes/qa-round-2/common.md` and every new session's prompt; see
[[feedback-development-modes]], [[feedback-usage-limit-pause]].
