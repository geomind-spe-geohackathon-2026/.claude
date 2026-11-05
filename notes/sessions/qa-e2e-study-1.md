# Handover: QA-E2E-study-I -> QA-E2E-study-II (2026-11-05 ~19:15 UTC)

## Role

QA-E2E-study-I of the QA round in `documents/project/plans/qa-round-e2e-ai.md` (row QA-E2E-study-I):
chat-first E2E tests on https://geomind.team with agent-browser of the study section only:
simulate, sensitivity, optimisation, comparison, uncertainty; Results page, charts, Compare, adopt;
Runs and logs (steps, cancel, resume, JSON). Mode HOTFIX; change no code, only test and report with
`documents/project/quality-assurance/qa.py` (reporter `QA-E2E-study-I`; the successor reports as
`QA-E2E-study-II`). Live runs, browser and LLM use are allowed for this thread
(`memory/feedback-no-tests-now.md`, lifted for the nine QA threads). Inputs: the competition data in
`gemini/examples/hackathon_2026/`. Projects named `QA-TEST QA-E2E-study-I <n>` / `QA-TEST
QA-E2E-study-II <n>`, never deleted; never touch another thread's project.

Rules from Sahand during this session: never stop after a bug, file it and go on (also in the plan,
"Never stop"); in chat with Sahand give times in Trondheim time (CET), files keep UTC; Persian in
chat, English in files; poll run state no more than once every 5 s (QA-217, DB pool), the scripts
poll every 20 s with a cached token; at most ~3 CPU cores (nice).

## How I test (scripts in `notes/sessions/qa-e2e-study-1-scripts/`, copy to your scratchpad)

- `seed.py "<project name>"` (run with `backend/.venv/bin/python` from `backend/`): new project with
  the three competition files in RAG, the reference case (`case.json` + `economics.json` + demand),
  plant v1 HackathonPlant and v2 HeatingAbsorptionCoolingPlant. Admin credentials are read from
  `backend/.env` at run time, never printed.
- `api.py METHOD PATH [params-json]`: the API as admin, token cached in a 0600 file in the scratch dir
  (edit TOK path).
- Browser: `agent-browser --session qa-e2e-study-I` (chat) and `--session qa-e2e-study-I-b` (pages);
  log in once per session with the admin account. `ask.sh "<message>"` types and sends in the open
  chat. `drive.sh <run>` waits and clicks Approve on every card (scrolls the button into view first:
  the Approve button sits below the JSON, QA-193); `drive-deny.sh <run> "<reason>"` denies the first
  card. Never edit a script while it runs in the background (bash reads it lazily).

## State

Projects (all kept): `QA-TEST QA-E2E-study-I 1` 8fcbf709-537a-40d9-ac1f-abadd1061775 (round 1, plant
now v6 adopted from opt1), `2` 8eabf827-1f43-4cf8-86a4-39147bea32a0, `3`
ac687987-8bfe-452f-8013-7a4b577a3655, `4` 4597d7cb-943b-4480-8447-6a41825bca4e.
Report: `documents/project/quality-assurance/reports/QA-E2E-study-I-2026-11-05.md` (rounds 1, 2,
retests); SCENARIOS row `E2E-study`.

My bugs: verified QA-205, QA-209, QA-213, QA-214, QA-228, QA-249, QA-275 (and retested QA-152).
Open / to retest when fixed: QA-215 (backend: plant_version on rows, dedup, sensitivity view),
QA-232 (stale chunk reload; needs a deploy while a tab is open), QA-237 (geomind part), QA-248
(P10/P90), QA-276 (optimum worse than the stored plant; compare with the stored plant), QA-296
(20 approval cards, 9 refused), QA-300 (raw "improvement:" lines), QA-312 (chat cannot adopt a result
since QA-237), QA-099 (15 digits in sensitivity/uncertainty answers; reopened by me).
QA-277 was marked duplicate by a fixer.

## Next steps

1. `python3 qa.py list` and retest every bug above that is `fixed`, by its steps, in a NEW project
   (`QA-TEST QA-E2E-study-II <n>`); write Retest and set verified / open.
2. New variants not yet done: a vague request ("is this plant good enough? make it cheaper"); a
   study on HackathonPlant (heat pump) instead of the absorption plant; a sensitivity of the
   discount rate with the Results/Study views; Export Markdown of a run; cancel while an approval card
   waits (QA-133/134 retest); two requests at once in two chats of one project.
3. After each round add a section to the report and update the SCENARIOS row; tell the coordinator
   (id in `.claude/STATUS.md`) new majors at once.
