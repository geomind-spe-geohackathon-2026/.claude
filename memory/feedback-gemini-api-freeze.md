---
name: feedback-gemini-api-freeze
description: Sahand rule 2026-11-02 10:17: gemini public API frozen from dev 6ba3984 (0.4.0); no API change in any later gemini work
metadata:
  type: feedback
  modified: 2026-11-02T10:17:57.838Z
---

Sahand (2026-11-02 10:17, "important, keep it in mind for everything we do on gemini"): from now on no gemini API may change.
Baseline: dev 6ba3984, version 0.4.0, its `public_api.json`.
**Why:** geomind, backend and the competition deliverables build on it; the API churned in every prompt so far.
**How to apply:** every gemini prompt states the freeze: no rename, removal or signature change of any public name (gm.*, gm.<folder>.*, file formats case/economics/plant/study JSON, module author contract forward/update/State). Internal refactors only. A test compares `public_api.json` with the 0.4.0 snapshot and fails on any difference. A truly needed addition is listed and asked first, never slipped in. Consequences noted 10:20: item 19b (one time-series type) only if internal; fluid-from-inlet fix keeps gm.call unchanged; batch size setting is an addition -> ask.
Related: [[gemini-scenario-design]], [[feedback-contribution-gemini-source-of-truth]].

10:19 Sahand clarified: rule = BACKWARD COMPATIBLE. Nothing existing may break (no rename/removal/signature or behaviour change); additions are allowed if they break nothing. Most important: everything the competition uses stays exactly the same. So API cleanups of leftovers (evaluate.run_all vs verdict, call_* names, physics.control/diagnostics, public ops) are NOT done (they would break). Test: 0.4.0 snapshot must be a subset of the current API (additions ok) + competition-surface test (examples/hackathon.py calls and outputs unchanged).
10:21 FINAL: one last breaking cleanup (<30 min: remove evaluate.run_all in favour of verdict; move physics.control/diagnostics out of physics; keep call_* and ops) released as 0.5.0. Freeze baseline = 0.5.0: from then backward compatible, nothing geomind relies on may change.
