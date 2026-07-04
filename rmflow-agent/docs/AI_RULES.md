# AI_RULES

## Resource Usage Rules

### Confirmed Resource: CRM Sandbox API

The only confirmed external integration resource is the CRM Sandbox API.

- Base URL: `https://sandbox.crm.BankA.vn`
- API documentation: available
- Rate limit: 100 requests/minute

## CRM Sandbox API Rules

- Do not integrate the CRM Sandbox API before mock CRM data and local backend endpoints work.
- Do not assume undocumented endpoints.
- Do not assume `POST /draft-email` exists unless confirmed in the API documentation.
- Do not assume `POST /call-script` exists unless confirmed in the API documentation.
- Do not assume product knowledge, campaign, or template APIs exist unless confirmed.
- Never expose CRM API keys to the frontend.
- Never call the sandbox API directly from the frontend.
- Never call the sandbox API directly from AgentService.
- All CRM API access must go through this path:

```text
AgentService
→ ToolRegistry
→ CRMClient
→ MockCRMClient or SandboxCRMClient
```

## CRMClient Strategy

The backend must support a CRM client abstraction:

```text
CRMClient
├── MockCRMClient
└── SandboxCRMClient
```

`MockCRMClient` reads from local JSON files.

`SandboxCRMClient` calls the CRM Sandbox API only after authentication method, endpoint list, request format, and response schema are confirmed from the API documentation.

The application must support:

```text
MOCK_MODE=true
CRM_SANDBOX_BASE_URL=https://sandbox.crm.BankA.vn
CRM_API_KEY=
```

When `MOCK_MODE=true`, the app uses local JSON mock data.

When `MOCK_MODE=false`, the app uses the CRM Sandbox API through `SandboxCRMClient`.

## Fallback Rules

- If the sandbox API fails, times out, or hits rate limit, the backend should fall back to mock data when possible.
- The UI must visibly show `Demo fallback mode` if fallback is active.
- All fallback events must be logged in the audit log.

## Rate Limit Rules

- Respect the CRM Sandbox API rate limit: 100 requests/minute.
- Avoid unnecessary repeated API calls.
- Prefer batching or caching when possible.
- Log request latency and response status for sandbox calls.
- Do not run stress tests against the sandbox API during demo preparation.

## Mock-first Rule

Build order must be:

```text
Mock data
→ Local mock API
→ CRMClient abstraction
→ ToolRegistry
→ ContextManager
→ AgentService
→ Frontend
→ Optional sandbox switch
```

Do not reverse this order.

## Data Grounding Rules

- Every recommendation must cite internal source IDs.
- Every agent answer should include the sources used.
- If source data is missing, the agent must say the data is missing.
- The agent must never invent customer facts, product terms, campaign eligibility, or interest rates.

## Human Approval Rules

- The agent must not auto-send customer-facing content.
- Email drafts and call scripts require human approval before being saved.
- Saving a draft requires an approval status.
- All approval events must be logged.

## Audit Log Rules

Every important action must create an audit log entry containing:

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
