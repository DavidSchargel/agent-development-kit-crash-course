# CLAUDE.md

## Rules

@.docs/rules/global_rules.md
@.windsurf/rules/ai-agent-development.md
@.windsurf/rules/postgres-database-rules.md
@.windsurf/rules/sql-database-operations-rules.md

## Documentation

<!-- @docs/ -->

## Project Overview
This is an educational Python project demonstrating Google's Agent Development Kit (ADK) through a series of progressive examples. Each numbered directory contains a self-contained example showcasing different ADK capabilities.

## Essential Commands

- See .windsurf/rules/global_rules.md

## Architecture and Code Organization

### Example Structure Pattern
Each example follows this consistent structure:
```
<number>-<feature-name>/
├── README.md                    # Example-specific documentation
├── <agent_name>/
│   ├── agent.py                # Core agent implementation
│   └── .env.example            # Environment variable template
```

### Key Architectural Decisions
1. **Agent-Based Design**: Each example demonstrates a specific ADK pattern (basic, tools, sessions, multi-agent, etc.)
2. **Modular Examples**: Each example is self-contained with minimal cross-dependencies

## Environment Configuration
Each agent example requires environment variables:
- `GOOGLE_API_KEY`: Required for Google Generative AI
- Additional API keys as needed (check .env.example files)

Always create `.env` files from `.env.example` templates before running examples.