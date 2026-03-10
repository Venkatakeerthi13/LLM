import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chat Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:

    st.session_state.chat.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=st.session_state.chat
        )

        reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.chat.append({"role": "assistant", "content": reply})
