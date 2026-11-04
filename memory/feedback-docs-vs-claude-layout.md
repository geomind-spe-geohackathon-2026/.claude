---
name: feedback-docs-vs-claude-layout
description: docs/ is for people, .claude/ and AGENTS.md are for agents; one layout in the project root and every repo
metadata:
  type: feedback
---

Sahand, 2026-11-04 (evening): `docs/` anywhere is for people; `.claude/` and `AGENTS.md` anywhere are for agents and Claude Code sessions. Every session must read both, so each `AGENTS.md` points to both. Everything handed over lives in the project root's `.claude/` (project-wide) or in the repo it is about, so parallel sessions read one source.

**Why:** parallel sessions on the Dell each had their own memory and copies; they drifted.

**How to apply:** follow `.claude/README.md` in the project root: `docs/<topic>/` for people; `.claude/docs` (reference), `.claude/notes` (current work), `.claude/archive` (finished prompts, phases, old notes); lowercase kebab-case names, dated snapshots end in `-YYYY-MM-DD`. Project-wide memory is `.claude/memory/` in the project root; add or change a fact there, not in a session's private memory. See [[shared-clones-and-production]].

**Since 2026-11-04 20:15 UTC:** the project root's people folder is `documents/` (repo `documents`, one folder per repo plus `project/`); the project root's `.claude/` is the repo `.claude`, with the project guide `.claude/AGENTS.md`; the root keeps only `CLAUDE.md` (`@.claude/AGENTS.md`), a pointer `AGENTS.md` and `README.md` (see `.claude/setup.md`). Repos keep `docs/`.
