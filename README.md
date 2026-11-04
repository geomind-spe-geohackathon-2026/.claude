# .claude: what agents read

`.claude/` holds what agents and Claude Code sessions read; people read `documents/` beside it
(project-wide) and each repo's `docs/`. This `.claude/` is the project-wide one, the repo `.claude`;
every code repo has its own `.claude/` with the same layout. Start with `AGENTS.md` here, then
`STATUS.md`. A new machine: `setup.md`.

| Folder | Holds | When to read |
|---|---|---|
| `STATUS.md` | Project root only. The short current state: production, clones, how we work now, open decisions. | First, every session; update it the moment any of it changes. |
| `memory/` | Project root only. The shared memory: standing rules (`feedback-*.md`), decisions and facts, one per file, indexed in `memory/MEMORY.md`. | At the start of every session. |
| `docs/` | Repos only. Reference for working on the code: API, conventions, testing, structure. | Before changing that repo. |
| `notes/` | Current work: briefs, status, handoffs between threads and sessions. | When you take over that work. |
| `archive/` | Finished work: task prompts (`archive/prompts/`), phase prompts (`archive/phases/`), old notes (`archive/notes/`). | Only when the history of a decision matters. |
| `handoff/` | Project root only. The handoff pack of 2026-11-04 and `path-map.md` (old `/mnt/project-files/...` paths to where the files are now). | When an old path or decision is unclear. |

## Naming

- File and folder names: lowercase, words joined by `-` (`status-2026-11-04.md`).
- A snapshot of a moment ends in its date, `-YYYY-MM-DD`; a living file has no date.
- One subject per file. Move a finished note to `archive/notes/`; never delete history.
- A fact every session needs goes in `memory/` (one file, one line in `MEMORY.md`), not in a note.
