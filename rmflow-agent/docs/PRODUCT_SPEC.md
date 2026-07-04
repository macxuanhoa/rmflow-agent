# PRODUCT_SPEC

## A. Final Sharpened Idea

RMFlow Agent is a Vietnamese source-grounded CRM action agent for bank Relationship Managers (RMs).

Its MVP purpose is narrow and operational:

1. help an RM decide which customer to follow up first in the morning
2. explain why that customer is prioritized using traceable source IDs
3. summarize customer context from CRM interactions and open opportunities
4. match the customer to a relevant campaign or product direction
5. generate a draft email or call script
6. require human approval before any save action
7. log every important action in an audit log

RMFlow is not a broad CRM automation platform. It is not a general chatbot. It is an action-oriented assistant designed to reduce the time an RM spends reading scattered notes, checking campaign fit, and preparing the next customer touchpoint.

## B. Target Context and Persona

### Primary User

- Role: bank Relationship Manager
- Working context: desktop-heavy internal CRM workflow
- Daily pressure: many customers, fragmented notes, campaign targets, limited time
- Success condition: prioritize the right customer, contact them with the right message, and keep the action traceable

### Secondary Stakeholders

- Business leads who care about follow-up quality and opportunity conversion
- IT and hackathon judges who need to see an agentic workflow with evidence, approval, and auditability

### User Constraints

- RM cannot trust AI output if it invents rates, campaign terms, or customer facts
- RM must retain control over final customer-facing communication
- RM needs explainable prioritization, not opaque scoring

## C. Current Manual Workflow

Today, an RM usually works like this:

1. open CRM and scan assigned customers manually
2. review recent notes, follow-up dates, and open opportunities one customer at a time
3. remember active campaigns separately or ask another teammate
4. decide who to contact first based on incomplete or inconsistent information
5. draft a call script or email manually in Vietnamese
6. copy or re-enter the draft into CRM
7. leave limited traceability on why that action was chosen

### Current Pain Points

- customer context is fragmented across multiple records
- prioritization is manual and inconsistent
- campaign relevance is easy to miss
- draft preparation consumes time
- evidence for recommendations is not obvious
- compliance and approval steps are easy to under-document

## D. Future AI-Agent Workflow

The target MVP workflow is:

1. RM asks in Vietnamese: `Sáng nay tôi nên chăm sóc khách nào trước?`
2. RMFlow retrieves mock CRM data for customers, interactions, opportunities, campaigns, products, and templates
3. RMFlow ranks customers with explainable rule-based scoring
4. RMFlow returns a prioritized answer with source IDs and tool trace
5. RM asks a follow-up question such as `Tại sao khách này được ưu tiên?`
6. RMFlow keeps `current_customer_id` in context and explains the recommendation from retrieved evidence
7. RM asks for campaign fit, next-best action, call script, or email draft
8. RMFlow generates a grounded draft using retrieved customer context, opportunity data, campaign fit, and template content
9. RMFlow marks the draft as `requires_approval = true`
10. RM approves before any save action is allowed
11. RMFlow writes an audit log with tools called, source IDs, approval status, crm mode, and latency

### Required Proof That This Is An Agent

The MVP must visibly show:

- current customer context
- retrieved source IDs
- tools called
- approval state
- audit log
- explainable recommendation logic

## F. MVP Scope

### Must-Have

- Vietnamese RM-facing interaction
- daily prioritization
- customer summary
- opportunity and campaign match
- next-best action recommendation
- draft email generation
- draft call script generation
- human approval before saving
- audit log
- mock-first data and backend path

### Should-Have

- explicit risk flags when eligibility is unclear
- visible demo fallback mode when sandbox fallback is active later
- stable response contract for backend and frontend integration

### Avoid In MVP

- real CRM sending
- full compliance engine
- mobile app
- Qdrant
- LangGraph
- full MCP server
- autonomous outbound communication
- opaque ML scoring

## J. Innovation and Impact Metrics

### Innovation

- source-grounded agent instead of a generic chat interface
- explicit approval workflow before customer-facing action
- visible tool trace and audit log
- mock-first architecture that can switch to sandbox later without rewriting agent logic

### MVP Impact Metrics

- time to identify first customer to contact
- time to produce first usable call script or email draft
- percentage of answers that include source IDs
- percentage of customer-facing drafts that correctly require approval
- percentage of hero demo flows completed without manual data lookup

### Demo Success Metrics

- hero query 1 returns a ranked customer list with reasons and source IDs
- hero query 3 works using remembered `current_customer_id`
- hero query 4 produces a grounded draft
- hero query 5 cannot save without approval and logs the event

## K. Value and Implementation Logic

### Why This Matters

Relationship Managers do not need another broad AI chat experience. They need a narrow assistant that helps them act faster on the next customer decision while remaining auditable.

### Why This MVP Is Feasible

- the hero workflow is narrow
- the data model is small and mock-friendly
- rule-based prioritization is explainable
- the LLM can be limited later to wording and draft generation only
- audit and approval are first-class concerns from the start

### Why This Architecture Is Practical

- mock JSON provides a stable starting point
- API contracts can be built before sandbox assumptions are confirmed
- `CRMClient` abstraction keeps future integration isolated
- frontend can show clear evidence instead of pretending hidden agent work

## L. Competitor / Alternative Comparison

### Manual CRM Workflow

- Strength: already trusted by teams
- Weakness: slow, fragmented, hard to scale consistently

### Generic LLM Chatbot

- Strength: fast drafting
- Weakness: weak grounding, poor traceability, weak approval discipline

### Full CRM Automation Suite

- Strength: broad scope
- Weakness: too large for MVP, too risky for hackathon timeline, often hides reasoning

### RMFlow Agent Position

RMFlow focuses on one high-value workflow:

`daily prioritization → customer summary → campaign match → next-best action → email/call script → approval → audit log`

This makes the MVP easier to prove, easier to demo, and safer to trust than a broad automation claim.
