---
name: feedback-coordinator-prompts
description: Sahand rule (2026-11-01 00:16): every Claude Code prompt runs in parallel with the main session as a pure coordinator that dispatches and merges, never doing the work itself
metadata:
  type: feedback
---

Sahand: tasks must run in parallel; Claude Code acts as coordinator, hands out tasks and collects them, and must not burn its own context doing the work. "Remember this."
**Why:** big prompts ran long and the main session's context filled with file dumps.
**How to apply:** in every prompt: main session only plans, dispatches subagents (sonnet for work, haiku for read-only search), each in its own worktree with disjoint file ownership, reviews diffs/summaries, merges, runs tests once; subagents report short summaries and write details to .tmp/<task>/; the main session never edits many files or reads large files itself. Supersedes the 2026-10-31 18:55 "parallel" note in [[prompt-writing-rules]].
2026-11-01 00:25: Sahand's Mac has no /mnt/project-files; a prompt that pointed at a project-files note blocked the run. **Every prompt must be self-contained**: embed reference material in the prompt (appendix), never refer to /mnt/project-files paths.
