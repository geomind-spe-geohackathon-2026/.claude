---
name: gemini-structure-optimisation-idea
description: "Parked idea (Sahand, 2026-11-03): optimise gemini plant modules and connections, not only sizes; discuss later"
metadata:
  type: project
---

Sahand wants studies to optimise the modules and connections of a plant, not only the numbers with a range. Parked on 2026-11-03, then approved the same evening (18:23): the owner asked for a GA design consistent with the rules and its implementation, in a new thread GEMINI II. The decided design is in gemini-work/.tmp/handover/GEMINI_II.md.

Proposal given: a superstructure plant that holds every candidate module and route; each optional module gets an on/off switch with bypass (the stream passes unchanged), route choices as a switch or a splitter fraction; a two-level search, structures outside (enumerate up to about 5 optional units, a genetic search beyond) and today's DE on sizes inside, as doublet counts are searched now. Free search over arbitrary connections was advised against (most are not physical). Estimate 2 to 4 days; additive API only (a new plant-file key), so it breaks the 0.5.13 freeze. For the hackathon the app can build structural variants and give them all to one study (already works, in parallel since 0.5.14).

**Why:** a study today searches only values with a range or options; the structure of each candidate plant is fixed.

**How to apply:** when Sahand raises it, start from this proposal and send a short design (file format, modules that get a bypass) for approval before code. See [[gemini-api-freeze-0-5-x]], [[gemini-workspace]].
