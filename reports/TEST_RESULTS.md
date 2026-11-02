# Test evidence

Executed locally on 2026-10-22 with Python 3.12, Streamlit 1.66.1, pandas 2.2.3 and pytest 9.1.1.

Command: `python -m pytest -q`

Result: **9 passed, 0 failed**.

Coverage includes domain calculations and edge cases, human-review gate validation, final-decision immutability, audit tamper detection, Streamlit startup and a project-specific UI interaction. Where optional local inference exists, its adapter is tested with a mock; no live-model performance is claimed.

`python -m portfolio.demo` completed successfully and regenerated JSON and SVG outputs. Initial UI tests exposed an entrypoint-path issue; it was corrected to resolve the app path relative to the test file before the passing run.

These are local test results. See the repository Actions tab for independently executed remote CI results; no remote pass is implied by this report.


## Cleanup validation — 2026-11-02

Executed locally with Python 3.12, Streamlit 1.66.1, pandas 2.3.3, pytest 9.2.0 and Ruff 0.17.3:

- `python -m pytest -q`: **10 passed** (25.46 seconds).
- `ruff check .`: passed.
- `ruff format --check .`: passed.
- `python -m portfolio.demo`: regenerated synthetic outputs successfully.

The added UI regression confirms that checking factual support and then editing the draft resets the confirmation. No live Ollama experiment, Docker/dev-container build or production deployment was performed. Remote CI status is separate from these local results.
