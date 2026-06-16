"""Prompt templates for criteria generation."""

CRITERIA_PROMPT = """
Taking the functional modules from the previous step, translate them into explicit, measurable Test Criteria.
Every requirement must have clear validation rules.

Output format: JSON array of test criteria objects.

Modules:
{modules}
"""
