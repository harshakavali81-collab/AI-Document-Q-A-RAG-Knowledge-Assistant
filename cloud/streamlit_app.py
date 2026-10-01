"""Community Cloud entry point with optional semantic dependencies."""
from pathlib import Path
import os
import runpy
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
# Root-level Community Cloud secrets are normally also environment variables.
# This explicit bridge keeps the existing app compatible with st.secrets.
for name in ("GROQ_API_KEY", "GROQ_MODEL"):
    if not os.getenv(name):
        try:
            value = st.secrets.get(name)
        except (FileNotFoundError, st.errors.StreamlitSecretNotFoundError):
            value = None
        if value:
            os.environ[name] = str(value)
runpy.run_path(str(ROOT / "app.py"), run_name="__main__")
