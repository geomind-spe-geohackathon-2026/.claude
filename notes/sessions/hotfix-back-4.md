# hotfix-back, generation 4: account handover (2026-11-05, usage 90 %)

Old session: hotfix-back-IV (successor of hotfix-back-III). No successor was started (coordinator
order: the work reopens on Sahand's account, `.claude/account-handover.md`).

## Role and first prompt

The first prompt of this generation: "You are hotfix-back-IV, the successor of hotfix-back-III.
Read notes/sessions/hotfix-back-3.md and follow it; your role's rules and mode are in it, so do
not ask the user for the mode." So: read `notes/sessions/hotfix-back-3.md` in full (role = hotfix
for BACKEND, DATA, INFRA; mode HOTFIX, never ask; no QA tests/live runs; deploy at once; backend
lock; two-call deploy `scripts/hotfix_deploy.sh`; the script does not tag, tag after the commit).
Coordinator id: read it in `STATUS.md` (was Coordinator-IV, session_01J2V3UYqrLbCNN9zst5WY8d).

## State

- Prod backend 1.1.98 (my release, tag v1.1.98, geomind 0.4.95, gemini 0.6.16): QA-144 fixed.
  `UsageTree` (`src/api/v1/assistant/runs/adapters/callbacks.py`) now keeps every nested run at any
  depth by run_id and parent; run total = max(own, sum of children). Test
  `tests/api/v1/assistant/runs/test_usage_tree.py`. QA-144 is `fixed`, not live-checked
  (retest recipe in the bug file).
- No lock held; backend, .claude and documents clones clean and pushed. No bug left `fixing`.
- Still failing on main, not ours: `test_execution.py::test_a_run_that_cannot_start_fails_with_geomind_message`,
  `test_runs.py::test_events_replay_and_end_at_the_root_run_finished`.

## Open requests from Coordinator-IV (not started, only read)

Source: `documents/project/plans/speed-case-plant-baseline.md`.

1. `ts` on every step event, in the stored run log and the stream, to measure elapsed time per
   stage. Findings so far: geomind events already carry `time` (set by `engine/log.py` with
   `utc_now()`), stored in each `run_events` row's `data` (`event.to_dict()`), but
   `Event.data()` (public data, used by the stream and `GET /runs/{id}/events`) drops `time`
   (`BASE_FIELDS` are excluded), and `gd.runlog` (geomind `types/runlog.py:137`, fixed JSON used by
   `services.read_log` via `adapters/replay.py:to_runlog`) has no per-step clock. Plan: in the
   backend add `ts` (= event `time`) to the step events' data in `EventPublisher.on_event`
   (`callbacks.py`, where `StreamEvent` is built; `step.started`/`step.finished`) and to the events
   the /events replay serves; for the log, inject `ts` per step after `to_runlog` by matching the
   stored `step.started` events (run_id/agent + index) with the runlog's steps, or hand a runlog
   `ts` field to hotfix-python-V if the injection is not clean. Update `docs/app-build/contracts.md`
   (additive) and regenerate `openapi.json` if a schema changes; offline test; deploy at once; tell
   the coordinator and hotfix-front-V.
2. "patch_plant: internal error" with no message, 18 calls in runs 753645c0 and eb7b95df: find the
   cause (backend or geomind; geomind part to hotfix-python-V) and give the real message. Read the
   run logs through the API (reads allowed; no live runs): `GET /assistant/runs/{id}/calls/{call_id}`
   for the failing calls; grep `internal` in geomind's tool wrapper and the backend Workspace
   (`runs/adapters/`) for where the message is lost. QA-081 had the same symptom for a refused
   resume (`execution.py:169` logs geomind's words).
3. IMP-025 integration check (code path only): events carry `instance`, `/runs/{id}/agents` shows
   it (backend 1.1.94 added it; verify against geomind 0.4.95).
4. Then Fatemeh's bugs first, then `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py next --area backend,data,infra --fixer <your name>` (none open at 17:40 UTC).
