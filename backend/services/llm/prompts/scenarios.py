"""Prompt templates for scenarios generation."""

SCENARIOS_PROMPT = """
For each Test Criterion provided, brainstorm all possible execution paths.
Split these into distinct testing categories:

- Positive (happy paths)
- Negative (error paths/fault injection)
- Edge Cases (boundary limits, unexpected interactions)

Output format: JSON array of scenario objects.

Criteria:
{criteria}
"""
