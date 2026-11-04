---
name: feedback-llm-model
description: Sahand rule 2026-11-02: never use Sonnet (or any Claude model) for geomind agents; DeepSeek everywhere, set explicitly
metadata:
  type: feedback
---

Sahand (2026-11-02 20:48, "never, never"): never use Sonnet for the agents; use deepseek/deepseek-v4.1-flash-1017 via OpenRouter provider relace/fp4 everywhere (prod, dev, evals, live runs), and check every place carefully.
**Why:** dev silently fell back to Sonnet because geomind's FIXED_DEFAULT_MODEL is anthropic/claude-sonnet-5.5 when GEOMIND_MODEL is unset (and FIXED_CHEAP_MODEL is Claude Haiku).
**How to apply:** always set GEOMIND_MODEL, GEOMIND_CHEAP_MODEL (geomind >=0.4.1) and GEOMIND_PROVIDER=relace/fp4 explicitly in every env file (backend .env.production, .env.dev, templates); verify inside containers with gd.runtime.state(); never rely on geomind's built-in fallbacks. Related: [[hosting]], [[feedback-no-defaults]].
2026-11-02 20:50 Sahand: for now NO live agent runs and NO LLM token use anywhere (only bug fixes); post-deploy smoke tests must not call the model.
