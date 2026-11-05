# Fatemeh QA (generation 1) handover

Written 2026-11-05 ~14:25 UTC by Fatemeh QA (session_01J2V3UX7XrrTa9jKv7ZTh9a), at 546k context.
Successor: Fatemeh QA-II.

## Role

Fatemeh's own QA session. She tests geomind.team in the browser and sends screenshots, run JSON
files and questions in Persian. This session:

- answers her in Persian, short and plain; writes every file in English;
- reads what she sends, finds the cause (code in the clones, production DB read-only), and files
  each bug with `documents/project/quality-assurance/qa.py` (`new`, fill the file from
  `TEMPLATE.md`, evidence in `evidence/QA-<nnn>/`, `save`); reporter "Fatemeh (...), Claude (...)";
- sends every new bug to the coordinator at once with `send_message` (coordinator id: read
  `.claude/STATUS.md` first, it changes: now Coordinator-IV, session_01J2V3UYqrLbCNN9zst5WY8d).
  Coordinator-IV's rule (2026-11-05): Fatemeh's bugs are top priority in every hotfix queue, any
  severity; send them to the coordinator, it routes them at once;
- writes ideas (not bugs) into `documents/project/quality-assurance/IMPROVEMENTS.md` (IMP-001 to
  IMP-023 so far) and sends them to the coordinator;
- changes no code, deploys nothing; it is not a hotfix session. No mode question needed: this
  session only writes to `documents/` and `.claude/notes`, `.claude/STATUS.md`.

Rules she gave in this session:

- Production DB reads are allowed (read-only SELECT on geomind-postgres via
  `sg docker -c "docker exec -i geomind-postgres sh -c 'psql -U \"\$POSTGRES_USER\" -d \"\$POSTGRES_DB\"'" < file.sql`).
  Put the SQL in a file in the scratchpad; never write to the DB.
- "Give the coordinator everything that makes the agents work better" (done as IMP-012..023).
- Before any handover, make sure every bug reached the others (done, see below).

## How to read a run

- Run JSON she uploads: `{run, steps[]}`; each step has `agent`, `llm_calls` (messages, answer,
  tokens, duration) and `tool_calls` (tool, input, output, duration, error). Summarise with a small
  Python script (timeline per step, tool errors), never read the whole file.
- DB: `runs` (status, loop, error, request, tokens), `run_events` (type, data: tool.started /
  tool.result / llm.completed / request / permission ...), `results` (summary.kpis, summary.checks,
  content.coverage / capacities / constraints), `studies`, `case_versions`, `plant_versions`,
  `chat_states`, `messages`, `activity`.

## State at handover

Her bugs still open or in progress (everything else she reported, QA-001 .. QA-131, is fixed or
verified):

- QA-109, QA-126, QA-127: fixing, hotfix-front-III (report default result and run; Days covered
  "Backup" display).
- QA-129, QA-130, QA-131: open, routed by Coordinator-IV to hotfix-python-IV
  (session_01J2V3UZqdULpCLT7XEFdd6t), top of its queue: optimiser cannot range size.doublets on a
  free plant; production pump at 185 % of its rating in lcts_best; sensitivity in chat tries
  run_python instead of gemini's sensitivity study.
- QA-107: open, no fixer (sent to Coordinator-IV to route with QA-126).
- QA-110 (case and plant History: open, compare, Saved by): backend part done (1.1.87), frontend
  part with hotfix-front-III; check it once live.
- Her cosmetic batch QA-100, QA-101, QA-117: hotfix-front-III; check once live.

Her projects:

- "geo mind testing" (cf0c3d9c-d925-4ffa-bd29-3ac8205090d3, chat 27379f2e): the first agent run
  that reached a feasible, optimised design (run 32a12115, 10:10-13:18 UTC): lcts_best 12 of 12
  pass, lcts 70.95 EUR/MWh, 1 doublet, electric boiler 21.5 % of the heat, capex 44.6 MEUR (23
  MEUR pipes: 4 x 5000 m, the agent's assumption). Sensitivity run 5cd1f2b8 computed nothing
  (QA-131).
- "test hack" (886404e4, chat 33c76f29): old runs, used for QA-009..QA-022.
- Reference: "SPE GeoHackathon 2026" (46d15d6b-ad9c-4e61-8a3a-c0cea9e20735): user-run studies on
  gemini's examples/hackathon_2026 (2026-11-02): "Optimise LCTS" 10 of 10 checks, full demand met,
  lcts 40.34, CO2 12.9 kt. The only other passing result. Sent to the coordinator as the PR
  fallback and as the proof of the short path (IMP-023).

Context she should keep in mind:

- Submission deadline: 2026-11-05 23:59 CET = 22:59 UTC (in STATUS.md). Sahand decides what goes
  in the PR; the coordinator does not handle the submission.
- Organiser answers (Discord #technical-q-and-a): return temperatures are the team's choice
  within the constraints (QA-094); grid CO2 reference 0.3 kg/kWh (QA-095); 330 d is the doublet's
  availability, the system meets the demand all 365 d (QA-091); depth may change; gas is CO2+CH4.
- Why agents rarely finish: they build plants from empty classes and fill ~125 values by hand;
  gemini's sample plants come with the values (IMP-023). Measured tool refusal rates in
  IMPROVEMENTS.md (IMP-012..022).

## Next steps

1. Report in to the coordinator (id from STATUS.md) with your title and id, and tell Fatemeh in
   Persian that you took over.
2. Keep answering her screenshots and questions as above; file and send every bug at once.
3. When hotfix-front-III and hotfix-python-IV deploy, check her bugs above on geomind.team and
   tell her what changed (QA-127/109 report defaults first: they decide tonight's report).
4. If she asks again, re-measure the tool refusal rates and the runs reaching simulate / check /
   optimize (queries in IMPROVEMENTS.md "Measured on production").
5. Hand over again at 300k context (`.claude/session-refresh.md`).
