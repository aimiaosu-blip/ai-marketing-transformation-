# How one draft moves through the prototype

`data/briefs.json` + `data/brand_policy.json` → `generate()` → editable Streamlit text → `evaluate()` → factual confirmation → `ReviewStore.decide()`.

## Responsibilities

- `app.py` handles inputs, draft session state, metrics display and the review form.
- `portfolio/marketing.py` holds the template, optional Ollama adapter, phrase checks and workflow arithmetic. Only the explicitly selected Ollama path makes a network request.
- `portfolio/governance.py` hashes an artifact and stores its decision in SQLite using a transaction. It rejects missing reviewer/reason, blocked approvals and repeat decisions for the same artifact.
- `portfolio/demo.py` reproduces committed outputs from synthetic input files.

## What gets versioned

The artifact hash covers text, policy, evaluation and factual-confirmation status. A text or policy change gives the checkbox a new Streamlit key, requiring fresh factual confirmation. The database stores the hash and decision metadata, not the full draft; it is not a document-history or restore feature.

Review rows include the preceding row's hash. Verification can detect edits that break the chain, but an administrator can delete or rewrite the database. Aliases are not authenticated identities.

## Separate sources of evidence

Dashboard labour metrics come from `data/workflow.json`. They are not timings collected from the interactive editor. A saved approval does not change that synthetic dataset.

A rule pass means only that no configured phrase/length violation was detected. Human factual confirmation remains necessary. The application does not publish content or implement organisational approval authority.

## Development environment

The dev container supplies Python and installs development dependencies. It does not run a model or deploy the app. Dependency ranges and the image tag can resolve differently over time; use a reviewed lock/snapshot if exact environment reproduction becomes a research requirement.
