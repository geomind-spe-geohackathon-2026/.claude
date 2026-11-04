---
name: feedback-no-anthropic-models
description: Sahand hard rule 2026-11-02 21:48: never Sonnet/any Anthropic model for geomind agents; DeepSeek everywhere; no model fallback in code
metadata:
  type: feedback
  modified: 2026-11-02T20:49:35.600Z
---

Sahand (2026-11-02 21:48 local, app thread): "never, ever use Sonnet for the agents; put DeepSeek everywhere; check everywhere carefully".
**Why:** dev live tests silently fell back to geomind's FIXED_DEFAULT_MODEL anthropic/claude-sonnet-5.5 (GEOMIND_MODEL unset); cost and model choice must be deepseek.
**How to apply:** every geomind/app prompt: no Anthropic model id as default/fallback anywhere (runtime.py FIXED_DEFAULT_MODEL/FIXED_CHEAP_MODEL, compaction.py context windows, openrouter.py CACHED_MODELS anthropic prefix, docs/tests/samples); models come from settings (prod deepseek/deepseek-v4.1-flash-1017, provider relace/fp4); live run with unset role refuses (no-defaults rule [[feedback-no-defaults]]); check-live fails on anthropic/ ids; grep guard test. Implemented as section M of /mnt/project-files/prompts/geomind-live-run-fixes.md (merged first, pushed alone). Not about Claude Code itself (prompts' subagents still sonnet/haiku for coding).
