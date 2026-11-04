# qa-func-3, generation 1: handover (2026-11-05 ~00:50 UTC)

Role: QA session "qa-func-3" of QA round 2 (economics, scoring, report). Instructions:
`.claude/notes/qa-round-2/common.md` and `.claude/notes/qa-round-2/qa-func-3.md` (the scenarios
S1-S9 are written there and pushed, commit 74fc527; the coordinator was told). Mode: hotfix round,
test and report only; do not ask the user for the mode. Browser: agent-browser only,
`--session qa-func-3`. Coordinator id: read `.claude/STATUS.md`.

## State

- No bugs reported by me yet. No agent run started.
- Project created: "QA2 qa-func-3 economics", id 2cc9eadb-9175-4375-881e-1e63624d024a
  (https://geomind.team/projects/2cc9eadb-9175-4375-881e-1e63624d024a/assistant/chat), shared
  memory Off. It has no chat yet: the first message (below) was typed with the three competition
  files attached but NOT sent; the browser was closed, so it is lost. Start S1 in this project.
- First message used (reuse it): "We are taking part in the GEMINI geothermal design hackathon.
  The attached PDF gives the reservoir, brine and gas data and the design constraints, and the
  two CSVs are the daily heating and cooling demand for 2027. Please build the case from these
  files, design a deep-geothermal plant that covers the heating and the cooling demand within the
  hard constraints, simulate it over the year, then work out the economics (CAPEX, OPEX, LCOH,
  LCOC, NPV) and check the design against every requirement in the PDF."

## Tips learned

- Run `agent-browser --session qa-func-3 set viewport 1440 1000` right after opening: at the
  default small viewport the New project dialog's Create button is off-screen and a click on it
  closes the dialog with no request (looks like a failed create; it is the tool, not a bug).
- Auto-approve in the chat composer is a toggle button; check `aria-pressed="true"` before you
  send (it read false after one click; click it again and check).
- Log in with FIRST_ADMIN_EMAIL / FIRST_ADMIN_PASSWORD from `backend/.env`, read at run time with
  grep/cut into shell variables; never print them.
- Reference numbers (CSV): heating peak 30.0 MW (28 Jan), 111.67 GWh; cooling peak 10.0 MW
  (19 Jul), 23.74 GWh, 219 non-zero days.

## Next steps

1. Open the project, set auto-approve on, attach the PDF and the two CSVs
   (`gemini/examples/hackathon_2026/`), send the first message: S1.
2. Then S2-S9 in order; one-line status per scenario under "Status" in qa-func-3.md.
3. Report bugs with qa.py; one line to the coordinator per blocker/major; hourly report.
