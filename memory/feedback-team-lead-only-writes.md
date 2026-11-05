---
name: feedback-team-lead-only-writes
description: IMP-025 design rule: only a team lead reads and writes project files; up to 4 sub-agents per task compute and return results; lead writes once, re-splits until done, reports to the project manager (2026-11-05)
metadata:
  type: feedback
---

User, Coordinator-IV's chat, 2026-11-05 16:05 UTC, the design of parallel agents (IMP-025):

1. Only the team lead of a team reads and writes the project's files (case, plant, studies,
   results, inputs). Sub-agents have NO read or write access to project files.
2. The lead takes a task, splits it into at most 4 sub-tasks and gives each to a sub-agent of its
   own team (same role or different roles: "Geoscientist I", "Geoscientist II", ...). The lead
   puts into each brief everything the sub-agent needs.
3. Sub-agents only do their sub-task and return the result to the lead.
4. When all sub-tasks are back, the lead writes ONCE. If a problem remains (gemini refuses, a gap),
   the lead splits it again among its team's sub-agents, and repeats until the task is done.
5. Then the lead reports to the project manager (project lead).

**Why:** one writer per team: no clashing saves, fewer refusals, faster runs.

**How to apply:** geomind: sub-agent tool sets hold no read/write tools for project files (only
pure compute and, where needed, Knowledge reading, which the user did not forbid: ask if unsure);
Team takes at most 4 briefs; lead prompts/skills follow steps 1-5. Backend: only the lead's
events save versions. Frontend: one line per sub-agent under its lead.
