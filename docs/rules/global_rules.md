# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational Python project demonstrating Google's Agent Development Kit (ADK) with 12 progressive examples. The project uses Python 3.13 and modern tooling including UV package manager, Ruff, and mypy.

## Common Development Commands

```bash
# Install dependencies
uv sync

# Run linting and formatting
poe lint

# Run tests with coverage
poe test

# Generate documentation
poe docs

# Run a specific example
cd 1-basic-agent
uv run adk web
```

## Architecture and Key Patterns

### Agent Structure Pattern

Each agent example follows this structure:

- `agent.py` - Main agent definition with prompt, model config, and tools
- `tools.py` (optional) - Custom tool functions with specific signatures
- Sub-agents in nested directories for multi-agent examples

### ADK Agent Components

1. **Prompt**: System instructions for agent behavior
2. **Model Config**: LLM provider and parameters
3. **Tools**: Built-in ADK tools (e.g., `Calculator`, `GoogleSearch`) or custom functions
4. **Memory**: Optional session state management

### Tool Integration Guidelines

- Built-in tools: Import from `google.adk.agents`
- Custom tools: Define in `tools.py` with proper type hints and docstrings
- Tool functions must have clear parameter descriptions for LLM understanding

### Multi-Agent Patterns

For examples 8-12, agents can invoke sub-agents:

- Parent agents define sub-agents in their tools list
- Sub-agents are fully independent with their own prompts and tools
- Use clear naming conventions: `parent_agent.py`, `sub_agents/child_agent.py`

## Code Organization

### Environment Configuration

- API keys: Set via environment variables (never hardcode)
- Model selection: Use `AGENT_MODEL` env var or update model config
- Provider flexibility: Examples use GeminiAPI, LiteLLM, and OpenRouter for multi-provider support

## Testing and Validation

When modifying agents:

1. Test agent responses with various prompts
2. Verify tool calls execute correctly
3. Check for proper error handling
4. Ensure examples remain educational and clear

## ADK-Specific Considerations

### Tool Limitations

- ADK built-in tools have specific capabilities and limitations
- Custom tools should handle errors gracefully
- Tool descriptions are critical for LLM understanding

### Agent Design

- Keep prompts focused and specific
- Use structured outputs when appropriate (see example 7)
- Consider token limits when designing multi-turn interactions

### Performance

- Agent initialization can be slow; reuse when possible
- Streaming responses improve user experience
- Consider caching for expensive operations

## Development Workflow

1. Always test changes with actual agent execution
2. Maintain backward compatibility with existing examples
3. Follow conventional commit prefixes (feat:, fix:, docs:, etc.)
4. Keep examples self-contained and educational
5. Update documentation when adding new patterns or tools
