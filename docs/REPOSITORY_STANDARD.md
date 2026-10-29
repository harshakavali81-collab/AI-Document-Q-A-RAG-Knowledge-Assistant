# Repository standard

## Layout

This repository keeps its working source paths. A shared portfolio structure does not require moving a React application, Python package, BI workbook or Verilog project into identical runtime directories.

| Area | Convention |
| --- | --- |
| Landing page | `README.md`: purpose, visuals, demo, features, stack, architecture, setup, tradeoffs and roadmap |
| Detailed reference | `PROJECT_GUIDE.md`: retained project-specific explanation and historical release notes |
| Documentation | `docs/`: design, inventory, reproduction and evidence |
| Work intake | `.github/ISSUE_TEMPLATE/`: bug and feature forms |
| Review | `.github/PULL_REQUEST_TEMPLATE.md`: linked issue, behavior and validation |
| Automation | `.github/workflows/portfolio-docs.yml`: README section and local-link checks |
| Source and tests | Existing project-specific paths listed below; no empty source/test placeholders |

## Workflow

1. Open an issue describing the user problem and measurable acceptance criteria.
2. Add it to a GitHub Project with Todo, In progress, Review and Done states when a board is configured.
3. Use a focused branch and meaningful commits, such as `docs: correct local setup paths` or `fix(api): reject malformed input`.
4. Run the project's documented checks and `python scripts/check_portfolio_docs.py`.
5. Open a pull request with actual validation results and `Closes #<issue-number>`.
6. Merge after review; record release evidence and update the issue/board.

Board creation, profile pins, repository social previews and milestone settings require account-level configuration. This file does not claim those settings have been applied.

## Validation scope

The documentation check validates the landing-page headings and local link targets only. It does not execute models, certify test coverage, inspect Git history for secrets, verify external websites, or prove production readiness. Existing application workflows remain the source of runtime CI evidence.

Keep credentials in local environment variables. A gitignore rule does not remove secrets already tracked or committed. Use only permitted sample data in public demos.

## Inventory at standardization

The following are the pre-existing public project files. New standardization files are described above. Historical guides may mention external bundles that are not part of this list.

- [`Dockerfile`](<../Dockerfile>)
- [`PACKAGE_CONTENTS.md`](<../PACKAGE_CONTENTS.md>)
- [`README.md`](<../README.md>)
- [`START_HERE.txt`](<../START_HERE.txt>)
- [`app.py`](<../app.py>)
- [`cli.py`](<../cli.py>)
- [`cloud`](<../cloud>)
- [`cloud/requirements.txt`](<../cloud/requirements.txt>)
- [`cloud/streamlit_app.py`](<../cloud/streamlit_app.py>)
- [`data`](<../data>)
- [`data/sample_documents`](<../data/sample_documents>)
- [`data/sample_documents/people_policy.txt`](<../data/sample_documents/people_policy.txt>)
- [`data/sample_documents/product_guide.txt`](<../data/sample_documents/product_guide.txt>)
- [`data/sample_documents/security_policy.txt`](<../data/sample_documents/security_policy.txt>)
- [`docs`](<../docs>)
- [`docs/ACTIVATE_LIVE_APP.md`](<../docs/ACTIVATE_LIVE_APP.md>)
- [`docs/AI_Document_QA_RAG_Full_Project_Guide.pdf`](<../docs/AI_Document_QA_RAG_Full_Project_Guide.pdf>)
- [`docs/DATA_DICTIONARY.md`](<../docs/DATA_DICTIONARY.md>)
- [`docs/DEMO_AND_INTERVIEW.md`](<../docs/DEMO_AND_INTERVIEW.md>)
- [`docs/GITHUB_AND_DEPLOYMENT.md`](<../docs/GITHUB_AND_DEPLOYMENT.md>)
- [`docs/PROJECT_REPORT.md`](<../docs/PROJECT_REPORT.md>)
- [`docs/VALIDATION.md`](<../docs/VALIDATION.md>)
- [`docs/WORKFLOW_AND_CODE_EXPLAINED.md`](<../docs/WORKFLOW_AND_CODE_EXPLAINED.md>)
- [`docs/Workflow_and_Structure_Diagrams.pdf`](<../docs/Workflow_and_Structure_Diagrams.pdf>)
- [`docs/diagrams`](<../docs/diagrams>)
- [`docs/diagrams/answer_flow.mmd`](<../docs/diagrams/answer_flow.mmd>)
- [`docs/diagrams/answer_flow.png`](<../docs/diagrams/answer_flow.png>)
- [`docs/diagrams/answer_flow.svg`](<../docs/diagrams/answer_flow.svg>)
- [`docs/diagrams/architecture.mmd`](<../docs/diagrams/architecture.mmd>)
- [`docs/diagrams/architecture.png`](<../docs/diagrams/architecture.png>)
- [`docs/diagrams/architecture.svg`](<../docs/diagrams/architecture.svg>)
- [`docs/diagrams/structure.mmd`](<../docs/diagrams/structure.mmd>)
- [`docs/diagrams/structure.png`](<../docs/diagrams/structure.png>)
- [`docs/diagrams/structure.svg`](<../docs/diagrams/structure.svg>)
- [`docs/tested-versions.txt`](<../docs/tested-versions.txt>)
- [`evaluation`](<../evaluation>)
- [`evaluation/RAG_Evaluation_Workbook.xlsx`](<../evaluation/RAG_Evaluation_Workbook.xlsx>)
- [`evaluation/__init__.py`](<../evaluation/__init__.py>)
- [`evaluation/evaluate.py`](<../evaluation/evaluate.py>)
- [`evaluation/evaluation_results.csv`](<../evaluation/evaluation_results.csv>)
- [`evaluation/questions.json`](<../evaluation/questions.json>)
- [`evaluation/results.json`](<../evaluation/results.json>)
- [`requirements-dev.txt`](<../requirements-dev.txt>)
- [`requirements-semantic.txt`](<../requirements-semantic.txt>)
- [`requirements.txt`](<../requirements.txt>)
- [`src`](<../src>)
- [`src/__init__.py`](<../src/__init__.py>)
- [`src/answering.py`](<../src/answering.py>)
- [`src/core.py`](<../src/core.py>)
- [`tests`](<../tests>)
- [`tests/test_pipeline.py`](<../tests/test_pipeline.py>)
