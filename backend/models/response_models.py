"""Response models for FastAPI endpoints."""

from pydantic import BaseModel
from typing import List, Dict, Any


class GapAnalysisResponse(BaseModel):
    """Response model for gap analysis endpoint."""

    status: str
    modules: List[Dict[str, Any]]


class CriteriaResponse(BaseModel):
    """Response model for criteria generation endpoint."""

    status: str
    testCriteria: List[Dict[str, Any]]


class ScenariosResponse(BaseModel):
    """Response model for scenarios generation endpoint."""

    status: str
    scenarios: List[Dict[str, Any]]


class TestCasesResponse(BaseModel):
    """Response model for test cases generation endpoint."""

    status: str
    testCases: List[Dict[str, Any]]
