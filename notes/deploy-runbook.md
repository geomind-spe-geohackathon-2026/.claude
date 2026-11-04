# Deploy handoff (geomind.team production on the NTNU Dell)

Last updated: 2026-11-04 18:49 UTC (backend 1.1.14 deploy).

## Live now
- Backend: main 5a8cb13, version 1.1.14 (geomind 0.4.25: ask_economics rows by id, cut at max_tokens), alembic 0014, geomind 0.4.25, gemini 0.6.4 (gemini-sandbox:0.6.4 pulled and tagged on the Dell), GEOMIND_MEMORY=on, ASSISTANT_RUN_MAX_TOKENS=off. Env file backend/.env (compose env_file [.env]). Rollback image: geomind-backend:prev (0fc4ba0, 1.1.13).
- Knowledge: cost-sources.csv and cost-sources.md from v0.4.24 seeded 2026-11-04 16:15 (workspace-wide, searchable=ready).
- Frontend: main 27c3a21, version 1.1.33 (B12, B14), bundle assets/index-DnxCbfcj.js, env file frontend/.env. Rollback image: geomind-frontend:prev (45e5fbb, 1.1.32).
- DB backups: ~/geomind-backups/ (latest geomind-prod-20261104T184649Z.dump).
- Sahand (2026-11-04 11:14): once geomind and gemini versions are ready, deploy everything without waiting for his OK.
- Production env edits are refused for Claude: give Sahand a one-line command (for example, swap the GEOMIND_ block from main's .env.example).

## Queued
- Nothing queued.

## Rules
- Deploy only main. Never run backend and frontend deploys at the same time.
- Frontend: Sahand gave standing approval (2026-11-03 15:13), so deploy whenever main has something new.
- Backend: needs Sahand's go, either directly or cited from his message.
- No live LLM runs. Writes to production data (for example the knowledge seed) are refused by the permission check; give Sahand the commands.
- Run the allowed commands exactly as written: first a separate `cd`, then the command with no pipe or `| tail`.

## Backend deploy
1. `cd backend && git fetch -q origin`; check origin/main and the diff for alembic, .env.example, compose.yml and requirements.txt.
2. Back up the DB: `sg docker -c "docker exec geomind-postgres sh -c 'pg_dump -U \$POSTGRES_USER -d \$POSTGRES_DB -Fc'" > ~/geomind-backups/geomind-prod-<ts>.dump`
3. If .env.example has new keys, add them to backend/.env.production (back it up first).
4. `git archive <main sha> | sg docker -c "docker build -q -t geomind-backend:candidate -"` (build from main even if dev is ahead), then `sg docker -c "docker tag geomind-backend:latest geomind-backend:prev"`.
5. `cd /home/fatemec/geomind-spe-hackathon-2026/backend`, then exactly: `sg docker -c "docker tag geomind-backend:candidate geomind-backend:latest && docker compose up -d --no-build fastapi celery"`
6. Check: https://api.geomind.team/api/v1/system/health shows the version; `docker exec geomind-fastapi python -m alembic current`; celery logs say "ready"; there are no errors in the logs.

## Frontend deploy
1. `cd frontend && git fetch -q origin && git pull -q origin dev` (dev == main when FRONTEND I asks); check that HEAD == origin/main.
2. `sg docker -c "docker tag geomind-frontend:latest geomind-frontend:prev"`
3. `cd /home/fatemec/geomind-spe-hackathon-2026/frontend`, then exactly: `sg docker -c "docker compose up -d --build"`
4. Check that the container is healthy and that `curl -s https://geomind.team/ | grep -o 'assets/index-[^"]*'` shows the new bundle.

## Reporting
Report to the coordinator only (send_message @parent), giving the commit, the version and the bundle or health result.
