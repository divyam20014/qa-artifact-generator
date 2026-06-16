# Architecture Overview

## System Design

The QA Artifact Generator is a **stateless, database-free** web application:

- **Frontend**: React/Next.js with React Context (sessionStorage)
- **Backend**: FastAPI with LLM integration (OpenAI/Anthropic)
- **Processing**: Sequential LLM prompt chaining

## Key Principles

### 1. Stateless Backend
- No database, no file persistence
- In-memory processing only
- Scalable horizontally

### 2. Frontend State Management
- React Context for global state
- sessionStorage for persistence
- Auto-cleared on browser close

### 3. LLM Prompt Chaining

```
Step 1: Gap Analysis (raw text) → modules + gaps
Step 2: Criteria Generation (modules) → test criteria
Step 3: Scenario Generation (criteria) → test scenarios
Step 4: Test Case Generation (scenarios) → test cases
```

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|----------|
| `/api/health` | GET | Health check |
| `/api/upload` | POST | Upload & parse BRD |
| `/api/analyze-gaps` | POST | Gap analysis |
| `/api/generate-criteria` | POST | Generate criteria |
| `/api/generate-scenarios` | POST | Generate scenarios |
| `/api/generate-testcases` | POST | Generate test cases |

## Security

- **Input Validation**: Pydantic models
- **File Limits**: 10MB max
- **No Persistence**: In-memory only
- **CORS**: Restricted origins
- **XSS Protection**: React built-in

## Performance

- Stateless for scalability
- Async/await for non-blocking I/O
- In-memory processing (no DB latency)
- JSON streaming support

## Development

```bash
# Backend
cd backend && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend && npm install && npm run dev
```

Visit:
- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000
