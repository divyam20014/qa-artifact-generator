"""Helper functions."""

import uuid


def generate_id(prefix: str) -> str:
    """Generate a unique ID with prefix."""
    return f"{prefix}-{str(uuid.uuid4())[:8].upper()}"


def generate_module_id() -> str:
    """Generate a module ID."""
    return generate_id("MOD")


def generate_gap_id() -> str:
    """Generate a gap ID."""
    return generate_id("GAP")


def generate_criteria_id() -> str:
    """Generate a criteria ID."""
    return generate_id("CRT")


def generate_scenario_id() -> str:
    """Generate a scenario ID."""
    return generate_id("SCN")


def generate_testcase_id() -> str:
    """Generate a test case ID."""
    return generate_id("TC")
