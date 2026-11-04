---
name: frontend-design-picks
description: 2026-11-03 design-source research for the GeoMind frontend (thread WEBSITE UX I): picks, doc link, limits
metadata:
  type: project
  modified: 2026-11-03T00:54:18.439Z
---

Thread "WEBSITE UX I" (cmsg_016VUmQoW7nUde2xdqUWA2PoLU8Zkv7qaEEXPLYmYbviQD), 2026-11-03. Sahand asked for design (not ideas) sources close to the project.
Doc (Persian): https://claude.ai/artifact/9zJ1CzqwMiFFCpjWYNCfBW
v1 picks (dashboard-first, superseded): all free, all shadcn-based: shadcn dashboard-01 + charts (Overview/Results), Tremor Blocks (KPI/charts, Recharts), mapcn (MapLibre map card: site + wells), React Flow UI (flowsheet), AI Elements (agent chat; moving into shadcn end Nov 2026), Origin UI + Kibo UI (upload, stepper, timeline, table), Magic UI (landing only). Paid ones skipped (ReUI, Shadcnblocks, Shadcn Studio map blocks).
Not yet approved by Sahand; no code changed.
Limit: the cloud container's browser/proxy blocks these design sites (403), so picks were made from page text, not visuals; Reddit blocked, Dribbble/Behance search empty.
PRODUCT FRAMING (Sahand 2026-11-03 01:54 +0100, "remember"): the app is mainly GEOTHERMAL and should feel like a SMALL EDITOR: drag-and-drop modules on a canvas, chat with agents, simulate and optimise a real geothermal job in one place. Design references must be editor-style (canvas + palette + inspector + chat + run/results panel), not map/dashboard-first.
v2 (editor-first, same doc rewritten 2026-11-03 ~02:10 +0100): one editor screen (palette left, canvas centre, chat/inspector right, results drawer bottom, Simulate/Optimise top); skeleton from React Flow Workflow Editor template (MIT) + React Flow UI; behaviour refs Node-RED AI Flow Builder (preview/apply/undo chat), SAP Astonish (run mode), Comfy Agent, Modelon Impact (experiments/sweeps), n8n (execute and refine). Dropped Tremor/shadcn charts: frontend deliberately uses hand-written SVG charts (docs/charts.md) and own role tokens + IBM Plex (docs/tokens.md). Frontend repo read from GitHub geomind-spe-geohackathon-2026/frontend main f4b3062; the linked device was Sahand's MacBook, which has no app code.
Related: [[frontend-design]], [[feedback-reply-format]].

2026-11-03 09:27 +0100 Sahand: REMOVE the Editor everywhere (done: frontend 1.0.1 cdc03f5). NO new features for now. Goal = better UI/UX STRUCTURE of the existing pages: better components in better places, taken from open-source libraries (shadcn/ui and friends) instead of building everything ourselves. Plan per page goes to Sahand before code.

2026-11-03 13:01 +0100 Sahand: restyle the frontend in the STYLE of flowctl (github.com/cvhariharan/flowctl, Apache-2.0; screenshots in its docs/site/static/images: flows, run, logs): clean light theme, blue primary, Inter, big page titles with subtitle + primary action right, tables in cards with row icons, run page = steps left + terminal log right. Keep OUR features and shadcn components; only tokens/layout change. He saw no visible change after the shadcn migration (explained: tokens kept on purpose); show before/after screenshots.

2026-11-03 13:08-13:20 +0100 Sahand: use the OFFICIAL shadcn theme (neutral, blue primary) as is — done in frontend 1.1.8 (3764faf). Then: make the app as close as possible to Claude's own UI ("familiar to users"): left sidebar (new chat, chats, projects, Case/Plant/Study/Results/Report pages; USER MENU AT THE BOTTOM like Claude), MAIN PANEL = CHAT always (first thing a user sees), Case/Plant/... open in a SIDE PANEL next to the chat with only EXPAND and CLOSE buttons; projects list opens in the main panel from the sidebar (no separate page). NO new features, only move things. Target v1.1.9.

2026-11-03 14:00-14:11 +0100 Sahand spec for the next round (after 1.1.9): ONE fixed main menu everywhere (Claude style): top = brand + sidebar toggle; New (opens New project dialog), Search, Projects, Scheduled ("soon"); no Artifacts/Customize. Then Pinned (pinned projects AND chats; pin via "..." menu; stored in browser for now). Then the open project's name with Overview, Runs and logs, Documents, Settings, then that project's chats only (project name instead of "Ungrouped"). These pages open in the MAIN panel. Design pages (Case/Plant/Study/Results/Report) leave the sidebar: they live in a resizable side panel titled "Design" with toggle buttons. ONE top bar only (like Claude). Resizable split, border turns blue while dragging. Projects page like Claude: search icon opens input, sort icon opens menu (last updated / date created / alphabetical). Sahand says wait for "start" before building each batch.
