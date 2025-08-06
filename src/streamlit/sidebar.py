import streamlit as st
from pathlib import Path

from src.notemind_management.create_notemind import create_notemind
from src.notemind_management.list_noteminds import list_noteminds
from src.note_management.get_notes import get_notes
from src.note_management.add_note import add_note

def sidebar():
    # Notemind menu
    st.sidebar.header("Active Notemind")
    st.session_state.active_notemind = st.sidebar.selectbox(
        label='Active Notemind',
        label_visibility='collapsed',
        options=[x.name for x in list_noteminds()])

    with st.sidebar.popover('New Notemind'):
        st.header('Create New Notemind')
        notemind_name = st.text_input(
            label='Notemind name',
            label_visibility='collapsed',
            placeholder='Notemind name'
        )
        if st.button(label='Create'):
            create_notemind(notemind_name)
            st.session_state.active_notemind = notemind_name
            st.rerun()

    # Note menu
    st.sidebar.header("Add Notes")
    note_path = st.sidebar.text_input(
        label='Note path',
        label_visibility='collapsed',
        placeholder='file path'
    )
    if st.sidebar.button(label='Add'):
        add_note(st.session_state.active_notemind, Path(note_path))

    st.sidebar.header("Active Notes")
    active_notes = []
    for note in get_notes(st.session_state.active_notemind):
        if st.sidebar.checkbox(note, True):
            active_notes.append(note)
