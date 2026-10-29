# EvidenceDesk — AI Document Q&A / RAG Knowledge Assistant

A portfolio project for Kavali Harshavardhan. Upload PDF, DOCX or TXT documents, retrieve relevant passages and inspect their source locations. Enable semantic retrieval and optional Groq generation for a full RAG workflow.

[Setup](#local-installation--setup-guide) · [Architecture](#architecture--system-design-diagram) · [Detailed guide](PROJECT_GUIDE.md) · [Repository standard](docs/REPOSITORY_STANDARD.md)

## Visuals

![Project architecture](<docs/diagrams/architecture.png>)

Existing project visual; diagrams and illustrative graphics are not evidence of a deployed application.

## Live Link / Demo

Run the local demo using the setup guide below. No public deployment URL has been verified for this documentation update.

## Key Features

- Source and supporting materials indexed in [Repository standard](docs/REPOSITORY_STANDARD.md).
- Detailed methodology and project context in [Project guide](PROJECT_GUIDE.md).

## Tech Stack

![Python](https://img.shields.io/badge/Python-334155?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-334155?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-334155?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-334155?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-334155?style=flat-square)

Dependency versions and optional packages are defined in the repository manifests.

## Architecture / System Design Diagram

[Architecture documentation / diagram](<docs/diagrams/architecture.png>)

## Local Installation & Setup Guide

```bash
git clone https://github.com/harshakavali81-collab/AI-Document-Q-A-RAG-Knowledge-Assistant.git
cd AI-Document-Q-A-RAG-Knowledge-Assistant
```

1. Clone or download this repository and open its root folder in VS Code.
2. Select **Terminal → New Terminal**. Run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Python 3.11 or 3.12 is recommended. If `py -3.11` is unavailable but Python is installed, use `python -m venv .venv`.

3. Open http://localhost:8501. Keep **Use fictional sample documents** checked and click **Build knowledge base**.
4. Ask: **How many annual leave days are available?** The sample answer contains 18 days and a source citation.
5. Expand a source to inspect the evidence. Upload your files and rebuild to replace the index. Ask complete standalone questions: conversational history is displayed, but follow-up question rewriting is not implemented.

macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

## Challenges & Solutions

**Repository organization:** this project uses `src/`. Keeping those paths stable avoids breaking imports, asset links and deployment commands while the documentation follows a shared format. Project-specific technical limitations and prior release evidence are retained in [Project guide](PROJECT_GUIDE.md).

## Future Improvements

- Capture a reproducible end-to-end demo with runtime versions and sample inputs.
- Expand regression checks for invalid inputs and documented edge cases.
- Record measured results, data provenance and deployment limitations alongside each release.

## Scope and supporting evidence

A portfolio project for Kavali Harshavardhan. Upload PDF, DOCX or TXT documents, retrieve relevant passages and inspect their source locations. Enable semantic retrieval and optional Groq generation for a full RAG workflow.

**Honest status:** The local lexical/excerpt path is tested. Semantic retrieval and live LLM generation are implemented but require a model download/API access and were not exercised live in the build environment. GitHub location: https://github.com/harshakavali81-collab/AI-Document-Q-A-RAG-Knowledge-Assistant. No public app deployment is included. Fictional sample documents are clearly labeled. No paid service, cloud account or API key is bundled.

## Repository Structure

| Location | Purpose |
| --- | --- |
| `src/` | Source modules |
| `tests/` | Tests |
| `docs/` | Documentation |
| `data/` | Data and samples |
| `.github/` | Issue forms, PR template and automated checks |

[Complete file inventory and workflow](docs/REPOSITORY_STANDARD.md). Runtime entry points retain their existing paths.

## Workflow & Tracking

Use the [bug and feature forms](https://github.com/harshakavali81-collab/AI-Document-Q-A-RAG-Knowledge-Assistant/issues/new/choose) to define work with acceptance criteria. Keep tasks in Todo → In progress → Review → Done, and link a pull request with `Closes #<number>`. See [the maintenance workflow](docs/REPOSITORY_STANDARD.md#workflow).

## License

Original project software is available under the [MIT License](LICENSE). See [licensing scope](docs/LICENSING.md) for third-party and data exclusions.

