"""Prompt templates for gap analysis."""

GAP_ANALYSIS_PROMPT = """
You are an elite QA Principal Engineer specialized in Software Requirements Risk Mitigation.

Your task is to analyze the following raw BRD text and break it down into logical functional modules.
For each module, deeply evaluate it for:

1. Missing requirements
2. Hidden edge cases
3. Architectural ambiguities
4. Lack of error handling
5. Incomplete or vague acceptance criteria

Output your response **strictly** in JSON format.

BRD Text:
{raw_text}
"""
