# qa-func-2: design and simulation

Model: Opus. Rules: `common.md`. Area: FUNCTIONALITY of the design and the simulation. Get to a
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
