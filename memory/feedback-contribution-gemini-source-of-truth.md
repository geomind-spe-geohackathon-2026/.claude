---
name: feedback-contribution-gemini-source-of-truth
description: Sahand standing rule (2026-11-01 15:16): main goal is contribution to the GEMINI project, not just winning; gemini is the source of truth and others design around it
metadata:
  type: feedback
  modified: 2026-11-01T15:16:58.192Z
---

Sahand ("always remember"): our main goal is CONTRIBUTION, helping the whole GEMINI project, not only winning the competition. The right, principled design is done in gemini; gemini is the primary source of truth, and geomind, backend and frontend build their own design on top of gemini (they adapt to gemini, never gemini to them).
**Why:** the work should be a lasting, upstream-quality contribution; the competition only sets priorities.
**How to apply:** judge every gemini change by "is this the right general design for the project", never by "does it help the hackathon score"; never bend gemini to suit geomind/backend or the competition inputs; when geomind is blocked, first ask whether gemini is missing a general capability, otherwise geomind adapts (e.g. old-API mapping notes). Extends [[feedback-general-not-competition]] and [[feedback-no-defaults]].
2026-11-01 15:20 Sahand: anything not in gemini's main design (stubs like plants.example, leftovers) is deleted; geomind switches to the new way later. Rule: no NotImplementedYet stubs or compatibility leftovers in the public API; features enter the API when built (planned ones listed in refactor-notes.md).
2026-11-01 20:23 Sahand: in the gemini thread, ignore geomind entirely (no geomind cost/impact arguments, no geomind work); judge gemini design on its own.
2026-11-03 00:58 (+0100) Sahand ("always remember"): NOBODY asks gemini for anything without his permission. If a thread needs a feature gemini lacks, it writes it into a list for Sahand to review and approve; never sends a request to the gemini thread directly. App's list: backend/docs/app-build/gemini-requests.md (Sahand reviews it; not a channel to gemini).
2026-11-04 11:51 UTC Sahand: gemini must NOT provide data/information for other packages (no deriving their inputs, no reference values on their behalf); they gather their own inputs. But unit problems, unclear errors and real gemini bugs ARE gemini's to fix.
