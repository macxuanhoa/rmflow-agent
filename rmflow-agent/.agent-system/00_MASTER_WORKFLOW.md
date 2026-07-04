# RMFlow Trae Master Workflow

## Purpose

This folder manages the Trae custom agents used to build RMFlow.

Important:

- `.agent-system/` is for agents used inside Trae
- `agents/` is for the RMFlow product agent inside the application

## Sequential Multi-Agent Order

1. Product Agent
2. Architect Agent
3. Backend Agent
4. AI Agent Engineer
5. Frontend Agent
6. Debugger Agent
7. Reviewer Agent
8. Demo/Pitch Agent

Do not use one generic agent for all phases.

## Trae Project Rule

Project rule name:

`RMFlow Project Rule`

Project rule content:

```text
You are working on RMFlow Agent, a Vietnamese source-grounded CRM action agent for bank Relationship Managers.

Always read these files before making major changes:
- docs/PRODUCT_SPEC.md
- docs/TECH_SPEC.md
- docs/API_SPEC.md
- docs/AI_RULES.md
- agents/RMFLOW_AGENT_SPEC.md
- agents/RMFLOW_AGENT_GUARDRAILS.md

General rules:
- Do not rewrite unrelated files.
- Do not change API contracts without updating docs/API_SPEC.md first.
- Do not change database schema without updating docs/DB_SCHEMA.md first.
- Keep changes small and reviewable.
- Prefer mock data first, real integration later.
- Every generated customer-facing output must require human approval.
- Never auto-send customer messages.
- Never invent customer data, product terms, campaign eligibility, or interest rates.
- Every agent answer must include internal source IDs when possible.
- Every tool call and LLM call must be logged.

Architecture rules:
- Frontend: Next.js + React + Tailwind.
- Backend: FastAPI.
- Agent orchestration: custom state machine first, LangGraph optional later.
- Mock CRM API first.
- Product KB: JSON keyword search first, vector DB later.
- Audit log must be visible in UI, not hidden only in backend.

Development rules:
- Before coding, list affected files and plan.
- After coding, list changed files and how to test.
- If debugging, rank possible root causes and fix the smallest issue first.
- If uncertain, ask or make the safest assumption and state it clearly.
```

## Phase Order

1. Setup repo
2. Mock data
3. Backend skeleton
4. Agent context state
5. Tool registry
6. Rule-based agent MVP
7. Draft email and call script
8. Approval workflow
9. Frontend UI
10. Visible audit log
11. LLM integration only after rule-based logic works

## Daily Task Template

```md
## Task
[One task only]

## Context
[Why this task matters]

## Files allowed to modify
[...]

## Do not touch
[...]

## Acceptance Criteria
- ...
- ...
- ...

## Test Checklist
- ...
- ...

## Instruction
Read docs/AI_RULES.md and relevant /agents files first.
Before coding, list affected files and implementation plan.
After coding, explain how to test.
```
