# RMFlow Backend

This backend implements Phase 2 only: local FastAPI mock API.

## Scope

- reads local JSON files from the project `data/` directory
- exposes mock CRM-like GET endpoints
- returns structured JSON responses
- does not call sandbox CRM API
- does not include LLM logic

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run the commands from the `backend/` directory.
