---
name: reference-start-sessions-bg-remote-control
description: On Sahand's account there is no Remote MCP (create_session); start sessions on the Dell with claude --bg --remote-control so they show in the claude.ai sidebar
metadata:
  type: reference
---

On Sahand's account (from 2026-11-05) the coordinator has no Claude Code Remote MCP tools
(`create_session`, `list_environments`, `send_message`). Start a session from the project root on the
Dell with:

`claude --bg --remote-control <title> -n <title> --model <model> --permission-mode auto "<first prompt>"`

It prints a short id (`claude logs|attach|stop <id>`); `claude agents --json` gives the full
sessionId. `--remote-control` makes it show in the claude.ai Code sidebar (the user wants every
session listed there by title; confirmed working). A session started without it can be moved
without losing context: `claude stop <id>`, then the same command with
`--resume <full sessionId>` (never while it holds `/tmp/geomind-backend.lock`).
Message sessions by title with SendMessage (peer messaging); the coordinator's own address is in
STATUS.md. Recurring coordinator tasks: CronCreate (session-only, expire after 7 days).

**Why:** the account handover moved the work to an account without the Remote MCP server.
**How to apply:** every successor (session-refresh.md) is started this way on this account.
