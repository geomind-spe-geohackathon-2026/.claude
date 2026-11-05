---
name: feedback-qa-through-chat
description: QA sessions test the product through the chat as far as possible: every stage is asked for in the chat, forms only when the chat cannot do it (2026-11-05)
metadata:
  type: feedback
---

User, in Coordinator-III's chat, 2026-11-05 ~10:20 UTC: QA sessions must test the product from the
chat as far as possible. The tester asks in the chat, as a user would: "set up the case from these
files", "design a plant", "simulate it", "run a study", "compare", "economics", "write the report".
Approvals and answers to the agents' questions go through the chat (question cards) too. Forms and
tabs (Case, Plant, Study, Results, Report) are used only to check what the chat produced, or when the
chat truly cannot do a step; then that gap is itself reported (improvement or bug).

**Why:** the product is agent-first; users drive everything from the chat, so that path must work.
**How to apply:** every QA brief and scenario drives each stage by a chat request; a scenario that
needs a form for an action is rewritten as a chat request, and a missing chat path is filed.
