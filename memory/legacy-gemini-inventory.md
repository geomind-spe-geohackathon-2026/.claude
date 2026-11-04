---
name: legacy-gemini-inventory
description: Results of the read-only feature inventory of the old GEMINI Flask app (gemini-legacy) on the user's Mac, for reimplementation
metadata:
  type: project
  modified: 2026-10-30T08:49:53.289Z
---

2026-10-30: user wants to reimplement the old GEMINI Flask backend and frontend themselves.
Source on user's Mac: /Users/sahand/Desktop/crust-team/gemini-legacy (read-only).
Prompts: /mnt/project-files/prompts/legacy-flask-feature-inventory.md and legacy-frontend-feature-inventory.md.
Outputs (user's Mac): backend moved to /Users/sahand/Desktop/crust-team/gemini-legacy-backend-analysis/backend-features.md (08:55 user: backend only, no frontend analysis at all).
gemini-legacy-frontend-features.md (frontend, running 2026-10-30 08:49); scratch .tmp-legacy-scan/ (routes.json).

Backend result: 98 features, 150 routes. Biggest domain well integrity (29), plants/assets (12).
Services: MySQL, InfluxDB, MongoDB, Redis, ChromaDB, Ollama, Grafana, AVEVA Data Hub, external schematic server
(hard-coded 185.92.222.87:8001/generate, no source). Domain data mostly JSON under gemini-project/.
Blockers: ESP failure .pkl model missing; schematic server API only inferable from JS; NLOG report from .xlsm template, untested.
Risks not to copy: only 20/150 routes need login, debug=True on 0.0.0.0, global per-process plant state, hard-coded secrets
(AVEVA client_secret exposed by an unauthenticated route). 17 routes have no frontend caller.
Open questions for user listed in section 7.4 of the features file (keep URLs?, unimplemented units chp/electric_boiler/heatpump/heat_demand in scope?, Ollama+Chroma?).
Related: [[repo-and-code-preferences]], [[gemini-repo-findings]].

2026-10-30 08:53 user plan: split old GEMINI into 4 separate repos: infrastructure (docker-compose files only),
backend (FastAPI), frontend (React + Vite + Tailwind), Python package (physics/engine). The backend inventory
is the feature list for the new FastAPI repo. Still design discussion; no prompt until user says "go".
Frontend result (08:57): 19 pages, 262 features, 117 distinct backend calls; Flask/Jinja + jQuery, JointJS diagram builder,
Plotly/uPlot, DataTables Editor (trial, replace), Grafana iframe. Client-side logic to port: ESP unit conversions, annulus alarms,
maintenance schedule, risk factor. Target output folder: /Users/sahand/Desktop/crust-team/gemini-legacy-frontend-analysis/frontend-features.md.
User wants backend and frontend analysed by separate sessions, each self-contained (no cross-references).

2026-10-30 09:15 frontend discussion thread "Plan new frontend features" (user uploaded frontend-features.md, 18 pages/260 features).
My proposals (awaiting user): groups shell/plant/data/wells+ESP/integrity/reports; merge P13 into diagram builder;
React Flow, TanStack Table, Plotly; domain logic from JS moves to backend/package; one long-job hook with timeout/cancel;
MVP for hackathon = shell, plant, data, wells/ESP, chat; postpone well integrity (P12), schematics (P11), NLOG.
2026-10-30 09:20 user: frontend features organised as domain / feature / use-case; names must be carefully chosen (user values naming).
Map at /mnt/project-files/frontend/feature-map.md: 7 domains (Workspace, Assistant, Plant Model, Measurements, Well Performance,
Well Integrity, Reporting), 27 features, 72 use-cases, 7 naming rules + "Why" per name. Open name choices asked: Flowsheet vs Plant Diagram,
Measurements vs Historian, Nodal Analysis vs Production Capacity.
2026-10-30 09:35 feature-map.md now covers frontend (260) + backend (98) IDs, columns Frontend/Backend. Renamed domain Measurements -> Time Series
(calculated tags), added Soft Sensors feature and technical Platform domain. Verified coverage with a script (all IDs mapped).
2026-10-30 09:32 harness discussion: I recommended harness as its own Python package (deps backend -> harness -> gemini; harness defines LLM/store/events interfaces, backend implements; CLI run without backend), first living inside the backend repo, own repo later. Asked user: separate repo from day one or this middle way. Pending.
2026-10-30 09:34 proposed backend tree (discussion): backend/{packages/harness (standalone: harness, agent, tools, interfaces LLM/RunStore, callbacks, hooks, cli), src/app/{platform, workspace, assistant/{chat,runs}, plant_model, time_series, well_performance, well_integrity, reporting}/<feature>/{router,service,schemas,models,tasks}.py, migrations, tests}. Rules: no physics in backend, only assistant/runs knows harness, features import only platform. Harness: interfaces (deps) vs callbacks (observers, same pattern as gemini engine) vs pre-hooks (can block: approval, token budget, access).
2026-10-30 09:35 user leaning to harness as separate repo (crust-team/harness, editable path dep in backend, pinned tag in CI/Docker). User wants "loop engineering" possible: my proposal = swappable Loop classes (ToolLoop, PlanExecuteLoop, VerifyLoop, MultiAgentLoop) over fixed harness infra, hooks per loop phase, eval suite of fixed tasks (accuracy/tokens/steps/time), record-replay of LLM responses, checkpoint/resume.
2026-10-30 09:45 researched prompt/context/harness/loop engineering (nested layers). Notes: /mnt/project-files/research/agent-engineering-layers.md. Correction: loop is outer layer, not a class inside harness; harness repo should separate harness/ (runtime, tools, hooks, context, observability) and loops/ (goals, verifiers, stop rules, maker/checker). Physics checks = strong verifiers.
2026-10-30 09:40 proposed system layout: crust-team/{infrastructure, frontend, backend, harness, gemini}; deps frontend->backend->harness->gemini. Harness tree: src/harness/{prompts, context, runtime, tools, verify, agents, loops, cli.py}, evals/, tests/, AGENTS.md. Frontend src/{app, domains/<domain>/<feature>, shared, lib}. Suggested package name swarmax instead of harness (pending).
2026-10-30 09:41 recommended agent package name `swarmax` (PyPI name already owned by the user, v0.0.1); rejected pollux/dioscuri (taken), conductor/foreman (generic), harness (one layer only). User approved 09:40 ("makes sense").
