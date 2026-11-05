# Coordinator, generation 5 (Coordinator-V): state at handover (2026-11-05, Sahand's account)

Read first: `.claude/AGENTS.md`, `STATUS.md`, `memory/MEMORY.md`, `session-refresh.md`,
`account-handover.md` (Phase 2), `notes/sessions/coordinator-4.md` (role and rules, unchanged).
Mode: HOTFIX (decided; do not ask). Chat with the user in Persian, short; files in English.

## Why this handover

Coordinator-V (Remote Control session in the NTNU Dell environment, cse_0171QAFoqEoKns9YW5jXiXcS)
has NO tool to create sessions (`create_session` / `list_environments` of the Claude Code Remote
MCP are missing; not a claude.ai connector, not a local MCP). The user wants every session opened
IN THE NTNU DELL ENVIRONMENT (the env of this session: Computer NTNU09811,
"geomind-spe-hackathon-..."), not as --bg, tmux or plain Remote Control sessions, not in the
default env. A fresh coordinator is opened to test whether it gets that tool.

## First thing to do

1. Check your tools (ToolSearch "create_session list_environments"). Tell the user in one line
   whether you can create sessions in the NTNU Dell environment.
2. If yes: `list_environments`, pick the NTNU Dell env, write its id in STATUS.md and in
   memory/reference-start-sessions-bg-remote-control.md, and start these four, all
   model claude-opus-5-5, cwd ~/geomind-spe-hackathon-2026, prompt
   "You are <title>. Read ~/geomind-spe-hackathon-2026/.claude/notes/sessions/<note> and follow it.
   Mode: HOTFIX, work directly on the default branch in the shared clone, no new branch, no
   worktree. The coordinator is <your title> (<your id>). Start now.":
   - hotfix-python-VII: hotfix-python-6.md (QA-145 on geomind main 0666b5d, NOT released, still
     0.4.95: finish tests, release 0.4.96, deploy; then QA-122, speed items, read_file, IMP-028,
     IMP-026)
   - hotfix-back-VI: hotfix-back-5.md (no open backend bug)
   - hotfix-front-VII: hotfix-front-6.md (no open frontend bug)
   - Manual QA-IV: manual-qa-3.md (Fatemeh's session; her run-log analysis is half done)
   Then tell Coordinator-V (SendMessage "Coordinator-V") to stop; the user archives it.
3. If no: tell the user, and stop; Coordinator-V stays the coordinator.

## Rules in force (all in memory/)

- Every session on Opus (feedback-session-models, 2026-11-05 change).
- Hotfix mode; no new branch, no worktree ever (feedback-no-branches-no-worktrees-hotfix).
- Sessions run in the NTNU Dell environment (reference-start-sessions-bg-remote-control).
- No QA tests (live, browser, LLM) until the user lifts it; Fatemeh's bugs first; deploy at once;
  lock /tmp/geomind-backend.lock holds; hand over at 300,000 tokens.
- Release summaries: Coordinator-V had a session cron (:07/:37); recreate with CronCreate.

## State

Production: backend 1.1.99 (geomind 0.4.95, gemini 0.6.16), frontend 1.1.113. No session other
than Coordinator-V is running; all clones clean and pushed; no lock.
