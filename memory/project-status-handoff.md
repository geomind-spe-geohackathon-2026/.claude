---
name: project-status-handoff
description: Where the GeoHackathon work stands (2026-10-27) and what a new thread should do next; links to all docs and files
metadata:
  type: project
  modified: 2026-10-27T22:37:18.984Z
---

State on 2026-10-27 22:40 UTC (first thread "Plan GeoHackathon GEMINI solution"):

Docs (Claude Docs, Persian):
- Plan + GEMINI review: https://claude.ai/artifact/SSfh6RdLGiQwcKx1Wabn4g
- System architecture (dashboard, harness, backend data model, GEMINI service, infra, task split): https://claude.ai/artifact/QxUm2M4Q19fnhrHLM6zfv1

Project files (/mnt/project-files/):
- context/: the 3 competition slides (png), the user's Swarmax ChatGPT notes, the user's local repo tree (backend/frontend/gemini/infrastructure)
- gemini-notes/gemini-repo-tree.md: annotated GEMINI tree
- swarmax-branch/*.patch: my 2 commits (move GEMINI into gemini/, add gemini_service FastAPI with /health, /models, /models/{name}/calculate + tests; Next.js landing; Vite dashboard). Apply with `git am` if the user wants them back.

Repo status: fork swarmax/gemini-geothermal-suite-open, main untouched. Branch swarmax/restructure and gh-pages were deleted by the user on 2026-10-27; only main remains on the fork. Push access works.
The user's real structure is local only, not pushed yet: backend/ (FastAPI, auth, celery, openrouter/postgres/redis/influx/chroma/minio clients), frontend/ (empty), gemini/, infrastructure/.

Decisions: harness lives in backend/src/harness on Celery workers; LLM via OpenRouter; frontend → backend → gemini service; LLMs orchestrate, numbers only from tools.
Inputs of the task are released 2026-10-29. Until then: input-independent work (surface models, yearly simulator, economics, tool wrappers, harness, logging, dashboard Run page).
Open: LLM model choice, SSE vs WebSocket, keep old Flask GUI or not, whether organisers give a demand scenario.

**How to apply:** start a new thread by reading this, [[repo-and-code-preferences]], [[gemini-repo-findings]], [[team-and-roles]]; do not edit the repo until the user explicitly asks.

- 2026-10-28 23:40 idea (user approved): benchmark repo, separate from the GEMINI repo, comparing our package with open-source tools (GEOPHIRES-X closest for design/economics, TESPy closest for plant API, DoubletCalc/ThermoGIS for doublets): feature table + comparable numbers on the same doublet case. Asked coordinator for a separate thread.
- 2026-10-28 23:50 thread "Compare GEMINI with open-source tools": plan at /mnt/project-files/benchmark/plan.md. Proposed repo swarmax/geothermal-benchmark (private); asked user whether I create it (decision card). Installable: GEOPHIRES-X (from GitHub, not on PyPI), pythermogis 0.1.6, tespy 0.11.3, pandapipes 0.16.0, oemof.solph 0.6.5.
- 2026-10-29 21:48 user's local layout: /Users/sahand/Desktop/crust-team/{backend,frontend,gemini,infrastructure}. GEMINI package repo = crust-team/gemini (has gemini/agentic, gemini/design, runs/ locally, not on GitHub refactor yet). Prompts must use these paths.
