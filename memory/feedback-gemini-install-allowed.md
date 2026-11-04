---
name: feedback-gemini-install-allowed
description: Sahand 2026-11-03 18:26 UTC: the geomind Dell session installs gemini wheels itself (allow rule added); never ask Sahand to run pip again
metadata:
  type: feedback
  modified: 2026-11-03T18:27:03.522Z
---

On 2026-11-03 18:26 UTC Sahand added an allow rule on the NTNU Dell to `~/geomind-work/geomind/.claude/settings.local.json`: `Bash(.venv/bin/python -m pip install -r requirements/gemini.txt)`. He said: "from now on, do it yourself."

**Why:** the auto-mode classifier twice refused the pip install of the sha256-pinned gemini release wheel (as "code from external"). Sahand had to run it himself, and that stalled the work.

**How to apply:** for every gemini upgrade, pin the version and sha256 in requirements/gemini.txt, then run the ABSOLUTE form `/home/fatemec/geomind-work/geomind/.venv/bin/python -m pip install -r /home/fatemec/geomind-work/geomind/requirements/gemini.txt` (the RC shell does not keep its cwd; Sahand was asked 18:29 UTC to add this absolute rule too). Do not ask Sahand to run it. If it is still refused, report the exact command text.

Related: [[feedback-ask-early-when-blocked]], [[feedback-no-editable-installs]].

2026-11-03 19:12 UTC: the 18:26 rule did NOT land in the geomind repo (the file was missing). The RC session cannot add allow rules itself (refused by the classifier). Sahand must create /home/fatemec/geomind-work/geomind/.claude/settings.local.json with the absolute rule. Until then, gemini installs still need Sahand.
2026-11-03 ~19:40 UTC: the rule now works; the gemini 0.6.0 install went through on the Dell (geomind dev30, 22e2ad7).

**Path changed 2026-11-04 (evening):** geomind moved from `~/geomind-work/geomind` to `/home/fatemec/geomind-spe-hackathon-2026/geomind`; use that path in the install command and in any allow rule.
