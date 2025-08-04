import streamlit as st

from src.querying.ask import ask

def chat_interface():
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt := st.chat_input("Ask about your notes"):
        with st.chat_message('user'):
            st.markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        response = ask(st.session_state.active_notemind, prompt)
        with st.chat_message('assistant'):
            st.markdown(response)
        st.session_state.messages.append({'role': 'assistant', 'content': response})

