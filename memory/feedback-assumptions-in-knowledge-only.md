---
name: feedback-assumptions-in-knowledge-only
description: hackathon-2026-assumptions.md (was assumptions.md) and the four general handbooks (handbook-*.md, which replaced the hackathon-2026 guides) live only in the global Knowledge, never uploaded into a project's inputs (2026-11-05)
metadata:
  type: feedback
---

User, in Coordinator-III's chat, 2026-11-05 ~10:00 UTC: it is very important that assumptions.md
is no longer given as an input of each project. It lives only in the global Knowledge (id
eb95027a, uploaded 09:52 UTC); projects get only the three competition files. The QA3 seed does
not upload it. The same holds for the planned hackathon guides (case, design, analysis, report).

Renamed 2026-11-05 by hackathon-guides: `documents/project/quality-assurance/inputs/hackathon-2026-assumptions.md`,
next to the general handbooks `handbook-case.md`, `handbook-design.md`,
`handbook-economics.md` and `handbook-report.md` (they replaced the four
`hackathon-2026-*-guide.md` files on 2026-11-05; the hackathon is their worked-example chapter);
Knowledge ids in `STATUS.md`.

**Why:** the user's choice: one shared place for these values, not a copy per project.
**How to apply:** never add assumptions or guide files to a project's files, a seed script or a
QA brief; agents find them through Knowledge search (and ask approval with the source).

Section titles are a contract (python-lead, 2026-11-05): geomind's case lead prompt cannot name the
file or its section numbers (a test forbids competition names in the package), so it asks for the
assumptions document's case, tolerance and economics sections by title. Keep the words "Case
values", "tolerances", "Economics" and "design values" in the titles of hackathon-2026-assumptions.md
(now §3, §4, §5, §6).
