# RMFLOW_AGENT_TOOLS

## Tool Rules

- every tool must return source IDs when relevant
- every tool call must be logged
- use mock JSON first
- do not call external APIs directly from the agent

## Tool Contracts

### `get_customers`

- Purpose: return assigned customers for an RM, optionally ranked for prioritization
- Input:
  - `rm_id`
  - `segment` optional
  - `status` optional
- Output:
  - list of customer objects
  - each object may include summary fields used in ranking
- Source IDs returned:
  - `customer_id`
- When to use it:
  - morning prioritization
  - customer list view
  - initial customer context retrieval

### `get_customer_by_id`

- Purpose: retrieve one customer profile by ID
- Input:
  - `customer_id`
- Output:
  - one customer object or not found result
- Source IDs returned:
  - `customer_id`
- When to use it:
  - follow-up questions such as `khách này`
  - customer summary generation

### `get_interactions`

- Purpose: return interaction history and upcoming follow-up signals
- Input:
  - `customer_id`
  - `limit` optional
  - `recent_only` optional
- Output:
  - list of interaction records
  - latest interaction indicators such as sentiment and next follow-up date
- Source IDs returned:
  - `interaction_id`
  - `customer_id`
- When to use it:
  - explain prioritization
  - summarize customer context
  - support next-best action

### `get_opportunities`

- Purpose: return open or recent opportunities for a customer
- Input:
  - `customer_id`
  - `status` optional
- Output:
  - list of opportunity records
- Source IDs returned:
  - `opportunity_id`
  - `customer_id`
- When to use it:
  - explain business value
  - support campaign match
  - support draft generation

### `get_campaigns`

- Purpose: return active campaigns that may match the customer
- Input:
  - `customer_id` optional
  - `segment` optional
  - `active_only` optional
- Output:
  - list of campaign records
  - optional eligibility reasoning
- Source IDs returned:
  - `campaign_id`
- When to use it:
  - campaign match
  - next-best action
  - draft generation with a campaign angle

### `search_product_kb`

- Purpose: retrieve product facts relevant to the customer need or campaign
- Input:
  - `keywords`
  - `customer_segment` optional
  - `risk_profile` optional
- Output:
  - list of product records or product snippets
  - eligibility notes and fictional demo pricing notes when available
- Source IDs returned:
  - `product_id`
- When to use it:
  - product recommendation
  - eligibility checks
  - email or call script grounding

### `search_templates`

- Purpose: retrieve email templates or call script templates by purpose
- Input:
  - `channel`
  - `purpose`
  - `product_category` optional
- Output:
  - list of matching templates or scripts
- Source IDs returned:
  - `template_id`
  - `script_id`
- When to use it:
  - generate email
  - generate call script

### `create_crm_email_draft`

- Purpose: create a draft email payload for save after approval
- Input:
  - `customer_id`
  - `template_id`
  - `draft_body`
  - `approval_status`
- Output:
  - draft payload with save eligibility status
  - may return validation failure if approval is missing
- Source IDs returned:
  - `customer_id`
  - `template_id`
  - `draft_id` if created
- When to use it:
  - after email draft generation
  - only when save is requested

### `create_crm_call_script`

- Purpose: create a call script payload for save after approval
- Input:
  - `customer_id`
  - `script_id`
  - `draft_body`
  - `approval_status`
- Output:
  - script payload with save eligibility status
  - may return validation failure if approval is missing
- Source IDs returned:
  - `customer_id`
  - `script_id`
  - `draft_id` or `saved_script_id` if created
- When to use it:
  - after call script generation
  - only when save is requested

### `write_audit_log`

- Purpose: record important system actions and outcomes
- Input:
  - `session_id`
  - `user_query`
  - `intent`
  - `tools_called`
  - `source_ids`
  - `crm_mode`
  - `fallback_status`
  - `latency`
  - `approval_status`
  - `output_summary`
- Output:
  - audit log record
  - generated `audit_log_id`
- Source IDs returned:
  - `audit_log_id`
- When to use it:
  - every important action
  - every customer-facing draft flow
  - every approval event
