# RMFLOW_AGENT_MEMORY

## Planned MVP Context State

- `session_id`
- `rm_id`
- `current_customer_id`
- `current_module`
- `active_context`
- `retrieved_sources`
- `pending_action`
- `approval_status`
- `last_draft_id`
- `last_agent_output_id`

## Memory Rules

- update `current_customer_id` when the user selects or asks about a customer
- preserve context for follow-up questions
- update `pending_action` when a draft is generated but not yet approved
- update `approval_status` when the user approves or rejects a draft
- update `last_draft_id` when a draft object is created or saved
- update `last_agent_output_id` on every successful agent response
- never fabricate missing context

## Follow-up Resolution Rules

### `khách này`

Interpret `khách này` as `current_customer_id`.

If `current_customer_id` is missing, ask the user to specify the customer and mark the context as incomplete.

### `script này`

Interpret `script này` as the latest call script linked to `last_draft_id` or the latest draft stored in `pending_action`.

If neither exists, say there is no current script in context.

### `lưu bản này`

Interpret `bản này` as the latest draft object referenced by `last_draft_id` or `pending_action`.

If approval is not confirmed, refuse the save and explain that human approval is required first.

### `tại sao khách đầu tiên được ưu tiên?`

Interpret `khách đầu tiên` as the first customer from the latest prioritization result in `active_context`.

If the latest prioritization result is not available, ask the user to rerun prioritization or specify the customer.
