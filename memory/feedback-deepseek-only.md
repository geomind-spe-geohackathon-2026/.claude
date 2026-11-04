---
name: feedback-deepseek-only
description: Sahand's rule: NEVER use Sonnet (or any Anthropic model) for geomind agents; DeepSeek everywhere (dev, prod, defaults, tests)
metadata:
  type: feedback
  modified: 2026-11-02T20:48:41.207Z
---

2026-11-02 21:48 (+0100) Sahand: "never, never use Sonnet for the agents; put DeepSeek everywhere; check everywhere exactly."
**Why:** the dev live tests ran the agents on anthropic/claude-sonnet-5.5, because GEOMIND_MODEL was unset on dev and geomind's own default was Sonnet. Only the coordinator step was on deepseek. Prod: deepseek/deepseek-v4.1-flash-1017 via Relace.
**How to apply:** every env (backend .env.dev, .env.production, CI, scripts) sets all geomind model vars to deepseek. The geomind package must not fall back to Sonnet (geomind thread). After any change, verify the model ids in the run logs, not just the env. Related: [[fatemeh-frontend-backend]], [[hosting]].
2026-11-02 21:50 (+0100) Sahand (all threads): NO live LLM runs / no token use for now; only fix bugs. Use mock/scripted mode until he lifts this.
2026-11-02 21:59: prod verified by Hosting: gd.runtime.state() default/coordinator/summarizer = deepseek, provider relace/fp4; backend e33a790 adds ASSISTANT_MODEL_PREFIX=deepseek/ guard (refuses other models). geomind runtime.py:15-16 Sonnet/Haiku defaults removed in 0.4.2.
