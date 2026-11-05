# Handover: QA-AI-analysis-I -> QA-AI-analysis-II (2026-11-05 ~20:05 UTC)

## Role

QA-AI-analysis thread of the QA round (`documents/project/plans/qa-round-e2e-ai.md`, row QA-AI-analysis-I). Mode:
HOTFIX, but change NO code: only test and report. Live runs and LLM use are allowed for this thread
(`memory/feedback-no-tests-now.md`, lifted for the nine QA-round threads). Backend layer only (api.geomind.team REST
and run logs), no frontend. Inspect every tool call and agent round trip. Input: `gemini/examples/hackathon_2026/`.
Report every bug with `documents/project/quality-assurance/qa.py` (problem, evidence, where from, proposed fix).
Projects are named `QA-TEST QA-AI-analysis-<n> ...`; never delete them; never touch another thread's project.
CPU: at most ~3 cores, nice. Chat with Sahand in Persian, files in English; give times in Trondheim time (CET) in chat.
Rules from Sahand during the session: a bug never ends testing - file it and go on; when a round ends start the next
(other scenarios, inputs, retests, accuracy/speed comparisons); retest a fix only once deployed; poll run state at most
once every 5 s (QA-217). The coordinator is in `.claude/STATUS.md`.

## Tools (copies in `.claude/notes/sessions/qa-ai-analysis-tools/`)

Put them in your scratchpad and fix the paths at the top (Q=..., STATE). Run from `backend/` with `.venv/bin/python`.
- `qa_ai.py setup <n> <PlantName> [noecon]` (project + documents + reference case [+ economics] + plant version 1 +
  chat), `send <n> "<text>"`, `status <run>`, `answer <run> <request> approve|deny:<reason>|text:<answer>`,
  `get <path> [out]`, `post <path> <json>`, `export <run> <out>`. Credentials from `backend/.env` via
  `scripts.seed_qa_projects` (never printed). State of projects in `state.json` (old one lists projects 1-15).
- `drive.py <run>`: polls every 15 s, approves every approval card (logged to cards-<run>.log), stops at a question
  or at the end; survives deploys.
- `trace.py <log.json> [width]`: one line per step and tool call of `/assistant/runs/{id}/log`.
- Reference numbers without LLM: `POST /design/study` kinds run, minimize, sensitivity, sample on `plant_version`;
  results at `/design/results/{id}`; report at `/reporting/design/{parts,preview,export}`.

## State

Reports: `documents/project/quality-assurance/reports/QA-AI-analysis-I-2026-11-05.md`, `-round2.md`, `-round3.md`;
SCENARIOS row `AI-analysis`.
Open bugs from this thread: QA-179 (minor, reopened: analysis lead overhead, sensitivity split by reading only the
site section), QA-278 (major, reopened, geomind/gemini: geomind `run_study` on `design/vN` gives HeatingFullCoolingPlant
52.8 and HeatingCoolingPlant 43.8 vs page `minimize` on plant_version 32.31 and 39.48 with the same ranges), QA-299
(fixed in gemini 0.6.27, not deployed at 19:53 UTC: P10/P90), QA-338 (minor, backend report studies section).
All others of this thread verified (list in round3 report). IMP-031, IMP-034.
Reference numbers (reference case + economics, HackathonPlant): run LCTS 45.102, capex 34.636 MEUR, NPV 28.453 MEUR;
sensitivity (gradient 13.59, electricity 11.84, discount 10.85, permeability 4.12, carbon 3.40, gas 0); sample 200/seed
42: p5 37.97, p50 46.10, p95 54.31; minimize (gemini 0.6.26+): 32.535 (30 ev), 31.487 (40 ev).

## Next steps

1. Retest QA-299 when gemini 0.6.27+ is live (STATUS.md), project 8 (485dbcfc-...): "Give me the P10, P50 and P90 ...".
2. Retest QA-278 and QA-179 when fixed (watch `qa.py list` / BUGS.md).
3. New scenarios not yet run: no-files / vague case-plus-cost in one request; uncertainty on site values only;
   evolve (structure search) through chat vs the page `evolve` study; report content via the agents vs
   `/reporting/design/export`.
