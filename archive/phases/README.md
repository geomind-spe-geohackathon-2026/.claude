# Implementation phases

Three repos move forward in parallel, each with its own phases. They meet only through the contracts in [contracts.md](contracts.md), so no repo waits for another to start.

```
crust-team/
├─ frontend/   React + Vite + Tailwind      → talks to backend through the HTTP API contract
├─ backend/    FastAPI                       → uses geomind through the geomind interface contract
├─ geomind/    agent package (was geomind)                 → uses gemini as a library
├─ gemini/     physics and engine (existing)
└─ infrastructure/  docker-compose (small; done inside backend phase 1)
```

## Phases per repo

| Step | Backend | Frontend | geomind |
|---|---|---|---|
| 1 | [B1 Foundations](backend/phase-1-foundations.md) | [F1 Shell](frontend/phase-1-shell.md) | [S1 Engine](geomind/s1-engine.md) |
| 2 | [B2 Assistant](backend/phase-2-assistant.md) | [F2 Assistant](frontend/phase-2-assistant.md) | [S2 Tools and context](geomind/phase-2-tools-and-context.md) |
| 3 | [B3 Plant and time series](backend/phase-3-plant-and-timeseries.md) | [F3 Plant model](frontend/phase-3-plant.md) | [S3 Design agents](geomind/phase-3-design-agents.md) |
| 4 | [B4 Well performance](backend/phase-4-performance.md) | [F4 Time series](frontend/phase-4-timeseries.md) | [S4 Compare and evals](geomind/phase-4-compare-and-evals.md) |
| 5 | | [F5 Well performance](frontend/phase-5-performance.md) | |

Later, after the hackathon: `integrity` and `reporting/regulatory`.

## How parallel work stays in sync

- **Contracts first.** `contracts.md` fixes the HTTP routes and payloads for steps 1 and 2, the live event types, and the geomind interfaces. Each repo builds against the contract, not against the other repo's code.
- **Mocks until the other side exists.** The frontend uses a mock API (MSW) built from the contract. The backend uses `geomind.providers.FakeLLM` and the contract's interfaces; it installs the real geomind as soon as S1 is done.
- **A contract change is a change to `contracts.md` first,** announced to all three. No repo changes a shared route or interface silently.
- **Integration points:**
  - After B1 + F1: the frontend switches from mocks to the real API for identity and projects.
  - After S1: the backend installs geomind (editable, `../geomind`) in B2.
  - After B2 + F2 + S2: the first full chat in the browser with gemini tools.
  - After S3: Challenge 2 designs appear in the browser with no extra backend or frontend work.

## What the competition needs

S1 to S4 plus B2 and F2. Everything else makes the product complete.

## Shared references

Put these in `crust-team/docs/` before starting; every phase refers to them:

```
crust-team/docs/feature-map.md               domains, features, use-cases, folder names
crust-team/docs/agent-engineering-layers.md  prompt, context, harness, loop
crust-team/docs/contracts.md                 contracts.md from this folder
crust-team/docs/phases.md                    this README
```

Legacy inventories, referred to by the porting phases (B3, B4, F3 to F5), stay where they are:

```
crust-team/gemini-legacy-backend-analysis/backend-features.md
crust-team/gemini-legacy-frontend-analysis/frontend-features.md
```

## Rules for every phase

- Folder names: one word, lower case, no underscores, as in the feature map.
- Code quality: simple, readable, just enough code; nesting at most 3; functions about 40 lines at most; no dead or speculative code; no comments inside code (docstrings only, plus fixed section headers).
- Tests: only the tests of changed code and its importers while working, in parallel; the full fast suite before each commit. Never call the network in tests. Temporary files go to `.tmp/` (git-ignored).
- Docs: update `AGENTS.md` and the docs folder in the same commit as the change, so a new session knows the current state.
- Subtasks and subagents use lighter models.
- If something is missing, unclear or risky, stop and say so instead of guessing.
- Commit after each step. Do not push until told to.
