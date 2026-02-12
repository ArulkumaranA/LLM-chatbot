import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv("YOUR_PATH to ENV .env")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="LLM Chatbot")



model = genai.GenerativeModel("models/gemini-flash-latest")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat_session.send_message(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )

    with st.chat_message("assistant"):
        st.markdown(response.text)
import streamlit as st

st.title("LLM Chatbot")

prompt = st.text_input("Ask something:")

if prompt:
    st.write(prompt)
