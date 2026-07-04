# DEMO_SCRIPT

## Opening Problem

Relationship Managers lose time every morning deciding who to contact first, rereading fragmented notes, and manually preparing follow-up messages. The risk is not just slow execution. It is inconsistent prioritization, missed campaign fit, and weak traceability.

## Manual Workflow Pain

Today the RM has to:

1. scan customer records manually
2. open recent interactions one by one
3. guess which opportunity is most urgent
4. remember active campaigns separately
5. draft a message or call plan manually
6. keep limited evidence on why that action was chosen

## Live Demo Prompt Sequence

### Prompt 1

`Sáng nay tôi nên chăm sóc khách nào trước?`

Show:

- prioritized customers
- source IDs
- tool trace

### Prompt 2

`Tại sao khách Nguyễn A được ưu tiên?`

Show:

- interaction evidence
- opportunity evidence
- campaign evidence
- explainable prioritization

### Prompt 3

`Khách này phù hợp campaign nào và nên đề xuất gì?`

Show:

- remembered `current_customer_id`
- campaign match
- product grounding
- next-best action

### Prompt 4

`Tạo cho tôi call script ngắn để gọi khách này.`

Show:

- generated draft
- template source
- `requires_approval = true`

### Prompt 5

`Tôi duyệt script này, lưu vào CRM.`

Show:

- approval state change
- save action
- audit log entry

## Explanation During Demo

### Tool Trace

Emphasize that the system is not inventing an answer. It is calling retrieval tools and showing what data was used.

### Source IDs

Explain that every recommendation is tied to source IDs such as `C001`, `I001`, `O001`, `CAM001`, `P001`, `SCP001`.

### Context State

Explain that the user does not need to repeat the customer name because the system keeps `current_customer_id` and workflow state.

### Approval Workflow

Explain that customer-facing drafts are never auto-sent and cannot be saved without approval.

### Audit Log

Explain that every important action creates a visible audit log entry with tools called, source IDs, approval status, latency, and crm mode.

## Business Impact

- faster first action of the day for RMs
- more consistent prioritization
- less manual drafting effort
- stronger explainability for internal review
- safer AI usage because approval and traceability are built in

## Fallback Demo Plan

If any dynamic component fails during the live demo:

1. switch to demo fallback mode
2. continue using mock data only
3. show that the workflow still keeps source IDs, approval, and audit logging
4. clearly state that sandbox integration is optional and not required for the MVP proof
