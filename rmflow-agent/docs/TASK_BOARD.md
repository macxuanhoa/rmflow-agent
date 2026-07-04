# TASK_BOARD

## Current Phase Status

- Phase 0: Scaffold repo - Done
- Phase 0.5: CRM Sandbox API strategy - Done
- Phase 1: Mock CRM data - Done in docs/data readiness form
- Phase 2 onward: Not started

## Team Task Division

### IT 1

- Backend
- Mock API
- CRMClient abstraction
- Future local endpoint implementation

### IT 2

- AgentService
- ToolRegistry
- ContextManager
- Approval and audit orchestration

### IT 3

- Frontend
- Demo UI
- Approval panel
- Tool trace and audit log visualization

### Business 1

- Product Spec
- Mock customer scenarios
- Prioritization logic review

### Business 2

- Demo Script
- Pitch
- Judge Q&A
- Demo fallback narrative

## Updated Roadmap

1. Phase 0: Scaffold repo
   - Status: Done
2. Phase 0.5: Add CRM Sandbox API strategy
   - Goal: Update docs for mock-first, sandbox-ready architecture
   - Status: Done
3. Phase 1: Mock CRM data
   - Goal: Create realistic JSON data that can map to sandbox API later
   - Status: Done in current repo
4. Phase 2: Local FastAPI mock API
   - Goal: Backend reads local JSON data and exposes CRM-like endpoints
5. Phase 3: CRMClient abstraction
   - Goal: Add MockCRMClient and SandboxCRMClient structure
6. Phase 4: ToolRegistry
   - Goal: Tools call CRMClient, not raw JSON or sandbox API directly
7. Phase 5: ContextManager
   - Goal: Keep current_customer_id, current_module, active_context, retrieved_sources, pending_action, approval_status, last_draft_id, last_agent_output_id
8. Phase 6: Rule-based AgentService
   - Goal: Support prioritization, customer summary, campaign match, next-best action
9. Phase 7: Draft generation
   - Goal: Generate email/call script from grounded context and templates
10. Phase 8: Approval workflow
    - Goal: Require human approval before saving drafts
11. Phase 9: Frontend UI
    - Goal: Show chat, context panel, tool trace, source chips, draft preview, approval buttons, audit log
12. Phase 10: Optional sandbox switch
    - Goal: Switch from MockCRMClient to SandboxCRMClient only after API docs confirm required endpoints

## Completed Checklist

- [x] repo scaffold created
- [x] Trae agent prompts created
- [x] CRM sandbox strategy documented
- [x] product spec completed
- [x] agent spec completed
- [x] API contract expanded
- [x] logical schema documented
- [x] demo script upgraded
- [x] mock data created
- [x] review output prepared

## Remaining Checklist

- [ ] implement local FastAPI mock API
- [ ] implement CRMClient abstraction
- [ ] implement ToolRegistry
- [ ] implement ContextManager
- [ ] implement rule-based AgentService
- [ ] implement draft save and approval endpoints
- [ ] build frontend demo UI
- [ ] add visible audit log panel
- [ ] verify hero flow end to end
