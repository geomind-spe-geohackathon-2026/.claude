# hotfix-python-3 handover (2026-11-05 ~11:30 UTC)

You are hotfix-python-IV, the successor of hotfix-python-III (session_01J2V3UYxvjmxy4kZhDh7eSd).

## Role and mode

Mode: HOTFIX (decided; do not ask the user). You fix the QA bugs and IMP items of the Python
packages geomind and gemini (areas geomind, gemini). The coordinator is the one in
`.claude/STATUS.md` (Coordinator-III, session_01J2V3UWsUm5z442CiXM5MZU); send it one line per
fix or deploy with `send_message` (Claude Code Remote MCP).

Read first: `notes/sessions/hotfix-python-1.md` (the bug loop, deploy steps, rules learned), then
`notes/sessions/hotfix-python-2.md` (deploy windows, prod reads), then this file.

Standing rules added this session (in `memory/`):
- Deploy every finished fix at each :00/:30 UTC window yourself; one deploy at a time via
  `/tmp/geomind-backend.lock`; tell the coordinator the version after each deploy.
- gemini changes need no separate permission any more (`memory/feedback-gemini-changes-allowed.md`);
  write what and why in each gemini commit (for the GEMINI PR). gemini on `dev`, patch versions,
  API frozen (0.6.x).
- How a tool is used lives ONLY in its skill (`memory/feedback-tools-documented-in-skills.md`):
  each tool in exactly one `geomind/skills/<name>/SKILL.md` (`tools:`), the tool docstring is one
  line + "Skill `<name>`.", the JSON schema exact. A test fails on a tool in no skill or two
  (`tests/unit/context/test_skills.py`). When you change a tool, change its skill.
- Economics may come from any sourced Knowledge document; an assumptions document covering the
  case comes first (`memory/feedback-economics-from-knowledge-documents.md`).
- Goal from the user (TOP priority): every agent tool's first-try refusal rate below 25 %
  (Fatemeh's numbers in `documents/project/quality-assurance/IMPROVEMENTS.md`, "Measured on
  production"). No LLM runs; unit tests that need no LLM for touched files.
- Unit tests: the geomind suite had ~66 stale failures before this session (list in
  `/tmp/a` on the Dell if it survives; else run the suite on a `git archive` of the base and
  compare). Only check that you add no new failures.

## State at handover

Production after the 11:30 deploy (check health and `STATUS.md`): backend 1.1.88, geomind
0.4.85, gemini 0.6.13 (local wheels). If 11:30 did not go out, the prepared commit is backend
main a02a06f, wheels in `backend/.tmp/hotfix-wheels/`.

Released this session: geomind 0.4.79 to 0.4.83, gemini 0.6.13.
- 0.4.79/0.4.80: QA-090 (stop rule), QA-091 (supply temperatures `running`, heat/cold delivered),
  QA-094 (return temperatures a design choice), QA-095 (organisers' CO2 row recommended first),
  economics from an assumptions document.
- 0.4.81: QA-104, QA-105 (per-energy map all or nothing), IMP-012/013 (evaluate_module and
  set_case fix slips with notes; evaluate_module `design`/`result`/`time`), a tool's skill sent
  with its first result (`context/skills.py::first_call_skill`, `engine/step.py::with_skill`).
- 0.4.82: every tool in exactly one skill (migration script `/tmp/hp3-scripts/migrate.py`);
  ask_user/ask_economics descriptions carry their skill section (`tool_section`); IMP-014,
  IMP-015 (`with_repeat_note`), IMP-018 (`dry_precheck` for build/patch/merge), QA-116 (a denied
  tool is not asked again in the request: `session.py::earlier_denial`).
- 0.4.84: read_rag by section (`outline=true`, `section=`), knowledge hits carry `section`
  (`tools/sections.py`; user request for handbooks handbook-plant-design.md etc.).
- 0.4.85: QA-119 (`moved_reference_depth` check), QA-120 (`refuse_percents`).
- 0.4.83: IMP-016 (`drivers.py::stuck_requirements`, 3 rounds), IMP-017 part 1 (a passed design
  with ranges is optimised once: `optimise_task`), QA-097, QA-099, QA-114.
- gemini 0.6.13: unmet_share with failed steps is undecided with the failed steps named
  (verdict `_share`); ElectricBoiler heat is backup in daily_coverage.

Bugs: QA-090, 091, 094, 104, 105 set fixed. After the 11:30 deploy set fixed with notes and write
their Fix sections (written): QA-097, QA-099, QA-114, QA-116, QA-119, QA-120 (claimed `fixing` by hotfix-python).
IMPROVEMENTS.md: IMP-012 to IMP-018 marked done. IMP-019 (one-value choice such as
`params.control.dispatch` = least_cost filled by the tool) waits for the user (no-default rule).

## Next steps, in order

1. After the 11:30 deploy: `qa.py set` QA-097/099/114/116 fixed, Fix sections, STATUS line, tell
   the coordinator (backend 1.1.88, geomind 0.4.83, gemini 0.6.13 + what changed).
2. Tools still above 25 % (IMPROVEMENTS.md table): simulate (missing plant values; dispatch is
   IMP-019), patch_plant (internal errors QA-083), build_plant (class with other modules), set_case
   (value forms, files without time zone), calculate (units; check after QA-074). For each: read
   the measured refusal texts, fix the tool (normalise a pure slip with a note, never a value),
   improve its refusal (what was wrong + the corrected shape + the skill section), and its skill
   (a correct example per call shape, common mistakes). IMP-020 (read_stored outline on a wrong
   path) and IMP-021 (examples from gemini's schema, offline evals from real refusals) are next.
3. Prompts still repeat tool usage in places (case lead's economics section, design prompts):
   move such text into the tool's skill and leave the skill's name (single source).
4. Queued by the coordinator (minor, geomind, not yet claimed): QA-123 (a capacities read says
   the heat exchanger is unused), QA-124 (the verdict gives no values for brine cooling, running
   time and reinjection though the result rows carry them). QA-122 waits for the user.
5. `qa.py next --area geomind,gemini --fixer hotfix-python`.
