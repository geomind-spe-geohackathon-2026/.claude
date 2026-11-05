# hotfix-python-6 handover (2026-11-05, stopped on Coordinator-V's word: reopen on the NTNU Dell)

You are hotfix-python-VII, the successor of hotfix-python-VI.

## Role and mode

Mode: HOTFIX (decided; do not ask the user). Same role as `hotfix-python-5.md` (read it, and
1-4 for the bug loop, deploy steps and rules). Coordinator: Coordinator-V (see `STATUS.md`);
one line per release.

First prompt of hotfix-python-VI, in full: "You are hotfix-python-VI, the successor of
hotfix-python-V (session_01J2V3UWw2qHaxMQh8g5F2JY, Fatemeh's account). Read
~/geomind-spe-hackathon-2026/.claude/notes/sessions/hotfix-python-5.md and follow it; your role's
rules and mode are in it, so do not ask the user for the mode. The coordinator is Coordinator-V
(local session geomind-spe-hackathon-2026-e9; message it with SendMessage). Start now."

New rules from the user this session (via the user and Coordinator-V):
- HOTFIX only: never a branch, never a git worktree. Work directly on geomind `main` in the
  shared clone. The old branch `wip/hotfix-python-V` is merged into main (leave it, push no other
  branch).
- A background session refuses file edits outside a worktree: this session had to be reopened
  as a normal session to edit. If edits are refused, ask the user in your own session and tell
  the coordinator in one line; never work around it.

## State

- Production unchanged: backend 1.1.98, geomind 0.4.95, gemini 0.6.16 (local wheels).
- WARNING: geomind `origin/main` = 0666b5d holds QA-145 work that is NOT released and still says
  version 0.4.95. Anyone who builds a geomind wheel from `../geomind` now ships it under 0.4.95.
  Finish and release it as 0.4.96 first (or tell hotfix-back not to build geomind until then).
- geomind main commits this session: d168ea9 (WIP from hotfix-python-V, fast-forwarded),
  3b9159d (engineer prompts), 0666b5d (lead reads the handbook with `read_knowledge` instead of
  `read_rag`, so the design lead still reads no project file; skills `working-in-a-team` (design
  team proposal form) and `designing-a-plant` (patch_plant list form, `no_change`); design tests
  updated; explanatory comments removed from code per test_code_quality).

## QA-145 progress (status fixing, Fixer hotfix-python)

Done: hotfix-python-5.md steps 1 and 2 (prompts, skills), most of step 3.
Engineer prompts: `prompts/design/{reservoir,well,energy}.md` now: brief only, tools
describe_module / search_knowledge / read_knowledge / finish (memory tools only inside the
`<!-- memory -->` block, else test_memory_off fails), output Proposal {changes, evaluations,
case_changes, couplings, note}.

Unit tests (`PYTHONPATH` not needed in the clone: `nice .venv/bin/python -m pytest -q -p
no:cacheprovider -n 8 tests/unit`; baseline failures list /tmp/hp5/base_fail.txt from a git
archive of a13b72d, which could not run the git-based code-quality tests). Still to do:
1. `tests/unit/tools/gemini/test_plants.py`: `test_patch_plant_names_a_split_riser_without_its_pump_depth`
   and `test_a_plant_ready_for_its_case_still_has_no_issues_after_the_run_check` call
   `patched_issues(plant, {})`: an empty patch is now refused `no_change`. Change the tests to
   read the issues another way (e.g. `read_plant` on the stored design or a real one-value
   patch), keeping the `no_change` refusal.
2. Add `tests/unit/agents/design/test_proposal.py` (test_mirror needs it): Proposal shape,
   `proposer_tools` names; and tests for `listed_changes` (list -> merge patch, a bad item is a
   ToolError at `changes.<i>`) and the `no_change` refusal.
3. Run the whole unit suite and compare with the baseline. Code-quality failures in
   case/lead.py, analysis/lead.py, web.py, mcp.py, python.py, builtins.py, delegate.py,
   module_call.py, runs.py, test_study.py, economics.py and the design-lead / process tests
   `test_it_is_complete`, superstructure, `quoting stopped` were already failing before
   (pre-existing; check with `git stash`-free means, e.g. a git archive plus `git init` in /tmp).
4. hotfix-python-5.md steps 4-6: `.claude/docs/agents.md` DesignLead row, CHANGELOG, version
   0.4.96 (pyproject.toml, `geomind/__init__.py`), tag, push, deploy (lock, backend bump),
   tell hotfix-front (no change needed) and Coordinator-V, `qa.py set QA-145 --status fixed`.

## Next steps after QA-145 (Coordinator-V order)

QA-122 geomind part (contract in hotfix-python-4.md), then the speed baseline top 10
(`documents/project/plans/speed-case-plant-baseline.md`), B2-B5, read_rag -> read_file rename,
IMP-028, IMP-026. Fatemeh's bugs jump to the top.
