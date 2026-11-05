# Account handover: force stop, then reopen every session on Sahand's account

Prepared by Coordinator-IV (2026-11-05, user's request). Run it ONLY when the user says so in the
coordinator's chat ("force stop" / "hand over to Sahand's account"). Until then nothing here runs.

Why: the usage of the current account (Fatemeh's) runs out; the work moves to Sahand's account,
where the same sessions are opened again from what is written in this folder.

## Phase 1: force stop (the current coordinator)

1. Send every running session (list: `STATUS.md`, line "Running sessions") exactly this message,
   with `send_message`, priority `now`:

   > FORCE STOP (user order, account handover). Stop now: no new step, no deploy. 1) If you hold
   > `/tmp/geomind-backend.lock` and a deploy is half done, finish only that deploy, else release
   > the lock. 2) Commit and push every repo you touched (stage by path); a change not ready to
   > ship goes on a branch `wip/<your-name>` and is pushed, never left uncommitted in the shared
   > clone. 3) Write your handover note `.claude/notes/sessions/<name>-<n>.md` exactly as
   > `.claude/session-refresh.md` step 2 says (role and full first prompt, state with exact ids and
   > versions, decisions, next steps in order, claimed bugs left `fixing` with where they stand).
   > 4) Commit and push `.claude`. 5) Do NOT start a successor. 6) Reply to the coordinator with
   > one line: note path and commit. Then stop; claim nothing, schedule nothing.

2. Wait for every reply (check with `get_session` / `list_events`; a session that does not answer
   in 10 minutes: interrupt it with `interrupt_session`, then write its note yourself from its
   transcript).
3. Delete this account's scheduled tasks of the coordinator (release summaries :07 and :37, any
   usage check) with `delete_trigger`; their ids are in `STATUS.md`.
4. Write the coordinator's own note `.claude/notes/sessions/coordinator-<n>.md` (role, rules, every
   session and its note, open decisions, deploy and QA rules in force).
5. Fill the table in Phase 2 below (one row per session to reopen, with its note path), update
   `STATUS.md` ("Account handover: stopped at <UTC>; reopen on Sahand's account per
   account-handover.md"), commit, push.
6. Tell the user in Persian: done, which notes, what Sahand pastes (Phase 2).
7. Do not archive the stopped sessions; the user decides.

## Phase 2: reopen on Sahand's account (Sahand, or his first coordinator)

On Sahand's account, in the same project folder on the NTNU Dell (`~/geomind-spe-hackathon-2026`,
already holding every clone): `git pull` in `.claude` and `documents`, then start the coordinator
first, with Opus, and this first prompt:

> You are Coordinator-<next numeral>, the successor of <last coordinator> on Fatemeh's account.
> Read ~/geomind-spe-hackathon-2026/.claude/account-handover.md (Phase 2) and
> ~/geomind-spe-hackathon-2026/.claude/notes/sessions/coordinator-<n>.md and follow them; your
> role's rules and mode are in them, so do not ask the user for the mode. Start now.

The new coordinator then:
1. Reads `STATUS.md`, the memory index, its note.
2. Recreates its scheduled tasks on the new account (release summaries "7 * * * *" and
   "37 * * * *", any usage check) and writes their ids in `STATUS.md`.
3. Starts every session in the table below with `create_session`: environment the Dell bridge (on
   the new account, `list_environments` gives its id), title = the next numeral, model and tags as
   listed, prompt:
   > You are <title>, the successor of <old title> (<old id>, Fatemeh's account). Read
   > ~/geomind-spe-hackathon-2026/.claude/notes/sessions/<note>.md and follow it; your role's rules
   > and mode are in it, so do not ask the user for the mode. The coordinator is <new id>. Start
   > now.
4. Writes every new id in `STATUS.md`, sends Manual QA's successor its own line, and tells the user.

## Sessions to reopen (filled at Phase 1, step 5)

| Old title | Old id | New title | Model | Tags | Note |
|---|---|---|---|---|---|
| (filled at force stop) | | | | | |

Models by rule (`memory/feedback-session-models.md`): coordinator and hotfix-python on Opus
(`claude-opus-5-5`); hotfix-back, hotfix-front, analysis, handbook and QA sessions on Sonnet
(`claude-sonnet-5-5`).

## Rules that travel with the work

Everything in `memory/` holds on the new account unchanged, in particular: hotfix mode; deploy at
once (no :00/:30 windows); Fatemeh's bugs first; only team leads write (IMP-025); no QA tests until
the user lifts it; hand over at 300,000 tokens; agents never on a Claude model.
