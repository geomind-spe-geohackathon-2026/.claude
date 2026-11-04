---
name: shared-clones-and-production
description: "This laptop's clones are shared with other sessions and production runs here; how to commit, test and hand over deploys"
metadata:
  node_type: memory
  type: project
  originSessionId: 6151c1ed-a06f-5f3c-933b-0beeedd6e182
  modified: 2026-11-04T12:32:51.539Z
---

Since 2026-11-02 the geomind backend and frontend clones on this machine are edited by other sessions, and production (geomind.team) runs on this laptop from main. Sahand tests on production; the dev database was wiped after the move.

**Why:** a `git add` of whole folders swept another session's edits into a commit, and chaining test and push pushed failing tests twice. The permission check refuses production deploys and `down -v` here even with relayed approval, so those steps go to the hosting thread or Sahand.

**How to apply:**
- Stage by explicit path. Check `git status` first.
- Run lint, tsc and tests, read the result, then push in a separate step, with `git pull --rebase` first.
- Do not build or restart production or delete volumes. Send the coordinator the pushed commits, and the exact command if a step is blocked. Never touch infrastructure files.
- Frontend commits are authored as Fatemeh Chitsaz (repo-local config); backend stays Sahand's.
- Another session may have uncommitted edits in a clone: stage only your own files by path. Python `-I` ignores PYTHONPATH.
- Port 5174 may be held by `ux/frontend`; run mock e2e with a temporary config on another port.
- Tests may need `.env.example` values exported if `backend/.env` is changed.
- Since 2026-11-03 the backend and frontend clones sit on `dev`. Commit there, test locally, then `git push origin dev:main` once tests pass; `main` goes to production through hosting.
- Chat text streams over `WS /assistant/runs/{id}/stream` with SSE as fallback; pacing lives in `frontend/src/domains/assistant/chat/paced-text.ts`.
- No git worktrees (Sahand, 2026-11-04 evening): one clone per repo in the project root; `.tmp/` stays in `.gitignore` for scratch files.
- Since 2026-11-03 the app thread is BACKEND I and does backend work only (Sahand's rule). Frontend tasks go to the frontend thread (WEBSITE UX I) through the coordinator.
- geomind is public since 2026-11-03 07:52 UTC: the backend pins its release wheel by URL and sha256 in `requirements.txt`, like gemini (no `vendor/`). Never use geomind 0.4.12.
- A deploy that runs a schema migration on production needs Sahand's own approval (0010 waited for it on 2026-11-03). Deploys go through the Deploy thread via the coordinator. Sahand said on 2026-11-03: test nothing on the local stack; unit tests are fine.
- Backend versions are in `src/version.py` with `CHANGELOG.md`, tagged `v<version>` on main, same scheme as the frontend: stay on 1.1, raise only the patch (Sahand, 2026-11-03); old tags v1.0.0-v1.0.3 stay; production runs 1.1.14 since 2026-11-04 18:48 UTC (geomind 0.4.25: ask_economics reads catalogue rows by id from knowledge, output at max_tokens is a cut; run 86ddac2a); before that 1.1.13 (memory(None) uses the run project; GET run sessions/agents/total; plain .env, run token cap off, /runs/{id}/agents; agent case/plant saved as project versions, MCP check with steps; geomind 0.4.24, gemini 0.6.4, migration 0014, per-role DeepSeek models, GEOMIND_MEMORY=on); API paths /workspace/rag and /workspace/mcp, project.mcp. The 133-row cost catalogue was re-seeded into Knowledge 2026-11-04 12:29 UTC (searchable). Still open: the nemotron switch after the comparison.
- Since 2026-11-03 the "Deploy" thread is the home for all production deploys, and Sahand wants Claude to run them itself (asking him for any permission it lacks). On 2026-11-03 he added allow rules in ~/.claude/settings.json on the Dell for exactly: `sg docker -c "docker tag geomind-backend:candidate geomind-backend:latest && docker compose up -d --no-build fastapi celery"` (run from backend/), `sg docker -c "docker compose up -d --build"` (run from frontend/), and `git push origin --delete *`. Run them as a single command after a separate `cd`, spelled exactly so, with no pipe or `| tail` (a pipe breaks the match and the deploy is refused). Claude cannot edit its own settings (refused as self-modification). Backend flow: `docker build -t geomind-backend:candidate .` from a clean main checkout, then the switch; fastapi runs `alembic upgrade head` on start. Public API is api.geomind.team.
- Keep MALLOC_ARENA_MAX=2 and GEOMIND_RETRY_COUNT=5 / GEOMIND_RETRY_DELAY=2 in the production env.
- Sahand, 2026-11-04 11:14 UTC: once geomind 0.4.22 and gemini 0.6.2 are released, finish the backend release without waiting for his OK, and deploy everything with every feature (migration 0014, new env lines, catalogue re-seed) through the Deploy thread.
- Since 1.1.11 (2026-11-04, Sahand's rule) production reads one plain `backend/.env` (compose `env_file: [.env]`), never `.env.production`; the tests read `.env.example` via `APP_ENV_FILE`, never `.env`. Every env file names the same settings (a test checks the two examples). Sahand edits the prod `.env`; give him env changes as one copyable command with the `cd`.
