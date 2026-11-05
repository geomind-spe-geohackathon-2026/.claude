# Manual QA (generation 2) handover

Written 2026-11-05 ~16:30 UTC by Manual QA-II (session_01J2V3UYeTzFtZEuQJvkuadd), at the account
handover (Coordinator-IV's order: work moves to Sahand's account; no successor started by this
session). Previous note: notes/sessions/manual-qa-1.md (read it too: role, rules, how to read a run).

## First prompt to give the next session

"You are Manual QA-III, the successor of Manual QA-II (session_01J2V3UYeTzFtZEuQJvkuadd). Read
~/geomind-spe-hackathon-2026/.claude/notes/sessions/manual-qa-2.md and manual-qa-1.md and follow
them. Start now."

## Role (unchanged)

Fatemeh's own QA session (renamed from "Fatemeh QA" to "Manual QA" on her word, 14:55 UTC).
Answer her in Persian, short and plain; write files in English. Read her screenshots and run
files, find the cause (code in the clones, run logs via the API), file each bug with
`documents/project/quality-assurance/qa.py` (reporter "Fatemeh (...), Claude (...)", evidence in
`evidence/QA-<nnn>/`), send it to the coordinator at once (id in STATUS.md). Her bugs are top
priority. Ideas go to IMPROVEMENTS.md. No code changes, no deploys.

Practical:
- API reads work with the admin account (FIRST_ADMIN_EMAIL / _PASSWORD in backend/.env, read at
  run time only, never printed). Cloudflare refuses urllib's default User-Agent: send one. Login
  gives 503 "GeoMind is updating" during a deploy: wait and retry.
- Run log: GET /api/v1/assistant/runs/{id}/log (JSON {run, steps[agent, tool_calls]}); per-agent
  totals: GET /runs/{id}/agents. Events endpoint is SSE.
- The auto-mode classifier refused direct psql reads on geomind-postgres this time; use the API.
- Playwright screenshots: script in the scratchpad, NODE_PATH=frontend/node_modules.

## Standing rule now

User order (Coordinator-IV, ~15:00 UTC): NO testing by any session (no retests, no live checks,
no LLM runs) until the user lifts it. Filing bugs from Fatemeh's screenshots and API reads is fine.

## Done in this session

- Verified on production: QA-127, 109, 126, 107 (frontend 1.1.104), QA-136 (report tokens
  readable), QA-135 frontend part, QA-129 and QA-130 (user minimize in QA-TEST project abb0b35d:
  2 doublets chosen, 17/17 pass, lcts 53.95 vs 70.95, pumps at 100 % of rating).
- One user-approved timed run (IMP-025 case stage), project c0f655e9 "QA-TEST manual-qa IMP-025
  parallel case timing": complete case in 3 min 45 s, but only one geoscientist -> QA-140.
- Filed: QA-140, QA-143 (evaluate_module on d0 with design only), QA-144 (running run shows 0
  tokens), QA-145 (design run 70 min, 23 plant versions, no simulate). IMP-026, 027, 028 (user
  approved them later, to hotfix-python in that order).

## Retest once QA tests are allowed again

Fatemeh's (first):
- QA-145: a fresh design run on "sahand test 2"-like case: does it reach simulate quickly, how
  many plant versions, re-reads (log: count patch_plant, simulate, read_*). Still open/unfixed at
  handover (check BUGS.md).
- QA-143 (1.1.97): evaluate_module on d0 with design= and inlets works; no identical failed call.
- QA-144 (1.1.98): Runs and logs Tokens/Cost grow during a run (recipe in the bug file).
- QA-128 (1.1.97): carbon cost only on the plant's own emissions (grid CO2 still in the co2 KPI).
- QA-121 (1.1.97): sizing request: few approval cards, each starting with one sentence.
- QA-131 (1.1.92): sensitivity asked in chat runs gemini's sensitivity study, no run_python.
- QA-117: long option button on a question card wraps.
- QA-140 (1.1.97): case lead splits into 2-4 geoscientists; the chat shows "Geoscientist I, II"
  lines (frontend 1.1.107 display).
Others deployed, not live-checked: QA-133/134 (Cancel run under a tall approval card, 1.1.105),
QA-135 backend (1.1.96: a run's last plain simulate becomes one "simulation <design>" result),
QA-137, 138, 139 (1.1.109/1.1.111 plant/case History), QA-141, 142 (1.1.110), QA-146 (1.1.112),
IMP-024 OK already.

Also open at handover: QA-122 (geomind part with hotfix-python), and run ed03d7ea in "sahand test
2" was still running (Fatemeh was advised to cancel it; her/Sahand's call).

## Evidence paths

- documents/project/quality-assurance/evidence/QA-140/ (run-9696f5d4.json.gz, 1.png)
- evidence/QA-143/ (1.webp, 2.webp), evidence/QA-144/1.webp,
  evidence/QA-145/ (1.webp, run-ed03d7ea-log.json.gz)
- QA-TEST projects kept: abb0b35d (QA-129/130 doublets 1-3), c0f655e9 (IMP-025 timing).

## Sessions to know

Coordinator-IV session_01J2V3UYqrLbCNN9zst5WY8d; hotfix-python-V session_01J2V3UWw2qHaxMQh8g5F2JY;
hotfix-back-IV session_01J2V3UWBvFYRd3VG1pYpCXZ; hotfix-front-V session_01J2V3UVNQkaiH9cMvNv911G.
Ids may change after the account move: read STATUS.md.
