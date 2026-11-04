# WEBSITE I: handover

Written 2026-11-03. Owner: Sahand (writes Persian, answer him in Persian; coordinator notes are English, answer in English).

## Machine and repos

Windows WSL2 Ubuntu 24.04, user `fatemec`, host NTNU09811, folder `~/geomind-spe-hackathon-2026`.

- `backend`, main at `1368fe3`. FastAPI, Celery, Postgres, Redis, MinIO.
- `frontend`, main at `e90a162`. React, Vite, Tailwind, React Flow.
- `ux/frontend`, branch `ux-agent-first`: separate chat-first UX work, not part of this thread.
- `gemini`, `geomind`, `infrastructure`: read-only for this work.
- Start with `backend/docs/app-build/status.md`, `handover.md`, `contracts.md` (held version 47), `requests.md`, `gemini-requests.md`, and `frontend/AGENTS.md`.

Production: geomind.team runs from main on this laptop. It is at backend `1368fe3`, frontend `e90a162`, gemini wheel 0.5.5, geomind 0.4.1 (`-e ../geomind` at c9a5c1c), deployed by hosting at 23:38 UTC on 2026-11-02. The projects SPE GeoHackathon 2026 and Live tests b, c and d are on production. The local dev database was wiped and now holds only seed data. The local stack is stopped.

## State right now

Sahand's "wait" holds: start nothing until he says to continue. Nothing is running.

Uncommitted in `backend`, tests and lint passed (568), not pushed:
- `.env.example`: adds `GEOMIND_MODEL`, `GEOMIND_CHEAP_MODEL`, `GEOMIND_PROVIDER`.
- `tests/api/v1/assistant/runs/test_adapters.py`: the env examples name only allowed models.
- `docs/app-build/contracts.md`: version 47, DeepSeek model example.
- `docs/app-build/status.md`: contract version line.

## Remaining work

Ready once Sahand says continue:
1. Commit and push the held change above. Rerun checks first.
2. Tidy the report process diagram lines; long lines between Treatment and Heating cross (`frontend/src/shared/plant/flowsheet-layout.ts`, `flowsheet-sheet.ts`).

Waiting on geomind 0.4.2 being final. Do not wire a partial version.
3. Wire it as a pinned release if available, otherwise tell the coordinator: env vars, a backend startup check with a clear error and a test, update `.env.dev` and example files, give the production variable names. `GEOMIND_CONTEXT_WINDOW=128000` takes effect then. Do not work around geomind problems in the app.
4. Drop `-e ../geomind` once released.
5. One approved live test, on a dev stack and a copy of the competition project, never production, capped at 1 USD in total: a design chat (size, optimise LCTS, explain), confirming `study.recorded` fires, results appear and the final answer shows; one budget-stop test with a tiny cap; verify in run logs that every step ran on DeepSeek. Report agents, tools, tokens, cost, time, answer quality, bugs and screenshots. Until 0.4.2 is final the no-token rule holds, and this approval covers only that test.
6. Check in 0.4.2: the `loops/design.py:293` crash, tool output size (`build_plant` about 30k characters, tokens reached 66k per call), and a clear budget stop message.

Waiting on others:
7. geomind items in `requests.md`.
8. gemini items in `gemini-requests.md`: for Sahand's review only.
9. Hosting: confirm `ASSISTANT_MODEL_PREFIX` is not changed on production. The three GEOMIND model lines were DeepSeek at 21:48 local on 2026-11-02.
10. Fatemeh: confirm `fatemeh.chitsaz@ntnu.no` is on her GitHub account.

Not yet seen by eye on production: the new report diagram, Plant zoom on the competition project, wide report tables on a phone with real data, Compare labels with several designs, Days covered in dark, Plant section with unit conversion.

Sahand's decision: rewrite about 98 old frontend commits to Fatemeh? Recommendation: no, it needs a force-push on main.

Small open items: a run shows `done` when its last tool failed; budget caps not retested on DeepSeek (item 5 covers it).

## Rules

- No comments in code; docstrings or the required JSDoc only.
- No default engineering or economic values. Everything general; competition numbers only in project data, never in code. Do not offer to limit the template list.
- Agents use DeepSeek only: `deepseek/deepseek-v4.1-flash-1017`, provider `relace/fp4`. Never Sonnet or any Anthropic model for agents. The app refuses others through `ASSISTANT_MODEL_PREFIX`. Do not pick Sonnet for helper subagents either.
- No live LLM runs or tokens except the approved test above.
- gemini is the source of truth. Ask gemini for nothing without Sahand's permission, and never contact its thread or repo. Only list needs in `backend/docs/app-build/gemini-requests.md`.
- gemini and geomind repos are read-only. Infrastructure files, production containers and infrastructure `.env` files are off limits. Never commit a `.env`.
- Never print keys, tokens or passwords.
- Production deploys and imports go through the coordinator to hosting. The permission check refuses them here, including `down -v` and production reads; do not work around it. Never `--reset` or `down -v`. When a fix is pushed and tested, send the coordinator the commits.
- Work on main for backend and frontend. Stage by explicit path, check `git status` first, run backend tests and frontend lint, typecheck and targeted tests, read the result, then `git pull --rebase` and push in a separate step.
- Other sessions edit these clones. Never test against another session's worktree (such as `gemini/.tmp/gemini-work`); use clean worktrees under the repo's `.tmp/`.
- Every git worktree goes only under the repo's own `.tmp/`.
- Frontend commits are authored as Fatemeh Chitsaz (repo-local config); backend stays Sahand's. No model identifiers in commits.
- Do not run unfinished code on the dev stack Sahand uses.
- Sahand's messages arrive late and his screenshots may show old builds: compare against timestamps and current code. Report plainly, claim only what was checked, and say what was not seen on production.

## Local testing

```
export NVM_DIR="$HOME/.nvm"; . "$NVM_DIR/nvm.sh"; nvm use 22
sg docker -c "bash /tmp/claude-1000/comp/fake-stack.sh"
sg docker -c "scripts/stack-down.sh"
```

`fake-stack.sh` is three lines in throwaway `/tmp`: from `backend`, export `ASSISTANT_LLM=fake ASSISTANT_SANDBOX=none`, then run `scripts/stack-up.sh`. This uses no tokens.

Playwright needs `LD_LIBRARY_PATH=$HOME/.local/pw-libs/root/usr/lib/x86_64-linux-gnu:$HOME/.local/pw-libs/root/lib/x86_64-linux-gnu`. Port 5174 may be held by `ux/frontend`; run mock e2e with a temporary config on another port. Keep `transfer/` and backups. Screenshots are in `screenshots/`.
