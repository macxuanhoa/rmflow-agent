# TECH_SPEC

## Source Mapping From Brainstorm

This technical specification is derived from the following brainstorm sections:

- G. Technical Architecture
- H. Data and Mock Data Design

***

## G. Technical Architecture

### Target Stack

- Frontend: Next.js + React + Tailwind
- Backend: FastAPI
- Agent orchestration: custom state machine first
- Context management: MCP-style session state
- Retrieval: JSON keyword search first
- Data source: local mock CRM data first
- External integration: CRM Sandbox API later through CRMClient abstraction
- Safety: human approval gate plus visible audit log
- Demo reliability: mock-first with optional sandbox mode

### Architecture Principle

RMFlow should be built as a mock-first, sandbox-ready system.

The MVP must work reliably using local mock CRM data before connecting to the CRM Sandbox API. Sandbox integration should be added only through a clean abstraction layer, so the application can switch between mock data and sandbox data without changing AgentService, ToolRegistry, or frontend logic.

The CRM integration path must follow this flow:

```text
AgentService
→ ToolRegistry
→ CRMClient
→ MockCRMClient or SandboxCRMClient
```

The frontend must never call the CRM Sandbox API directly.

AgentService must never call the CRM Sandbox API directly.

### CRM Integration Strategy

The CRM Sandbox API is the confirmed external integration resource.

- Base URL: `https://sandbox.crm.BankA.vn`
- API documentation: available
- Rate limit: 100 requests/minute

The backend must not call the CRM Sandbox API directly from controllers or AgentService. All CRM access must go through a CRM client abstraction.

Required CRM client structure:

```
CRMClient
├── MockCRMClient
└── SandboxCRMClient

```

`MockCRMClient` should read from local JSON files.

`SandboxCRMClient` should call the CRM Sandbox API only after the API documentation confirms the required endpoints, authentication method, request format, and response schema.

The application must support:

```
MOCK_MODE=true
CRM_SANDBOX_BASE_URL=https://sandbox.crm.BankA.vn
CRM_API_KEY=

```

When `MOCK_MODE=true`, the system uses local JSON mock data.

When `MOCK_MODE=false`, the system uses the CRM Sandbox API through `SandboxCRMClient`.

If the sandbox API fails, times out, or hits the rate limit, the system should fall back to mock mode when possible and show a visible `Demo fallback mode` indicator in the UI.

### API Usage Rules

- Do not assume undocumented CRM endpoints.
- Do not assume `POST /draft-email` exists unless confirmed in the CRM API docs.
- Do not assume `POST /call-script` exists unless confirmed in the CRM API docs.
- Do not assume product knowledge, campaign, or template APIs exist unless confirmed.
- Do not expose CRM API keys to the frontend.
- Do not call the sandbox API directly from the frontend.
- Do not call the sandbox API directly from AgentService.
- Do not hard-code sandbox URLs inside business logic.
- Respect the rate limit: 100 requests/minute.
- Log every sandbox request, response status, latency, and fallback event.
- Keep mock data schema close to expected sandbox API fields.

### Future Backend Structure Reference

This structure should be used later in Phase 3 onward. Do not implement it during docs-only updates.

```text
backend/app/
├── clients/
│   ├── crm_client_base.py
│   ├── mock_crm_client.py
│   └── sandbox_crm_client.py
├── tools/
│   ├── customer_tools.py
│   ├── interaction_tools.py
│   ├── opportunity_tools.py
│   ├── campaign_tools.py
│   ├── product_tools.py
│   ├── template_tools.py
│   ├── draft_tools.py
│   └── audit_tools.py
├── services/
│   ├── agent_service.py
│   ├── context_manager.py
│   └── audit_service.py
└── api/
    ├── health.py
    ├── chat.py
    ├── customers.py
    ├── interactions.py
    ├── opportunities.py
    ├── campaigns.py
    ├── products.py
    ├── templates.py
    ├── drafts.py
    ├── approvals.py
    └── audit_logs.py
```

### Updated Build Roadmap

```text
Phase 0: Scaffold repo
Status: Done

Phase 0.5: Add CRM Sandbox API strategy
Goal: Update docs for mock-first, sandbox-ready architecture

Phase 1: Mock CRM data
Goal: Create realistic JSON data that can map to sandbox API later

Phase 2: Local FastAPI mock API
Goal: Backend reads local JSON data and exposes CRM-like endpoints

Phase 3: CRMClient abstraction
Goal: Add MockCRMClient and SandboxCRMClient structure

Phase 4: ToolRegistry
Goal: Tools call CRMClient, not raw JSON or sandbox API directly

Phase 5: ContextManager
Goal: Keep current_customer_id, current_module, active_context, retrieved_sources, pending_action, approval_status

Phase 6: Rule-based AgentService
Goal: Support prioritization, customer summary, campaign match, next-best action

Phase 7: Draft generation
Goal: Generate email/call script from grounded context and templates

Phase 8: Approval workflow
Goal: Require human approval before saving drafts

Phase 9: Frontend UI
Goal: Show chat, context panel, tool trace, source chips, draft preview, approval buttons, audit log

Phase 10: Optional sandbox switch
Goal: Switch from MockCRMClient to SandboxCRMClient only after API docs confirm required endpoints
```

***

## H. Data and Mock Data Design

### Expected Mock Data Files

The MVP should start with local JSON mock data.

Required files:

```
data/customers.json
data/interactions.json
data/opportunities.json
data/campaigns.json
data/products.json
data/email_templates.json
data/call_scripts.json

```

### Minimum Demo Data Requirements

The mock data must include at least 3 hero customer scenarios:

1. High-value savings follow-up customer
2. Loan follow-up customer
3. Campaign-eligible customer

Every record must have stable source IDs so the agent can cite evidence in its answer.

Required ID fields:

```
customer_id
interaction_id
opportunity_id
campaign_id
product_id
template_id

```

The mock data must support these demo questions:

```
Sáng nay tôi nên chăm sóc khách nào trước?

Tại sao khách này được ưu tiên?

Khách này phù hợp campaign nào và nên đề xuất gì?

Tạo cho tôi call script ngắn để gọi khách này.

Tạo email follow-up cho khách này.

```

### Required Data Fields

`customers.json` should include:

```
customer_id
rm_id
anonymized_name
segment
age_range
city
products_owned
balance_range
risk_profile
preferred_channel
relationship_manager_id

```

`interactions.json` should include:

```
interaction_id
customer_id
date
channel
interaction_type
rm_note
outcome
sentiment
next_follow_up_date

```

`opportunities.json` should include:

```
opportunity_id
customer_id
product_category
product_name
probability_score
expected_value
reason
next_action
status

```

`campaigns.json` should include:

```
campaign_id
campaign_name
target_segment
product_focus
start_date
end_date
eligibility_rule

```

`products.json` should include:

```
product_id
product_name
product_category
eligibility
rate_or_fee
suitable_profile
risk_notes

```

`email_templates.json` should include:

```
template_id
purpose
product_category
tone
required_fields
template_text

```

`call_scripts.json` should include:

```
script_id
purpose
product_category
opening
questions
objection_handling
closing

```

### Mock Data Design Rules

The mock data should be designed to map cleanly to the CRM Sandbox API later.

Rules:

- Use anonymized Vietnamese customer aliases only.
- Do not include real personal data.
- Do not invent real bank product rates unless clearly marked as mock/demo data.
- Use realistic but fictional customer scenarios.
- Make every recommendation traceable to source IDs.
- Keep data small enough for demo reliability.
- Prefer 3 strong demo customers over many shallow records.

### Future Sandbox Mapping

When CRM Sandbox API details are confirmed, map local mock files to sandbox endpoints.

Expected mapping:

```
customers.json       → GET assigned customers / customer profile endpoint
interactions.json    → GET interaction history endpoint
opportunities.json   → GET open opportunities endpoint
campaigns.json       → GET active campaigns endpoint, if available
products.json        → product knowledge endpoint or internal mock KB
email_templates.json → template endpoint or local template library
call_scripts.json    → template endpoint or local script library

```

If the sandbox API does not provide product, campaign, or template endpoints, keep those as local knowledge files for MVP.

### Data Priority Scoring Support

The mock data must support transparent next-best-action scoring.

Suggested scoring factors:

```
due follow-up date
opportunity expected value
opportunity probability score
campaign match
customer sentiment
risk profile

```

The agent should be able to explain priority using evidence, for example:

```
KH Nguyễn A được ưu tiên vì:
- Có lịch follow-up đến hạn từ interaction I001
- Có opportunity O001 với expected value cao
- Phù hợp campaign CAM001
- Từng thể hiện sentiment positive trong lần trao đổi gần nhất

```

### Data Output Requirement

Every agent response should be able to return:

```
summary
key_findings
recommended_action
sources
tools_called
requires_approval
risk_flags
audit_log_id

```
