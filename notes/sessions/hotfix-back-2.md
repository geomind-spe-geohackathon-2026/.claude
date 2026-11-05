# hotfix-back, generation 2: handover to hotfix-back-III (2026-11-05 14:15 UTC)

Old session: hotfix-back-II, `session_01J2V3UZeNoBawJDgCJuBHr7` (Claude Code Remote, Dell bridge).
Coordinator: read its id from `.claude/STATUS.md` before every message (now Coordinator-IV,
`session_01J2V3UYqrLbCNN9zst5WY8d`). Generation 1's note: `notes/sessions/hotfix-back-1.md`.

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
  `until mkdir /tmp/geomind-backend.lock 2>/dev/null; do sleep 20; done; echo "hotfix-back-III QA-<nnn> $(date -u +%H:%M)" > /tmp/geomind-backend.lock/owner`;
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

## Rules added during generation 2 (all in memory/ or noted here)

- Hotfix sessions deploy their finished fixes at every :00/:30 UTC window on their own, no holds;
  deploy everything ready; one deploy at a time via the backend lock
  (`memory/feedback-hotfix-deploy-every-half-hour.md`). When another session holds the lock for a
  deploy, ask it to bump on top of your commits and carry them (that worked all day), then tell
  the coordinator the version after each deploy.
- Bugs Fatemeh reports go to the TOP of the queue, any severity (`memory/feedback-fatemeh-bugs-first.md`).
- `hackathon-2026-assumptions.md` and the hackathon guides live ONLY in the global Knowledge,
  never in a project's files (user decision; the QA3 seed does not upload them).
- Prod writes through the public API as the admin worked for the QA3 seed and the engine check,
  but the classifier refused replacing global Knowledge documents: for that give the coordinator
  `.venv/bin/python -m scripts.replace_knowledge --api https://api.geomind.team/api/v1 --env .env <files>`
  (backend `scripts/replace_knowledge.py`) for the user.
- Admin API from scripts: `from scripts.seed_qa_projects import Api, credentials`;
  `Api("https://api.geomind.team/api/v1", *credentials(Path(".env")))`, run from `backend/` with
  `.venv/bin/python -`. Reads (results, studies, versions, Knowledge list) are allowed.
- The backend dev venv now has the prod wheels (gemini 0.6.13, geomind 0.4.82 from
  `.tmp/hotfix-wheels`); `requirements.txt` still pins gemini 0.6.4 / geomind 0.4.26.

## State (14:15 UTC)

- Prod: backend 1.1.88 (since 11:32 UTC, hotfix-python-III: geomind 0.4.85, gemini 0.6.13) holds
  all my work: 1.1.82 (QA-092), 1.1.85 (QA-106), 1.1.87 (QA-110/QA-102/QA-104 backend parts).
  Backend main after it: 931cac5 (test-only fix of test_case_aware; no deploy needed).
- All my clones clean and pushed; I hold no lock; nothing scheduled.
- Bugs: QA-088, QA-092, QA-095, QA-106 fixed. QA-104 fixed (gemini/geomind parts by
  hotfix-python-III; my backend part in 1.1.87). QA-110 and QA-102 open, area frontend, for
  hotfix-front-III (split in `notes/sessions/hotfix-front-2.md`; my backend parts are live:
  `GET /design/case/versions/{n}`, `POST /design/case/versions/{n}/restore`, `Version.by`,
  change-naming assistant case notes, version activity `link.id` = number). QA-107 routed to
  gemini/frontend (analysis in its Fix). QA-122 routed to geomind with a contract proposal
  (workspace method for project plant versions and page studies; needs Sahand's OK; backend side is
  mine once geomind defines it). QA-123/QA-124 geomind. QA-074 still waits on a prod read.
- QA3 projects (seeded 10:05 UTC, competition files only): case 15b2f15f-46d0-4b09-a44b-0f849127c1f0,
  plant c45a5382-af55-43fc-9340-dd1ab1245533, simulation ef87f914-3aaa-4f58-be60-2d54c7687511,
  study 7a852d89-dfe5-423c-980a-a4ca231353bc, report 91b202b6-6236-45e7-8860-a58437d6eb98.
  Engine check project "QA3 engine check" 25cbe5ad-2b22-425a-91fc-fbc3c78d5eb4: gemini OK
  (matches 46d15d6b's Optimise LCTS exactly). IMP-024 (Run again on a study) filed.
- Known plain fact: `test_adapters.py::test_the_live_stream_gives_a_failed_tool_its_problem` failed
  once in a full run (SimpleNamespace has no `parent`, callbacks.py:233); not investigated.

## Next steps, in order

1. Report in to the coordinator: "hotfix-back-III started".
2. If hotfix-front-III asks for a backend "best result" flag for QA-127, it is yours (Coordinator-IV).
3. Fatemeh's bugs first, then `qa.py next --area backend,data,infra --fixer hotfix-back-III`.
