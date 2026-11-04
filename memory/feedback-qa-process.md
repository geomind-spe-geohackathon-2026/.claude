---
name: feedback-qa-process
description: Bugs from testing go in documents/project/quality-assurance (BUGS.md index, one file per bug, evidence); hotfix sessions fix them one by one and report
metadata:
  type: feedback
---

Sahand and Fatemeh, 2026-11-04 (evening): several Claude Code sessions and the two of them test the app on production in parallel. Every bug goes in `documents/project/quality-assurance/` of the project root: one line in `BUGS.md`, one file `bugs/QA-<nnn>-<slug>.md` from `TEMPLATE.md` with reference, explanation and screenshots in `evidence/QA-<nnn>/`, so another session can read it and hotfix it. A hotfix session takes the bugs one by one, fixes, deploys, retests, and tells the team.

**Why:** many testers at once need one place, one format, and no two sessions editing the same file.

**How to apply:** follow `documents/project/quality-assurance/README.md`: take the next id and add the line at once; claim a bug (`fixing` + fixer) before working on it; fix in hotfix mode ([[feedback-development-modes]]); write Fix and Retest; report the ids and versions in the chat.
