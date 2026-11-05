# hotfix-back, generation 1: handover to hotfix-back-II (2026-11-05 ~09:40 UTC)

Old session: hotfix-back, `session_01J2V3UWh6RugyR1DAxrkNhH` (Claude Code Remote, Dell bridge).
Coordinator: read its id from `.claude/STATUS.md` before every message (was Coordinator-II
`session_01J2V3UXD6UT73meeapsG2MS`; Coordinator-III takes over around 09:45 UTC).

## Role and mode

You are the hotfix session for the BACKEND, DATA and INFRA areas of the GeoMind project.
Mode: HOTFIX (decided; never ask the user for the mode). Chat with Fatemeh/Sahand happens through
the coordinator; every file in English; never write a secret anywhere (read `backend/.env` only at
run time, never copy or print values).

Read first: `.claude/AGENTS.md`, `.claude/STATUS.md`, `.claude/memory/MEMORY.md`,
`documents/project/ops/development-modes.md` ("Hotfix, step by step"),
`documents/project/quality-assurance/README.md` (incl. "Who fixes what"), `backend/AGENTS.md`,
`.claude/session-refresh.md`.

The loop (original instructions, adapted by the later rules below):
1. Claim: `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py next --area backend,data,infra --fixer hotfix-back`
   (or `qa.py claim <id> --fixer hotfix-back` when the coordinator names a bug). Never edit BUGS.md
   by hand. To move a bug to another session: `qa.py set <id> --status open --area <area> --note "for <session>: <why>"`.
2. Read the bug and its evidence. Fix in the backend whatever can be fixed there (50/50 rule);
   geomind and gemini belong to hotfix-python-II (you do not edit those clones, except the cost
   catalogue data in `geomind/data/knowledge/` when the coordinator gives you data work); the
   frontend belongs to hotfix-front.
3. Fix on backend `main`: only what the bug needs. Bump the backend patch in `src/version.py`,
   `CHANGELOG.md` (with the bug id), `docs/app-build/contracts.md` line 3 and `openapi.json`
   `"version"` (regenerate with `.venv/bin/python scripts/to_openapi.py` after route/schema
   changes). Stage by path.
4. Deploy with exactly two calls: `cd /home/fatemec/geomind-spe-hackathon-2026/backend`, then
   exactly `scripts/hotfix_deploy.sh` (the allow rule matches only that text).
5. `qa.py set <id> --status fixed --note "..."`; check on prod; `verified` or back to `open`.
6. One line to the coordinator per fix (send_message).

## Rules given during the session (most are in memory/ or the QA README)

- Backend lock: before changing any backend file
  `until mkdir /tmp/geomind-backend.lock 2>/dev/null; do sleep 20; done; echo "hotfix-back-II QA-<nnn> $(date -u +%H:%M)" > /tmp/geomind-backend.lock/owner`;
  pull right after; keep it through commit, push and deploy; release with
  `rm /tmp/geomind-backend.lock/owner && rmdir /tmp/geomind-backend.lock` (`rm -rf` is refused).
- Commit and push before a bug and as soon as it is fixed; never leave a clone dirty. One change
  per commit; message says what, why and ids so it can be reverted (`memory/feedback-commit-often.md`).
- Deploys only in :00/:30 UTC windows, batching; a blocker may go at once. Before a deploy, list
  running runs and name them in the commit (they are resumed since QA-035, not cut). The
  coordinator may announce a deploy hold: then deploy only a blocker.
- At the start of every step check `get_session` (no id) `external_metadata.rate_limit_info`: if
  status is not "allowed" and `resetsAt` is in the future, finish the step, commit, push, release
  the lock, tell the coordinator, wait. A `resetsAt` in the past means the window has reset.
- Hand over at 300,000 used tokens (`.claude/session-refresh.md`).
- Production DB reads and data writes through `docker exec ... psql` and the Knowledge re-seed are
  often refused by the auto-mode classifier: then give the coordinator the exact command for
  Sahand. Starting new infra services was refused too (Sahand runs `docker compose up -d`).
- Backend code holds docstrings only, no `#` comments (`tests/test_no_comments.py`).
- No default values: a missing setting is an error naming it.

## State

- Prod: backend 1.1.79 (geomind 0.4.73, gemini 0.6.10). Backend `main` holds 1.1.80 and 1.1.81
  (mine, QA-088) plus hotfix-python-II's work; hotfix-python-II deploys the batch at 10:00 UTC with
  geomind 0.4.78 and gemini 0.6.12 (the hold ended). Do not deploy that batch separately.
- All clones clean and pushed; the backend lock is free; nothing scheduled.
- Open with me:
  - QA-088 `fixing`: 1.1.80 (f0c0562) `GET /design/study/{id}/agent-record` + done agent studies
    show progress 1/1; 1.1.81 (0ae7fca) on `study.recorded` one result row per simulated entry of
    the artifact's `runs` (needs geomind 0.4.77+). After the 10:00 deploy: set QA-088 fixed with
    the versions; retest = an agent study recorded after 10:00 shows in the Results tab.
  - QA-074 (open, area now geomind/gemini/frontend, fixer still hotfix-back): analysis in its Fix
    section (provider retries, not an idle worker); waits on a prod read (query in the bug).
- In progress: the QA3 seed (task from Sahand via the coordinator, after the 10:00 deploy):
  `backend/scripts/seed_qa_projects.py` (commit 7c25748) is written and pushed but NOT run.
  Run it from `backend/` after 10:00:
  `.venv/bin/python -m scripts.seed_qa_projects --api https://api.geomind.team/api/v1 --env .env --sample ../gemini/examples/hackathon_2026`
  It prints one JSON line per project (ids, case version, plant versions, result ids). It uses only
  the public API as the admin (FIRST_ADMIN_* read from `.env`). Not tried yet: the auto-mode
  classifier may refuse prod writes; if so, give the coordinator the command for Sahand. Facts:
  the sample case names `data/demand.csv` and `economics.json` (uploaded as case files); the two
  sample plants check clean against the case with gemini 0.6.4 (no sizing step needed); a page
  study runs ONE plant version, so "one run study over both plants" (QA3 report) is two ranked
  `run` studies (objective `lcts`, metric `co2`); tell the coordinator that. Reply to the
  coordinator with the five project ids and what each holds.
- Cleanup owed (one commit, no deploy needed on its own): turn my `#` comments into docstring text
  (test_no_comments): `backend/src/api/v1/assistant/runs/adapters/callbacks.py` lines ~273 and ~474,
  `backend/src/api/v1/assistant/runs/execution.py` ~175 and ~181,
  `backend/src/api/v1/design/study/services.py` ~145.

## Things built this session worth knowing (all in backend CHANGELOG)

QA-007/017/021/024/031 (per-chat auto-approve in Redis, `GET/PUT /assistant/chat/{id}/auto-approve`),
QA-032 (date column → time on case CSV upload), QA-035 (worker resumes running runs on start),
QA-040/049 (plant-level `backup`/`depth` listed and named missing), QA-044 (bad Last-Event-ID = new
stream), QA-046 (usage includes running nested runs), QA-056/077/081 (request/state consistency:
row follows newest request, ended runs never return to waiting, stale or already-answered resumes
handled, `geomind_refused`), QA-058 (`answer` event), QA-060 (`infrastructure/maintenance`
fallback page), QA-068 (`provider_refused`), `GET /assistant/runs/{id}/calls/{call_id}`, evolve
`/design/study/{id}/structures` and `/structures/{rank}/plant`, SearXNG
(`infrastructure/searxng`) and the run_python sandbox on the worker (docker socket, `DOCKER_GID`,
`GEOMIND_SANDBOX_*`, `GEOMIND_SEARCH_URL`), cost catalogue cleanup (geomind 0.4.52, QA-006/045).

## Next steps, in order

1. Report in to the coordinator (id from STATUS.md): "hotfix-back-II started".
2. After the 10:00 UTC deploy: check health, set QA-088 fixed.
3. Run the QA3 seed; report the five project ids.
4. The `#` comment cleanup commit.
5. Then the loop: `qa.py next --area backend,data,infra --fixer hotfix-back`.
