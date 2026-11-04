---
name: gemini-problem-design
description: 2026-10-31 23:15+ thread "Shape the gemini usage API": decisions on units (Quantity + enum), strict typed Problem JSON, assumptions groups, constraint roles
metadata:
  type: project
  modified: 2026-10-31T23:32:04.993Z
---

Discussion only, no repo change, no prompt yet (wait for «go»). Continues [[gemini-remaining-work]].

Usage flow (23:15): Problem.from_json -> plants.capabilities -> optim.size -> optim.minimize -> simulate -> evaluate.report -> compare. Frictions: hand sizes in plant.json, mixed units, manual frame reading, hidden plan= kwarg in optim.

AGREED:
- Units: every dimensioned value = gm.units.Quantity (exists, unused today) at API boundary; JSON {"value","unit"}; unit = Unit(str, Enum) from the existing unit table; each field typed by quantity so only units of that dimension are allowed; engine stays SI. ("2500 m" strings question unanswered.)
- Problem = strict entry boundary, typed, unknown key = error. Sections: demand {start, step, heating/cooling: profile file/column/unit + supply/return temperature}, site {ground, reservoir (reference_depth, thickness, permeability, pressure, pressure_at_other_depth "hydrostatic"), fluid (moved from plant), air}, choices {doublets min/max, depth min/max}, constraints, assumptions (name kept). Everything not about the plant leaves plant.json (consumer return temps/pressures, fluid, air). Supply-temp constraints dropped (demand implies them). No "d*." glob site keys.
- Constraints on roles not module paths (Q1 yes).
- Per-value "source" tag REJECTED.
- Assumptions in 5 groups: finance {currency, discount_rate, lifetime, price_year}, prices {electricity, gas, heat, cold, waste_disposal, chemical, co2}, emissions {grid_carbon_intensity (renamed from electricity_emission_factor), methane_gwp}, costs {drilling, pump, heat_pump, boiler, chp, chiller, exchanger, degasser, flare, gas_makeup}, allocation {heat_cost_share}.
- No defaults in package [[feedback-no-defaults]]; physical constants stay.

OPEN (23:34): constraint role list proposed: doublet {production_flow, brine_cooling, production/injection_temperature, pump_power, pump_efficiency, volume_imbalance, wellhead_pressure}, heat_pump {heat_output, cop, lift}, boiler {heat_output, fuel_input}, chp {heat_output, power_output}, chiller {cold_output, cop}, heat_exchanger {duty, approach}, heating_supply/cooling_supply {temperature, unmet}, plant {electricity_bought, gas_bought, co2, heat_surplus}; over each|sum|mean|max|min|duration; when always|running; applied per unit. Asked: no cross-unit totals for now? new modules declare role+quantities? Also open: grid_carbon_intensity as time profile?
23:36 Sahand: keep discussing Problem; once Problem is settled, give ONE prompt for it. Sent 12 open points with recommendations (profile file or inline values; start/step read from file; only heating+cooling now; reservoir temp from gradient OR given; pressure_at_other_depth enum hydrostatic|constant; air const or profile; choices closed {doublets, depth, plant_families}, sizes via optim.size; no cross-unit constraints; modules declare roles; carbon intensity profile allowed; drop "2500 m" strings; Python classes gm.run.Demand/Site/Choices). Waiting.
Later answers (23:45-23:50): [[gemini-case-decisions]].
