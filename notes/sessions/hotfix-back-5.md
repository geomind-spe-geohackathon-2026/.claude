# hotfix-back, generation 5: handover (2026-11-05)

Old session: hotfix-back-V (successor of hotfix-back-IV). Reopened in the NTNU Dell environment on
the coordinator's order (user's word). Model: Opus (user's word, via Coordinator-V).

## Role and first prompt

First prompt of this generation: "You are hotfix-back-V, the successor of hotfix-back-IV
(session_01J2V3UWBvFYRd3VG1pYpCXZ, Fatemeh's account). Read
~/geomind-spe-hackathon-2026/.claude/notes/sessions/hotfix-back-4.md and follow it; your role's
rules and mode are in it, so do not ask the user for the mode. The coordinator is Coordinator-V
(local session geomind-spe-hackathon-2026-e9; message it with SendMessage). Start now."

So: read `notes/sessions/hotfix-back-3.md` (all rules: role = hotfix for BACKEND, DATA, INFRA;
mode HOTFIX, never ask; backend lock `/tmp/geomind-backend.lock`; two-call deploy `cd backend`
then `scripts/hotfix_deploy.sh`; the script does not tag: tag `v<version>` after the commit and
push it; version bump in `src/version.py`, `openapi.json`, `CHANGELOG.md`,
`docs/app-build/contracts.md` line 3).

## Rules given in this generation (Coordinator-V, user's word)

- HOTFIX mode only, strict: work directly on `main` in the shared clone; never a new branch,
  never a worktree.
- Message the coordinator with SendMessage by its ListAgents name (`Coordinator-V`; it was
  `ntnu09811-sprightly-conway` before a rename). Reply one line per release.
- A read of the prod database (`docker exec geomind-postgres psql ...`) is refused by the
  classifier ("Production Reads"); do not work around it, say so in the report.
- The local `backend/.venv` has an old geomind (0.4.82); prod runs the wheels in
  `backend/.tmp/hotfix-wheels` (geomind 0.4.95, gemini 0.6.16). Read the wheel to check geomind
  code that prod runs.

## State

- Prod backend 1.1.99 (my release, tag v1.1.99, commit 6da2df0, deployed, health ok):
  `ts` (ISO time of the event) on `step.started`/`step.finished` in the stream and `/events`
  (`ToolProblems.public`, `runs/adapters/callbacks.py`), and `ts` on every step of the run log
  (`with_step_ts` after `gd.runlog`, `runs/adapters/replay.py`). Test
  `tests/api/v1/assistant/runs/test_step_ts.py`. Additive contract change noted.
- patch_plant "internal error" (runs eb7b95df, 753645c0, 05:28-06:06 UTC): predates QA-083
  (backend 1.1.75, geomind 0.4.71: internal tool errors carry class, message, file:line). No
  backend defect, no release. Not re-checked on prod data (DB read refused).
- IMP-025 integration checked (code only): geomind 0.4.95 events carry `instance`
  (BASE_FIELDS); backend passes it through stream, /events, /agents (1.1.94).
- QA-122: backend part live since 1.1.90 (`Workspace.project_designs`, `plant_version`); the
  geomind part stays with hotfix-python-VI (coordinator agreed). Not claimed.
- `qa.py next --area backend,data,infra`: none open. QA-145 (geomind,backend) is `fixing` by
  hotfix-python.
- No lock held; backend, .claude, documents clones clean and pushed. No bug of mine `fixing`.
- Still failing on main, not ours: `test_runs.py::test_events_replay_and_end_at_the_root_run_finished`,
  `test_execution.py::test_a_run_that_cannot_start_fails_with_geomind_message`.

## Next steps

1. Report in to Coordinator-V (read its name in `STATUS.md` / ListAgents).
2. Fatemeh's bugs first (Manual QA-III), then
   `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py next --area backend,data,infra --fixer <your name>`;
   claim, fix on main, bump, commit, tag, push, deploy, set `fixed` with a retest recipe, tell
   the coordinator one line per release.
3. If none open: tell the coordinator in one line and wait.
