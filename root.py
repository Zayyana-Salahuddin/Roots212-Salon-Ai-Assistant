# Replace this file with your actual application code.
# Suggested API key loading:

import os
import streamlit as st

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
