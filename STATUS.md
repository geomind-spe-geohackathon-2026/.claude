# Status: read first, keep current

The short, current state every session needs. Read it at the start of every session. When any of
it changes, change it here at once (one line, with the UTC time), before you go on.

Last updated: 2026-11-05 09:30 UTC.

## Production (geomind.team, api.geomind.team, on the NTNU Dell)

- 09:40 UTC (hotfix-back-II): QA-092 fixed in backend 1.1.82 (9da4bbf; plant-changing tools and simulate on a stored design save the next plant version; a plain simulate still writes no Results row), goes out with hotfix-python-II's held batch. QA-095 row co2-grid-organisers-2026 (300 g/kWh) on geomind main 3a5027d: live only after a geomind release (Sahand's word) and a Knowledge re-seed by Sahand. QA3 seed runs after the batch deploy.

- RELEASED, NOT DEPLOYED (hotfix-python-II, held by the coordinator until functional-qa-I's run in chat cb8b9b2d reaches its final comparison, latest 10:30 UTC): geomind 0.4.78 (QA-074 constant g, QA-079, QA-084, QA-085, QA-086, QA-088 full runs in agent study records, shape agreed with hotfix-back) and gemini 0.6.12 (request 35, m/s2 kg/m2 units). Prod still runs backend 1.1.78 / geomind 0.4.73 / gemini 0.6.10.

- Backend 1.1.78 (2026-11-05 07:30 UTC, hotfix-python-II): geomind 0.4.73 + gemini 0.6.10 LOCAL wheels (QA-081 gd.errors.AlreadyAnsweredError, backend must treat it as no-op; QA-087 six web searches per agent and run).

- Backend 1.1.76 (2026-11-05 07:00 UTC, hotfix-python-II): geomind 0.4.72 + gemini 0.6.10 LOCAL wheels (QA-082 root: simulate summary no longer fails on an ESP failure group).

- Backend 1.1.75 (2026-11-05 06:30 UTC, hotfix-python-II): gemini 0.6.10 + geomind 0.4.71 LOCAL wheels (QA-082 depth named first, simulate changes set plant options; QA-083 internal errors carry their cause, bare inlet names coded).

- Backend 1.1.73 (2026-11-05 05:30 UTC, hotfix-python-II): gemini 0.6.8 + geomind 0.4.69 LOCAL wheels (QA-080: flow range over several requirements; case lead writes one min+max rule).

- Backend 1.1.72 (2026-11-05 05:00 UTC, hotfix-python-II): geomind 0.4.68 + gemini 0.6.7 LOCAL wheels (QA-076 gm.check no longer raises on incomplete plants, engineers own their parts; QA-078 random calculation ids C+6hex). 1.1.71 (04:30): geomind 0.4.66 (QA-072).

- Backend 1.1.69 (2026-11-05 02:00 UTC, hotfix-python-II): geomind 0.4.65 + gemini 0.6.6 LOCAL wheels (QA-071 English-only short web queries; gm.study.structure_plant for the evolve structures view). Sandbox image stays gemini-sandbox:0.6.5. Includes the structures view endpoints (1.1.66-1.1.68). Frontend 1.1.71 (Compare structures).

- Backend 1.1.65 (2026-11-05 01:30 UTC, hotfix-python-II): geomind 0.4.64 LOCAL wheel (QA-047 findings in problem state; QA-070 nested agents rerun after a restart).

- Backend 1.1.64 (2026-11-05 01:06 UTC, hotfix-python-II): geomind 0.4.62 LOCAL wheel (QA-069: set_case returns plants_need).

- Backend 1.1.63 (2026-11-05 01:02 UTC, hotfix-python-II): geomind 0.4.61 LOCAL wheel (skills connectors, economics, report, comparing-designs; prompt-to-skills step done as agreed: only sometimes-needed how-to moved).

- Backend 1.1.61 (2026-11-05 00:22 UTC, hotfix-python-II): geomind 0.4.60 LOCAL wheel (QA-065 doublet-count requirement, QA-061 no internal note on question cards).

- Backend 1.1.58 (2026-11-05 00:16 UTC, hotfix-python-II): geomind 0.4.58 LOCAL wheel (web_search/read_web_page over SearXNG live; calculate takes plain numbers/pi/e beside one sourced operand); 1.1.57: geomind 0.4.57 (run_python live in gemini-sandbox:0.6.5, checked from geomind-celery); 1.1.56: geomind 0.4.56 (skills folder
  `geomind/skills/<name>/SKILL.md` with roles; `calculate` tool, results in problem state `calculations`),
  gemini 0.6.5, alembic 0014. 1.1.55 gave the worker the run_python sandbox (docker socket) and SearXNG.
  Deploys resume running runs (QA-035).
- Frontend 1.1.57 (2026-11-05 00:00 UTC: busy indicator and activity line by the agent name, QA-048). Hotfix sessions deploy themselves with two calls:
  `cd <repo>`, then exactly `scripts/hotfix_deploy.sh`.
- Agents: every role on `deepseek/deepseek-v4.1-flash-1017`, OpenRouter provider `morph/fp8` first
  (`GEOMIND_PROVIDER=morph/fp8`), since 2026-11-04 20:20 UTC; `GEOMIND_CONTEXT_WINDOW=200000`.
  Never a Claude model.

## Clones (project root, one clone each, no worktrees)

- `.claude` (this, agents) and `documents` (people) are repos too, on `main`; set up a machine with `.claude/setup.md`.

- backend, frontend, geomind, infrastructure on `main`; gemini on `dev` (its default branch).
- No worktrees anywhere (removed 2026-11-04 20:30 UTC). Old local files: `~/geomind-archive/`
  (screenshots, QA screenshots of 2026-11-03, the old root git); DB backups `~/geomind-backups/`.

- Knowledge re-seeded by Sahand 2026-11-04 ~23:35 UTC with geomind 0.4.52 cost-sources (153 sourced
  rows). No row yet for opex.per_energy of the three chillers and opex.fixed.adsorption_chiller.

- Usage-window check: send_later trig_01BA7egki6ZQA6XkYPzLAysF in Coordinator-III, next 2026-11-05 14:11 UTC
  (resetsAt 14:10 UTC + 1 min). Last pause 01:50-04:12 UTC, resumed; pauses and resumes per `memory/feedback-usage-limit-pause.md`.

## How we work now

- Mode: ask the user at the start of every session (development, production, hotfix);
  `documents/project/ops/development-modes.md`. Current mode of the last session: hotfix.
- QA: testing the live app; every bug in `documents/project/quality-assurance/BUGS.md` (QA-001 to QA-019; statuses there,
  QA-007 blocker: ask_economics fails again and again); ideas in `IMPROVEMENTS.md` (IMP-001 to IMP-011,
  QA-010 and IMP-006 need Sahand's decision). Run a61cfb19 was left `waiting` with no process after the 20:02 UTC deploy (QA-017).
- No file holds Persian text; chat with the user in Persian.
- Commit and push everything when a piece of work ends.

## QA round (started 2026-11-04 20:00 UTC)

- Hotfix sessions resumed 2026-11-04 20:25 UTC (paused 20:10-20:25). Deploy windows at :00 and :30 UTC
  only (a blocker may go at once); every deploy still ends running agent runs until QA-035.

- Coordinator: Coordinator-III, session_01J2V3UWsUm5z442CiXM5MZU (since 2026-11-05 09:30 UTC; opens and
  closes the sessions, sends reports). Coordinator-II (session_01J2V3UXD6UT73meeapsG2MS) archived; its
  handover note is `notes/sessions/coordinator-2.md`. Generation 1 (session_01J2V3UXGweG4JrR4wkEWtg9) archived;
  its handover note is `notes/sessions/coordinator-1.md`.
- Hotfix sessions (who fixes what: `documents/project/quality-assurance/README.md`):
  hotfix-front-II (session_01J2V3UVLf5yhPSiTnivcPyR since 2026-11-05 09:30 UTC, successor of hotfix-front; note notes/sessions/hotfix-front-1.md; area frontend; QA-093),
  hotfix-back-II (session_01J2V3UZeNoBawJDgCJuBHr7, since 2026-11-05 09:30 UTC, successor of hotfix-back session_01J2V3UWh6RugyR1DAxrkNhH; note notes/sessions/hotfix-back-1.md; areas backend, data, infra, backend clone; QA3 seeding, QA-095, QA-092 triage),
  hotfix-python-II (session_01J2V3UXSA2mo8MG4igf5y4n since 2026-11-04 23:52 UTC, areas geomind, gemini; local wheels; QA-090/091/094).
  Archived 09:32 UTC by Coordinator-III: hotfix-front, hotfix-back, functional-qa-I, -2, -3 (run B cef908d9 cancelled).
  They claim with `qa.py next`, take `/tmp/geomind-backend.lock` before editing the backend, and
  deploy with `scripts/hotfix_deploy.sh` (one deploy at a time).
- QA sessions qa-1, qa-4, qa-5 paused by Sahand 2026-11-04 23:25 UTC and ARCHIVED ~23:30 UTC;
  their state is in `notes/sessions/qa-paused-2026-11-04.md`. QA round 2 started 2026-11-04 23:36 UTC (briefs `notes/qa-round-2/`, agent-browser only):
  all on Sonnet since 23:45 UTC. Since 2026-11-05 00:25 UTC (Sahand, usage) only
  functional-qa-I (was qa-func-1-II) session_01J2V3UWQ5zYo1TfCiAKXF4d runs QA: one project through the whole pipeline, owning
  qa-func-1/2/3 scenarios. qa-func-2-II, qa-func-3-II and qa-ux archived (00:20-00:40 UTC); their state is in
  their files in `notes/qa-round-2/`. QA-031 and QA-053 retests are still open (qa-ux did not finish).
  Since 2026-11-05 04:12 UTC three functional QA sessions (Sonnet, competition files only):
  functional-qa-I session_01J2V3UWQ5zYo1TfCiAKXF4d (case + start-to-end design loop),
  functional-qa-2 session_01J2V3UYx2foVYxpZKRTvMhq (economics, verdict, explainer, report, agent log),
  functional-qa-3 session_01J2V3UVgJnF99ApUaSbM43F (studies, evolve, compare structures, agent tools, robustness). (Started 2026-11-04 20:11 UTC; instructions in `notes/qa-round-2026-11-04/`):
  qa-1 session_01J2V3UXnAof6WqpiA2JPxxG, qa-2 session_01J2V3UYuCFrxrXdWLCwzWro,
  qa-3 session_01J2V3UWmkUwP3g42jGxxz9g, qa-4 session_01J2V3UZkFGKUyXLCP3gYmk4,
  qa-5 session_01J2V3UVCHoDxQNsjwpBxtzH, qa-6 session_01J2V3UXM3DCMhq41Hx27eqV,
  qa-7 session_01J2V3UVMbdhwimT6VJxfNMq, qa-8 session_01J2V3UW8MS1wyUTdvJmh8UC.

- TEMPORARY for the QA round: prod backend `.env` has `RATE_LIMIT_REQUESTS=1000` (was 100; all QA
  sessions share the admin account, QA-024). Set it back to 100 after the round (Fatemeh runs it;
  backup `~/env.backend.before-ratelimit.bak`).
- `~/.claude/settings.json` allows `scripts/hotfix_deploy.sh` (added by Fatemeh 2026-11-04 20:35 UTC).

## Feature in progress (hotfix mode)

- DONE 2026-11-05 01:02 UTC: skills folder + calculate, run_python, web_search/read_web_page (SearXNG) live
  (geomind 0.4.58-0.4.61), chat views live (frontend 1.1.67), sometimes-needed how-to moved into skills;
  spec `notes/features/agent-tools-2026-11-05.md`; hotfix-python, hotfix-back, hotfix-front.
- 2026-11-05 ~00:15 UTC (Sahand): SearXNG up (geomind-searxng, geomind network only), image
  gemini-sandbox:0.6.5 built, prod backend `.env` has GEOMIND_SEARCH_URL, DOCKER_GID, ASSISTANT_SANDBOX,
  GEOMIND_SANDBOX_* (backup `~/env.backend.before-sandbox.bak`). Worker change deploys next (hotfix-back).

## To do in development mode after the QA round

- Backend `requirements.txt` still pins geomind 0.4.26; production runs local wheels (geomind up to
  0.4.41) from `backend/.tmp/hotfix-wheels`: pin the released version, empty the folder.
- Frontend `src/api/schema.d.ts` was patched by hand for QA-040 (1.1.49): run `npm run gen:api` and
  review the ~1100-line diff.
- Set the prod backend `RATE_LIMIT_REQUESTS` back to 100 (QA round only).
- Run every automated test that needs no LLM in every repo; the hotfixes ran none.
- QA-011 (resume a nested run after a provider failure), QA-013 (IMP-001) and QA-047's record of
  half-done engineer work are development work.
- QA-045's data part: three catalogue rows need a person-approved price year, then a Knowledge
  re-seed.

## Open decisions (waiting for Sahand)

- SUBMISSION DEADLINE (organisers, Discord #technical-q-and-a, 2026-11-04): Thursday 2026-11-05 23:59 CET
  = 22:59 UTC. A pull request is enough (to GEMINI's development branch); for the gemini bugs we fixed,
  explain what and where in it, no separate PR. Sahand decides what goes in. Organiser rules found by
  Fatemeh's QA session: return temperatures are the team's choice within the constraints (QA-094); grid CO2
  reference 0.3 kg/kWh (QA-095); 330 d is the doublet's availability, the full system must meet the demand
  all 365 days (QA-091); depth may change; gas is CO2+CH4, several handling options allowed.

Decided 2026-11-04 21:40 UTC: QA-010 option A (agent proposes labelled assumptions in one question,
user approves; hotfix-python), QA-006 option A (research cited rows, Sahand approves, then re-seed;
hotfix-back writes proposed rows to evidence/QA-006/).

Still open (Sahand answers later; the full write-up is in the coordinator's chat of 21:35 UTC):
3. QA-045 data: three rows in USD/FRF with no price year. Proposed: leave them (the tool skips
   them now), convert after the hackathon.
4. gemini requests 33-38 (geomind `.claude/docs/plan.md`, none sent). Proposed: approve 36
   (check names params.backup), 38 (dimensionless % accepted), 33 (check vs simulate); the rest later.
5. QA-031: auto-approve with no tab open needs a backend setting per chat. Proposed: build it.
6. A development round after QA for QA-011, QA-013 (IMP-001), QA-047.
7. geomind tags v0.4.27-v0.4.45 were pushed and released by CI during the hotfix round (the rule
   was "release only on Sahand's word"); prod runs the local 0.4.45 wheel; pin it in development.
8. Set prod `RATE_LIMIT_REQUESTS` back to 100 after QA (now counted per browser since QA-024).
9. Done 2026-11-05 00:20 UTC: Coordinator-II is running (handover was automatic).
