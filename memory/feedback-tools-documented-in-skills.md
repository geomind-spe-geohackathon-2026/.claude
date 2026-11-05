---
name: feedback-tools-documented-in-skills
description: How to use an agent tool lives in one place only, its skill; tool code may be changed or debugged so tools work better (2026-11-05)
metadata:
  type: feedback
---

User, in Coordinator-III's chat, 2026-11-05 ~10:35 UTC: every agent tool must be introduced to the
agents through the skills, so that how to use a tool is written in exactly one place; no second or
third source (tool docstring, prompt, guide) that explains the same usage differently. The tools
themselves may also be changed, debugged and fixed so they work better. Goal: every tool's
first-try refusal rate below 25 %.

Consequences:
- Each tool belongs to exactly one skill (`tools:` in the SKILL.md frontmatter); the skill holds the
  full usage: arguments, allowed values, units, correct examples, common mistakes.
- The tool's own description (sent with every call by function calling) stays a one-line purpose
  plus the name of its skill; its JSON schema stays exact (names, types, enums, required) but carries
  no usage prose. Prompts name the skill, never re-explain the tool.
- Since a skill reaches a model only when loaded, the agent loop makes sure it is there: the skills
  of a role's tools are given to that role (loaded up front or on the first call of a tool), and a
  refusal points to the skill section.
- A test fails if a tool is in no skill or in two.

**Why:** several sources drift apart and agents get conflicting instructions; refusal rates were
49-82 % on the main tools.
**How to apply:** when changing a tool, change its skill; never add usage text elsewhere.
