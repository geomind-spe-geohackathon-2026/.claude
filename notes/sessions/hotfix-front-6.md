# Handover: hotfix-front-VI (generation 6) -> hotfix-front-VII

Written 2026-11-05 by hotfix-front-VI (Sonnet, then Opus), on Coordinator-V's order (session moves
to the NTNU Dell environment). No successor started by me; the coordinator reopens it.

## Role, first prompt and rules

Read `notes/sessions/hotfix-front-2.md` (original first prompt, in full), `hotfix-front-3.md`,
`-4.md` and `-5.md` (rules, build-check lesson). Mode: HOTFIX (decided; do not ask).
User orders given this generation via Coordinator-V:
- HOTFIX only: work directly on `main` in the shared frontend clone. Never a new branch, never a
  git worktree.
- No tests, no lint, no `npm run check`: only the required image build check
  (`nice sg docker -c "docker build --no-cache -q -t geomind-frontend:check ."`, grep
  `error|sha256`), then commit by path, push, deploy at once with `scripts/hotfix_deploy.sh`
  (two Bash calls: `cd .../frontend`, then the script), wait for 200, read the bundle name.
- No QA/live tests (`memory/feedback-no-tests-now.md`).
- Reply to Coordinator-V one line per release. Coordinator-V's address: `Coordinator-V` (if the
  bare name fails, use `ListAgents` and the shown name with its `[ref]`). Manual QA is now
  `Manual QA-III`; message it after each deploy too.

## State

Production: frontend 1.1.113 (bundle index-TsXgd_n9.js), main = origin/main = 77fa7f3, clean.
Done this generation:
- 1.1.113: plan E2 stage timer. Each agent line of the busy list (`WorkingAgents` in
  `chat/blocks.tsx`) shows `· <time>` via `StageTimer`; `AgentNode.startedAt` (`chat/view.ts`)
  is the server `ts` of the agent's first `step.started` (backend 1.1.99, `ts?` added to
  `shared/sse/types.ts`), else the browser clock at the first event. `view.test.ts` `toShape`
  zeroes `startedAt`. Not live-checked.
- QA-146 offline: `src/shared/sse/agent-names.test.ts` (`toAgentName("")` = "Coordinator").
No frontend bug open or `fixing` (last `qa.py list`: QA-122 geomind open, QA-145 geomind/backend
fixing by hotfix-python).

Note: vitest in the clone fails for most chat tests (local `node_modules` lacks
`class-variance-authority`, `sonner`); only `view.test.ts` ran (19/19). Tests are not wanted now.

## Next steps (in order)

1. `qa.py list --status open`: frontend bugs by severity, Fatemeh's first; claim, fix, deploy.
2. If none: one line to Coordinator-V and wait.
3. Retests owed (Manual QA-III, when tests are allowed): QA-139, 141, 142, 146, E2 timer; earlier
   QA-117, 118, 133, 134.
