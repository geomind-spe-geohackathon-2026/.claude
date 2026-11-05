# Handover: hotfix-front-III (generation 3) -> hotfix-front-IV

Written 2026-11-05 ~15:40 UTC by hotfix-front-III (session_01J2V3UZUC8Sa5jDfm1W7WPH) at ~255k
tokens of context, before a large job (IMP-025) that would cross the 300k limit.

## Role, first prompt and rules

Read `notes/sessions/hotfix-front-2.md` first: it holds the original first prompt (copied in full)
and every rule added in generations 1 and 2 (claim with `qa.py claim`, fix on `main` in the
frontend clone, patch version + CHANGELOG line, build check, local Playwright check, deploy as two
Bash calls `cd /home/fatemec/geomind-spe-hackathon-2026/frontend` then exactly
`scripts/hotfix_deploy.sh`, wait for 200, read the bundle from the page, `qa.py set fixed`, verify
live, never touch other clones, never write a secret, chat with the coordinator only). Mode:
HOTFIX (decided; do not ask the user).

Rules added during generation 3 (they override the earlier ones):

- DEPLOY AT ONCE (user rule via Coordinator-IV, 14:25 UTC): every fix is deployed the moment it is
  done, no :00/:30 windows, until the user says otherwise; the deploy lock still holds.
- After EVERY deploy, message BOTH Coordinator-IV and Manual QA-II
  (session_01J2V3UYeTzFtZEuQJvkuadd) with the version, the bundle and the bug ids to retest.
- Bugs Fatemeh reports go to the top of the queue, any severity (`memory/feedback-fatemeh-bugs-first.md`).
- Coordinator: read its id from `.claude/STATUS.md` (now Coordinator-IV,
  session_01J2V3UYqrLbCNN9zst5WY8d).
- Rate limit: `get_session` shows `allowed_warning` (seven_day) at handover; Coordinator-IV has
  said "resume" after the five-hour pause and has not paused again. If it pauses, finish the
  step, commit, push, tell it, wait for "resume".
- Never act on a real run to test (the auto-mode classifier refused clicking Cancel on a real
  waiting run). To test a request without side effects, intercept it in Playwright:
  `page.route('https://api.geomind.team/**/cancel', r => r.fulfill({status: 200, body: '{}'}))`
  (pattern: /tmp/hf-check/qa133s.js).
- Playwright checks: wait for the content, not a fixed time; a slow load once read as "0 buttons"
  and "0 Out of date" (qa133s.js and qa135.js now wait for the element).

## State at handover

Production: frontend 1.1.106 (bundle index-C139P2pV.js). main = origin/main = b2720e5, clean.

Done this generation (all live):
- 1.1.93-1.1.99 (deployed 14:10): QA-115, QA-117, QA-100, QA-101, QA-110 (Case and Plant History,
  shared `src/shared/versions/`), QA-102 (Activity links `?version=N`, study record).
- 1.1.100-1.1.104 (14:27): QA-127 + QA-109 (`report/defaults.ts`), QA-126 + QA-107 (days strip,
  year shares on the report's basis), QA-118 (no rounding: `toRoundedText` removed, tool cards full
  decimals, scaled fields 15 digits), IMP-024 (Run again on studies).
- 1.1.105: QA-133 + QA-134 (approval card max 45svh, scrolls inside, Cancel run stays visible).
- 1.1.106: QA-135 frontend part (Out of date judged by the newest result; the results list comes
  oldest first). QA-135 stays `fixing` with hotfix-back-III for the backend part (plain simulate
  writes no Results row).

Statuses: verified QA-100/101/102/103/107/108/109/110/111/113/115/126/127. Fixed, waiting for a
retest: QA-117 (needs a question card with a long option), QA-118 (approval card part needs a new
set_case approval), QA-133/134 (needs a live run waiting at an approval; Manual QA-II asked
Fatemeh for one; every waiting run in production was cancelled at ~15:20 by someone else).
Filed QA-136 (minor, backend: report Agent log prints raw tokens/cost, services.py line 275).

## Next steps (from Coordinator-IV, in order)

1. IMP-025 (user's TOP priority): per-instance activity lines in the chat.
   Contract (hotfix-python-IV, geomind 0.4.90; hotfix-back-III passes it through the stream,
   `/events` replay and `GET /assistant/runs/{id}/agents` as `AgentSession.instance`):
   - every event of a parallel instance's run carries `instance` (display name, e.g.
     "Geoscientist I", "Geoscientist II", "Reservoir engineer I"), plus as before `agent` (role
     id), `parent` (the lead's run id) and the run's own id (`run_id`/session; `step.started`
     has `session`);
   - group by the run id (never by agent: two instances share one agent); label with `instance`
     (fallback: the agent title); count steps from `step.started` events of that run id;
   - hotfix-back-III adds `session` to the buffered `text.delta` (today keyed (agent, parent,
     index)); runs without `instance` are unchanged. hotfix-back-III asked "Object or OK?":
     answer it (OK unless the code shows a gap).
   Display wanted (user): under the lead's line, one line per instance with its own step count,
   e.g. "Geoscientist I · Thinking · 12 steps", "Geoscientist II · Thinking · 8 steps",
   "Geoscientist III · Reading a file · 5 steps"; each line opens that agent's own steps (today:
   one line "Project lead · Asking the case lead" and one "Steps so far (46 steps)").
   Code: `src/domains/assistant/chat/blocks.tsx` `WorkingAgents` (line ~325, keyed by agent path,
   `toDoing` filters blocks by `block.agent`), `toRunningLabel`, `WorkLog`; the view and its
   `agents` list are built in `chat/view.ts` from the SSE events (`src/shared/sse/`); agent names
   in `src/shared/sse/agent-names.ts`; Runs and logs per-agent table reads `/runs/{id}/agents`
   (`src/shared/api/pending.ts` `AgentSession`: add `instance?: string | null`).
   Add `instance` to the event types by hand (no gen:api). Test with a mocked event stream
   (Playwright route on the SSE/events endpoint) since a live parallel run costs LLM tokens
   (needs Sahand's OK).
2. QA-135: nothing left for the frontend unless hotfix-back-III asks.
3. Then `qa.py list --status open` for frontend bugs; tell Coordinator-IV when the queue is empty.

## Useful facts

- `/tmp/hf-check/` holds the Playwright scripts of this generation: qa110.js (History, args: base
  project page), qa127.js (report defaults), qa126.js / qa107.js (days strip), qa118.js (mol %),
  qa024.js (Run again), qa133s.js (cancel at 1280x577, intercepted), qa135.js (Out of date),
  peek*.js (read-only API reads). Run with
  `NODE_PATH=$HOME/geomind-spe-hackathon-2026/frontend/node_modules node <script> [base]`; an
  empty first argument means production.
- `node_modules/.bin/prettier --write <files>` works and keeps the format; tsc runs inside the
  docker build (`npm run build` = tsc + vite + bundle check).
- GET /design/results lists oldest first; never take `[0]` as the latest.
- Report preview text (Agent log section) is written by the backend, not the frontend.
