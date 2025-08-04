import streamlit as st

from src.streamlit.sidebar import sidebar
from src.streamlit.chat_interface import chat_interface

from src.querying.ask import ask

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Side bar
# Assigns st.session_state.active_notemind
sidebar()

# Title and header
st.title("Notemind")
st.header(st.session_state.active_notemind)

# Chat interface
chat_interface()
