---
name: persian-rtl-formatting
description: How to format Persian replies so mixed Persian/English text reads correctly right-to-left
metadata:
  type: feedback
---

User (2026-10-27) said mixed RTL/LTR Persian replies are hard to read.
**Why:** English words/code inside Persian lines flip the line direction, especially when a line or bullet starts or ends with English.
**How to apply:** start every line and bullet with a Persian word, never with English or `code`; put an RLM mark (U+200F) after inline English/code segments and at line ends that finish with English; minimise inline English, move names/paths into separate code blocks (code blocks stay LTR); avoid tables mixing scripts. Related: [[project-status-handoff]].
