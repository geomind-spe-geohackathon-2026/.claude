---
name: feedback-io-naming
description: Sahand rule (2026-10-31): file/data readers are from_<format>, writers to_<format> (from_csv/from_json/from_dict, to_csv/to_json/to_dict); in docs and Claude coding rules
metadata:
  type: feedback
---

2026-10-31 20:54 Sahand: method structure for reading/writing files must be from_csv, from_json, from_dict ... and to_csv, to_json, to_dict ...; add to docs, Claude coding rules and anywhere else needed.
**Why:** one predictable naming pattern for all I/O across gemini (and geomind).
**How to apply:** in every prompt/design: reader = classmethod on the class it returns (gm.Problem.from_json(path), gm.Plant.from_dict(d)); writer = object method (problem.to_json(path)); plain function only when it returns no gemini class (gm.data.from_csv -> demand frame). No read_/write_/load_/save_/parse_/dump_ public names (quality test). Put in conventions.md + AGENTS.md. Related: [[gemini-target-structure]], [[prompt-writing-rules]].
