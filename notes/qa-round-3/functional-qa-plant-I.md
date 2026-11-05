# functional-qa-plant-I

Read `README.md` here (your row) and `../qa-round-2/common.md`. Your project: "QA3 plant" (id in
STATUS.md once seeded). Test only your stage; report bugs with qa.py (reporter
functional-qa-plant-I). Check every number against the PDF and CSVs.

Reference figures (PDF + CSVs): heating peak 30.0 MWth (28 Jan), 111.67 GWh/yr, min 2.67 MW;
cooling peak 10.0 MWcool (19 Jul), 23.74 GWh/yr, 146 zero-cooling days. Reservoir 2500 m TVD,
30 C/km, 12 C surface (~87 C midpoint). Supply 100 C heating, 20 C cooling. 1-3 doublets, 50-300
m3/h per doublet, brine cooling <= 40 C, 330 operating days, pump efficiency 70 %, GLR 0.8, 80 % CH4.
One doublet at 300 m3/h, dT 40 K gives roughly 13-14 MWth.

## Scenarios

Chat first (user rule, feedback-qa-through-chat): every action below is a chat request like a user's; answer agent questions and approvals in the chat. Tabs only verify what the chat produced; if the chat cannot do a step, file that gap as a bug.

One request at a time in the QA3 plant chat (case already set; no case redo).

- plant-I-S1 Configurations offered. Chat: "Which plant configurations can cover this heating and
  cooling demand?" Correct: families named (geothermal only, + heat pump, + gas boiler/CHP on the
  co-produced gas, + chillers/absorption for cooling), each tied to the case; the 87 C vs 100 C gap
  (lift needed) is recognised; no value invented.
- plant-I-S2 Sizing, heating. Chat: ask for a sized plant for the heating peak. Correct: doublet count
  1-3, flow 50-300 m3/h each, brine return <= 40 C; geothermal heat <= ~13-14 MWth per doublet at
  300 m3/h; backup/lift sized for the 30 MW peak and the 35 non-operating days; numbers reproduce
  by hand.
- plant-I-S3 Sizing, cooling. Cooling by chiller / heat-driven (absorption) from geothermal heat;
  capacity >= 10 MWcool peak; COP/source of any value stated and labelled, not defaulted.
- plant-I-S4 Hard-constraint check. Ask for a plant with 4 doublets, or 400 m3/h, or 45 C brine
  return. Correct: gemini check refuses/flags it, agents explain why in plain words, offer a legal
  fix; user sees the reason.
- plant-I-S5 Design change by chat: "use two doublets", "deeper wells", "add a gas boiler". Correct:
  a new plant version is stored (QA-092), the change is visible in the plant view, others unchanged;
  survives a page reload.
- plant-I-S6 Explanation. Ask "why this configuration and these sizes?" and "what are the risks?".
  Correct: reasoning cites the case numbers, calculations shown (calculate/run_python), missing
  models named and filled with an explained simplified calculation (judged item).
- plant-I-S7 Missing values. Ask for a heat pump/chiller with no COP or cost given. Correct: agent
  asks once, or proposes a sourced/labelled value for approval; never a silent default.
- plant-I-S8 Compare alternatives. Ask for two plant variants compared on capacity and key
  checks, plus a recommendation. Correct: table consistent with S2/S3 numbers; token use visible.
- plant-I-S9 Verify in the plant tab (read-only check of what the chat built; no editing in forms). Parts, connections, sizes in the plant page match chat statements;
  units correct (m3/h, MWth, C); no console errors.

## Status

- 2026-11-05: scenarios written; waiting for the coordinator to send the QA3 plant project id.
- 2026-11-05 11:10 UTC PAUSED by coordinator. Project c45a5382-af55-43fc-9340-dd1ab1245533, chat 6732957b-7035-481a-bc31-7f4abcda2a76 (browser session functional-qa-plant-I, logged in).
  S1 in progress (backend 1.1.84 at start, 1.1.86 now): explanation-only request; agent asked "Build plant" repeatedly after two denials -> QA-116 (major). I then approved to continue; the run is still going (130 steps, retrying build/patch after validator refusals, no text answer yet; plant proposed with 1 doublet). Resume: check the chat's run state, answer any approval, wait for the text answer, then S2-S9. Not yet done: S2-S9.
