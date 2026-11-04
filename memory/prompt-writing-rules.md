---
name: prompt-writing-rules
description: Standing rules for every Claude Code prompt I write for this repo (tests speed, docs update, speak up about needs)
metadata:
  type: feedback
  modified: 2026-10-28T21:45:15.225Z
---

User (2026-10-28 21:44) asked that every future prompt I write for local Claude Code:
- keeps tests fast: new tests go in the right tier/marker, reuse session fixtures and the short-window data fixture, no fast-tier test over ~1 s (see faster-tests.md prompt and .claude/docs/testing.md once it exists);
- updates the docs in `.claude/docs/` (and AGENTS.md "Start here") in the same task, so a new session can read the docs and know the current state;
- and that I proactively tell the user if something else is needed (missing step, dependency, risk) instead of staying silent.
**Why:** test time had grown too long; new sessions must self-orient from docs.
**How to apply:** add a "Tests" and "Docs" phase to every prompt in /mnt/project-files/prompts/; mention needs in the reply. Related: [[package-structure-decisions]].
- 21:47 user: two test datasets — fast (one month, default, local + PR CI) and slow (full year, CI gate for merging to main). Never delete or shrink existing datasets/goldens; only add.
- 21:50 user: all work on ONE branch `dev` (prompt branch-dev.md renames current branch to dev, deletes other branches except main if fully merged). Every prompt: work directly on `dev`, commit there, push origin dev at end, no new branches, no PR. Pending prompts already updated.
- 22:59 user: tests always parallel (-n auto); default verification < 120 s; while working run ONLY relevant tests (scripts/test_changed.py), default pytest before commit, slow tier only in CI. Every future prompt must say: "verify with scripts/test_changed.py while working and default parallel pytest (<120 s) before each commit; never run the slow tier locally". Prompt: parallel-and-targeted-tests.md.
- 23:00 CHANGE: user says work on branch `refactor` (not `dev`). All pending prompts switched to `refactor`. branch-dev.md is obsolete; asked user whether it was already run.
- 23:07 user: don't clutter docs/ with temporary files. Temporary reports (audit lists, baselines, speed notes, scratch) go to `.tmp/` at repo root, which is in .gitignore. Every prompt: write temp outputs to .tmp/, only lasting docs in docs/ or .claude/docs/.
- 23:23 UPDATE (supersedes 22:59): two test profiles. development = default, local, every task/commit: only tests of changed files AND of everything that imports them (transitive, scripts/test_changed.py), parallel, fast dataset, budget < 300 s (not 120). release = CI before merge to main / releases: full suite, slow dataset, parallel. Never run full suite locally. parallel-and-targeted-tests.md was NOT run (obsolete, merged into full-cleanup.md section 2b). Every future prompt must state this rule.
- 23:30 user: code quality is the top goal: fewer bugs, simple, readable, "just enough" code, no pointless indentation, keep all features. Quality bar (in full-cleanup.md §0b, to repeat in future prompts): nesting ≤ 3, functions ~≤ 40 lines, flake8 max-complexity=10, guard clauses, no dead/speculative code, no golfed code, full-word names, comments why, explicit gm.errors, failing test before each bug fix.
- 23:35 user: no "magic" structures; user API simplest possible, package simple+clean with all features; when unsure how to implement, follow torch source patterns (design reference only, never name torch in repo). In full-cleanup.md §0c. GitHub `refactor` still at 96d3443 (16:10) on 2026-10-28 23:35: newer prompt work is local/unpushed.
- 23:34 user: NO comments inside code. Only fixed section-header comments (# Modules, # Parameters, ... # Outlets) and tool directives (# noqa etc.); explanations go in docstrings. Was not in the GitHub docs; full-cleanup.md §0b rule 6 adds it to conventions.md + a tokenize test. Repeat in every prompt.
- 2026-10-29 00:14 user: subagents/subtasks must use lighter models (e.g. sonnet/haiku), not the main model.
- 2026-10-31 18:55 Sahand: we are short of time; every prompt must tell Claude Code to work in parallel as far as safe and finish fast (not 1-2 h per prompt). Pattern used: dependent base section first alone, then parallel sonnet subagents in separate git worktrees on temp branches with disjoint file ownership, main agent merges in section order, targeted tests while working, e2e once, remove worktrees. (Supersedes "subagents read-only only".)
