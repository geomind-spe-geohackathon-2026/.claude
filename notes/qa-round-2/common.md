# QA round 2: rules for every QA session

You are a QA session of GeoMind, started by the coordinator. Mode: HOTFIX round; you only TEST and
REPORT (decided; do not ask the user for the mode). You change no repo except the QA files
(through `qa.py`) and your own scenario file in `.claude/notes/qa-round-2/`.

Read first: `~/geomind-spe-hackathon-2026/.claude/AGENTS.md`, `.claude/STATUS.md`,
`.claude/memory/feedback-qa-round-2.md`, `documents/project/quality-assurance/README.md`, then
your own file in `.claude/notes/qa-round-2/` and the other QA files there (to avoid overlap).

## Inputs: the competition files only

`~/geomind-spe-hackathon-2026/gemini/examples/hackathon_2026/`: `GEMINI_Hackathon_Challenge_Requirements.pdf`,
`GEMINI_Heating_Demand_Daily_2027.csv`, `GEMINI_Cooling_Demand_Daily_2027.csv`. Nothing else in
that folder (no case.json, plants, economics.json) and no other data. Read the PDF yourself; you
write every user message in the chat yourself, as a real engineer user would, from those files.
When an agent asks for a value the files do not give, answer as a user would (approve a sourced or
clearly labelled assumption, or say you do not know); note what was asked.

## Tool: agent-browser only

- Use `agent-browser` (installed globally; start with `agent-browser skills get core`). Never use
  Playwright or write Playwright scripts.
- Always pass `--session <your-name>` so sessions do not share a browser. One browser at a time;
  `agent-browser --session <your-name> close` when you pause or finish.
- Prefer `snapshot -i` (accessibility refs) over screenshots; take a screenshot only as bug
  evidence. Keep scratch files under `/tmp/<your-name>/`, never in a repo.
- Live site https://geomind.team (API https://api.geomind.team). Log in with the admin account:
  FIRST_ADMIN_EMAIL / FIRST_ADMIN_PASSWORD in `~/geomind-spe-hackathon-2026/backend/.env`. Read
  them at run time only; never print them or write them into a file, message or bug.

## Projects and runs

- Make your own projects named "QA2 <your-name> <purpose>"; keep them (never delete). Never act in
  another session's or person's project or chat (you may look).
- Agent runs are live (deepseek on OpenRouter). Spend is not a limit; run one run at a time per
  session. A provider error (429, 5xx, timeout) is one bug, not one per occurrence.
- Deploys happen at :00 and :30 UTC; runs survive them. Read versions from
  https://api.geomind.team/api/v1/system/health for every bug.

## Your scenarios

Before testing, write your scenarios into your file `.claude/notes/qa-round-2/<your-name>.md`
under "Scenarios" (id `<your-name>-S1`, ...; goal, steps, what correct looks like, checked against
the PDF and CSVs), commit and push it (stage that file only; `git pull --rebase` first), and send
the coordinator one line. Stay inside your area; the other sessions' areas are in their files.
Then test, keep a one-line status per scenario in that file, and add new scenarios as you learn.

## Bugs: qa.py, never by hand

1. `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py list` to see if
   it is there; if so add your evidence and steps to that file and `qa.py save <id>`.
2. Otherwise `qa.py new "<title>" --severity <blocker|major|minor|cosmetic> --area
   <frontend|backend|geomind|gemini|data|infra> --reporter <your-name>`, fill the file (where:
   URL, project, chat, run id, step; versions; steps; expected; actual; a cause only as a marked
   guess), evidence (screenshots, run JSON from Runs and logs) in the folder it prints,
   `qa.py save <id>`.
   Blocker: the pipeline cannot go on. Major: wrong result or a detour needed. Minor: confusing or
   noisy. Cosmetic: looks only.
3. Wrong numbers are bugs: check results against the PDF and CSVs (and physics sense).
4. Retest: when a bug in your area is set `fixed`, retest it on the live site and write Retest in
   its file (`qa.py save`); reopen it if it still fails.

## Reporting

- Send the coordinator (its id is in `.claude/STATUS.md`) one short line per new blocker or major
  at once, and a short report every hour: scenarios done, bug ids. Never message other sessions.
- Every file in English. Commit and push at once; never leave uncommitted changes in a shared
  clone. Keep CPU low (nice long jobs).
- At 75 % context, hand over as `.claude/session-refresh.md` says (to `<your-name>-II`, same model).
- When your scenarios are all done and their bugs retested, run them once more with variations,
  report, and wait for the coordinator.
