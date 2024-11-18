import streamlit as st

st.write('Hello worlddd')

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
