# hotfix-back, generation 6 (hotfix-back-VI, renamed hotfix-back-lead): handover (2026-11-05)

Thread "Lead backend hotfixes" (cmsg_016VUmQoW7nUde2xdqUWA2PoVv5N9NXhKzJ4o3vJJ7KHvV), NTNU Dell.
First prompt: continue hotfix-back-V; read account-handover.md, notes/sessions/hotfix-back-5.md,
coordinator-5.md; Fatemeh's bugs first, then `qa.py next --area backend,data,infra`. Chat with
Sahand in Persian, files English, times in chat in Trondheim time (CET).

## Role now (Sahand 18:28 UTC): team LEAD only

`memory/feedback-hotfix-teams.md`. The lead fixes nothing itself: it claims bugs, gives each member a
bug and a disjoint file list, reviews, stages by path, commits per bug, bumps, tags, pushes, deploys,
sets bugs with qa.py. Members (both on the Dell, own threads):
- back-m1: cmsg_016VUmQoW7nUde2xdqUWA2PoA3ZZw99RR8fzMGURGsfHcs: QA-270, then QA-274; owns
  src/api/v1/reporting/**, src/core/gemini/evaluate.py, runs/adapters/designs.py, runs/adapters/simulated.py.
- back-m2: cmsg_016VUmQoW7nUde2xdqUWA2PoVjRZQuqCh5NgeuyepXKZbB: QA-231 (+QA-144; QA-277 is its
  duplicate), then QA-220; owns runs/adapters/callbacks.py, sessions.py, replay.py.
The lead has no thread-message tool: assignments went through the coordinator (send_message @parent).

## Deploy (hotfix mode, no tests rule; Sahand: no waiting for permission, no GitHub releases)

- Lock: `until mkdir /tmp/geomind-backend.lock 2>/dev/null; do sleep 10; done; echo "<name> $(date -u +%H:%M)" > /tmp/geomind-backend.lock/owner`; release `rm .../owner; rmdir ...`.
- Bump `src/version.py`, `openapi.json` (`"version"` line), `docs/app-build/contracts.md` line 3,
  `CHANGELOG.md`; commit by path; `git tag v<N>`; `git push origin main v<N>`; `scripts/hotfix_deploy.sh`.
- `hotfix_deploy.sh` (1.1.104, 1.1.106): builds gemini (dev HEAD) and geomind (main HEAD) from the
  local clones into the image (`Dockerfile.hotfix`); their HEAD must be pushed; uncommitted edits in
  gemini/geomind block nothing; the backend clone must be clean (members' uncommitted backend edits
  block every deploy: commit or wait).
- Batch deploys: every deploy restarts celery; runs resume (QA-176/188 fix) but Manual QA asked for
  fewer restarts. Python-lead commits are complete at HEAD: no go/handshake needed any more.
- The classifier refuses: prod DB reads, answering a run via the API as admin, force pushes.

## Released this generation (all deployed, health ok)

1.1.104 local-build deploy; 1.1.105 kombu<5.7; 1.1.106 geomind 0.4.106 (my engine fix QA-176/184/188:
delegation.py end_orphans keeps the open step's nested runs and resumes them; QA-201
GEOMIND_TEAM_SIZE=8, no default, prompts use `{team_size}`); 1.1.107 QA-167 (project lead gets
list_plants/list_studies, geomind 0.4.108); 1.1.108 QA-217 (agents view cache, pool 20+20); 1.1.109
QA-223, QA-213 reason; 1.1.110 QA-237 (agent runs save no plant versions; adopt/save only) + QA-239
`feasible`; 1.1.111 QA-241, QA-244, QA-249 `prompt`; 1.1.112 QA-252 compare concurrency 3 retries 1;
1.1.113 QA-255 new projects get all enabled MCP servers; 1.1.114 QA-242 step-limit stop = done;
1.1.115/1.1.116 QA-264 (answer on an answered request resumes the run). Env files: all four backend
env files hold the same variable names (Sahand's rule); infra pairs checked equal.
Knowledge: hackathon-2026-assumptions 9f98c448 then others re-uploaded it (latest by
handbook-econ-report-I); QA-161 fixed (data).

## Open

- QA-264: fixed in 1.1.116; Manual QA-IV must answer request-1290 on run bfcec811 once more to unstick it.
- QA-237, QA-239: backend parts live; python parts open (left as fixing / their owners).
- QA-255 UI part with front-lead.
- Queue not yet assigned: QA-215 backend part (plant_version on every result row, dedup equal
  designs, tornado row for a sensitivity study), QA-240 form part (sample study offers
  heating_coverage/cooling_coverage that fail).
- Pre-existing failing tests on main (not ours): test_runs.py::test_events_replay_and_end_at_the_root_run_finished,
  test_execution.py::test_a_run_that_cannot_start_fails_with_geomind_message, test_delegate.py
  step_limit message (geomind).

## Next steps

1. Collect m1/m2 reports, review diffs, commit per bug, one batched deploy, qa.py set fixed with a
   Fix and Retest section in each bug file.
2. Assign QA-215 and QA-240 to whichever member is free (disjoint files).
3. Report each release to the coordinator in one line.
