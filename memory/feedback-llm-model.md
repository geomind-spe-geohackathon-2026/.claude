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

**2026-11-04 19:56 UTC (Fatemeh, done):** production and `.env.example` run every role on `nvidia/nemotron-3.5-super-vl:free`; the backend's `ASSISTANT_MODEL_PREFIX` default is that id (backend 1.1.16). DeepSeek is no longer used.

**2026-11-04 20:16 UTC (Fatemeh, done):** back to DeepSeek, as the alias `~deepseek/deepseek-flash-latest` for every OpenRouter model setting (17 roles, `.env.example`, `ASSISTANT_MODEL_PREFIX` default), `GEOMIND_PROVIDER=deepseek`; backend 1.1.21.

**2026-11-04 20:20 UTC (Fatemeh, done, current):** `deepseek/deepseek-v4.1-flash-1017` for every OpenRouter model setting, provider `morph/fp8` (`GEOMIND_PROVIDER=morph/fp8`); backend 1.1.22. Supersedes the two entries above.
