# Handover: hotfix-front-V (generation 5) -> next hotfix-front (account handover)

Written 2026-11-05 by hotfix-front-V (Sonnet), stopped by the account handover order (usage 90 %).
No successor was started.

## Role, first prompt and rules

Read `notes/sessions/hotfix-front-2.md` (original first prompt, copied in full), `hotfix-front-3.md`
and `hotfix-front-4.md` (rules). Mode: HOTFIX (decided; do not ask). In short: claim with
`qa.py claim <id> --fixer <name>`; fix on `main` in the frontend clone only; patch version +
CHANGELOG line; build check; commit by path, push; deploy at once as two Bash calls
(`cd /home/fatemec/geomind-spe-hackathon-2026/frontend`, then exactly `scripts/hotfix_deploy.sh`);
wait for 200, read the bundle from the page; `qa.py set fixed`; after each deploy message BOTH the
coordinator (id in `STATUS.md`) and Manual QA-II (session_01J2V3UYeTzFtZEuQJvkuadd).
NO QA TESTS until the user lifts it (`memory/feedback-no-tests-now.md`): no live checks, no
Playwright, no LLM runs; offline unit tests and builds are allowed.

LESSON: the build check must be `nice sg docker -c "docker build --no-cache -q -t geomind-frontend:check ."`
and its output grepped for `error|sha256`. A cached `-q` build once passed while the real deploy
build failed on a tsc error (unused variable in a test; tsconfig includes tests).

## State

Production: frontend 1.1.112 (bundle index-CKyM7tml.js), main = origin/main = 5ddc296, clean.
Done this generation (all live, none live-checked, all `fixed`, waiting for retest):
- 1.1.110: QA-141 (no "Start from template" on the empty-plant card; templates-dialog.tsx deleted;
  the card points to the chat), QA-142 (Steps so far / Worked through / each agent line open their
  steps in a Dialog, `StepsWindow` in `chat/blocks.tsx`).
- 1.1.111: QA-139 follow-up: plant version Flowsheet tab is the Plant page's `Canvas` read-only
  (`readOnly`, `changed` props in `canvas.tsx`; `VersionCanvas` in `plant/history-panel.tsx`);
  changed modules outlined and marked "changed" (`module-node.tsx`).
- 1.1.112: QA-146 (unnamed "· Thinking · 0 steps" line): `toAgentName("")` now returns
  "Coordinator", an empty `instance` falls back to the agent name (`shared/sse/agent-names.ts`,
  `chat/agents.ts`). CAUSE IS A GUESS (I never saw the event). Not retested.
No bug is left `fixing` with me. No frontend bug was open at the last `qa.py list --status open`.

## Next steps (in order)

1. QA-146: when tests are allowed, retest. If a nameless or "0 steps" line still shows, read the
   run's events (`/assistant/runs/{id}/events`) for the event with an empty `agent`/`instance`;
   if the event carries no agent id, tell hotfix-back-IV (session_01J2V3UWBvFYRd3VG1pYpCXZ) or
   hotfix-python-V which part is missing.
2. `qa.py list --status open` for frontend bugs; take them by severity (Fatemeh's first).
3. Plan E2 stage timer: the coordinator mentioned it; I got no details. Ask the coordinator for the
   spec before starting.
4. Retests owed (Manual QA-II, when allowed): QA-139, 141, 142, 146; earlier: QA-117, 118, 133, 134.
5. Known test debt: unit tests were not run this generation; `plant/page.test.tsx` and
   `chat/blocks.test.tsx` were edited (templates tests removed/replaced, details assertion replaced
   by `queryByRole("dialog")`); run `npm run check` in a container when allowed.
