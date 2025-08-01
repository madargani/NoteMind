import streamlit as st
from pathlib import Path

from src.notemind_management.list_noteminds import list_noteminds
from src.note_management.get_notes import get_notes
from src.note_management.add_note import add_note

# Sidebar
st.sidebar.header("Active Notemind")
active_notemind = st.sidebar.selectbox(
    label='Active Notemind',
    label_visibility='collapsed',
    options=[x.name for x in list_noteminds()])

st.sidebar.header("Add Notes")
note_path = st.sidebar.text_input(
    label='note_path',
    label_visibility='collapsed',
    placeholder='file path'
)
if st.sidebar.button(label='Add'):
    add_note(active_notemind, Path(note_path))

st.sidebar.header("Active Notes")
active_notes = []
for note in get_notes(active_notemind):
    if st.sidebar.checkbox(note, True):
        active_notes.append(note)

# Title and header
st.title("Notemind")
st.header(active_notemind)

prompt = st.chat_input("Ask about your notes")

with st.chat_message('user'):
    st.write('hello')
with st.chat_message('assistant'):
    st.write('hello back')
