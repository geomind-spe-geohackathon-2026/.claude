# Report: removing the old project name (2026-11-05, hotfix)

Task from the coordinator: the old project name (and its `sx.` alias) must not appear anywhere; it
becomes `geomind` (GeoMind in prose). This note is named without the old name on purpose.

## Renamed (pushed to `main`)

| Repo | Commit | What |
|---|---|---|
| `.claude` | 7294837 | 14 memory and handoff files; `memory/geomind-architecture.md` (the file rename itself went in with d40f71a, another session's commit); `[[...]]` links fixed; old GitHub account URLs dropped |
| `documents` | 699fd72 | `project/design/geomind-system-design-notes.md` (git mv + text), `project/plans/benchmark.md` |
| `backend` | 048f70d | two docs/archive notes, text only |
| `geomind` | 6f4009f | archive phases, handover note, `docs/design/design.md` (also the split string of the old name), text only |
| `frontend`, `infrastructure` | none | no hits |

Lines that described the rename itself were rewritten as "the first package name" / "the old
name", so they don't read "geomind -> geomind".

## Live runtime identifiers

None found. No compose file, `.env`/`.env.example`, CI file, git remote, branch, tag, Docker
container, volume or network on the Dell holds the old name (checked with `docker ps -a`,
`docker volume ls`, `docker network ls`, plus a grep of untracked and ignored files and the
`~/env.*.bak` backups). No migration needed.

## Left, and why

- `gemini` (not edited: gemini changes need Sahand's permission):
  - `gemini/.claude/archive/notes/cleanup-findings.md:3`: names the repo `<old name>/gemini` on GitHub.
  - `gemini/.claude/archive/notes/todo.md:3`: the same repo name.
  Proposed fix (text only, archive): replace with "gemini on an old personal GitHub account".
- External: the old personal GitHub account (it owned the first gemini fork) and the old domain
  still exist outside this project. Renaming them is Sahand's call; no file links to them any more.
- Git history: older commit messages and the commit messages of this task contain the name.
  They can't be changed without rewriting shared history, so they stay.
- Clean: user-level `~/.claude` and the private session memory (`~/.claude/projects/*/memory`), as
  well as `~/geomind-archive`.
