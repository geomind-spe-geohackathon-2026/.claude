# Handover: hotfix-front-IV (generation 4) -> hotfix-front-V

Written 2026-11-05 ~17:05 UTC by hotfix-front-IV (session_01J2V3UYdmZAR648WwY59MMj). Reason: user
decision, hotfix-front moves to Sonnet (`memory/feedback-session-models.md`), not the context limit.

## Role, first prompt and rules

Read `notes/sessions/hotfix-front-2.md` (the original first prompt, copied in full, and the rules of
generations 1-2) and `notes/sessions/hotfix-front-3.md` (rules of generation 3). Mode: HOTFIX
(decided; do not ask the user). In short: claim with `qa.py claim <id> --fixer hotfix-front-V`; fix
on `main` in the frontend clone only; patch version + CHANGELOG line; build check
`nice sg docker -c "docker build -q -t geomind-frontend:check ."`; commit by path, push; deploy at
once as two Bash calls `cd /home/fatemec/geomind-spe-hackathon-2026/frontend` then exactly
`scripts/hotfix_deploy.sh`; wait for 200 and read the bundle from the page; `qa.py set fixed`;
after every deploy message BOTH Coordinator-IV and Manual QA-II with version, bundle, ids.
Coordinator id: read it from `.claude/STATUS.md` (Coordinator-IV session_01J2V3UYqrLbCNN9zst5WY8d).
Manual QA-II: session_01J2V3UYeTzFtZEuQJvkuadd. User requests come via the coordinator: file each
with `qa.py new ... --area frontend --reporter "user via coordinator"`, fill the file, claim it.

New rule this generation (overrides the "verify live" steps of the earlier notes):

- NO QA TESTS until the user lifts it (`memory/feedback-no-tests-now.md`, 16:55/17:00 UTC): no
  live checks or retests on geomind.team, no browser (Playwright) checks, no LLM/agent runs.
  Offline unit/code tests and builds ARE allowed. So: fix, build check, deploy, set `fixed`, and
  leave `verified` to a later retest. Do not run the /tmp/hf-check scripts against production or
  a local container while this holds.

## State at handover

Production: frontend 1.1.109 (bundle index-DwO4tlF4.js). main = origin/main = ebc5b51, clean.
Backend 1.1.95 with geomind 0.4.91 (IMP-025 instances live).

Done this generation (all live):
- 1.1.107 (5aa65f3) IMP-025 display: one chat line per parallel instance under its lead
  ("Geoscientist I · Thinking · 12 steps"), each line is a `<details>` that opens that instance's
  own steps. Keyed by actor = agent path + `|` + instance (`toActor` in `chat/view.ts`): geomind's
  public `Event.data()` has no run_id (only `step.started` has `session`), so agent+instance is the
  key; blocks' `agent` field holds the actor; `AgentNode` has `key`, `path`, `instance`;
  `toWorkingAgents` returns AgentNode[]; `toAgentTitle` in `chat/agents.ts`. Noted in
  `documents/project/quality-assurance/IMPROVEMENTS.md` IMP-025. Manual QA-II was to watch a real
  parallel run; no report back yet.
- 1.1.108 (97dd942) QA-138: "Start from template" removed from the Plant toolbar. The empty-plant
  card still offers it (not asked; ask the coordinator if it should go too).
  NOTE: `domains/design/plant/page.test.tsx` lines ~426-491 still click the toolbar button; fix
  that test if you run the unit tests.
- 1.1.109 (ebc5b51) QA-137 (History window `max-h` instead of fixed height, Plant and Case) and
  QA-139 (plant version "Flowsheet" tab, `VersionFlowsheet` in `plant/history-panel.tsx`, drawn
  with `toFullFlowsheetSvg`; `VersionDetail` in `shared/versions/history.tsx` takes `views`).
  QA-137/138/139 verified live just before the no-test order.

## Next steps (in order)

1. User (Coordinator-IV, ~17:05 UTC): no templates anywhere. File a bug (minor, frontend, "user via
   coordinator") and remove "Start from template" from the empty-plant card too (`EmptyPlant` in
   `domains/design/plant/page.tsx`, with its `TemplatesDialog`; then `templates-dialog.tsx` is
   unused: delete it if nothing else imports it). The card then needs another way to start a
   plant (point to the chat / add a module; ask the coordinator if unclear). Build, deploy, fixed.
2. User request (Coordinator-IV, ~16:55 UTC), NOT filed yet: file it (`qa.py new`, minor,
   frontend, "user via coordinator") and claim it. In the chat, clicking "Steps so far (N steps)"
   or an agent's line ("Reservoir engineer · Thinking", and each instance line "Geoscientist II
   · ...") must NOT expand the steps inline (the chat jumps/scrolls); open them in a window
   (dialog or side panel) with that agent's steps, live-updating, scrollable, closable; the chat
   stays where it is.
   Code: `src/domains/assistant/chat/blocks.tsx`: `WorkLog` (the "Steps so far" / "Worked
   through" `<details>`) and `WorkingAgents` (one `<details>` per AgentNode; its own work is
   `blocks.filter(b => b.agent === agent.key).filter(isWork)`), both render `WorkItem`. Replace
   the `<details>` with a button that opens a Dialog (`@/components/ui/dialog`, as in
   `shared/layout/history-button.tsx`); render the list inside from the live `blocks` prop so it
   updates; keep which agent is open by `agent.key` in state so it stays open while the agent's
   line exists (if the agent finishes, keep the dialog open on its blocks). Build check, deploy,
   set fixed; no live check (rule above).
3. Then `qa.py list --status open` for frontend bugs; tell Coordinator-IV when the queue is empty.

## Useful facts

- Prettier: `node_modules/.bin/prettier` from the clone root. Many files were not prettier-clean
  before; format only files that were clean at HEAD (check with
  `git show HEAD:<f> | node_modules/.bin/prettier --stdin-filepath <f> | diff -q - <(git show HEAD:<f>)`).
- tsc runs only inside the docker build (`npm run build`); `tsconfig.json` includes tests, so
  type changes must keep test files and mocks compiling (that is why `instance` is optional on
  the event Origin).
- /tmp/hf-check/imp025.js (mocked 3-instance SSE stream, read-only) and qa137.js exist for when
  QA checks are allowed again.
