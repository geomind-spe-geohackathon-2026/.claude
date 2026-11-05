# speed-analysis-I: handover note

Role: analysis session for task A of `documents/project/plans/speed-case-plant.md`. Started by
Coordinator-IV (session_01J2V3UYqrLbCNN9zst5WY8d), Sonnet, mode hotfix (decided; do not ask the user).

## First prompt (copied)

Read AGENTS.md, STATUS.md, MEMORY.md (feedback-no-tests-now.md, feedback-team-lead-only-writes.md,
cpu-budget-dell.md), then the plan. Tasks A1 and A2: an OFFLINE analysis of the agent runs stored on
production since 2026-11-05 00:00 UTC. Read-only: list runs and read their events/agents/logs through the
API (backend/scripts/seed_qa_projects.py has Api and credentials; from backend/: .venv/bin/python,
--env .env). NEVER start, approve, cancel or change a run, project or Knowledge entry; no live QA checks;
no LLM. Output: documents/project/plans/speed-case-plant-baseline.md: per run and per stage (case, plant,
sizing, simulate): elapsed time, steps, approval and question cards, sub-agent instances; per tool the
first-try refusal rate; the top 10 refusal/stall causes with counts, an example message and the fix each
calls for (prompt, skill, tool schema, gemini message), named for hotfix-python. Stage files by path,
commit, push. Then send Coordinator-IV a summary of the top 10. Hand over at 300k context.

## State

Done: baseline written (documents 6711075), top 10 sent to Coordinator-IV, who gave it to hotfix-python-V
(causes) and hotfix-back-IV (event `ts`, `patch_plant: internal error`). Scripts in
`documents/project/plans/speed-baseline-scripts/` (README has the run order). No successor started.

## Re-run the baseline (after a geomind release)

1. `mkdir -p /tmp/sa/scripts /tmp/sa/data`; copy the scripts there (they hardcode `/tmp/sa`).
2. From `backend/`: `.venv/bin/python /tmp/sa/scripts/fetch.py`, then `fetch2.py` (edit the date filter
   `>= '2026-11-05'` to the release time; use only new runs), then `nice -n 10 python3 analyse.py`,
   `write.py`, `report.py`. Only GET calls. About 540 MB of logs for 41 runs.
3. Write `speed-case-plant-baseline-<geomind version>.md` beside the first one (keep the first).

## What to compare

- Case: wall time (target < 5 min), refusals (baseline 6 of 41 calls), cards (2 Q + 2 A), instances (0).
- Plant: active min per run (baseline 78), refused share (16%), runs reaching `optimize` (1 of 17).
- Simulate refused share (35%). Per-tool first-try refusal: evaluate_module 52%, patch_plant 40%,
  calculate 52%, run_python 81%, build_plant 43%, read_stored 9.7%.
- Top-10 cause counts (T3 284, T1 249, T4 191, T2 174, T5 139, T7 91, T6 88, T8 83, T9 68, T10 29); a
  fixed cause should fall to near 0. Repeats/re-reads (read_case 533, evaluate_module repeats 159).
- Caveats: no step timestamps (active min = model + tool time, parallel instances add up; wall includes
  user waits) until hotfix-back adds `ts`; then compute elapsed per stage from it. No QA runs may be
  started by this session (feedback-no-tests-now.md): analyse only runs that already exist.
