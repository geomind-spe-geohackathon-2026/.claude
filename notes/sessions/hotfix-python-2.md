# hotfix-python-2 handover (2026-11-05 ~09:40 UTC)

You are hotfix-python-III, the successor of hotfix-python-II (session_01J2V3UXSA2mo8MG4igf5y4n).

## Role and mode

Mode: HOTFIX (decided; do not ask the user). You fix the QA bugs of the Python packages geomind
and gemini (area geomind, gemini). The coordinator is the one in `.claude/STATUS.md`
(Coordinator-III, session_01J2V3UWsUm5z442CiXM5MZU at handover); send it one line per fix or
deploy with the `send_message` tool of the Claude Code Remote MCP server.

Your full role rules are in `notes/sessions/hotfix-python-1.md` (Role and mode, the bug loop,
"Rules learned"): read that file first, then this one. What changed since:

- Deploy windows: start a deploy ONLY at :00:00 or :30:00 UTC sharp (QA sessions run long
  start-to-end runs; a deploy restarts the worker, and a running nested agent starts over). When
  the coordinator puts a hold on deploys, release but do not deploy.
- Commit often, one change per commit, message "QA-nnn: what, why" (`memory/feedback-commit-often.md`).
- Usage pause: check `get_session` rate_limit_info at each step; a past `resetsAt` means reset
  (`memory/feedback-usage-limit-pause.md`).
- Hand over at 300,000 used tokens of context (`session-refresh.md`).
- No QA ids in model-facing text (tool messages, prompts): only in code comments and changelogs.
- Prod reads: read-only one-liners inside geomind-celery work (`asyncpg` with `POSTGRES_URL`,
  tables `run_events`, `run_artifacts`, `chat_states`, `runs`); copying prod files out to the host
  was refused, so reproduce INSIDE the worker (e.g. call geomind's own `run_plant` with a fake
  context whose `session.load_artifact` reads `run_artifacts`, as done for QA-082).
- pip wheel builds from the working tree: never leave geomind or gemini edits uncommitted while
  a deploy prep builds wheels.
- The deploy prep I use (lock, wheels, backend patch bump, CHANGELOG, contracts.md line 3,
  openapi.json version, commit, push) is in this session's history; the pattern: take the lock,
  `git pull` the backend, remove the old wheels, `pip wheel --no-deps -w .tmp/hotfix-wheels
  ../geomind ../gemini`, bump `src/version.py` + `openapi.json` "version" + contracts.md line 3 +
  a CHANGELOG section, commit, push; then at :00/:30 `cd backend` and `scripts/hotfix_deploy.sh`
  (two separate Bash calls), then release the lock.

## State at handover

Production (if the 10:00 deploy went through; check `STATUS.md` and the health version): backend
1.1.81-ish with geomind 0.4.78 + gemini 0.6.12 local wheels. Before it: backend 1.1.78, geomind
0.4.73, gemini 0.6.10.

Released this session (all tags pushed): geomind 0.4.56 to 0.4.78 (skills folder, calculate,
run_python, web tools, skills step, QA-061, 065, 069, 070, 072, 074, 076, 078, 079, 080, 081
(geomind side), 082, 083, 084, 085, 086, 087, 088, 047 part 2); gemini 0.6.6 to 0.6.12
(structure_plant, gm.check no-raise, flow range over several rules, depth named first, bare inlet
refused, ESP curve windows = request 35, m/s2 and kg/m2 units).

Open, still with the backend: QA-081's backend part (catch `gd.errors.AlreadyAnsweredError` as a
no-op and stop the double answer) is hotfix-back's.

## In progress: QA-090 + QA-091 (claimed by hotfix-python, status fixing), and QA-094

Cause (verified offline on gemini's hackathon example): the case lead wrote the brief's fixed
supply temperatures as `{on: cooling_supply, quantity: temperature, min: 20, max: 20, over: each,
when: "always"}` (and 100 C for heating_supply). On days with no cooling demand the cooling grid
does not operate (146 of 365 days in the example), so `always` judges those days too: worst 25 C,
fails; with `when: "running"` worst 20 C, passes. The design lead then chases R9 for hours.
gemini's "running" = the module carried flow (`operating` column), which is what we need: no
gemini change.

Decision (Coordinator-II, 2026-11-05 ~09:30): 
1. The case lead writes supply-temperature requirements with `when: "running"` AND adds the
   delivered-energy requirements as gemini's sample does (gemini/examples/hackathon_2026/README.md
   "Requirements of the case": heat_delivered / cold_delivered, `unmet_share` <= 0.01; read the
   sample case.json for the exact form: `unmet_share` takes no `when`).
   Robust option I planned: geomind `set_case` turns a supply-temperature rule with `when`
   `always` or none into `running` and lists it in `converted` with the reason (QA ids only in
   comments).
2. The design lead stops chasing one failing requirement after a few rounds (say 3 changes aimed
   at it): it reports the requirement plainly (value, limit, why), then asks the user (accept,
   change the requirement, stop) or delivers the best design with the open violation named, then
   simulates, compares and finishes.
3. Close QA-090 and QA-091 together (one as duplicate of the other).
4. Project 61134432's case version 10 needs the fix: say how (the case lead rewrites the
   requirements when the user asks "fix the supply temperature rules", or a set_case).
Coordinator-III adds for QA-091: 330 d is the doublet's availability; the whole system must meet
demand all 365 days (so the delivered-energy rule is over the whole year).

QA-094 (major, routed to you): treat network return temperatures as a design freedom with a
recorded reason, not a case change (`geomind/prompts/design/energy.md` line ~65); the organisers
confirmed return temperatures are the team's choice within the constraints.

## Next steps, in order

1. Read `STATUS.md`; confirm the 10:00 deploy is live (health version, `geomind 0.4.78 gemini
   0.6.12`); if it did not happen, deploy the held batch at the next :00/:30.
2. QA-090/091: the four points above; one commit each; release geomind 0.4.79; deploy at :00/:30;
   write Fix in both bug files (qa.py set, one as duplicate); tell the coordinator.
3. QA-094.
4. Then `qa.py next --area geomind,gemini --fixer hotfix-python`.
