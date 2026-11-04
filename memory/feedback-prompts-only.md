---
name: feedback-prompts-only
description: When the user pastes a task, they usually want a Claude Code prompt written, not the work done here
metadata:
  type: feedback
---

2026-10-29 user: "I only want you to give me a prompt, not do anything else." I had started doing
the porting analysis in the cloud repo.
**Why:** the user runs the work in their local Claude Code; I write the prompts.
**How to apply:** when a task arrives, write/refine a prompt into /mnt/project-files/prompts/
following [[prompt-writing-rules]]; do not clone, edit or analyse the repo unless asked explicitly.

2026-10-30 08:17 user: during design talk, do NOT hand over or edit prompts; just discuss. Only write/give the next prompt when the user says "go" (give it) — that also means the previous prompt has been run.
