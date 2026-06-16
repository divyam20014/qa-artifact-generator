"""FastAPI application entry point for QA Artifact Generator."""

from fastapi import FastAPI, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging

from config.settings import Settings
from models.request_models import (
    GapAnalysisRequest,
    CriteriaRequest,
    ScenariosRequest,
    TestCasesRequest,
)

# Initialize logger
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="QA Artifact Generator API",
    description="Stateless API for generating QA artifacts from BRDs",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Exception Handlers ---
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors."""
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "code": "VALIDATION_ERROR",
            "message": "Request validation failed",
            "details": exc.errors(),
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "code": "HTTP_ERROR",
            "message": exc.detail,
        },
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """Handle generic exceptions."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred",
        },
    )


# --- Health Check ---
@app.get("/api/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "qa-artifact-generator",
        "version": "1.0.0",
    }


# --- Document Upload ---
@app.post("/api/upload", tags=["Document Ingestion"])
async def upload_file(file: UploadFile):
    """Upload and parse a document file (PDF, DOCX, or TXT)."""
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain",
    ]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Use PDF, DOCX, or TXT.",
        )
    
    try:
        content = await file.read()
        raw_text = content.decode("utf-8") if file.content_type == "text/plain" else f"File: {file.filename}"
        
        return {
            "status": "success",
            "filename": file.filename,
            "rawText": raw_text[:500],
        }
    except Exception as e:
        logger.error(f"File parsing failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to parse file")


# --- Gap Analysis ---
@app.post("/api/analyze-gaps", tags=["Analysis"])
async def analyze_gaps(request: GapAnalysisRequest):
    """Analyze BRD text for gaps and inconsistencies."""
    if not request.rawText or not request.rawText.strip():
        raise HTTPException(status_code=400, detail="rawText cannot be empty")
    
    try:
        result = {
            "status": "success",
            "modules": [
                {
                    "moduleId": "MOD-001",
                    "moduleName": "Authentication",
                    "summary": "User authentication and session management",
                    "gaps": [
                        {
                            "gapId": "GAP-001",
                            "description": "Missing account lockout specification",
                            "severity": "High",
                            "impact": "Security vulnerability",
                        }
                    ],
                }
            ],
        }
        return result
    except Exception as e:
        logger.error(f"Gap analysis failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to analyze gaps")


# --- Generate Criteria ---
@app.post("/api/generate-criteria", tags=["Generation"])
async def generate_criteria(request: CriteriaRequest):
    """Generate test criteria from modules."""
    if not request.modules:
        raise HTTPException(status_code=400, detail="modules cannot be empty")
    
    try:
        result = {
            "status": "success",
            "testCriteria": [
                {
                    "criteriaId": "CRT-001",
                    "moduleId": "MOD-001",
                    "description": "System must lock account after 5 failed attempts",
                }
            ],
        }
        return result
    except Exception as e:
        logger.error(f"Criteria generation failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate criteria")


# --- Generate Scenarios ---
@app.post("/api/generate-scenarios", tags=["Generation"])
async def generate_scenarios(request: ScenariosRequest):
    """Generate test scenarios (Positive, Negative, Edge Cases)."""
    if not request.criteria:
        raise HTTPException(status_code=400, detail="criteria cannot be empty")
    
    try:
        result = {
            "status": "success",
            "scenarios": [
                {
                    "scenarioId": "SCN-001",
                    "criteriaId": "CRT-001",
                    "scenarioType": "Positive",
                    "title": "Successful login with valid credentials",
                }
            ],
        }
        return result
    except Exception as e:
        logger.error(f"Scenarios generation failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate scenarios")


# --- Generate Test Cases ---
@app.post("/api/generate-testcases", tags=["Generation"])
async def generate_testcases(request: TestCasesRequest):
    """Generate comprehensive test cases from scenarios."""
    if not request.scenarios:
        raise HTTPException(status_code=400, detail="scenarios cannot be empty")
    
    try:
        result = {
            "status": "success",
            "testCases": [
                {
                    "testCaseId": "TC-MOD-001-001",
                    "scenarioId": "SCN-001",
                    "title": "Verify successful login",
                    "type": "Positive",
                    "preConditions": "User account exists",
                    "steps": ["1. Navigate to login", "2. Enter credentials", "3. Click signin"],
                    "expectedResult": "User is logged in",
                }
            ],
        }
        return result
    except Exception as e:
        logger.error(f"Test cases generation failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate test cases")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=Settings.FASTAPI_HOST,
        port=Settings.FASTAPI_PORT,
    )
