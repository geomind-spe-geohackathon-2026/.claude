# hotfix-back, generation 3: handover to hotfix-back-IV (2026-11-05 ~17:10 UTC)

Old session: hotfix-back-III, `session_01J2V3UVuLrkzKAZV6dAkLmu` (Claude Code Remote, Dell bridge).
Coordinator: read its id from `.claude/STATUS.md` before every message (now Coordinator-IV,
`session_01J2V3UYqrLbCNN9zst5WY8d`). Earlier notes: `notes/sessions/hotfix-back-1.md`, `-2.md`
(read `-2.md` for the full loop; everything in it still holds unless changed below).
Model: you run on Sonnet (user, 16:50 UTC; `memory/feedback-session-models.md`).

## Role and mode

The hotfix session for the BACKEND, DATA and INFRA areas. Mode: HOTFIX (decided; never ask).
Chat with Fatemeh/Sahand goes through the coordinator; every file in English; never write a
secret anywhere (read `backend/.env` only at run time).

Read first: `.claude/AGENTS.md`, `.claude/STATUS.md`, `.claude/memory/MEMORY.md`,
`documents/project/ops/development-modes.md` ("Hotfix, step by step"),
`documents/project/quality-assurance/README.md`, `backend/AGENTS.md` (import boundaries:
gemini only in `src/core/gemini/`, geomind only `import geomind`/`geomind.<name>` in
`runs/adapters/`), `.claude/session-refresh.md`, and `notes/sessions/hotfix-back-2.md`.

## Rules in force (new or changed in generation 3)

- NO QA TESTS (user, 16:55 UTC, `memory/feedback-no-tests-now.md`): no live checks or retests on
  geomind.team, no browser checks, no agent/LLM runs. Offline unit/code tests that need no LLM
  ARE allowed. So after a deploy set bugs to `fixed` (not `verified`) with a retest recipe.
- DEPLOY AT ONCE (user, ~14:40 UTC): deploy every finished fix immediately, no :00/:30 windows;
  the backend lock still holds; tell the coordinator each version.
- Team lead only writes (`memory/feedback-team-lead-only-writes.md`): in IMP-025 only the lead
  writes project files; instances are for display/usage.
- Backend lock: `until mkdir /tmp/geomind-backend.lock 2>/dev/null; do sleep 20; done; echo
  "hotfix-back-IV <id> $(date -u +%H:%M)" > /tmp/geomind-backend.lock/owner`; pull; keep it
  through commit, tag, push, deploy; release `rm /tmp/geomind-backend.lock/owner && rmdir
  /tmp/geomind-backend.lock`. Other sessions (hotfix-python-IV) deploy too: bump on top of the
  latest version on main.
- Deploy: two calls, `cd /home/fatemec/geomind-spe-hackathon-2026/backend`, then exactly
  `scripts/hotfix_deploy.sh`. The script does NOT tag: after the commit run
  `git tag -a v<version> -m "..." && git push origin v<version>`.
- Version bump each fix: `src/version.py`, `openapi.json` `"version"` (or regenerate with
  `.venv/bin/python scripts/to_openapi.py` after schema changes), `CHANGELOG.md`,
  `docs/app-build/contracts.md` line 3.
- Full offline suite with design tests takes >15 min; run the touched areas with
  `-n 8 -p no:cacheprovider --no-cov` (CPU budget: <= ~24 cores, `nice`).
- Known failing on main, NOT ours (sent to hotfix-python-IV): `test_execution.py::
  test_a_run_that_cannot_start_fails_with_geomind_message` and `test_runs.py::
  test_events_replay_and_end_at_the_root_run_finished`.
- Prod writes via the admin API to cancel runs are refused by the classifier: give the coordinator
  the exact command for the user (see generation 3's QA-133 message pattern).

## State (17:10 UTC)

- Prod: backend 1.1.96 (geomind 0.4.91, gemini 0.6.15 local wheels). hotfix-python-IV is about to
  deploy gemini 0.6.16 + geomind 0.4.93 on top.
- My releases today: 1.1.90 QA-122 backend (Workspace `project_designs` + `plant_version`),
  1.1.91 QA-136 (verified), 1.1.93 IMP-025 part 1 (VersionRecorder saves one at a time),
  1.1.94 IMP-025 part 2 (live text/usage/tool problems keyed by run_id; `instance` through
  stream, /events, buffered text.delta + `session`, `AgentSession.instance`), 1.1.96 QA-135
  option C (`runs/adapters/simulated.py` SimulationRecorder: the run's last plain simulate becomes
  one result on root run.finished).
- Bugs: QA-135 `fixed` (backend part, not live-checked). QA-118, QA-126, QA-133, QA-134 routed to
  frontend with causes in their files. QA-122: geomind part with hotfix-python-IV. QA-074 still
  waits on a prod read.
- I hold no lock; backend, .claude, documents clones clean and pushed.

## Next steps, in order

1. Report in to the coordinator: "hotfix-back-IV started".
2. IMP-025 integration: once geomind with `instance` is live, check the code path only (no live
   runs while the QA-test stop holds): events carry `instance`, `/runs/{id}/agents` shows it.
3. Fatemeh's bugs first, then `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py next --area backend,data,infra --fixer hotfix-back-IV`.
