---
name: reference-start-sessions-bg-remote-control
description: Every session runs in the NTNU Dell environment (the `claude remote-control` bridge on the Dell) in ~/geomind-spe-hackathon-2026; never --bg, never plain Remote Control sessions
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

**Change, 2026-11-05 (user):** do NOT use `--bg`: a background session refuses edits in the shared
clones (it wants a worktree). Start every session as a normal interactive session in tmux:
`tmux new-session -d -s '<title>' -x 220 -y 50 -c ~/geomind-spe-hackathon-2026 "claude --remote-control '<title>' -n '<title>' --model claude-opus-5-5 --permission-mode auto '<first prompt>'"`
(add `--resume <sessionId>` to keep a session's context). Watch with `tmux capture-pane -p -t '<title>'`.

**Change, 2026-11-05 (user, "save this"): every session is started IN THE NTNU DELL ENVIRONMENT**
(the self-hosted bridge: the `claude remote-control` process running on the Dell), working folder
`~/geomind-spe-hackathon-2026`, not as a Remote-Control-enabled local/tmux session and not `--bg`.
Start it from claude.ai/code (New, environment "NTNU Dell", folder ~/geomind-spe-hackathon-2026) or
with `claude --environment <ccpool_... id of the NTNU Dell environment>` from that folder. Opus,
hotfix mode, no branch, no worktree ([[feedback-no-branches-no-worktrees-hotfix]],
[[feedback-session-models]]). The tmux method above is only a stopgap.
