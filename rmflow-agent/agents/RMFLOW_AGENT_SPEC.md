# RMFLOW_AGENT_SPEC

## A. Final Sharpened Idea

RMFlow Agent is a Vietnamese source-grounded CRM action agent for bank Relationship Managers.

Its job is to help the RM move from question to approved customer action using grounded internal data only.

The MVP is intentionally narrow:

- daily prioritization
- customer summary
- opportunity and campaign match
- next-best action
- email or call script draft
- approval
- audit log

## D. Future AI-Agent Workflow

### End-to-End Workflow

1. User submits a Vietnamese query.
2. Router detects intent only.
3. Orchestrator decides which tools to call.
4. Tools retrieve mock CRM, product, campaign, and template data.
5. Context state is updated with customer and workflow references.
6. Prompt Builder combines:
   - CRM API or mock results
   - product KB or template retrieval results
   - conversation context
   - retrieved source IDs
7. LLM generates the final answer only from retrieved data.
8. If the output is a customer-facing draft, `requires_approval` must be `true`.
9. A save action is blocked until approval is confirmed.
10. Audit log is created for every important action.

### Intent Scope

- `daily_prioritization`
- `customer_summary`
- `campaign_match`
- `next_best_action`
- `generate_email`
- `generate_call_script`
- `approve_draft`

## E. Agentic Behavior Proof

The product must visibly show:

- tool trace
- source IDs
- approval status
- audit log
- context state

The router must not generate final answers.

The orchestrator must not invent data. It only decides which tools to call based on intent and context.

The final answer must be grounded in retrieved data only.

## F. MVP Scope

### Included

- mock-first workflow using local JSON
- explainable prioritization
- grounded next-best-action recommendation
- professional Vietnamese draft generation
- approval gate before save
- visible audit log

### Excluded

- direct sandbox CRM usage
- direct frontend CRM access
- real email sending
- autonomous action without approval
- vector database
- LangGraph
- full MCP server

## R. Revised Final Version

RMFlow Agent should be built as a layered, auditable action system.

### Agent Architecture

```text
User Query
→ Router
→ Orchestrator
→ ToolRegistry
→ CRMClient / Product KB / Template Retrieval
→ Prompt Builder
→ LLM
→ Structured Response
→ Approval Gate if needed
→ Audit Log
```

### Component Responsibilities

- `Router`: detect intent only, never generate final answers
- `Orchestrator`: choose tools based on intent, context, and approval state
- `ToolRegistry`: expose normalized business tools with source IDs
- `CRMClient`: abstract data access through `MockCRMClient` first and `SandboxCRMClient` later
- `Prompt Builder`: merge retrieved facts, sources, and context into a grounded prompt
- `LLM`: generate final language only from retrieved facts
- `Approval Workflow`: required before saving any email or call script
- `Audit Log`: record every important action

### Non-Negotiable Rules

- never invent customer, product, campaign, or pricing facts
- if source data is missing, say it is missing
- always include source IDs when available
- no auto-send
- no save without approval for customer-facing drafts
