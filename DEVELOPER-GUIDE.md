# Developer Guide: Agent Development Kit (ADK) Crash Course

This guide provides a high-level overview of the Agent Development Kit (ADK) Crash Course repository. It's intended for developers who are new to this project but have general programming experience, to help them understand its structure, setup, and core concepts.

## 1. Architecture Overview

This repository is structured as a **collection of educational examples** designed to teach Google's Agent Development Kit (ADK). It does not represent a single, monolithic application but rather a series of small, focused projects, each demonstrating a specific feature or capability of the ADK framework.

Each numbered directory (e.g., `1-basic-agent`, `2-tool-agent`) is a self-contained example. The primary architectural pattern is **Agent-based**, where each example showcases how to build LLM-powered agents for various tasks.

There is no overarching complex architecture like MVC or Microservices spanning the entire repository; instead, focus is on individual agent implementations.

## 2. Directory Structure Overview

The main directories and their purposes are as follows:

* **`/` (Root Directory)**:
  * `1-basic-agent/`, `2-tool-agent/`, ... `12-loop-agent/`: Individual example projects. Each contains its own `README.md` and a subdirectory with the agent's Python code (e.g., `1-basic-agent/greeting_agent/`).
  * `.venv/`: (Created by user) Python virtual environment for project dependencies.
  * `.git/`: Git version control files.
  * `.gitignore`: Specifies intentionally untracked files that Git should ignore.
  * `README.md`: Main project overview, setup instructions, and example descriptions.
  * `GEMINI_MODELS.md`: Information about supported Gemini models, their capabilities, and pricing.
  * `requirements.txt`: A list of Python dependencies for the project.
  * `agent-development-kit-crash-course.code-workspace`: VS Code workspace configuration file.
* **`/<example-name>/<agent-module-name>/`** (e.g., `1-basic-agent/greeting_agent/`):
  * `agent.py`: Contains the core logic and implementation for the specific example agent.
  * `.env.example`: Template for environment variables (primarily `GOOGLE_API_KEY`).
  * `__init__.py`: Makes the directory a Python package.
  * `README.md`: (Inside `/<example-name>/`) Provides specific details about that example.

## 3. Key Functions & Modules

The core logic resides within each individual example project. The most critical files are generally:

* **`/<example-name>/<agent-module-name>/agent.py`**: This file is the heart of each example, containing the agent's definition, tool integrations (if any), and interaction logic. For instance, in `1-basic-agent/greeting_agent/agent.py`, you'll find the simplest form of an ADK agent.

The `README.md` in the root directory provides a good summary of what each example (`1-basic-agent` through `12-loop-agent`) demonstrates.

## 4. Data Flow (Conceptual)

Given the nature of the repository (a collection of examples), data flow is specific to each agent example. However, a general conceptual flow for most agents is:

1. **User Input**: The user provides a query or command to the agent (typically via a command-line interface when running the `agent.py` script).
2. **Agent Processing**: The ADK framework, along with the custom logic in `agent.py`, processes this input.
3. **LLM Interaction**: The agent interacts with a Google Gemini Large Language Model (LLM), sending the processed input (and potentially previous conversation context or tool outputs).
4. **LLM Response**: The LLM generates a response.
5. **Agent Output**: The agent processes the LLM's response and presents it to the user.

For tool-using agents (e.g., `2-tool-agent`), the flow might involve the LLM requesting the use of a tool, the agent executing the tool, and the tool's output being fed back to the LLM for further processing before a final response is generated.

## 5. Core Dependencies

The project relies on the following major external libraries (as defined in `requirements.txt`):

* **`google-adk[database]==0.3.0`**: The core Google Agent Development Kit framework. The `[database]` extra suggests capabilities for persistent storage.
* **`yfinance==0.2.56`**: Yahoo Finance API; likely used in an example agent that requires financial data.
* **`psutil==5.9.5`**: A cross-platform library for retrieving information on running processes and system utilization; its specific use case within an example agent would need further investigation.
* **`litellm==1.66.3`**: A library to simplify interactions with various LLM providers, allowing for easier switching between models.
* **`google-generativeai==0.8.5`**: The Google Generative AI SDK, used for direct interaction with Gemini models.
* **`python-dotenv==1.1.0`**: Used for managing environment variables by loading them from `.env` files.

## 6. Setup & Execution

Follow these steps to set up the development environment and run the examples:

### a. Environment Setup (Done once)

#### Via uv

```shell
uv init
uv venv
source .venv/bin/activate
```

#### Via Suggested Setup in README.md

1. **Create Virtual Environment** (in the root directory of the repository):

    ```bash
    python -m venv .venv
    ```

2. **Activate Virtual Environment**:
    * macOS/Linux:

        ```bash
        source .venv/bin/activate
        ```

    * Windows CMD:

        ```bash
        .venv\Scripts\activate.bat
        ```

    * Windows PowerShell:

        ```bash
        .venv\Scripts\Activate.ps1
        ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### b. Setting Up API Keys (For each example you want to run)

1. Obtain a `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/apikey) by creating a project and enabling the API.
2. Navigate to the specific agent's directory within an example folder (e.g., `cd 1-basic-agent/greeting_agent/`).
3. Rename the `.env.example` file in that directory to `.env`.
4. Open the `.env` file and replace the placeholder with your actual API key:

    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

### c. Running an Example

1. Ensure your virtual environment is active and the API key is set up for the desired example.
2. Navigate to the example's agent directory (e.g., `cd 1-basic-agent/greeting_agent/`).
3. Run the agent script:

    ```bash
    python agent.py
    ```

    (Or `python main.py` if the entry point is named `main.py` in some examples. Based on current findings, `agent.py` is common.)

## 7. Testing Strategy

No dedicated test files (e.g., `*_test.py`, `*.spec.js`) or specific test directories (e.g., `/tests`) were found in the repository at the time of this analysis.

Testing appears to be primarily manual, by running the individual agent examples and observing their behavior. There is no evidence of a formal unit, integration, or end-to-end testing framework being used across the examples.

## 8. Highlighted Conventions & Patterns

* **Modular Examples**: The codebase is organized into distinct, numbered example directories, each focusing on a specific ADK feature.
* **Environment Variables for Configuration**: API keys and other sensitive configurations are managed using `.env` files, with `.env.example` files serving as templates. This is a common pattern for security and configurability.
* **`agent.py` as Entry Point**: Within each example's specific module directory, `agent.py` typically serves as the main script or defines the core agent logic.
* **READMEs per Example**: Each numbered example folder contains its own `README.md` providing context for that specific example, supplementing the main project `README.md`.

## 9. Documentation Overview

The repository contains the following key documentation files:

* **`README.md` (Root Directory)**:
  * **Purpose**: Provides a general introduction to the ADK Crash Course, lists all the examples with brief descriptions, and gives detailed instructions for setting up the Python virtual environment and installing dependencies.
  * **Key Points**: Crucial for initial setup, understanding the project's goal, and navigating the different examples.
* **`GEMINI_MODELS.md` (Root Directory)**:
  * **Purpose**: Offers an overview of the various Google Gemini models compatible with ADK.
  * **Key Points**: Details model capabilities (input types, best use cases), pricing per million tokens (input/output), token information, and guidelines for selecting the appropriate model based on needs like budget, performance, or task complexity. It also links to the official Gemini API documentation for the most current information.
* **`/<example-name>/README.md`** (e.g., `1-basic-agent/README.md`):
  * **Purpose**: Provides specific information, context, and potentially more detailed running instructions for the individual example it resides in.

## 10. IDE and Coding System Rules

No specific IDE or coding system rule files (e.g., `.cursorrules`, `.windsurfrules`, `.roomodes`, linters configurations beyond standard Python practices) were identified in the repository. Development likely follows general Python conventions.

## 11. MCP (Model Control Protocol) Integrations

No MCP integration files (e.g., `mcp.json` in `.cursor`, `.vscode`, or `.windsurf` directories) were found. This project does not appear to use MCP integrations as per the file structure.

## 12. Environment Variables

The primary environment variable required by the examples is:

* **`GOOGLE_API_KEY`**:
  * **Purpose**: This key is essential for authenticating requests to Google's Generative AI services, which power the Gemini models used by the ADK agents.
  * **Location**: Each example's specific agent directory (e.g., `1-basic-agent/greeting_agent/`) contains a `.env.example` file. You need to copy this to `.env` and fill in your key.

It's possible that specific examples might introduce other environment variables, which would be documented in their respective `README.md` or `.env.example` files.

---
*This guide was generated based on a static analysis of the repository. Some dynamic behaviors or configurations might require runtime inspection.*
