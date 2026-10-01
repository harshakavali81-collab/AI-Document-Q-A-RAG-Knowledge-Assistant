# Activate semantic search, live answers and hosting

Cloud entry point: `cloud/streamlit_app.py`. Its adjacent requirements file installs the base and optional semantic dependencies. MiniLM downloads automatically when you select semantic and build the index. Model weights are not bundled with the repository.

## Account steps

1. Sign in to https://share.streamlit.io and choose Create app.
2. Select repository `harshakavali81-collab/AI-Document-Q-A-RAG-Knowledge-Assistant`, branch `main`, main file `cloud/streamlit_app.py`.
3. Select Python 3.11 in advanced settings.
4. Enter these root-level TOML secrets using your own values:

```toml
GROQ_API_KEY = "YOUR_OWN_KEY"
GROQ_MODEL = "AN_ACTIVE_MODEL_ID_FROM_YOUR_GROQ_CONSOLE"
```

5. Deploy. Dependency installation and model download may take several minutes. Hosting resource limits can prevent semantic mode from fitting; use a larger Python host if needed.
6. Build the fictional samples in lexical mode first.
7. Select semantic and rebuild. This downloads the MiniLM model into the host cache.
8. Enable Groq AI answers and consent. Ask the annual-leave question and inspect its citation.

Do not commit actual secret values or paste them into chat. The app already supports the insufficient-information response and source inspection.

## Current validation status

The baseline project has passed GitHub tests. The cloud entry point has a local UI smoke test. A model-host connection from the assistant environment timed out; the semantic dependency installation was stopped. No Groq key/model or authorized Streamlit account is available in that environment. Therefore model download, live generated answers and public deployment remain unverified until the account steps complete. This file is deployment configuration, not proof of a working hosted URL.

Official documentation:
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management
