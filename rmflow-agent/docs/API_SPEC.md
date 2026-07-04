# API_SPEC

## Current Status

This file defines the intended mock-first API surface. No endpoints are implemented yet.

The only confirmed external integration resource is the CRM Sandbox API:

- Base URL: `https://sandbox.crm.BankA.vn`
- API documentation: available
- Rate limit: 100 requests/minute

## Integration Strategy

- Build local backend endpoints first using mock JSON data.
- Do not call the CRM Sandbox API during this phase.
- Do not assume undocumented sandbox endpoints.
- Do not assume `POST /draft-email` exists unless confirmed in the API documentation.
- Do not assume `POST /call-script` exists unless confirmed in the API documentation.
- Do not assume product knowledge, campaign, or template endpoints exist unless confirmed.
- Frontend must never call the CRM Sandbox API directly.
- AgentService must never call the CRM Sandbox API directly.
- All CRM API access must follow:

```text
AgentService
→ ToolRegistry
→ CRMClient
→ MockCRMClient or SandboxCRMClient
```

## CRM Modes

```text
MOCK_MODE=true   -> use local JSON mock data
MOCK_MODE=false  -> use CRM Sandbox API through SandboxCRMClient
```

If sandbox requests fail, time out, or hit rate limit, the backend should fall back to mock data when possible.

## Standard Agent Response Contract

```json
{
  "summary": "",
  "key_findings": [],
  "recommended_action": "",
  "draft": null,
  "sources": [],
  "tools_called": [],
  "requires_approval": false,
  "risk_flags": [],
  "audit_log_id": "",
  "crm_mode": "mock",
  "fallback_status": "none",
  "latency_ms": 0,
  "context": {
    "session_id": "",
    "rm_id": "",
    "current_customer_id": "",
    "current_module": "",
    "approval_status": "",
    "pending_action": "",
    "last_draft_id": "",
    "last_agent_output_id": ""
  }
}
```

## Planned Endpoints

These are planned local backend endpoints for the RMFlow MVP. They are not assumptions about sandbox endpoints.

- `GET /api/health`
- `GET /api/customers`
- `GET /api/interactions`
- `GET /api/opportunities`
- `GET /api/campaigns`
- `GET /api/products`
- `GET /api/templates`
- `GET /api/audit-logs`
- `POST /api/chat`
- `POST /api/draft-email`
- `POST /api/call-script`
- `POST /api/approve-action`

## Response Rules

- Return structured JSON only.
- Include source IDs whenever business output depends on CRM or KB data.
- Include approval status for customer-facing drafts.
- Include `crm_mode`, `fallback_status`, and latency when relevant.
- Log every tool call and LLM call.

## Request And Response Examples

### `GET /api/health`

Response:

```json
{
  "status": "ok",
  "service": "rmflow-agent-backend",
  "crm_mode": "mock",
  "fallback_status": "none"
}
```

### `GET /api/customers`

Example request:

```text
GET /api/customers?rm_id=RM001
```

Response:

```json
{
  "items": [
    {
      "customer_id": "C001",
      "rm_id": "RM001",
      "anonymized_name": "KH Nguyễn A",
      "segment": "affluent",
      "balance_range": "700M-1B VNĐ",
      "preferred_channel": "phone"
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `GET /api/interactions`

Example request:

```text
GET /api/interactions?customer_id=C001
```

Response:

```json
{
  "items": [
    {
      "interaction_id": "I001",
      "customer_id": "C001",
      "channel": "phone",
      "interaction_type": "deposit_follow_up",
      "sentiment": "positive",
      "next_follow_up_date": "2026-07-05"
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `GET /api/opportunities`

Example request:

```text
GET /api/opportunities?customer_id=C001
```

Response:

```json
{
  "items": [
    {
      "opportunity_id": "O001",
      "customer_id": "C001",
      "product_category": "term_deposit",
      "product_name": "Tiết kiệm 12 tháng linh hoạt Demo",
      "expected_value": 700000000,
      "probability_score": 0.82,
      "status": "open"
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `GET /api/campaigns`

Example request:

```text
GET /api/campaigns?customer_id=C001
```

Response:

```json
{
  "items": [
    {
      "campaign_id": "CAM001",
      "campaign_name": "Summer Savings Boost Demo",
      "product_focus": "term_deposit",
      "eligibility_rule": "affluent customers with idle balance and recent deposit interest"
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `GET /api/products`

Response:

```json
{
  "items": [
    {
      "product_id": "P001",
      "product_name": "Tiết kiệm 12 tháng linh hoạt Demo",
      "product_category": "term_deposit",
      "pricing_note": "Fictional demo term. Not a real Bank A rate."
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `GET /api/templates`

Response:

```json
{
  "items": [
    {
      "template_id": "T001",
      "purpose": "deposit_follow_up_email",
      "product_category": "term_deposit",
      "channel": "email"
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `GET /api/audit-logs`

Response:

```json
{
  "items": [
    {
      "audit_log_id": "A001",
      "session_id": "S001",
      "intent": "daily_prioritization",
      "tools_called": [
        "get_customers",
        "get_interactions",
        "get_opportunities",
        "get_campaigns"
      ],
      "source_ids": [
        "C001",
        "I001",
        "O001",
        "CAM001"
      ],
      "approval_status": "not_required"
    }
  ],
  "total": 1,
  "crm_mode": "mock"
}
```

### `POST /api/chat`

Request:

```json
{
  "session_id": "S001",
  "rm_id": "RM001",
  "message": "Sáng nay tôi nên chăm sóc khách nào trước?"
}
```

Response:

```json
{
  "summary": "KH Nguyễn A nên được ưu tiên trước.",
  "key_findings": [
    "Có lịch follow-up đến hạn từ I001",
    "Có opportunity O001 với expected value cao",
    "Phù hợp campaign CAM001"
  ],
  "recommended_action": "Gọi KH Nguyễn A để chốt nhu cầu tiết kiệm kỳ hạn 12 tháng.",
  "draft": null,
  "sources": ["C001", "I001", "O001", "CAM001"],
  "tools_called": ["get_customers", "get_interactions", "get_opportunities", "get_campaigns"],
  "requires_approval": false,
  "risk_flags": [],
  "audit_log_id": "A001",
  "crm_mode": "mock",
  "fallback_status": "none",
  "latency_ms": 182,
  "context": {
    "session_id": "S001",
    "rm_id": "RM001",
    "current_customer_id": "",
    "current_module": "daily_prioritization",
    "approval_status": "not_required",
    "pending_action": "",
    "last_draft_id": "",
    "last_agent_output_id": "OUT001"
  }
}
```

### `POST /api/draft-email`

Request:

```json
{
  "session_id": "S001",
  "customer_id": "C001",
  "template_id": "T001",
  "draft_body": "Xin chào anh/chị...",
  "approved": true
}
```

Response:

```json
{
  "draft_id": "D001",
  "status": "saved",
  "approval_status": "approved",
  "source_ids": ["C001", "T001"],
  "audit_log_id": "A005"
}
```

### `POST /api/call-script`

Request:

```json
{
  "session_id": "S001",
  "customer_id": "C001",
  "script_id": "SCP001",
  "draft_body": "Em chào anh/chị...",
  "approved": true
}
```

Response:

```json
{
  "draft_id": "D002",
  "status": "saved",
  "approval_status": "approved",
  "source_ids": ["C001", "SCP001"],
  "audit_log_id": "A006"
}
```

### `POST /api/approve-action`

Request:

```json
{
  "session_id": "S001",
  "draft_id": "D002",
  "approval_status": "approved",
  "approved_by": "RM001"
}
```

Response:

```json
{
  "draft_id": "D002",
  "approval_status": "approved",
  "saved": true,
  "audit_log_id": "A007"
}
```

## Audit Log Requirements

Every important action should create an audit log entry with:

```text
session_id
user_query
intent
tools_called
source_ids
crm_mode
fallback_status
latency
approval_status
output_summary
created_at
```

## Sandbox Details Still Requiring Confirmation

The CRM API documentation still needs to confirm:

- authentication method
- exact endpoint list
- request and response schema for each endpoint
- whether draft save endpoints exist
- whether product, campaign, and template endpoints exist
- customer, interaction, and opportunity field names
- rate limit response behavior
- timeout and retry expectations

## Change Control

Do not change API contracts without updating this file first.
