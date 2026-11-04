---
name: feedback-units-geomind-defines-gemini-converts
description: Sahand rule 2026-11-03 08:37 UTC: consumers (geomind, app) choose WHICH display units; ALL unit conversion is done by gemini, never by hand in the consumer
metadata:
  type: feedback
---

Sahand (2026-11-03 08:37 UTC, GEOMIND 1): "which units to display is defined in geomind; doing the conversions itself is wrong. gemini must do the conversions."
**Why:** gemini is the source of truth ([[feedback-contribution-gemini-source-of-truth]]); a second conversion table in a consumer can drift from gemini.
**How to apply:** geomind keeps its own choice map (READ_UNITS: power->MW, pressure->bar, ...) and passes those units to gemini (units= on Results.get/summary, gm.units.convert). No conversion factors or unit arithmetic in geomind (a test guards this). Display-unit options were NOT requested from gemini.
Also 2026-11-03 08:31 UTC: requests to gemini only for completely new features or bugs, never changes to existing structure/signatures/outputs; see /mnt/project-files/notes/geomind-gemini-needs.md.
- 08:38 UTC Sahand: where gemini cannot convert a unit, LIST it for Sahand; never ask gemini directly without telling him first.
