"""Prompt templates for test case generation."""

TESTCASES_PROMPT = """
Expand each Test Scenario into an actionable, professional test case document.
The test steps must be:

- Practical
- Explicit
- Tightly bound to the application's logical functionality

Output format: JSON array of test case objects with testCaseId, scenarioId, title, type, preConditions, steps, expectedResult.

Scenarios:
{scenarios}
"""
