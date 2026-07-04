# RMFLOW_AGENT_EVALS

## Test Case 1

- Query: `Sáng nay tôi nên chăm sóc khách nào trước?`
- Expected intent: `daily_prioritization`
- Expected tools:
  - `get_customers`
  - `get_interactions`
  - `get_opportunities`
  - `get_campaigns`
  - `write_audit_log`
- Expected context changes:
  - set `active_context` to latest prioritization result
  - keep `current_customer_id` empty until user selects a customer
  - set `last_agent_output_id`
- Expected source IDs:
  - at least one `customer_id`
  - at least one `interaction_id`
  - at least one `opportunity_id` or `campaign_id`
- Expected approval state: `requires_approval = false`
- Pass criteria:
  - ranked customers are returned
  - top customer has grounded explanation
  - source IDs are visible
  - audit log ID is returned

## Test Case 2

- Query: `Tại sao khách Nguyễn A được ưu tiên?`
- Expected intent: `customer_summary`
- Expected tools:
  - `get_customer_by_id`
  - `get_interactions`
  - `get_opportunities`
  - `get_campaigns`
  - `write_audit_log`
- Expected context changes:
  - set `current_customer_id = C001`
  - set `current_module = customer_summary`
  - set `last_agent_output_id`
- Expected source IDs:
  - `C001`
  - `I001`
  - `O001`
  - `CAM001`
- Expected approval state: `requires_approval = false`
- Pass criteria:
  - answer explains why C001 is prioritized
  - answer references due follow-up, opportunity value, and campaign fit
  - source IDs are visible

## Test Case 3

- Query: `Khách này phù hợp campaign nào và nên đề xuất gì?`
- Expected intent: `campaign_match`
- Expected tools:
  - `get_customer_by_id`
  - `get_campaigns`
  - `search_product_kb`
  - `get_opportunities`
  - `write_audit_log`
- Expected context changes:
  - reuse existing `current_customer_id`
  - set `current_module = campaign_match`
  - set `last_agent_output_id`
- Expected source IDs:
  - current `customer_id`
  - matched `campaign_id`
  - matched `product_id`
- Expected approval state: `requires_approval = false`
- Pass criteria:
  - agent does not ask again for customer if context exists
  - recommendation is grounded in campaign and product evidence
  - risk flag appears if eligibility is incomplete

## Test Case 4

- Query: `Tạo cho tôi call script ngắn để gọi khách này.`
- Expected intent: `generate_call_script`
- Expected tools:
  - `get_customer_by_id`
  - `get_interactions`
  - `get_opportunities`
  - `get_campaigns`
  - `search_product_kb`
  - `search_templates`
  - `write_audit_log`
- Expected context changes:
  - reuse `current_customer_id`
  - set `pending_action = generate_call_script`
  - set `approval_status = pending`
  - set `last_draft_id`
  - set `last_agent_output_id`
- Expected source IDs:
  - current `customer_id`
  - relevant `interaction_id`
  - relevant `opportunity_id`
  - relevant `campaign_id`
  - relevant `product_id`
  - `script_id`
- Expected approval state: `requires_approval = true`
- Pass criteria:
  - draft is produced
  - draft is grounded and concise
  - approval requirement is explicit
  - audit log ID is returned

## Test Case 5

- Query: `Tôi duyệt script này, lưu vào CRM.`
- Expected intent: `approve_draft`
- Expected tools:
  - `create_crm_call_script`
  - `write_audit_log`
- Expected context changes:
  - set `approval_status = approved`
  - keep `last_draft_id`
  - clear or update `pending_action`
  - set `last_agent_output_id`
- Expected source IDs:
  - current `customer_id`
  - current `script_id`
  - saved `draft_id` or script save ID
- Expected approval state: `requires_approval = false` after save confirmation
- Pass criteria:
  - save action is blocked if approval context is missing
  - save confirmation only happens after approval
  - audit log records approval and save outcome
