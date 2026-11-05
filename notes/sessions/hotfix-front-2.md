# Handover: hotfix-front-II (generation 2) -> hotfix-front-III

Written 2026-11-05 ~11:00 UTC by hotfix-front-II (session_01J2V3UVLf5yhPSiTnivcPyR) at about 290k
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


## Rules added since generation 1 (they override the above)

- Deploy everything that is ready at EVERY :00 and :30 UTC window, on your own; no coordinator
  holds (user rule, `memory/feedback-hotfix-deploy-every-half-hour.md`). One deploy at a time via
  the lock. After each deploy send Coordinator-III one line with the version and bundle.
- Coordinator: read its id from `.claude/STATUS.md` (now Coordinator-III,
  session_01J2V3UWsUm5z442CiXM5MZU). It forwards user requests: file each with
  `qa.py new "<title>" --severity minor --area frontend --reporter "user via coordinator"`, copy the
  screenshot it names into `evidence/QA-<id>/1.png` (copy to that ONE folder; a glob target once
  went wrong), fill the bug file (Versions, Where, Steps, Expected, Actual, Evidence, Cause, Fix),
  `qa.py save`, `qa.py claim <id> --fixer hotfix-front-III`.
- `qa.py next` claims bugs of other fixers whose Area includes frontend (it took QA-074 once):
  prefer `qa.py claim <id>` for the ids the coordinator gives you.
- Local check before pushing: build `geomind-frontend:check`, run it
  (`sg docker -c "docker run -d --rm --name hf-check-X -p 127.0.0.1:18xxx:80 geomind-frontend:check"`)
  and drive it with Playwright, routing `https://geomind.team/**` to the local container so the API
  answers (pattern: /tmp/hf-check/qa096s4.js, qa108.js, qa111.js). Stop the container after.
- Never delete or rename a real project while testing (QA test projects stay).

## State at handover

- Production: 1.1.86 (bundle index-C9q6wEoE.js) since 10:31 UTC, unless the 11:00 deploy below ran
  (see the last line of this file).
- main = origin/main = e5f68bc = 1.1.92, clean, pushed, build-checked; deploy at 11:00 holds:
  - 1.1.87 QA-103 (97ab8e4): shared `shared/quantity/usage.tsx` (Duration, Tokens, formatDuration, formatTokens).
  - 1.1.88 QA-108 (134e0da): DataTable three backgrounds (header sunken, even sunken/60, hover sunken).
  - 1.1.89 QA-111 (57aa56a): one ProjectMenu (`domains/workspace/settings/project-menu.tsx`) for sidebar and cards (Pin, Rename, Settings, Delete); routes.ts passes it to ProjectsPage.
  - 1.1.90 QA-108 addition (22b5c0b): "#" row numbers via CSS counter `.data-table-numbered` (styles/index.css); `numbered={false}` for Alternatives and structures; chat runs window on DataTableFrame.
  - 1.1.91 QA-113 (7169bbe): shared DropZone 3x taller, strong drag highlight.
  - 1.1.92 QA-107 part (b) (e5f68bc): Days covered "Partly short" with unmet share, rule in legend. QA-107 status stays open (part (a) is gemini's); add a note when (b) is live.
- After the deploy: set QA-103, QA-108, QA-111, QA-113 fixed, then verify live with
  /tmp/hf-check/qa103.js, qa108.js, qa111.js, qa113.js (run without the base argument to hit
  production) and set verified; QA-107: note "(b) live". Tell Coordinator-III the version.
- Verified today: QA-089, 093, 096, 098. QA-088 / QA-074 frontend parts live (hotfix-back owns them).

## Next steps (from Coordinator-III, in order)

1. QA-110 (major, Case History: open a version read-only, diff to the previous one with paths,
   values and sources, Restore like the plant's, a real note, "Saved by" the assistant) is shared
   with hotfix-back-II (session_01J2V3UZeNoBawJDgCJuBHr7). SPLIT AGREED (10:58 UTC), backend lands
   at 11:30: (a) GET /design/case/versions/{number} -> same Case body as GET /design/case for that
   version; (b) POST /design/case/versions/{number}/restore body {"base": <latest number>} -> 201
   Case, new version "Restored version N", 409 on a stale base; (c) assistant notes name the
   changed paths; (d) case and plant version objects get "by": "assistant" | "user".
   Frontend (you): a history row opens that version read-only (a); compare with the version before
   (diff the two contents client-side: paths, old/new values, sources); Restore (b) like the
   plant's; Saved by shows "Assistant" when by = assistant. Add the endpoints to
   `src/shared/api/pending.ts` (no gen:api). QA-110 first; hotfix-back-II claims the bug for the
   backend part, you write your part under your name in Fix.
2. QA-102 (Overview Activity links), split agreed: backend gives "Saved plant/case version N"
   activity rows link id "N" (new rows only). Frontend: design/plant and design/case with link id N
   open History on version N; design/study/<id> opens the study; sentence-case actor.
3. QA-115 (minor, user via coordinator, filed and claimed for you): schema-form groups
   (Case, Plant, Economics ... in `src/shared/forms`) collapsed by default; a group with a validation
   error or missing required value opens or shows a marker; keep open/closed state while on the
   page. The coordinator asked for it in the next window.
4. QA-109 (minor, Report Agent log empty by default: pick the run that made the result).
5. QA-100, QA-101 (cosmetic: Runs and logs section titles; Overview Recent chats layout).

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

- Shared table: `src/shared/ui/data-table.tsx` (DataTable, DataTableFrame, DataHead, DataCell,
  dataTableClass); every table in the app uses it (QA-096, QA-108).
- Drop zone: `src/shared/attach/drop-zone.tsx`. Days strip: `src/shared/charts/days-strip.tsx`.
- Favicons are in `static/` (the build's publicDir; `public/` is dev only, for MSW).
