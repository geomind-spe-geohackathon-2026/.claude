---
name: feature-agent-tools
description: Sahand 2026-11-05: geomind gets a skills folder (geomind/geomind/skills, per tool, per role) and three tools: calculate (sourced operands only), run_python (Docker sandbox), web_search/read_web_page (self-hosted SearXNG)
metadata:
  type: project
---

Sahand asked on 2026-11-05 (~00:00 UTC) for three agent tools and a skills folder, built now in
hotfix mode. The calculator only combines numbers that have a source; agents never invent the
operands. Python runs in the Docker sandbox. Web search uses self-hosted SearXNG (free, no key);
agent-browser was rejected for the app's agents (heavy, token-costly, blocked, unsafe). Web values
go to user approval with source.

**Why:** agents need arithmetic and code without making up numbers, and a source for data no
file, Knowledge row or connector gives.
**How to apply:** spec `.claude/notes/features/agent-tools-2026-11-05.md`; owners hotfix-python,
hotfix-back, hotfix-front. See [[feedback-no-defaults]], [[feedback-decisions-2026-11-05]].
