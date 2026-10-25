# IBM DevOps Capstone Project

[![Build Status](https://github.com/Shreyaslad99/ibm-devops-capstone/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Shreyaslad99/ibm-devops-capstone/actions/workflows/ci-build.yaml)

A starter project for the IBM DevOps and Software Engineering capstone. It includes a Flask REST API for account CRUD operations, unit tests, and a GitHub Actions workflow.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

The API runs locally on `http://127.0.0.1:8080`.

## Test

```bash
pytest
```

## CI

GitHub Actions runs the test suite on pushes and pull requests to `main`. See the [workflow runs](https://github.com/Shreyaslad99/ibm-devops-capstone/actions).

## Project files

- `service/`: Flask application and REST routes
- `tests/`: automated tests
- `.github/workflows/ci-build.yaml`: CI build workflow
- `user-story.md`: sample user story
- `submission/EVIDENCE_CHECKLIST.md`: checklist for the course rubric

## Evidence and course requirements

This repository is a starter scaffold, not a claim that every capstone task has already been completed. Replace the evidence templates under `submission/templates/` with actual outputs captured from your own environment. Add the required screenshots for your Kanban board, REST API commands, security/CORS tests, container/Kubernetes tasks, and Tekton pipeline. Do not submit placeholder text as real evidence.
