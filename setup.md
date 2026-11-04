# Set up the project root on a machine

The project root (`geomind-spe-hackathon-2026/`) is a plain folder of clones. Clone them side by
side, then write the three small root files that point into `.claude` and `documents`.

```sh
mkdir -p ~/geomind-spe-hackathon-2026 && cd ~/geomind-spe-hackathon-2026
for r in .claude documents backend frontend geomind gemini infrastructure; do
  git clone git@github.com:geomind-spe-geohackathon-2026/$r.git "$r"
done
git -C gemini switch dev   # gemini's default branch is dev
printf '@.claude/AGENTS.md\n' > CLAUDE.md
printf '# GeoMind project\n\nAgents: read `.claude/AGENTS.md`. People: read `documents/README.md`.\n' > AGENTS.md
printf '# GeoMind\n\nPeople: start with `documents/README.md`. Agents: `.claude/AGENTS.md`.\n' > README.md
```

`CLAUDE.md` in the root loads the project guide into every Claude Code session opened in the root
or in any clone under it.
