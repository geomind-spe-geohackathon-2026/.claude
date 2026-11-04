# hotfix-python-1 handover (2026-11-05 ~00:00 UTC)

You are hotfix-python-II, the successor of hotfix-python (session_01J2V3UVLj3VrnUPsEatss4J).

## Role and mode

Mode: HOTFIX (decided; do not ask the user). You fix the QA bugs of the Python packages geomind
and gemini and build the geomind parts of the agent-tools feature. The coordinator is the one in
`.claude/STATUS.md` (Coordinator-II, session_01J2V3UXD6UT73meeapsG2MS at handover); send it one
line per fix or deploy with the `send_message` tool of the Claude Code Remote MCP server.

Read first: `.claude/AGENTS.md`, `.claude/STATUS.md`, `.claude/memory/MEMORY.md` (and
`memory/feedback-decisions-2026-11-05.md`), `documents/project/ops/development-modes.md`
("Hotfix, step by step"), `documents/project/quality-assurance/README.md`, `geomind/AGENTS.md`,
`gemini/AGENTS.md`.

### The bug loop (from the first brief)

1. Claim: `python3 ~/geomind-spe-hackathon-2026/documents/project/quality-assurance/qa.py next
   --area geomind,gemini --fixer hotfix-python` (or `qa.py claim QA-nnn --fixer hotfix-python`).
   Never edit BUGS.md by hand. Use `qa.py set ... --area backend` to move a bug to another area.
2. 50/50 rule: what can be fixed as well in the backend or frontend goes there.
3. Fix on the default branch: geomind `main`, gemini `dev` (push gemini only to dev). No tests,
   no lint. Raise the patch version (geomind: pyproject.toml and geomind/__init__.py
   `__version__`; gemini: pyproject.toml only), a CHANGELOG line (`docs/CHANGELOG.md` in both)
   with the bug id, commit "QA-nnn: <title>", stage by path, push, tag `v<version>`, push the tag.
   Commit and push at once; never leave a shared clone dirty.
4. Deploy (backend lock):
   `until mkdir /tmp/geomind-backend.lock 2>/dev/null; do sleep 20; done; echo "hotfix-python-II QA-nnn" > /tmp/geomind-backend.lock/owner`;
   in `backend/`: `git pull -q --rebase origin main`; remove the package's old wheel from
   `.tmp/hotfix-wheels/`; `nice .venv/bin/python -m pip wheel -q --no-deps -w .tmp/hotfix-wheels ../geomind`
   (and `../gemini` for gemini); raise the backend patch in `src/version.py`, `CHANGELOG.md`
   (a section naming the bug and the local wheel), `docs/app-build/contracts.md` line 3 and the
   `"version"` line of `openapi.json` (find its line with grep; it moves); commit
   "QA-nnn: <package> <version> (local wheel)", push main. Then deploy with TWO separate Bash
   calls, exactly: `cd /home/fatemec/geomind-spe-hackathon-2026/backend`, then
   `scripts/hotfix_deploy.sh` (no `&&`, no pipe: the allow rule matches only that). Free the lock
   with `rm /tmp/geomind-backend.lock/owner && rmdir /tmp/geomind-backend.lock`.
   The script prints health and `geomind X gemini Y`: check your versions.
5. `qa.py set QA-nnn --status fixed --note "<package> <version>, backend <version>, commit, deployed"`.
6. Check in the prod worker only with `sg docker -c "docker exec geomind-celery python -c '...'"`
   one-liners (running a copied script in the container and reading the prod DB were refused).

Rules learned: every file in English; no secrets in files; keep CPU low (`nice`); no QA ids in
prompt texts or model-facing tool messages (QA-054); geomind converts no units (gemini does);
avoid `rm -rf` in commands (refused); Sahand allowed gemini edits for this round in the old
session's own chat (2026-11-05): gemini on `dev`, release, deploy.

## State at handover

Production: backend 1.1.54 (main dfc685c), geomind 0.4.55 (main c3b167c, tag v0.4.55),
gemini 0.6.5 (dev b20c2964, tag v0.6.5). Local wheels in `backend/.tmp/hotfix-wheels/`:
geomind-0.4.55, gemini_geothermal_suite_open-0.6.5. hotfix-back owns geomind's catalogue data
(it released 0.4.52); always pull before a bump.

Fixed this round (all deployed, most not yet retested live): QA-002, 004, 009, 010, 011, 012,
013 (IMP-001: ask_economics fills recommended rows), 014, 015, 016, 018, 020, 023, 026, 034,
037 (set_case precheck before approval), 039, 041, 042, 043, 045, 047 (part), 050, 052, 054, 055.
Moved: QA-032, QA-049 to backend.

Open for you:
- gemini request 35 (ESP out_of_range should name the flow range): left, geomind covers it with
  `runs.curve_ranges`; a cheap way would compute the range only when the check fails.
- QA-047 second part: keep half-done engineer/geoscientist work across a cancel or interrupt
  (a work-in-progress record in the problem state). Sahand wants it built in hotfix mode.
- The agent-tools feature below.

## Next: the agent-tools feature (Sahand's OK to build, release and deploy)

Spec: `.claude/notes/features/agent-tools-2026-11-05.md`. Open QA bugs in geomind/gemini come
first. Order for you:
1. Skills folder `geomind/geomind/skills/<name>/SKILL.md` (frontmatter name, description, tools,
   roles), the system prompt lists only a role's skills, `read_skill(name)` keeps its signature;
   move `prompts/skills/` (designing-a-plant, gemini-units, reading-results) there, old names
   still work. Then the `calculate` tool (operands are references to sourced values only;
   units through gemini; result stored as a derived value with id and source chain; effect
   compute). Release, deploy, one line to the coordinator, and send it the result shape of
   `calculate` for hotfix-front.
2. `run_python` (bring back `gd.sandbox.DockerSandbox`, removed after 0.4.21; the backend's
   `runs/adapters/session.py::build_sandbox` already passes it when it exists; image
   `gemini-sandbox:<gemini version>`; limits from runtime settings, missing = error), then
   `web_search` / `read_web_page` (SearXNG at `GEOMIND_SEARCH_URL`; unset = tools not offered).
   Send each result shape to the coordinator as soon as it is fixed.
3. Last: move the how-to from the role prompts into skills, step by step.

Check your context with `get_session` (no id) at the start of each piece; at 75 % follow
`.claude/session-refresh.md` (your successor is hotfix-python-III).

## Open question from the coordinator (answer it first)

hotfix-back proposes these settings for run_python and search; reply to the coordinator in one
line, OK or the names/formats geomind needs (check `geomind/runtime.py`, which lists the sandbox
settings as removed: bring them back): `ASSISTANT_SANDBOX=docker`,
`GEOMIND_SANDBOX_IMAGE=gemini-sandbox:0.6.5`, `GEOMIND_SANDBOX_TIMEOUT=60s`,
`GEOMIND_SANDBOX_MEMORY=1g`, `GEOMIND_SANDBOX_DISK=256m`, `GEOMIND_SANDBOX_CPU=1`,
`GEOMIND_SEARCH_URL=http://searxng:8080`.
