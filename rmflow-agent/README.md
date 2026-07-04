# rmflow-agent

RMFlow Agent is a Vietnamese source-grounded CRM action agent for bank Relationship Managers.

## Current Phase

This repository is scaffolded for Phase 0 only:

- repo structure created
- Trae multi-agent workflow documented
- project rule content prepared
- product and technical document templates prepared
- RMFlow in-product agent documents prepared
- placeholder mock data files created

No backend or frontend business logic is implemented yet.

## Directory Purpose

- `.agent-system/`: prompts and operating workflow for Trae custom agents
- `docs/`: product, technical, API, DB, AI rules, task, debug, review, and demo documents
- `agents/`: RMFlow product agent specification, prompt, tools, memory, guardrails, and evals
- `data/`: mock CRM data files for the MVP
- `backend/`: reserved for FastAPI backend
- `frontend/`: reserved for Next.js frontend

## Sequential Multi-Agent Order

1. Product Agent
2. Architect Agent
3. Backend Agent
4. AI Agent Engineer
5. Frontend Agent
6. Debugger Agent
7. Reviewer Agent
8. Demo/Pitch Agent

## Important Separation

- `.agent-system/` = agent prompts used to build inside Trae
- `agents/` = agent definition files for the RMFlow product itself

## Next Build Step

Use the Architect Agent first and only validate structure, folder purpose, build order, and what to mock before any implementation starts.
