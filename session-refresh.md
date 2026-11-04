# Session refresh: hand over before the context fills

Every Claude Code session of this project hands its work to a fresh session once its context
reaches 75 %. A long session gets slow and expensive and forgets; a fresh one starts small with
only what matters.

## When

Check your context at the start of every piece of work (a bug, a scenario step, a report), and
after any long tool output:

- the `get_session` tool of the Claude Code Remote MCP server, with no `session_id`, returns your
  own session; `external_metadata.context_usage` has `used_tokens` and `max_tokens`;
- at `used_tokens / max_tokens >= 0.75`, finish only the step you are in, then hand over.

## How

1. Commit and push everything (every repo you touched; `qa.py` changes are already pushed).
   Release `/tmp/geomind-backend.lock` if you hold it. Leave every claimed bug as `fixing` with a
   note of where it stands.
2. Write the handover note `.claude/notes/sessions/<name>-<n>.md` (for example
   `coordinator-1.md`, `hotfix-back-1.md`, `qa-3-1.md`; `n` counts your generation). Write only
   what the next session needs and cannot read elsewhere:
   - your role and the file with your full instructions (`notes/qa-round-2026-11-04/qa-3.md`, or
     the first prompt of a hotfix or coordinator session, copied in full);
   - the state: what is done, what is in progress (exact ids, versions, commits, runs, projects);
   - decisions and rules the user gave during your session that are not yet in `memory/` (write
     those into `memory/` too);
   - the next steps, in order;
   - for the coordinator: every session's name and id and what it is doing.
   Commit and push the `.claude` repo.
3. Start your successor with the `create_session` tool of the Claude Code Remote MCP server:
   - `environment_id`: the Dell's bridge, `env_016GdNnRFgDJDikcqrVDEN8i`;
   - `title`: your name with the next Roman numeral: `Coordinator-II`, `hotfix-back-II`,
     `qa-3-II`, then `-III` and so on;
   - `tags`: the same as yours;
   - `model`: `claude-opus-5-5` for hotfix sessions only, `claude-sonnet-5-5` for every other
     session (`memory/feedback-session-models.md`);
   - `prompt`: "You are <title>, the successor of <your name> (<your session id>). Read
     ~/geomind-spe-hackathon-2026/.claude/notes/sessions/<name>-<n>.md and follow it; your role's
     rules and mode are in it, so do not ask the user for the mode. Start now."
4. Tell the coordinator (its id is in `.claude/STATUS.md`) with `send_message`: your successor's
   title and id. The coordinator updates `STATUS.md`.
5. Stop: claim nothing, schedule nothing. The coordinator archives the old session once the
   successor has reported in.

## The coordinator's own refresh

The same steps, and in the note: every running session (name, id, role, state), the open
decisions for the user, and the deploy and QA rules in force. After `Coordinator-II` is running,
the old coordinator updates `STATUS.md` with the new coordinator id, sends every session one line
("the coordinator is now <title>, <id>"), and tells the user in the chat. Sessions always read the
coordinator's id from `STATUS.md` before they message it.
