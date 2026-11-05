# Manual QA (generation 3) handover

Written 2026-11-05 by Manual QA-III (bg job a5296a2e, session_0171QAFri1Kj544jtiKTDVzA, Sahand's
account, for Fatemeh), on Coordinator-V's order (user's order: this session closes and reopens in
the NTNU Dell environment). Read manual-qa-2.md and manual-qa-1.md too: role, rules, how to read a
run, retest list.

## First prompt to give the next session

"You are Manual QA-IV, the successor of Manual QA-III (session_0171QAFri1Kj544jtiKTDVzA). Read
~/geomind-spe-hackathon-2026/.claude/notes/sessions/manual-qa-3.md, manual-qa-2.md and
manual-qa-1.md and follow them; your role's rules are in them, so do not ask the user for the
mode. Start now."

## Role and rules (unchanged, plus new)

Fatemeh's own QA session: answer her in Persian, short; files in English; read her screenshots and
run files, file bugs with qa.py, send each to the coordinator (Coordinator-V; peer name in
STATUS.md, message with SendMessage). No code changes, no deploys. NO QA tests (live checks,
browser, LLM runs) until the user lifts it; API reads are fine.
New (Coordinator-V, user's order, strict): no new branch, no worktree, ever; documents/ and
.claude/ changes go directly on main. Sessions use SendMessage/ListAgents (no Remote MCP).

## Answered for Fatemeh this session

- "Which bugs remain?": BUGS.md has only QA-145 (fixing) and QA-122 (open) not fixed; 94 fixed
  but not live-checked, 50 verified. Coordinator-V: QA-145 is hotfix-python-VI's top item
  (waiting for the user to approve its edit permission in that session); QA-122 (geomind part;
  backend part live since 1.1.90) stays with hotfix-python-VI right after QA-145.
- hotfix-front-VI: frontend 1.1.113 live (stage timer per agent line). Its owed retests: QA-139,
  141, 142, 146, 117, 118, 133, 134.

## IN PROGRESS: Fatemeh's open question (do this first)

"Read the logs of all runs so far and find exactly what the agents' problems are now." Not yet
answered to her. Method and data so far:

- Tools in `notes/sessions/manual-qa-3-tools/`: `api.py` (admin login from backend/.env at run
  time, UA header), `ana.py` (per run: steps, tool calls, errors, identical repeat calls, reached
  simulate/check/optimize, patch count, LLM vs tool minutes, agents; tool error rates), `err.py
  <since> <n>` (error clusters), `tool.py <since> <tool> <n> <width>` (clusters for one tool).
  They expect `runs.json` (all runs: GET /workspace/projects, then /assistant/runs?project=..)
  and `logs/<run>.json.gz` (GET /assistant/runs/{id}/log) in the working dir: re-fetch into
  your job tmp (42 runs of 2026-11-05, 126 MB). Output of ana.py: `ana-2026-11-05.txt`.
- Note: there is NO run after 15:17 UTC (tests stopped), so no run uses geomind >= 0.4.92;
  findings describe 0.4.87-0.4.91. Say this to Fatemeh.

Findings so far (2026-11-05, 42 runs, 00:13-15:17 UTC):
1. Only one run finished a design end to end (32a12115, 188 min). Case-only runs are fine
   (QA3 case runs 1-5 min, 0-1 errors; 9696f5d4 3.8 min). Every design run is long (37-430
   min), reaches simulate rarely, and is cancelled or fails.
2. Tool error rates (all day): evaluate_module 81 % (305/377), calculate 74 %, run_python 72 %,
   build_plant 61 %, simulate 56 %, patch_plant 52 %, set_case 38 %, web_search 27 %,
   read_plant 16 %, read_stored 15 %.
3. Identical repeat calls (same tool + same input) are huge: e.g. ed03d7ea 138 of 264,
   37950240 295 of 595, 3bdd7ebb 371 of 992 (QA-145 pattern: re-reads).
4. Internal (code) errors, worth a bug if still present on current code: patch_plant "internal
   error" 18x (runs 753645c0, eb7b95df, 06:00 UTC) and 2x "TypeError: unhashable type: 'dict' at
   _utils/reader.py:190" in c801850b (15:17, the latest run, sahand test 2); simulate internal
   7x (f59e5d2c, c4f00b5c, eb7b95df); build_plant internal 6x; reviewer JSONDecodeError
   (32a12115). Check if the reader.py:190 one is filed (STATUS mentions "patch_plant internal
   error explained" at backend 1.1.99).
5. Misleading message: evaluate_module says "invalid inlet 'source_in'; valid names:
   source_in, sink_in: Stream.fluid: no value" (19x): the name is valid, the fluid is missing.
   Also inlets=[] 16x+ (HeatPump, Doublet, ElectricBoiler): agents call it with no inlets.
6. read_stored / calculate / run_python: agents guess path 'd1' when keys are flat 'd1.esp',
   'd1.well' ... (~40x), and module ports (absorption_chiller.generator_in) that a result
   doesn't hold. run_python refuses "code holds data literals" 22x.
7. Plant values the agents cannot know: doublet gradient/surface_temperature (belong in the
   case), drainage_radius, roughness, reservoir.*, esp.* curves (simulate missing_value 19+8+6x,
   build_plant 21x, patch_plant 15x); control.dispatch missing 14x; ownership refusals
   ("is the reservoir_engineer's", ~30x) bounce work between engineers.
8. Not done yet: per-run timeline of the latest design runs (ed03d7ea, c801850b) to see where
   the time goes; LLM-side problems (invalid/empty answers, finish refusals: "result is stale"
   2x); turn this into a short Persian answer and file new bugs (internal errors, misleading
   evaluate_module message, read_stored flat keys) after checking BUGS.md for duplicates and
   the current code.

## Next steps

1. Report in to Coordinator-V; tell Fatemeh in Persian you took over.
2. Finish the open question above, answer Fatemeh, file the new bugs, send them to Coordinator-V.
3. Keep the retest list (manual-qa-2.md + hotfix-front-VI's list above) for when tests are
   allowed.

## Manual QA-IV, 2026-11-05 ~17:00 UTC

- Log findings checked against live code (geomind 0.4.96, gemini 0.6.16) and filed: QA-147 (read_stored/calculate cannot read dotted keys like d0.esp, geomind), QA-148 (gemini reader.py TypeError on a mapping in inlets; chiller condenser loop has no tear first guess; needs Sahand's OK), QA-149 (evaluate_module 81 % refused). Sent to Coordinator-V. Not refiled (already fixed): control.dispatch IMP-019, failed_before QA-143, QA-145, m/s2.
- Run 32a12115 summary for the report thread: documents/project/quality-assurance/reports/run-32a12115-complete-design.md (a99fad8); sent to Coordinator-V to forward.

## Manual QA-IV, 2026-11-05 evening (times CET, Sahand's rule)

- Report live run (agent): run bfcec811-c5ad-496e-a829-6ec44de3251c, project 0b986dd6-8f95-4383-9d15-5e589ff122c9, started 18:37 CET; QA-IV answers its cards by hand (Sahand: no auto-approve, answer for the best showcase). Tools: scratchpad liverun/answer.py, watch.py, show.py (copy from this note if the scratchpad is gone: answer = POST /assistant/runs/{id}/answer {request, answer:{approved,reason}|{text}}). First run d4ab496f cancelled (15 plants, no study).
- No-agent results for the report: clean project 8d5d21e0-ecb0-4894-9cfd-bdd61f670ac7 (gemini 0.6.26): evolve 29.55 EUR/MWh 8.54 kt; absorption plant 28.61; sensitivity, sample (27/50 feasible), run. Older projects 4678c5c6 (has 2 failed studies) and abf7ce3a (cancelled) are superseded. Write-up: documents/project/quality-assurance/reports/no-agent-showcase-gemini-0.6.17.md.
- Bugs filed this evening: QA-182/183/184, 201 (task, team size 8), 212 (reopened), 238/239/240, 244 (reopened), 254 (verified), 264 (verified), 267 (verified), 281, 282, 287 (blocker).
