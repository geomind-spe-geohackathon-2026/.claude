# Handover: hotfix-front (generation 1) -> hotfix-front-II

Written 2026-11-05 09:25 UTC by hotfix-front (session_01J2V3UYxh6obK4VSajGwZvk), at about 515k
tokens of context (rule: hand over at 300k, `.claude/session-refresh.md`).

## Role and first prompt (copied in full)

> You are the hotfix session "hotfix-front" of the GeoMind project, started by the coordinator
> session on Fatemeh's word. Mode: HOTFIX (already decided; do not ask the user for the mode).
>
> Read first, in this order: ~/geomind-spe-hackathon-2026/.claude/AGENTS.md, .claude/STATUS.md,
> .claude/memory/MEMORY.md, documents/project/ops/development-modes.md (section "Hotfix, step by
> step"), documents/project/quality-assurance/README.md, and frontend/AGENTS.md.
>
> Your job: fix the QA bugs of the FRONTEND, one at a time, fastest path to production
> (geomind.team), and loop until none is left:
> 1. Claim: `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py next --area frontend --fixer hotfix-front`. It prints the bug id and file, or nothing when no open frontend bug is left. Never work on a bug you did not claim, and never edit BUGS.md by hand.
> 2. Read the bug file and its evidence. Decide the repo the fix really belongs in. You own the frontend clone only (~/geomind-spe-hackathon-2026/frontend). If the fix belongs in the backend, geomind or gemini, run `qa.py set <id> --status open --note "belongs in <repo>: <why>"` after changing its Area in the bug file to that repo, save it (`qa.py save <id>`), and take the next. When the bug could be fixed as well in the frontend as in a Python package, fix it in the frontend.
> 3. Fix on `main` in the frontend clone: only the code the bug needs. Run NO tests, NO lint, NO checks. Raise the patch version in package.json and add a CHANGELOG.md line with the bug id. Commit with the bug id and title in the message (e.g. "QA-005: chat question shows as one paragraph"), stage files by path, push main.
> 4. Deploy at once: `cd ~/geomind-spe-hackathon-2026/frontend && scripts/hotfix_deploy.sh` (it waits for the shared deploy lock, builds the image once, compose never builds). Report the bundle it prints.
> 5. `qa.py set <id> --status fixed --note "frontend <version>, commit <sha>, deployed"`.
> 6. Check the fix on geomind.team by the bug's steps (Playwright in frontend/node_modules; if the browser cannot start for missing system libraries, check what you can with curl and say so in the note). Then `qa.py set <id> --status verified --note "<what you checked>"`, or back to `open` with what still fails.
> 7. Send the coordinator a one-line report with send_message: ids, versions, anything that needs a person. Then go to step 1.
>
> Rules: chat replies may be short English; every file in English; never write a secret anywhere (the admin login for geomind.team is FIRST_ADMIN_EMAIL / FIRST_ADMIN_PASSWORD in ~/geomind-spe-hackathon-2026/backend/.env: read it at run time, never copy it into a file or a message). Never touch the backend, geomind, gemini or infrastructure clones; another session (hotfix-back) owns them. Keep CPU low (nice for builds). When no open frontend bug is left, tell the coordinator and wait; check again every 10 minutes with qa.py list --status open.

## Rules added during the session (they override the prompt above)

- The coordinator is read from `.claude/STATUS.md` (now Coordinator-II
  session_01J2V3UXD6UT73meeapsG2MS; Coordinator-III takes over soon). Messages to it: one line,
  only for a fix shipped, a blocker or a needed decision.
- Deploy only in windows at :00 and :30 UTC, batching fixes; a blocker may go at once. The
  coordinator can put a deploy hold on (deploy only blockers) and lifts it.
- Deploy as TWO separate Bash calls, nothing else on the line: `cd /home/fatemec/geomind-spe-hackathon-2026/frontend`,
  then exactly `scripts/hotfix_deploy.sh` (that is the allow rule). The site gives ~30 s of 404
  while the new container starts: wait until `curl https://geomind.team/` answers 200, then read
  the bundle from the page (the script prints an empty `bundle:`).
- Before you push: check the build with `nice sg docker -c "docker build -q -t geomind-frontend:check ."`
  (the local node_modules is stale, so `tsc`/`npm run` do not work; no other tests or lint).
- Commit and push often, one change per commit, message with what, why and the ids, so any
  change can be reverted (`memory/feedback-commit-often.md`). Never leave the clone dirty between steps.
- At the start of every step check `get_session` (no id): `rate_limit_info.status` must be
  `allowed`; otherwise finish the step, commit, push, tell the coordinator, wait for "go on".
  Hand over at 300k context tokens (`session-refresh.md`).
- No periodic checks or wakeups; when no frontend bug is open, tell the coordinator and wait for
  its message. One `send_later` per deploy window is fine.
- Bugs owned by another fixer (hotfix-back, hotfix-python): add a note with your frontend part
  (`qa.py set <id> --status <its status> --fixer <its fixer> --note ...`); never change status/fixer.

## State at handover

- Production frontend: 1.1.77 (bundle index-Bl3Hb3Ei.js, deployed 06:00 UTC).
- `main` = origin/main = 8673032 = 1.1.80, clean, pushed, build-checked, NOT deployed yet.
  The deploy hold is lifted: deploy it at 10:00 UTC (coordinator's word). It holds:
  - 1.1.78 (74122f8) QA-088 frontend part: agent study rows show a summary from
    `GET /design/study/{id}/agent-record` with "Open record" (new route `design/study/:studyId/record`,
    `src/domains/design/study/record-page.tsx`, `agent-record.ts`); a 404 keeps "Open run" only.
    QA-088 belongs to hotfix-back (status fixing): add a "frontend part deployed" note.
  - 1.1.79 (e131a37) QA-074 frontend part: chat tokens/cost = max(run usage, sum of finished
    steps), "Steps so far (N steps)". QA-074 belongs to hotfix-back (status open): add a note.
  - 1.1.80 (8673032) QA-089 (mine, `fixing`): Runs and logs step list as a compact agent tree
    (`src/domains/assistant/runs/log-page.tsx`).
- My other bugs: QA-027, 028, 029, 030, 031, 033, 038, 053, 057, 058, 059, 062, 073 are `fixed`
  (live, but their behaviour needs a live run, a 429, a waiting run etc. to recheck); verify them
  when such a situation shows up. All others I fixed are `verified`.
- No reminder is scheduled (I deleted the 10:00 one when handing over).

## Next steps, in order

1. 10:00 UTC: check rate limit and clean clone; deploy (two calls); wait for 200; read the bundle.
2. `qa.py set QA-089 --status fixed --note "frontend 1.1.80, commit 8673032, deployed"`; then check
   read-only the run log of run 3bdd7ebb (project 61134432): agent tree, the selected step's agent
   open, no wrapped labels; set QA-089 verified or open.
3. Notes on QA-088 and QA-074 ("frontend part deployed, 1.1.78 / 1.1.79"), keeping status and fixer.
4. One line to the coordinator (id from STATUS.md), then `qa.py next --area frontend --fixer hotfix-front-II`.

## Useful facts about this code

- Hand-written API types for endpoints not yet in `schema.d.ts` go in `src/shared/api/pending.ts`
  (`PendingPaths`); do not run `npm run gen:api` in hotfix (it brings ~1100 lines of other changes).
- Live tool.finished carries only the first 200 chars of a result; the chat fetches the full call
  from `GET /assistant/runs/{run_id}/calls/{call_id}` when a calculate/run_python/web_search/
  read_web_page/set_case card opens (`src/shared/sse/tool-views.tsx`, `chat/blocks.tsx`).
- `streamEvents` (`src/shared/sse/stream.ts`) passes each stored event once by id (QA-081).
- Agent display names: `src/shared/sse/agent-names.ts`.
- Decisions on requests come from the public `answer` event (`chat/answers.ts`, `view.ts`).
- Playwright: scripts in /tmp/hf-check, run with
  `NODE_PATH=$HOME/geomind-spe-hackathon-2026/frontend/node_modules node <script>`; sign in by
  POST `https://api.geomind.team/api/v1/identity/authn/login` with the env credentials and put
  `{accessToken, refreshToken}` into localStorage `geomind.session`. An empty chat is `/assistant/chat?new`.
