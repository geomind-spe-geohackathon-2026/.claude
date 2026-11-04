---
name: repo-and-code-preferences
description: Where team code goes (user's fork) and the rule to extend the GEMINI repo itself rather than build a separate system
metadata:
  type: feedback
  modified: 2026-10-27T17:44:41.350Z
---

- Team code lives in the user's fork: https://github.com/swarmax/gemini-geothermal-suite-open (stated 2026-10-27). Work on a branch, not main.
- The user wants to extend the GEMINI repo itself as much as possible, instead of building a separate project beside it.

- Repo layout (team's own, 2026-10-27): backend/ (team FastAPI monolith: identity/auth, health, clients for postgres/redis/influx/chromadb/minio/openrouter, alembic, celery), frontend/{landing (Next.js), dashboard (Vite+React+Tailwind)}, gemini/ (whole GEMINI suite + internal gemini_service FastAPI on :8001), infrastructure/ (compose per service + traefik). Flow frontend → backend → gemini service.
- Branch swarmax/restructure pushed 2026-10-27 (push access works now). backend/ and infrastructure/ exist only on the user's machine so far.

**Why:** the user wants the hackathon solution to read as an extension of GEMINI (the slides reward filling GEMINI's missing models).

**How to apply:** put new physics models in src/gemini_model (StaticModel API), real calculation modules in src/gemini_framework/modules/<unit>/ (fill the empty unit placeholders such as heatexchanger and heatpump), the agent in src/gemini_application (next to chatpopup), UI pages as Flask blueprints in src/gemini_interface, and tests in unit_test. Follow the repo's black/isort/flake8 settings (line length 100). Only put code outside GEMINI's structure when it has no natural home there. See [[gemini-repo-findings]].

- 2026-10-27 21:42: user said "don't change anything at all" (don't change anything at all). Make no edits, commits or pushes to the repo until they explicitly ask again. Branch swarmax/restructure was already pushed before this; main untouched.

- 2026-10-27 23:10: user explicitly approved restructuring (accepts it hurts upstream mergeability). Pushed branch claude/project-thread-ta051i: GEMINI moved to gemini/ unchanged, CI runs in gemini/, docs deploy only from main (so gh-pages isn't recreated). backend/, frontend/, infrastructure/ still to be added from the user's machine.

- 2026-10-27 23:16 (feedback): right after that push the user said "don't do anything until I tell you". **Why:** "let's change the structure" was them thinking aloud in a design discussion, not a go-ahead. **How to apply:** during discussions, only discuss and propose; take no action (repo or otherwise) until the user gives a clear, direct instruction to execute.

- 2026-10-27 23:24 target-tree discussion (not executed yet, waiting for user's go): package root `gemini/` (was src/; user chose name `gemini`) with model/, framework/, application/, agent/; tests/, datasets/geothermal_example/, examples/, docs/ (API only), ci/. Flask interface, framework app.py runner, chatpopup, docker-compose → outside the package (web app/backend/infrastructure). Open: keep gemini_application inside package (my proposal).

- 2026-10-27 23:47 tree decisions so far (still discussion only, nothing executed): package `gemini/` with physics/ (renamed from model; flat for now, grouping subsurface/equipment/fluid/integrity undecided), monitoring/ (proposed rename of framework, not confirmed), simulation/, economics/, agent/; root: tests/, datasets/, examples/, docs/. Removed from tree: application/ and ci/.
