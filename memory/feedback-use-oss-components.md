---
name: feedback-use-oss-components
description: Sahand 2026-11-03 09:41 +0100: frontend must not define its own UI components where an open-source one exists (shadcn/ui first)
metadata:
  type: feedback
---

Sahand (2026-11-03 09:27-09:41 +0100, WEBSITE UX I): no new features now; improve UI/UX structure of existing pages with ready open-source components. "As far as possible we must not define components ourselves, remember."
Approved plan (doc https://claude.ai/artifact/5tRDoYKogHFW6gS8Js8tdh): shadcn/ui as the official base (vendored from github raw, since ui.shadcn.com is blocked by the cloud proxy), shadcn Charts (Recharts) instead of hand SVG charts, AI Elements for the chat look, React Flow UI for the plant canvas, Origin UI for upload/stepper/unit inputs.
**How to apply:** take the library component as is (only token class mapping allowed); write our own component only when no open-source one fits, and say so. Update docs/conventions.md, docs/charts.md accordingly. Related: [[frontend-design-picks]], [[feedback-no-pull-requests]].
