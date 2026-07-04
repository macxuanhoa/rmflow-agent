# DB_SCHEMA

## Status

MVP starts with local JSON files, not a production database.

These are logical schemas for mock-first implementation and later API alignment.

## Customer

```json
{
  "customer_id": "C001",
  "rm_id": "RM001",
  "anonymized_name": "KH Nguyễn A",
  "segment": "affluent",
  "age_range": "40-49",
  "city": "Ho Chi Minh City",
  "products_owned": ["CASA", "term_deposit_matured"],
  "balance_range": "700M-1B VNĐ",
  "risk_profile": "conservative",
  "preferred_channel": "phone",
  "relationship_manager_id": "RM001",
  "notes": "Demo customer only"
}
```

## Interaction

```json
{
  "interaction_id": "I001",
  "customer_id": "C001",
  "rm_id": "RM001",
  "date": "2026-07-02",
  "channel": "phone",
  "interaction_type": "deposit_follow_up",
  "rm_note": "Customer asked about 12-month options.",
  "outcome": "interested_follow_up_needed",
  "sentiment": "positive",
  "next_follow_up_date": "2026-07-05"
}
```

## Opportunity

```json
{
  "opportunity_id": "O001",
  "customer_id": "C001",
  "rm_id": "RM001",
  "product_category": "term_deposit",
  "product_name": "Tiết kiệm 12 tháng linh hoạt Demo",
  "expected_value": 700000000,
  "probability_score": 0.82,
  "reason": "Idle balance and recent interest inquiry.",
  "next_action": "Call for term confirmation.",
  "status": "open"
}
```

## Campaign

```json
{
  "campaign_id": "CAM001",
  "campaign_name": "Summer Savings Boost Demo",
  "target_segment": "affluent",
  "product_focus": "term_deposit",
  "start_date": "2026-07-01",
  "end_date": "2026-08-31",
  "eligibility_rule": "Affluent customers with idle balance and recent deposit interest.",
  "pricing_note": "Fictional demo campaign. Not a real Bank A program."
}
```

## Product

```json
{
  "product_id": "P001",
  "product_name": "Tiết kiệm 12 tháng linh hoạt Demo",
  "product_category": "term_deposit",
  "eligibility": "Suitable for conservative affluent customers with idle funds.",
  "rate_or_fee": "Fictional demo term band A. Not a real Bank A rate.",
  "suitable_profile": "Conservative customers seeking stable savings planning.",
  "risk_notes": "Do not present as a real public rate."
}
```

## EmailTemplate

```json
{
  "template_id": "T001",
  "channel": "email",
  "purpose": "deposit_follow_up_email",
  "product_category": "term_deposit",
  "tone": "professional_vietnamese_banking",
  "required_fields": ["customer_name", "product_name", "next_step"],
  "template_text": "Kính gửi {{customer_name}}, ..."
}
```

## CallScript

```json
{
  "script_id": "SCP001",
  "channel": "call",
  "purpose": "deposit_follow_up_call",
  "product_category": "term_deposit",
  "opening": "Em chào anh/chị...",
  "questions": ["Anh/chị đang quan tâm kỳ hạn nào?"],
  "objection_handling": ["Nếu khách chưa chắc, đề nghị giữ lịch hẹn ngắn."],
  "closing": "Em xin phép gửi thêm thông tin sau cuộc gọi."
}
```

## AuditLog

```json
{
  "audit_log_id": "A001",
  "session_id": "S001",
  "user_query": "Sáng nay tôi nên chăm sóc khách nào trước?",
  "intent": "daily_prioritization",
  "tools_called": ["get_customers", "get_interactions"],
  "source_ids": ["C001", "I001"],
  "crm_mode": "mock",
  "fallback_status": "none",
  "latency": 182,
  "approval_status": "not_required",
  "output_summary": "Recommended C001 first.",
  "created_at": "2026-07-04T09:00:00Z"
}
```

## AgentSessionState

```json
{
  "session_id": "S001",
  "rm_id": "RM001",
  "current_customer_id": "C001",
  "current_module": "campaign_match",
  "active_context": {
    "latest_ranked_customers": ["C001", "C003", "C002"]
  },
  "retrieved_sources": ["C001", "I001", "O001", "CAM001", "P001"],
  "pending_action": "generate_call_script",
  "approval_status": "pending",
  "last_draft_id": "D002",
  "last_agent_output_id": "OUT004"
}
```

## Change Control

Do not change logical schema assumptions without updating this file first.
