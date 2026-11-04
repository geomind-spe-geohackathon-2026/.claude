# GeoMind / GeoHackathon handoff (2026-11-04, 16:35 UTC)

A cold-start context pack for a new Claude account. Read this file first, then `memory/MEMORY.md`.

## 1. What is in this zip

| Folder | Contents |
|---|---|
| `HANDOFF.md` | This file: the goal, repos, prod state, flow, rules, open work, threads. |
| `memory/` | The whole project memory, as it stood at handoff. `MEMORY.md` is the index. Every `[[name]]` link in it is a file here (all links resolve). |
| `project-files/` | The `.md` docs from the shared project folder: bugs, geomind, notes, qa, frontend, backend, gemini, prompts, phases (contracts), handoff, benchmark, context. |
| `repo-docs/<repo>/` | Copies of AGENTS.md, README.md, CHANGELOG.md, docs/rules.md and geomind's `.claude/docs/plan.md` from each repo's `main` branch. The code itself is on GitHub. |

Only `.md` files are included (Sahand's choice). CSVs, images, PDFs, wheels and `.env` files are left out. The input demand CSVs and the challenge PDF are on the organiser's side and in the old project's `inputs/`. The cost catalogue CSV is in the geomind repo and the app's Knowledge base.

There are no secrets in this pack. Env variables are listed by name only (section 7).

## 2. Goal and challenge

- The event is the **SPE Europe Energy GeoHackathon Express**, on the GEMINI geothermal digital twin. The product is **geothermal first**.
- **Challenge 1 (50%):** an agentic AI workflow.
- **Challenge 2 (50%):** an integrated heating and cooling design, plus the agent log.
- **Deliverables:** a report of at most 5 pages or 10 slides, a video of at most 5 minutes, and the GitHub repos. **None of these have been started.**
- **Organiser clarifications (2026-11-01):**
  - The source runs 330 days a year and the backup covers all 365.
  - Well depth may change.
  - Multiple doublets and backup units are allowed.
  - Return temperatures are our choice.
  - Supply is 100 °C for heating and 20 °C for cooling.
- **Team:** Sahand (owner, GitHub `SahandNZ`), Fatemeh Chitsaz (frontend/backend; the NTNU Dell is hers), and Claude.
- **Upstream base:** https://github.com/GEMINI-Digital-Twin/gemini-geothermal-suite-open. The team fork is https://github.com/swarmax/gemini-geothermal-suite-open.

## 3. Repos (GitHub org `geomind-spe-geohackathon-2026`)

| Repo | Role | main at handoff |
|---|---|---|
| `gemini` | Physics/engine package (`import gemini as gm`). It is the source of truth for plant, case, units and economics. The frozen baseline is 0.5.0 (b07b7ff), and later changes must be backward compatible. Port types changed in 0.6.0, when one `Port(...)` replaced Inlet/Outlet. | 2e0862a, tag v0.6.4 |
| `geomind` | Agent package (`import geomind as gd`). It holds the agent teams (`agents/<team>/<name>.py`, `prompts/<team>/<name>.md`), the tools (gemini, rag, mcp, memory) and the loops. The backend imports it as a pinned wheel. | 2936fa4, tag v0.4.24 |
| `backend` | FastAPI + Celery + Postgres/Redis/MinIO/Influx/Chroma. It handles chat, runs, SSE, projects, design case/plant, Knowledge (RAG) and Connectors (MCP). It is the only place that imports geomind. | 0fc4ba0, tag v1.1.12 |
| `frontend` | React + Vite + Tailwind with the stock shadcn theme. The UI names are Knowledge (RAG), Connectors (MCP) and Library. | 45e5fbb (1.1.32) |
| `infrastructure` | Shared services, one compose and .env per service: traefik, cloudflared, postgres, redis, minio, influxdb, chromadb, pgadmin. | 9af0ef5 |

The dependency direction is frontend -> backend -> geomind -> gemini.

Key repo docs:
- geomind: `.claude/docs/plan.md` holds the plan and the numbered gemini requests.
- gemini and geomind: `docs/rules.md`.
- backend and frontend: `CHANGELOG.md`.

## 4. Production and hosting

- **Live:**
  - App: https://geomind.team
  - API: https://api.geomind.team
  - Traefik dashboard: https://traefik.geomind.team/dashboard/
- **Host:** the NTNU Dell (Fatemeh's laptop), with the app repos in `/home/fatemec/geomind-spe-hackathon-2026`.
  - Traffic goes through a Cloudflare Tunnel to Traefik (`https://geomind-traefik:443`). Certificates come from Let's Encrypt via the Cloudflare DNS challenge.
  - The laptop must not sleep.
  - DB backups are in `~/geomind-backups/`.
- **Machines:** only Sahand's MacBook (`/Users/sahand/Desktop/geomind-spe-geohackathon-2026/`) and the NTNU Dell. Do not use the ASUS.
- **Prod now (2026-11-04 16:15 UTC):**
  - Backend 1.1.12 (main 0b2ca9f, tag v1.1.12), which pins geomind 0.4.24 and gemini 0.6.4 plus the `gemini-sandbox:0.6.4` image. Alembic head is 0014. The rollback image `geomind-backend:prev` is 1.1.11 (85ed4cf). The DB backup is `geomind-prod-20261104T160921Z.dump`.
  - Frontend 1.1.32 (45e5fbb). The rollback image `geomind-frontend:prev` is cd042d1.
  - Knowledge was re-seeded with the v0.4.24 `cost-sources.csv` (171 rows) and its `.md`.
- **Wheels:**
  - geomind 0.4.24: `https://github.com/geomind-spe-geohackathon-2026/geomind/releases/download/v0.4.24/geomind-0.4.24-py3-none-any.whl`, sha256 `f8d1b911f938e77ca8f0887d37ca9c57770b4b1ef19217c7d89a8737208ec098`.
  - gemini 0.6.4: sha256 `aaa89e1673849f16bc082b59eee834577acb950f0328501c0d5a7a1d5d1aa7b9`.
- **Prod models:** DeepSeek (`deepseek/deepseek-v4.1-flash-1017`, PROVIDER=deepseek) for every role, with `GEOMIND_MEMORY=off`. A switch to nemotron is pending (section 8).
- **Running services:** see `project-files/notes/run-services.md`. Note: that doc still mentions `.env.production`. That is outdated, because there is now ONE plain `.env` per repo.
- **After the hackathon:** revoke the Cloudflare tokens and change the admin password.

## 5. Release and deploy flow

1. All new work goes on `dev`, and `main` stays stable. When tests pass, merge dev into main with `--ff-only`, so the two never diverge. Then tag and release.
2. Do not open pull requests. Merge locally, push, and delete the branch.
3. Releases:
   - geomind is released from main (tag plus a wheel on GitHub Releases).
   - gemini is released from dev (main = dev).
   - Consumers pin released wheels. Never use `-e` installs anywhere.
4. Versioning is semver with a CHANGELOG. The frontend and backend stay on v1.1.x (patch bumps only).
5. Deploys are run by the "Deploy" thread, through a Claude Code Remote Control session on the NTNU Dell.
   - Deploy only `main`, backend first and then frontend.
   - Build from pushed commits in a clean checkout.
   - Tag the running images `:prev` first.
   - Run `pg_dump` before any migration or import.
   - Smoke test: the site returns 200, API health returns 200, and login works.
6. Sahand has given standing approval for backend and frontend deploys. Deploy requests are relayed to the deploy runner with Sahand's approval message attached.
7. The deploy runner cannot edit the prod env or write prod data. Sahand runs those commands himself.
8. Never run `docker compose down -v`, and never stop prod containers, without Sahand's OK.
9. Git worktrees go only under each repo's `.tmp/`, which is gitignored.
10. Frontend commits are authored as `Fatemeh Chitsaz <fatemeh.chitsaz@ntnu.no>`. Past commits are not rewritten unless Sahand approves.
11. Work happens in small, fresh Claude Code sessions on the NTNU Dell, to keep token use low. The long session only coordinates, merges and releases. Write a handoff note after each piece (`.tmp/handoff/<piece>.md`).

## 6. Standing user rules (all still in force)

Full text and reasons are in `memory/` (`feedback-*.md` and `MEMORY.md`).

**Communication**
- Chat with Sahand in Persian. Every file must be in English, with no Persian (rule from 2026-11-04). Times are given in his local time, UTC+1.

**Models and spend**
- **Never** use a Claude model for the geomind agents.
- No live runs, end-to-end tests or LLM token use without Sahand's OK. The current state is a **test stop** (2026-11-04 14:25 UTC).
- The live-test cap is 10 USD in total on the OpenRouter key. Check the real usage on the key page; local tallies undercount.
- Tests get no step, context or run-token limits, but log how efficient they are.
- Context is counted per agent and per session, never summed over the whole workflow. A whole-run budget is a separate cost setting.

**gemini**
- Nobody requests anything from gemini without Sahand's permission. Threads write a copy-paste list for Sahand instead. Never message the gemini thread with other threads' requests.
- The gemini thread touches only the gemini repo, and its findings are not relayed elsewhere without Sahand's OK.
- gemini never provides data or inputs for other packages. It only gets bugs, unit problems and unclear errors, and only entirely new features or bugs go on a list for it.
- Consumers choose the display units, and gemini does all conversions.
- geomind's Dell session may install gemini wheels itself.

**Design and API**
- No default values: a missing value is an error. The exception is port-type fields.
- Everything stays general, not tied to this competition.
- Non-plant data lives in Problem, and the compiler is separate.
- I/O naming is `from_/to_ csv/json/dict`.
- Do not change any API already given to others. The exceptions are the port types and the approved rename: in backend and geomind, "documents" became rag and "connectors" became mcp.
- Same-role files in the backend and frontend share names, and the backend's name wins.
- Knowledge means RAG and Connectors means MCP. Never mix either with agent memory.

**Frontend**
- No new features. Only improve the layout and UX with existing open-source components (stock shadcn).
- The Editor page has been removed everywhere. Keep the name "Library".
- The flow is agent-first, starting in chat, and the manual UI stays.

**Priority**
- Bugs and critical items only, until the whole app works end to end once.
- Fix bugs in the frontend and backend, and change geomind as little as possible. Send no bugs to gemini for now (2026-11-04 16:27 UTC).

**Data**
- Every value that does not come from the user's files needs the user's approval, asked in one question showing the source, publisher, year, currency year and link.
- The cost catalogue stays in Knowledge, not in the wheel.

**Testing**
- Test nothing locally; work on production (dev -> main -> prod).
- No 5-minute status reports.

## 7. Env variable names (no values)

Backend `.env` (keep the key names in sync with `.env.example`; a test enforces this):

- **App:** `APP_NAME`, `APP_ENV`, `APP_DEBUG`, `APP_LOG_LEVEL`, `APP_CORS_ORIGINS`, `API_PORT`, `FRONTEND_PORT`, `MALLOC_ARENA_MAX`, `PROJECT_IMPORT_MAX_BYTES`, `RATE_LIMIT_REQUESTS`, `RATE_LIMIT_WINDOW_SECONDS`
- **Auth:** `JWT_SECRET_KEY`, `JWT_ALGORITHM`, `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`, `JWT_REFRESH_TOKEN_EXPIRE_DAYS`, `FIRST_ADMIN_EMAIL`, `FIRST_ADMIN_PASSWORD`, `LOCAL_ADMIN_EMAIL`, `LOCAL_ADMIN_PASSWORD`
- **Data services:**
  - `POSTGRES_URL`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_PORT`, `POSTGRES_POOL_SIZE`, `POSTGRES_MAX_OVERFLOW`
  - `REDIS_URL`, `REDIS_PASSWORD`, `REDIS_PORT`, `CELERY_BROKER_URL`
  - `MINIO_ENDPOINT`, `MINIO_PORT`, `MINIO_CONSOLE_PORT`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, `MINIO_ROOT_USER`, `MINIO_ROOT_PASSWORD`, `MINIO_BUCKET_NAME`, `MINIO_SECURE`
  - `INFLUXDB_URL`, `INFLUXDB_ORG`, `INFLUXDB_BUCKET`, `INFLUXDB_TOKEN`
  - `CHROMADB_URL`
- **LLM:** `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL`, `ASSISTANT_RUN_MAX_TOKENS` (prod sets it to `off`)
- **geomind:**
  - `GEOMIND_PROVIDER`, `GEOMIND_CONTEXT_WINDOW`, `GEOMIND_MAX_OUTPUT_TOKENS`, `GEOMIND_MAX_STEPS`, `GEOMIND_ENGINEER_MAX_STEPS`, `GEOMIND_DESIGN_CONCURRENCY`, `GEOMIND_RETRY_COUNT`, `GEOMIND_RETRY_DELAY`, `GEOMIND_MCP_TIMEOUT`, `GEOMIND_MEMORY` (prod sets it to `off`), `GEOMIND_MEMORY_SIMILARITY`
  - `GEOMIND_EVOLVE_EVALUATIONS`, `GEOMIND_EVOLVE_POLISH`, `GEOMIND_EVOLVE_POPULATION`, `GEOMIND_EVOLVE_SEED`, `GEOMIND_EVOLVE_STOP_GENERATIONS`, `GEOMIND_EVOLVE_STOP_SECONDS` (prod sets both STOP variables to `off`)
  - The per-role models are `GEOMIND_<ROLE>_MODEL`, where ROLE is one of COORDINATOR, PROJECTLEAD, CASELEAD, DESIGNLEAD, ANALYSISLEAD, SUPPORTLEAD, GEOSCIENTIST, RESERVOIRENGINEER, WELLENGINEER, PROCESSENGINEER, ENERGYSYSTEMSENGINEER, INTEGRATIONENGINEER, ECONOMIST, REVIEWER, EXPLAINER, SUMMARIZER, CURATOR.

Frontend `.env`: `VITE_API_URL`, `VITE_API_MODE`, `VITE_FEATURE_OPERATION`. nginx does not proxy `/api`.

Infrastructure: one `.env` per service folder, copied from that folder's `.env.example`.

## 8. Open work at handoff

1. **B13 (URGENT, backend):** every project-loop run fails with "internal error in geomind" right after routing. It was seen at 16:22 and 16:27 UTC in project "test 17:20" (12408e95…) and reproduces with a typed message. The cause has not been found. The next step is to read the run's JSON log (Runs and logs -> download) or the Celery worker log on the Dell. The fix goes in the backend, touching geomind only if unavoidable. Assigned to BACKEND I.
2. **B12 (frontend):** the coordinator's loop route is shown as raw JSON. In `src/shared/sse/route.ts`, `fromRoute()` must accept a loop route without `agent` and ignore extra fields. Assigned to FRONTEND I.
3. **B14 (frontend, to confirm):** files attached in the New project dialog stay in the composer after a suggestion chip is sent. A chip click should send the pending attachments. Assigned to FRONTEND I.
4. Bugs B1–B11 were routed earlier; their status is in `project-files/bugs/bug-list-2026-11-04.md`. B3 (H2S species) was fixed in gemini 0.6.4.
5. **gemini requests 33, 34 and 35:** written in geomind `.claude/docs/plan.md` (see `repo-docs/geomind/.claude_docs_plan.md`) but NOT sent. They await Sahand.
   - 33: `gm.check` should list `params.control.dispatch`/`outages` and `esp_depth` as missing.
   - 34: an `invalid_unit` problem should carry its quantities and accepted units.
   - 35: the ESP `out_of_range` message should name the valid flow range.
6. **Nemotron switch:** Sahand decided (2026-11-03) that all geomind agents move to `nvidia/nemotron-3.5-super-vl:free` on OpenRouter, with a context window of 200000, about 20 rpm and 1000 calls a day. Prod stays on DeepSeek until he says so.
7. **Per-agent usage UI:** context used and remaining, tokens, cost and tool calls per agent, plus run totals. It is live in backend 1.1.12 and frontend 1.1.32 but untested on the site.
8. **Hackathon deliverables:** the report, the video and the agent log are not started.
9. **Future, on hold:**
   - Semantic RAG with embeddings (search today is lexical only). This needs Sahand's OK first.
   - An end-to-end run to the verdict, which needs the site elevation.
   - Cited sources for the unsourced economics keys (discount_rate, some opex.variable, opex.fixed.circulation_pump/ice_storage, corrosion_inhibitor).
10. **Spend:** about 8 of the 10 USD on the OpenRouter key had been used by midday on 2026-11-04. Check the key page before any run.

## 9. Where the thread homes were (old account)

These threads are in the old claude.ai project "geohackathon" and cannot be reached from the new account. In the new account, recreate them as needed:

- **Coordinator:** the project chat.
- **GEOMIND II:** the geomind home thread. The status list is `project-files/geomind/status-2026-11-04.md`, and the handoff notes are `project-files/geomind/handoff.md` and `handover.md`.
- **GEMINI II:** the gemini home thread. Its handover is `gemini-work/.tmp/handover/GEMINI_III.md` on the Dell, and `project-files/gemini/handoff-gemini-ii.md`.
- **BACKEND I:** the backend home thread (`project-files/backend-i.md`).
- **FRONTEND I:** the frontend home thread (`project-files/frontend/next-round.md`).
- **Deploy:** runs deploys through Remote Control on the NTNU Dell.
- **Collect UI and geomind bugs:** only lists bugs and changes no repo (`project-files/bugs/`). Nothing from it is sent anywhere without Sahand's OK.
- **QA test everything on production:** `project-files/qa/qa-prod-2026-11-03.md`.
- **Closed:** GEOMIND 1, GEMINI 1.

Old artifacts (they may not be visible from the new account):
- UX direction: https://claude.ai/artifact/TehS6XZQ7SUsNNdEYrFby5
- Feature list: https://claude.ai/artifact/1knPPo4pR5Grson1sckwTe

## 10. Suggested first steps in the new account

1. Create a project with the five repos and connect GitHub access to org `geomind-spe-geohackathon-2026`.
2. Import `memory/` into the new project memory: copy the files, or paste `MEMORY.md` first.
3. Put `project-files/` into the new project's shared folder.
4. Start with B13: get the failing run's log from the Dell, fix it in the backend, and deploy under the standing deploy approval.
