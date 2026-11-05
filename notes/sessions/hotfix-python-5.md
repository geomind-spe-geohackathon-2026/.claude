# hotfix-python-5 handover (2026-11-05, account handover at 90 % usage)

You are hotfix-python-VI, the successor of hotfix-python-V (session_01J2V3UWw2qHaxMQh8g5F2JY).
The work reopens on Sahand's account (`.claude/account-handover.md`); no successor was started.

## Role and mode

Mode: HOTFIX (decided; do not ask the user). You fix the QA bugs and IMP items of the Python
packages geomind and gemini (areas geomind, gemini) and work the speed plan's B and C items. The
coordinator is the one in `.claude/STATUS.md` (was Coordinator-IV, session_01J2V3UYqrLbCNN9zst5WY8d);
send it one line per fix or deploy with `send_message`, and the same to Manual QA-II
(session_01J2V3UYeTzFtZEuQJvkuadd), if they still run.

First prompt of hotfix-python-V, in full: "You are hotfix-python-V, the successor of
hotfix-python-IV (session_01J2V3UZqdULpCLT7XEFdd6t). Read
~/geomind-spe-hackathon-2026/.claude/notes/sessions/hotfix-python-4.md and follow it; your role's
rules and mode are in it, so do not ask the user for the mode. Start now."

Read first, in order: `notes/sessions/hotfix-python-1.md` (bug loop, deploy steps, rules learned),
`hotfix-python-2.md`, `hotfix-python-3.md`, `hotfix-python-4.md` (rules in force: deploy at once,
lock `/tmp/geomind-backend.lock`, Fatemeh's bugs first, no QA tests/LLM runs, offline unit tests
allowed, lead-only-writes IMP-025 rule, gemini changes allowed with what/why in each commit),
then this file. No new user rules came in this session.

## State

- Production (checked in geomind-celery at ~15:20 UTC): backend 1.1.97, geomind 0.4.95, gemini
  0.6.16 (local wheels). QA-128, 140, 143, 121 are live. I did not hold the lock at handover
  (hotfix-back-IV held it for QA-144 since 15:14).
- geomind `main` = a13b72d (Release 0.4.95), clean. gemini untouched by me.
- QA-128 judgement told to the coordinator: grid electricity CO2 is no longer priced (still in the
  co2 metric); a case flag could price it if the user wants.
- Unit-test baseline of geomind HEAD a13b72d (git archive in /tmp/hp5/base, run with
  `PYTHONPATH=/tmp/hp5/base .venv/bin/python -m pytest -q -p no:cacheprovider -n 8 tests/unit`):
  56 failed, 2148 passed, 17 errors (output /tmp/hp5/base.txt if it survives). Add no new failure.

## In progress: QA-145 (major, Fatemeh, TOP; status fixing, Fixer hotfix-python) = plan C1/C2

Bug: `documents/project/quality-assurance/bugs/QA-145-*.md` ("sahand test 2" run ed03d7ea: 70 min,
plant v23, 0 simulate; 27 hand patch_plant, 3 empty; 107 of 231 calls re-reads; 3 design_lead
sessions failed at a deploy and work was redone). Log: `evidence/QA-145/run-ed03d7ea-log.json.gz`
(steps[].tool_calls[] with `tool`, `input`, `output`).

WIP pushed on geomind branch `wip/hotfix-python-V`, commit d168ea9 (NOT on main, not released):
- `geomind/agents/design/proposal.py` (new): `Change{path, value, source, reason}`,
  `Evaluation{module, point, why}`, `Proposal{changes, evaluations, case_changes, couplings, note}`,
  `proposer_tools(agent)`: describe_module (kept), search_knowledge, read_knowledge,
  search_memory, read_memory, finish.
- reservoir.py, well.py, energy.py: engineers use `proposer_tools` + `Output(Proposal)`; no
  read_case/read_plant/read_profile/patch_plant/evaluate_module/read_stored/search_rag any more.
- design/lead.py: `team()` returns only `fill_parts` (Team of reservoir/well/energy systems
  engineers, list briefs ≤4, instances named "<Role> <Roman>"); process and integration
  engineers and the single-engineer tools are removed from the lead (their agent classes and
  prompts still exist, unused); ENGINEER_TOKENS 4000; lead gets `read_rag`.
- tools/gemini/plants.py: `patch_plant(changes=dict | list)`: `listed_changes` turns the
  engineers' `[{path, value, ...}]` into a merge patch; `wrapped_choices` now runs after
  `placed_parameters`; a patch that changes nothing is refused `no_change` and stores nothing.
- prompts/design/lead.md: a 7-step gated design path from handbook-design ch 0 (read once; build
  once; split `issues` by the 0.3 groups into one `fill_parts`; one patch_plant with all changes;
  simulate as soon as `missing` is 0; fix from failures by owner (0.5); optimize); old team
  rules (process -> integration -> fill_parts -> merge_designs, small-step patches) removed;
  reuse stored `findings` after a restart.

Still to do for QA-145 before release:
1. Rewrite the engineer prompts (`prompts/design/reservoir.md`, `well.md`, `energy.md`): Inputs =
   the brief only; Tools = the proposer tools; workflow: read the brief, describe_module only for
   a module not in the appendix, Knowledge for sourced values, return `changes` with the plant
   path and plant-file value form, `evaluations` instead of evaluate_module, case changes,
   couplings; drop every read_case/read_plant/patch_plant/evaluate_module line. The handbook
   0.3 groups: I subsurface and wells, II treatment and gas, III heating, IV cooling.
2. Skills: `working-in-a-team` "Parallel instances" (fill_parts list form, the Proposal shape,
   the lead's one write); `designing-a-plant` patch_plant section (list form, `no_change`);
   check `tests/unit/context/test_skills.py` (each tool in exactly one skill).
3. Tests: `tests/unit/agents/design/test_lead.py` (tool names, order text, fill_parts tests),
   `tests/unit/engine/test_memory_off.py`, `tests/unit/prompts/test_prompt.py`
   (well-engineer pump-depth text), `tests/unit/agents/design/test_reference.py`; add tests for
   `listed_changes` and the `no_change` refusal. Compare with the baseline above.
4. Docs: `.claude/docs/agents.md` DesignLead row; CHANGELOG; bump geomind patch (0.4.96:
   pyproject.toml and `geomind/__init__.py`), merge the branch into main (fast-forward or rebase
   onto main first), tag, push, deploy (hotfix-python-1.md steps; bump backend on top of main),
   tell hotfix-front (frontend `blocks.tsx` labels fill_parts "Asking the team"; agent-names.ts
   has the engineer names: no change needed) and the coordinator.
5. Parts that may need the backend (give to hotfix-back): one plant version per stage instead of
   per patch (the lead-only write mostly gives it), reuse of finished engineers' work after a
   design_lead restart (findings are already saved per QA-047; the prompt now says to reuse them).
6. Then `qa.py set QA-145 --status fixed` with the Fix section.

## Next steps after QA-145, in order (Coordinator-IV)

1. Plan `documents/project/plans/speed-case-plant.md`: B2 (case lead plan step: map fields to
   ≤4 groups using handbook-case.md ch 0 "Case checklist for the case lead"; point the case lead
   prompt at it via `read_rag(section=...)`), B3 (one set_case, one approval card with sources,
   one question card), B4 (the refusals of run 9696f5d4: no_case x2, update_state list form,
   set_case files-only, set_case date without time zone; no-defaults: a time zone only from the
   case's own data, never assumed), B5/C4 IMP-027 budgets (wall-clock and rounds per sub-agent,
   set by the lead; Delegate `steps` exists, add a time limit), C3.
2. Baseline `documents/project/plans/speed-case-plant-baseline.md` (41 runs, 8914 calls, 17 %
   refused; plant ~78 active min/run, 1 of 17 done; simulate 35 % refused). Its top 10, in this
   priority: #10 stalls and re-reads (a concrete next step on the 2nd identical refusal,
   "unchanged since step N" for repeated reads, budgets); #1 read_stored/read_result dotted
   paths; #4 calculate/run_python; #2 evaluate_module inlets; #3 empty plant values before the
   first build; #5 patch_plant ownership; then #6-#9 (#9 = B4); web_search 12 words. Details in
   the file.
3. Then (hotfix-python-4.md list): read_rag -> read_file and search_rag -> search_files rename
   (old names kept via `tools.base` RENAMED_TOOLS), QA-122 geomind part, IMP-028, IMP-026, the
   two backend tests failing since geomind 0.4.89, why design_lead sessions failed in run
   ed03d7ea, `qa.py next --area geomind,gemini --fixer hotfix-python`.
