---
name: fresh-sessions-for-work
description: Sahand wants heavy work done in fresh sessions (subagents) on the NTNU Dell to keep token use down
metadata:
  node_type: memory
  type: feedback
  originSessionId: 79f44894-62ce-5cab-9c31-1e512b813fd8
  modified: 2026-11-03T23:50:50.348Z
---

Sahand (2026-11-03 23:50 UTC): "use fresh sessions on the NTNU Dell wherever you can so our token use in Claude Code doesn't grow".

**Why:** a long coordinating session's context gets expensive; fresh sessions start small.

**How to apply:** delegate implementation, test runs and investigations to fresh subagents, working in the repo's one clone (no worktrees since 2026-11-04 evening); keep the main session for coordination, merges, release and reports. See [[gemini-workspace]].
