# GeoMind project: start here

Paths in this file are from the project root (`geomind-spe-hackathon-2026/`), the folder that
holds `.claude/`.

GeoMind is the team's entry to the SPE Europe Energy GeoHackathon on the GEMINI geothermal digital
twin: agents in chat select, size and check a geothermal heating and cooling plant. The product is
general, geothermal first; the competition is one example input.

The project root holds one clone of each repo, `.claude/` (this repo) and `documents/`. Dependencies run one way: frontend -> backend -> geomind
-> gemini. Production (geomind.team, api.geomind.team) runs on this machine, the NTNU Dell.

## First: read the status, then ask the mode

Read `.claude/STATUS.md`: production, the clones, the mode rules, open
decisions. Then ask the user the mode.

## Hand over at 300,000 tokens of context

Check your context at the start of every piece of work (`get_session` of the Claude Code Remote MCP
server, `context_usage`). At 300,000 used tokens, hand your work to a fresh session named `<name>-II`, `-III` ...:
follow `.claude/session-refresh.md` exactly. Read the coordinator's current id in `STATUS.md`
before you message it.

## Write what every session needs, at once

Parallel sessions share one source: the project root's `.claude/`. The moment you learn something
another session needs, write it there before you go on:
- a rule or a decision from the user: a file in `.claude/memory/` and one line in `MEMORY.md`;
- a change of state (a deploy, a version, a branch, a blocker, an open decision): `.claude/STATUS.md`;
- a bug: `documents/project/quality-assurance/` (see its README).
Never keep such a fact only in your own chat or your private memory. `.claude/` and `documents/`
are repos like the others (`.claude` and `documents` on GitHub): commit and push them too.

## Ask the mode

At the start of every session, before any change, ask the user which mode this session works in:
**development**, **production** or **hotfix** (`documents/project/ops/development-modes.md`).
Work by that mode's rules until the user changes it. Without an answer, change nothing. In every
mode, commit and push before you start a piece of work and as soon as it is done: uncommitted work
in a shared clone blocks every deploy of that repo.

## Read both: `.claude/` for agents, `documents/` and `docs/` for people

Every folder follows one rule: what people read is in `documents/` (the project root, one folder
per repo plus `project/`) and in each repo's `docs/`; what agents read is in `.claude/` (here and
in each repo), `AGENTS.md` and `CLAUDE.md`. A session reads both before working.

1. `.claude/STATUS.md`, `.claude/README.md`: the layout and naming rules, then
   `.claude/memory/MEMORY.md`, the shared memory and every standing rule.
2. `documents/README.md`: what the project is; contracts,
   operations, bug lists, QA reports and plans across repos.
3. The repo you work in: its `AGENTS.md`, its `.claude/README.md` and its `docs/`.

## Quality assurance

People and sessions test geomind.team in parallel and report every bug in
documents/project/quality-assurance/ (`documents/project/quality-assurance/README.md`): one line in `BUGS.md`, one file in
`bugs/`, screenshots and run JSON in `evidence/`. A hotfix session takes the open bugs by
severity, marks one `fixing` before it starts, fixes it in hotfix mode, writes Fix and Retest in
its file, sets the status, and tells the team in the chat. Follow its README exactly.

## Repos (GitHub org `geomind-spe-geohackathon-2026`)

| Folder | Repo | Role |
|---|---|---|
| `gemini/` | gemini | Physics and engine (`import gemini as gm`); the source of truth for plant, case, units, economics. |
| `geomind/` | geomind | Agent package (`import geomind as gd`). |
| `backend/` | backend | FastAPI, Celery, Postgres, Redis, MinIO, InfluxDB, Chroma; the only importer of geomind. |
| `frontend/` | frontend | React, Vite, Tailwind, stock shadcn. |
| `infrastructure/` | infrastructure | Shared services: one compose and `.env` per service. |

## Rules that hold everywhere

The full list with reasons is in `.claude/memory/` (files `feedback-*.md`). The ones broken most:

- Chat with Sahand in Persian; write every file in English. Never write a secret into a file.
- In chat give every time in Trondheim time (Europe/Oslo, CET now), never UTC.
- The geomind agents never use a Claude model (production: `deepseek/deepseek-v4.1-flash-1017`, provider `morph/fp8`, on OpenRouter). No live run, end-to-end
  test or LLM token use without Sahand's OK.
- Nobody asks gemini for anything without Sahand's permission; list needs for him instead.
- `main` is what production runs. The mode decides the branch, the tests and the way to `main`
  (`documents/project/ops/development-modes.md`):
  - development: work on `dev`; run every automated test that needs no LLM; fast-forward `main`
    locally, tag, deploy;
  - production: work on `dev`; the same tests; a pull request a person approves and merges on
    GitHub; never merge locally;
  - hotfix: work directly on the default branch (`main`; for gemini `dev`, which is its default);
    run no tests; tag, push, deploy at once.
- One clone per repo, no git worktrees: work in the clone itself, on the branch the mode names.
- Stage files by path: these clones are shared by
  parallel sessions.
- Releases and deploys follow `documents/project/ops/release-and-deploy.md`.
- No default values: a missing value is an error. Data that no user file gives comes from the
  Knowledge base (RAG) or a connector (MCP), and the user approves it with its source.
