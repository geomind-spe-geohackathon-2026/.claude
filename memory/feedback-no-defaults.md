---
name: feedback-no-defaults
description: Sahand rule (2026-10-31 23:30): gemini package holds NO default values for assumptions; every user sets what they need
metadata:
  type: feedback
---

Sahand: "nothing should be a default in the package; whoever needs something sets it themselves."
**Why:** defaults hide case-dependent choices (prices, cost factors, price year, GWP) inside a general library.
**How to apply:** Assumptions/Problem fields have no defaults, even cited ones (the 7 cited ones: price_year 2015, methane_gwp 29.8, drilling/heat_pump/boiler/chp/degasser cost) move into sample problem files with their sources; a missing value -> missing_assumption error or empty result. 23:31 confirmed: universal physical constants and standard correlations stay in the package (not assumptions); equipment params (pump efficiency, carnot_fraction) have no defaults. Related: [[feedback-general-not-competition]], [[gemini-problem-design]].
