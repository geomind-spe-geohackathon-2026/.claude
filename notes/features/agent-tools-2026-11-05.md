# Feature: skills folder and three agent tools (Sahand, 2026-11-05 ~00:00 UTC)

Built now, in HOTFIX mode (decided: features go in hotfix mode; release and deploy without asking).
Owners: hotfix-python (geomind), hotfix-back (backend, infrastructure), hotfix-front (frontend).
The coordinator (see `.claude/STATUS.md`) tracks it; each session reports each step in one line.
Shared rules hold: no default values (a missing setting is an error naming it), every value an
agent uses has a source, APIs given out do not change (add, never rename), gemini does all unit
conversions, the geomind agents never use a Claude model.

## 1. Skills folder: `geomind/geomind/skills/` (hotfix-python)

- One folder per skill: `skills/<name>/SKILL.md`, optional extra files beside it (examples,
  reference tables) the skill links to.
- `SKILL.md` starts with frontmatter: `name`, `description` (one line; this is what the system
  prompt lists), `tools` (the tools it explains), `roles` (`<team>/<name>` of the agents that see
  it, or `all`). The body is the how-to.
- Each agent's system prompt lists only the skills of its roles; `read_skill(name)` keeps its name
  and signature, and refuses (with the list) a skill the role does not have.
- Move the three skills of `prompts/skills/` (`designing-a-plant`, `gemini-units`,
  `reading-results`) into the new folder under the same names; old names keep working.
- A tool's error points at its skill ("read_skill('calculator') for the rules").
- New skills, first round: `calculator`, `python`, `web-search`, `knowledge` (RAG), `connectors`
  (MCP), `asking-the-user` (approvals with source, labelled assumptions), `setting-the-case`,
  `gemini-check`, `simulation`, `economics`, `report`. Take the how-to out of the role prompts
  into these skills; the role prompts keep the role, its duties and its limits. Do this last,
  step by step, so behaviour does not change by accident.

## 2. `calculate` (hotfix-python; frontend shows it)

- The agent never types a number. Operands are references to sourced values: a case field path,
  a catalogue row (Knowledge), a user-approved value, a stored result (with its reference and
  field), or an earlier calculation's id.
- Operations: add, subtract, multiply, divide, power, min, max, sum, mean; units go through gemini
  (quantities in, quantity out; no hand-written 24 or 1000).
- A bare literal is refused with a clear error; the one exception is the integer exponent of `power`
  (Sahand, 2026-11-05).
- The result is stored as a derived value: id, value, unit, expression, and the chain of sources
  of every operand. Later tools and the report can cite it by id.
- effect `compute`.

## 3. `run_python` (hotfix-python, hotfix-back; frontend shows it)

- geomind had a Docker sandbox until 0.4.21; backend `runs/adapters/session.py::build_sandbox`
  still passes `gd.sandbox.DockerSandbox()` when geomind has one, and the image
  `gemini-sandbox:<gemini version>` (gemini installed) exists. Bring it back.
- No network; limits from settings (`sandbox_timeout`, `sandbox_memory`, `sandbox_disk`,
  `sandbox_cpu` already in `runtime.py`; missing = error); project files read-only.
- Numeric inputs come only as named references to sourced values (as in `calculate`), injected as
  variables; the code itself may hold no data literals the agent made up (structural constants
  such as indices are fine; say in the skill what is allowed).
- Stored with the run: code, inputs with sources, stdout, stderr, output files, exit status,
  time. Its numbers are derived values citing the code.
- effect `execute`. hotfix-back: make the prod worker able to start the sandbox container (Docker
  access, image present for gemini 0.6.5), set `ASSISTANT_SANDBOX=docker` and the limits in prod
  `.env` (Sahand runs prod `.env` edits if the deploy cannot; give him the exact lines).

## 4. `web_search` and `read_web_page` (hotfix-python, hotfix-back; frontend shows it)

- Search backend: SearXNG, self-hosted on the Dell (hotfix-back): `infrastructure/searxng/`
  with its own compose and `.env`, like the other services; JSON output enabled; reachable only
  from the backend's network, never public. Setting `GEOMIND_SEARCH_URL` (missing = the tools are
  not offered, and asking for them is an error naming the setting).
- `web_search(query, limit)`: results with title, URL, snippet, engine, date if known.
- `read_web_page(url)`: the main text of one page (no scripts, no clicking), with URL, title,
  publisher, date; size-capped; HTML only plus PDF text if easy. effect `external`.
- Any value taken from the web goes to the user for approval with its source (URL, publisher,
  year, currency year), exactly like Knowledge and connector values; then it is a sourced value
  `calculate` and `run_python` can use.
- The backend may swap SearXNG for a paid API later behind the same tools.

## 5. Frontend (hotfix-front)

- Chat shows a calculation as the expression with each operand's source (links), and the result.
- Chat shows a code run as collapsible code, inputs with sources, output, and status.
- Chat shows search results and read pages as source cards (title, publisher, date, link); web
  values in approval cards show their link.
- Wait for the tool result shapes from hotfix-python before building; ask the coordinator.

## Order

1. hotfix-python: the skills folder (step 1 without the prompt slimming) and `calculate`;
   release, deploy. hotfix-back in parallel: SearXNG service and the sandbox on the worker.
2. hotfix-python: `run_python`, then `web_search`/`read_web_page`; tell the coordinator each
   result shape; hotfix-front builds the views.
3. hotfix-python: move the how-to from role prompts into skills.
4. The QA sessions test the new tools (the coordinator adds them to their briefs).

## 6. Busy indicator next to the agent name (hotfix-front; Sahand 2026-11-05 ~00:05 UTC)

While an agent is working, the chat shows an animated indicator (spinning circle or pulsing
dots) to the left of that agent's name; it goes away when the agent's turn ends, waits for an
approval, or fails. Each working agent has its own, nested agents too. Stock shadcn/lucide;
respect prefers-reduced-motion. Independent of sections 1-5; ship at once.

Addition (Sahand ~00:10 UTC): to the RIGHT of the working agent's name, one short line of what
it is doing now, replaced by the next as each step ends. Source: the current tool call mapped to
a short phrase per tool ("Reading the case", "Running the simulation", "Searching the web for
<query>"); no tool running = "Thinking"; an unknown tool shows its name humanised. One line,
truncated with an ellipsis, full text in a tooltip; muted; no layout jump.

Decided (Sahand 2026-11-05 ~00:20 UTC): `calculate` allows exactly one plain number, the integer
exponent of `power`; it is structural, not data.

Changed (Sahand 2026-11-05 ~00:25 UTC): `calculate` takes named constants (`pi`, `e`; kind
`constant`) and plain numbers with a unit (kind `number`, shown as plain in the expression), but
every calculation needs at least one sourced operand (case, assumption, catalogue, stored,
calculation); constants do not count. This replaces "a bare literal is refused" above.
