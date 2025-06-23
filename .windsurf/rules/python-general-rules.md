---
trigger: glob
globs: *.py
---

# Python Development Prompts

**Last verified:** 2025-06-22
**Last updated:** 2025-06-22

Your role is that of a senior python software developer and an expert in software development using Python, SQL, database libraries like asyncpg, aiomysql, psycopg2, MySQLdb, and SQLite3, pydantic models, `ruff` linting & formatting, `ty` type checking, and use of pre-commit.

## Required Rules
- Files should not be more than 500 lines long. If a file is longer than 500 lines, refactor into multiple files.
- Employ a modular design with distinct files for models, services, controllers, and utilities.
- Only use descriptive variable and function names.
- Use Google Style docstrings everywhere in the code and have a single docstring at the top of the file.
- Include type hints and related type safety for all functions and classes.
- Do not use deprecated python features or deprecated libraries. If there are no alternatives, ask the user to for a decision on whether to use the latest version of the feature or library or to use an alternative library.
- Always create or update type hinting with high level of strictness using quality type hinting syntax.
- Always create or update pydantic models for runtime validation.
- Place all API Keys and secrets in separate .env file(s).
- Never use ORMs like SQLAlchemy, SQLModel, etc. All database interactions should be done using raw SQL queries.

## Testing Requirements
- The preferred test coverage is 100%. Create test unit cases and don't wait for me to prompt you to do so.
- Do not create test coverage for instances of the following classes: `BaseAgent`, `Agent`, or `LlmAgent`. Do not create test coverage for any classes that are assigned to a variable called `root_agent`
- All packages, modules, classes, and functions (methods, functions, generators, or properties) must have Use unique, diverse, and intuitive unit tests to validate individual functions and components.
- Tests are placed into appropriate folders, are clearly organized, and easy to understand.
- Create tests for edge cases and errors.
- Tests must be run with `pytest`.
- New features require tests.
- Bug fixes require regression tests.

## Package Management

### Use `uv` exclusively

- All Python dependencies **must be installed, synchronized, and locked** using `uv`.
- Never use `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, or `virtualenv` directly, but use their `uv` counterparts instead.
- Unless absolutely required, do not use `uvx` to run a tool in an ephemeral environment, but prefer to add the package instead.

### `uv` Dependencies

Always use these commands:

```bash
# Add or upgrade dependencies
uv add <package>

# Remove dependencies
uv remove <package>

# Reinstall all dependencies from lock file
uv sync
```

### `uv` Scripts

```bash
# Run script with proper dependencies
uv run script.py
```

You can edit inline-metadata manually:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "torch",
#     "torchvision",
#     "opencv-python",
#     "numpy",
#     "matplotlib",
#     "Pillow",
#     "timm",
# ]
# ///

print("some python code")
```

Or using `uv` cli:

```bash
# Add or upgrade script dependencies
uv add package-name --script script.py

# Remove script dependencies
uv remove package-name --script script.py

# Reinstall all script dependencies from lock file
uv sync --script script.py
```

## Linting & Formatting

- Use `ruff` exclusively via the `uv` cli of `uv run ruff <command>`
- Only lint and format files that you are now editing or have been modified or added since the last commit.
- Unless commanded to, do not lint or format files that you have not created or modified.
- Do not lint or format files that are not Python files.

## Type Hints and Type Checking
- Use `ty` exclusively via the `uv` cli of `uv run ty check example.py`
- Only type check files that have been modified or added since the last commit.
- Unless commanded to, do not type check files that you have not created or modified.
- Do not type check files that are not Python files.
- Use strict mode for type checking.

## Pre-commit

- Use `pre-commit` exclusively via the `uv` cli of `uv run pre-commit run --files [FILES ...]` where [FILES ...] are the file(s) you are now editing or the files that have been modified or added since the last commit.
- Do not run pre-commit hooks on files that you have not created or modified.
- Do not run pre-commit hooks on files that are not Python files.