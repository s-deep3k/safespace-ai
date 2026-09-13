# SETUP STREAMLIT
import streamlit as st
st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 SafeSpace - AI Mental Health Therapist")
# Check if chat history exists in session state, if not initialize it
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# User asks question
user_input = st.chat_input("Whats on your mind? (Type 'exit' to end the session)")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    fixed_dummy_response = "I'm here to listen. Can you tell me more about how you're feeling?"
    st.session_state.chat_history.append({"role": "assistant", "content": fixed_dummy_response})

# Show response from Backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
