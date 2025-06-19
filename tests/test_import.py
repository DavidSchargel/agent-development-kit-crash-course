"""Test Agent Development Kit (ADK) Masterclass with Brandon."""

import agent_development_kit_crash_course


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(agent_development_kit_crash_course.__name__, str)
