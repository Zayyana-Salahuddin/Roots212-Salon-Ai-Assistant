import streamlit as st
import json
import os
import uuid
import numpy as np
import faiss

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from groq import Groq

# =====================================
# CONFIG
# =====================================

st.set_page_config(
    page_title="Roots212 AI Assistant",
    page_icon="💇",
    layout="wide"
)

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =====================================
# GROQ CLIENT
# =====================================

@st.cache_resource
def get_client():
    return Groq(api_key=GROQ_API_KEY)

client = get_client()

# =====================================
# MODEL
# =====================================

@st.cache_resource
def load_model():
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

model = load_model()

# =====================================
# LOAD JSON
# =====================================

@st.cache_data
def load_data():

    with open(
        "salon_data.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

data = load_data()

# =====================================
# CREATE DOCUMENTS
# =====================================

docs = []

def flatten_json(obj):

    if isinstance(obj, dict):

        for k, v in obj.items():

            if isinstance(v, (dict, list)):
                flatten_json(v)

            else:
                docs.append(f"{k}: {v}")

    elif isinstance(obj, list):

        for item in obj:
            flatten_json(item)

flatten_json(data)

# =====================================
# EMBEDDINGS
# =====================================

@st.cache_resource
def create_faiss():

    embeddings = model.encode(docs)

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(embeddings)

    return index

index = create_faiss()

# =====================================
# SESSION STATE
# =====================================

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:

    chat_id = str(uuid.uuid4())

    st.session_state.current_chat = chat_id

    st.session_state.chats[chat_id] = []

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.image("roots.jpeg", width=180)

    st.title("Roots212 AI")

    if st.button("➕ New Chat"):

        new_id = str(uuid.uuid4())

        st.session_state.current_chat = new_id

        st.session_state.chats[new_id] = []

        st.rerun()

    st.divider()

    for cid in st.session_state.chats:

        if st.button(
            f"💬 {cid[:8]}",
            key=cid
        ):
            st.session_state.current_chat = cid
            st.rerun()

# =====================================
# HEADER
# =====================================

col1, col2 = st.columns([1, 4])

with col1:
    st.image("roots.jpeg", width=120)

with col2:
    st.title("Roots212 Hair Salon")
    st.caption(
        "Luxury Hair • Color • Styling • Botox"
    )

st.divider()

# =====================================
# BUTTONS
# =====================================

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "📅 Book Appointment",
        "https://roots212inc.salonist.io/booking-online"
    )

with c2:
    st.link_button(
        "📷 Instagram",
        "https://www.instagram.com/roots212hairsalon/"
    )

st.divider()

# =====================================
# CHAT
# =====================================

chat_history = st.session_state.chats[
    st.session_state.current_chat
]

for msg in chat_history:

    with st.chat_message(msg["role"]):

        st.markdown(
            msg["content"]
        )

# =====================================
# QUESTION
# =====================================

question = st.chat_input(
    "Ask about services, prices, booking..."
)

if question:

    chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    q_embedding = model.encode(
        [question]
    )

    D, I = index.search(
        np.array(q_embedding,
                 dtype=np.float32),
        5
    )

    context = "\n".join(
        [docs[i] for i in I[0]]
    )

    prompt = f"""
You are Roots212 Hair Salon AI Assistant.

Answer only using salon data.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[
        0
    ].message.content

    with st.chat_message(
        "assistant"
    ):
        st.write(answer)

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# =====================================
# FOOTER
# =====================================

st.divider()

st.markdown(
"""
### 📸 Follow Roots212

Instagram:
https://www.instagram.com/roots212hairsalon/

Website:
https://roots212.com
"""
)
