# Feature: compare the best unique structures of an evolve study (Sahand, 2026-11-05 ~01:45 UTC)

Hotfix mode. Owners: hotfix-back (API), hotfix-front (page). gemini already gives the data.

## What the user gets

From a finished `evolve` study ("Find the best structure"), a button "Compare structures" opens a
NEW window/tab (its own route, e.g. `/projects/:project/studies/:study/structures`, also a link
the user can share or reopen) with the best UNIQUE structures, up to 10:

- One row per structure (no two rows with the same `structure`), ranked: feasible before
  infeasible, then by the first objective (then the others), as gemini ranks them.
- Columns: rank; the structure in plain words (which optional equipment is in, which
  alternative was picked); feasible, with the reason when not; the objectives and the main
  metrics in display units (cost of heat/cooling, CAPEX, heat and cooling delivered, emissions,
  whatever the study's metrics are); the parameters the search set.
- Pareto-front members are marked when there are several objectives.
- Select 2 or 3 rows to compare side by side: every metric and parameter in one table, the
  differences highlighted.
- Per row: "Open this design" (its plant: the structure with its parameters) and, if the backend
  allows, "Save as a plant of the project".

## Data

`gm.study.evolve` returns `structures` (the best design of each valid structure, no plant; the
plant is that structure with its parameters), `front`, `best`, `objectives`, `rejected`,
`budget` (`Evolution.to_dict`). The page takes the top 10 of `structures` by gemini's ranking.

## hotfix-back

An endpoint (e.g. `GET /api/v1/projects/{id}/studies/{study}/structures?limit=10`) that reads the
stored evolve result and returns `{objectives, budget, structures: [{rank, structure, feasible,
reason, violation, metrics, parameters, on_front}]}` (display units, as stored); 404 for a study
that is not an evolve study or has no result. Optional: build the plant of one structure for
"Open"/"Save". Add it to contracts.md; tell the coordinator the shape.

## hotfix-front

The button on an evolve study row and on its result; the new route and page (stock shadcn table,
row selection, side-by-side compare); loading, empty and error states. Wait for the shape.
