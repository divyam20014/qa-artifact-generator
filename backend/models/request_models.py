"""Request models for FastAPI endpoints."""

from pydantic import BaseModel, Field
from typing import List, Dict, Any


class GapAnalysisRequest(BaseModel):
    """Request model for gap analysis endpoint."""

    rawText: str = Field(
        ...,
        min_length=1,
        max_length=50000,
        description="Raw BRD text to analyze",
    )


class Module(BaseModel):
    """Module model from gap analysis."""

    moduleId: str
    moduleName: str
    summary: str
    gaps: List[Dict[str, Any]]


class CriteriaRequest(BaseModel):
    """Request model for criteria generation endpoint."""

    modules: List[Module] = Field(
        ...,
        min_items=1,
        description="Modules from gap analysis",
    )


class TestCriteria(BaseModel):
    """Test criteria model."""

    criteriaId: str
    moduleId: str
    description: str


class ScenariosRequest(BaseModel):
    """Request model for scenarios generation endpoint."""

    criteria: List[TestCriteria] = Field(
        ...,
        min_items=1,
        description="Test criteria",
    )


class TestScenario(BaseModel):
    """Test scenario model."""

    scenarioId: str
    criteriaId: str
    scenarioType: str
    title: str


class TestCasesRequest(BaseModel):
    """Request model for test cases generation endpoint."""

    scenarios: List[TestScenario] = Field(
        ...,
        min_items=1,
        description="Test scenarios",
    )
