"""
Tool Agent.

This agent uses tools to perform tasks.
"""

from datetime import datetime, timezone

from google.adk.agents import Agent
from google.adk.tools import google_search


def get_current_time() -> dict:
    """Get the current UTC time as a formatted string.

    Returns
    -------
        dict: Dictionary with 'current_time' key containing UTC timestamp
              in YYYY-MM-DD HH:MM:SS format (e.g., '2024-03-15 14:30:45').
    """
    return {"current_time": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}  # noqa: UP017


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use one of the following tools:
    - google_search
    - get_current_time
    """,
    tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time],  # <--- Doesn't work
)
