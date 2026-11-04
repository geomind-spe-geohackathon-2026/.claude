# qa-func-2: design and simulation

Model: Sonnet (Sahand 2026-11-04 23:45 UTC). Rules: `common.md`. Area: FUNCTIONALITY of the design and the simulation. Get to a
complete case quickly with your own project (one chat request with the competition files,
auto-approve on); do not test the case step (qa-func-1's area) unless it blocks you.

Cover at least:
- The design team proposes configurations and sizes that meet the PDF's hard constraints
  (1-3 doublets, flow per doublet, brine cooling limit, operating days, backup covering the
  year, supply 100 C heating and 20 C cooling) and covers the demand peaks.
- Plant families: geothermal only, with heat pump, with gas boiler or CHP on the co-produced gas,
  cooling by chillers; asking for a family by chat; the comparison of families.
- gemini check: what it refuses, whether the agents fix it, whether the user sees why.
- The simulation: it runs over the year; results and charts match the demand CSVs (supplied vs
  demanded heat and cooling, unmet demand, temperatures, flows); physics sense.
- Design changes by chat ("use two doublets", "deeper wells") and a new simulation; the stored
  design survives a reload and a cancelled run.
- Parameter lists the plant or study still needs are named clearly (QA-049, QA-052).

## Scenarios

(write them here before you test)

Reference figures (from the PDF and the CSVs, checked by script): heating 365 days, peak 30.0 MWth
(28 Jan), 111.67 GWh/yr (sum of daily MW x 24), min 2.67 MW; cooling peak 10.0 MWcool (19 Jul),
23.74 GWh/yr, 146 days with zero cooling. Reservoir 2500 m TVD, 30 C/km, 12 C surface -> ~87 C at
the midpoint; 100 C heating supply therefore needs a temperature lift (heat pump or boiler/CHP)
or a deeper well (~2.95 km for 100 C). Max brine cooling 40 C, flow 50-300 m3/h per doublet,
1-3 doublets: one doublet at 300 m3/h and dT 40 C gives about 1030*~4.0 kJ/kgK*83 kg/s*40 K ~
13-14 MWth, so the 30 MW heating peak needs 2-3 doublets or a backup/lift. GLR 0.8 Nm3/m3, 80 %
CH4 (gas for a boiler or CHP). 330 operating days of the doublet; backup covers the rest.

- qa-func-2-S1 Fast path to a design. New project "QA2 qa-func-2 base", auto-approve on, one chat
  message with the PDF and both CSVs asking for a complete design and simulation. Correct: the
  run reaches a design without the user filling values the files give; any open value is asked
  once and clearly (QA-049, QA-052 lists).
- qa-func-2-S2 Hard constraints in the design: 1-3 doublets, 50-300 m3/h per doublet, brine
  cooling <= 40 C, 330 operating days, backup covering the other days and the peaks, supply
  100 C heating and 20 C cooling, pump efficiency 70 %, equal production/injection volumes.
  Correct: each one is visible in the plant/design and respected (checked against the reference
  figures above, physics sense of the heat per doublet).
- qa-func-2-S3 Plant families: the design team proposes and compares families (geothermal only,
  with heat pump, with gas boiler or CHP on the co-produced gas, cooling by chillers) with reasons;
  the user can ask for a family by chat ("compare a heat-pump design with a gas-boiler design").
  Correct: a comparison table/explanation with sizes and the reasons; the requested family is built.
- qa-func-2-S4 gemini check: watch what gm.check / build_plant refuses during S1-S3; correct: the
  agents fix it themselves or ask the user one clear question; the user sees why in the chat.
- qa-func-2-S5 Simulation: runs the whole year; results/charts: supplied vs demanded heat and
  cooling per day match the CSVs (peaks 30 / 10 MW, totals 111.67 / 23.74 GWh), unmet demand
  shown and explained, temperatures (producer ~87 C or by depth, injection >= producer - 40 C),
  flows within 50-300 m3/h per doublet, doublet days <= 330. Physics sense (COP, gas use).
- qa-func-2-S6 Design change by chat: "use two doublets" then "make the wells deeper, 3000 m";
  correct: only that changes, the design is re-checked and a new simulation runs; results differ
  in the expected direction (deeper -> hotter brine, more heat per doublet).
- qa-func-2-S7 Persistence: the stored design survives a page reload and a cancelled run
  (cancel during the simulation or design, then ask to continue: work reused, QA-047).
- qa-func-2-S8 Missing-parameter lists: the plant/study lists of parameters still needed are
  named clearly, no value the case already has is asked again (QA-049), backup/control params are
  accepted (QA-052).

## Status

(one line per scenario; updated while testing)
