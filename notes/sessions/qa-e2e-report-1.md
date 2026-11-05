# Handover: QA-E2E-report-I -> QA-E2E-report-II (2026-11-05 20:50 UTC)

## Role

QA thread QA-E2E-report-I of the QA round `documents/project/plans/qa-round-e2e-ai.md` (row
QA-E2E-report-I: chat to report, S5). Mode HOTFIX; change NO code, only test and report.
Sahand lifted the no-tests rule for this thread (`memory/feedback-no-tests-now.md`): live runs,
browser and LLM use allowed. Rules: never stop after a bug (file it with qa.py, go on); report
times to Sahand in Trondheim time (CET) in chat, files keep UTC; chat with Sahand in Persian,
files in English; poll run state no more than once every 5 s (QA-217; I poll every 45 s);
at most ~3 CPU cores (nice); projects named 'QA-TEST QA-E2E-report-I <n>', never deleted, never
touch other threads' projects. Coordinator: Coordinator-V (id in STATUS.md).

## Tools and how I worked

- agent-browser, session `qa-e2e-report-I` (logged in as admin; credentials from
  `backend/.env` FIRST_ADMIN_* read at run time, never printed).
- Set-up through the API with `backend/scripts/seed_qa_projects.py` functions (case.json +
  demand.csv + economics.json as case v3; plants HackathonPlant v1, HeatingAbsorptionCoolingPlant
  v2; optional page `run` study of v1). Run with `backend/.venv/bin/python` from `backend/`.
  Do not pipe the seed into `head` (SIGPIPE killed project 6's seed before the plants).
- Run logs: `GET /assistant/runs/<id>/log` -> steps[].tool_calls (tool, input, output, duration).
- Reference numbers: page study of v1 on case v3: LCTS 45.102, LCOH 43.753, LCOC 51.445 EUR/MWh,
  CAPEX 34.636 MEUR, OPEX 3.654 MEUR/yr, CO2 13.774 kt, 15/15 checks. v2: LCTS 49.281, CAPEX
  23.956, OPEX 4.978, CO2 20.960, gas bought 65,190 MWh, boiler 76,830 MWh. v1 on case v4
  (heating return 50 degC): LCTS 41.772, CO2 12.504.

## State

Report: `documents/project/quality-assurance/reports/QA-E2E-report-I-2026-11-05.md` (rounds 1-3,
timing and accuracy tables); SCENARIOS.md row E2E-report.

Projects (keep): 1 0e44cb05 (2 chats' worth of runs, case v3, results v1/v2), 2 fa329839 (case
v4), 3 a9ff33c4, 4 8b484b52, 5 c60d19cd, 6 07912156 (from-scratch hhpc design, adopted as
plant v1), 7 551392b1.

Bugs I filed: verified QA-165, 166, 167, 233, 234, 257, 269, 270, 289, 290, 334, 337 (and
retested others' QA-313, 323, 325: verified). Open: QA-347 (major, cross-team request
unroutable), QA-274 (minor, chat sensitivity studies never saved as results; reopened twice,
fix note repeats commit 8936366), QA-242 (minor, fixing: 'stop' at step limit -> run failed).

## Next steps

1. Retest QA-274, QA-347, QA-242 when `qa.py list` shows them fixed (steps in each bug file).
2. New scenarios in the report section: report through the chip after a design run made in
   chat; Export Markdown/PDF of a sensitivity result (once QA-274 works); a report request in
   another language wording; deny the report's first approval; a reload during a report run.
3. After each round, append to the report file and update the SCENARIOS row; tell the
   coordinator new blockers/majors at once.
