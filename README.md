# MCP-Paper-Reviewer
AI-powered academic paper reviewer built using Model Context Protocol (MCP) and OpenAI tool calling.
This project simulates a lightweight conference-style peer review system that can analyze research papers, detect logical gaps, and identify missing citations through structured AI tools.

## Project Structure:
* server.py        — MCP server exposing review tools (paper analysis logic)
* client.py        — OpenAI client that connects to the MCP server and invokes tools
* checklist.txt    — Review checklist / rubric for evaluation
* .env             — Environment variables (API keys, config; not committed)
* pyproject.toml   — Python project metadata and dependencies
* main.py — optional entrypoint / orchestration script.

## Requirements
1. Python 3.10+ (Use a virtual Environment)


## Features

* Load and review academic papers from `.txt` files
* Detect logical gaps and reasoning flaws
* Identify missing or weak citations
* Structured tool-based AI reasoning
* MCP-based modular architecture
* Suitable for experimentation with LLM tool calling

---

## Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd referee-ai
```

### 2. Create and Activate Virtual Environment

**Windows (PowerShell):**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

If using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or if using `pyproject.toml`:

```bash
pip install .
```

---

### 4. Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

**Do not commit `.env` to source control.**

---

## Running the Project

### Start the MCP Server

```bash
python server.py
```

### Run the Client (New Terminal)

```bash
python client.py server.py
```

---

## Example Usage

User prompt in client:

```
Load paper from ./papers/sample.txt and review it for ICLR.
```

The client will automatically:

1. Load the paper
2. Call analysis tools
3. Generate a structured AI review

---

## Notes

* `paper.txt` is only a sample — you can load **any `.txt` research paper**.
* `checklist.txt` controls evaluation criteria and can be customized.

---

## Team Memebers:
1. Aishwarya Gadhave
2. Vishwajeet Godse
3. Vaishnavi Repal
---

## Contributing

Contributions and feature ideas are welcome.
Open an issue to discuss improvements such as:

---

## License

No license specified yet.
Add a `LICENSE` file if you plan to distribute or publish publicly.

---


