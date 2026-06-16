# QA Artifact Generator

An AI-powered, database-free web application that analyzes Business Requirement Documents (BRDs) and automatically generates comprehensive QA artifacts including test cases, scenarios, criteria, and gap analyses.

## 🎯 Features

- **BRD Analysis**: Upload PDF, DOCX, or TXT files for intelligent requirement analysis
- **Gap Identification**: Automated detection of missing requirements, edge cases, and architectural ambiguities
- **Test Criteria Generation**: Convert requirements into measurable acceptance criteria
- **Scenario Mapping**: Generate positive, negative, and edge-case test scenarios
- **Test Case Generation**: Create actionable, comprehensive test cases with pre-conditions, steps, and expected results
- **Multi-Format Export**: Download test cases as Excel (.xlsx), Markdown (.md), or JSON
- **Stateless Architecture**: No database—all data managed in-memory with sessionStorage
- **Project Import/Export**: Save and restore entire analysis workflows as JSON

## 📋 Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Document Parsing**: pdfplumber, python-docx
- **LLM Integration**: OpenAI, Anthropic

### Frontend
- **Framework**: Next.js 14+ (React 18)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Context + sessionStorage

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI or Anthropic API Key

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
cp ../.env.example .env
# Add your OPENAI_API_KEY to .env
uvicorn main:app --reload
```

Server: `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
echo 'NEXT_PUBLIC_API_URL=http://localhost:8000' > .env.local
npm run dev
```

Application: `http://localhost:3000`

## 🔄 Workflow

1. **Step 1 - Ingestion**: Upload a BRD or paste raw text
2. **Step 2 - Gap Analysis**: AI identifies gaps and ambiguities
3. **Step 3 - Criteria Mapping**: Convert requirements to test criteria
4. **Step 4 - Test Suite**: Generate and export test cases

## 📤 Export Options

- **Excel (.xlsx)**: Professional spreadsheet with formatting
- **Markdown (.md)**: Document for wikis and repositories
- **JSON (.json)**: Full project state for import/restore

## 🔒 Security

- Zero file persistence (no disk writes)
- In-memory processing only
- Session-based state with automatic expiry
- Strict input validation

## 📚 API Documentation

Swagger UI: `http://localhost:8000/docs`
ReDoc: `http://localhost:8000/redoc`

## 🧪 Testing

```bash
# Backend
cd backend && pytest tests/ -v

# Frontend
cd frontend && npm test
```

## 📖 Documentation

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed system design.

---

**Built to streamline QA workflows** ❤️
