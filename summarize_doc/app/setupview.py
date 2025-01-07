import streamlit as st
from .sidebar import sidebar_view
def setup_view():
    st.set_page_config(page_title='Summarize Document', page_icon='📑', layout='centered')
    st.title('Summarize Document 📑')
    st.write("This app summarizes text from a document. You can upload a text or PDF file and get a summary of the text.")
    if 'extracted_text' not in st.session_state:
        st.session_state.extracted_text = ""
    sidebar_view()
    st.write(st.session_state.extracted_text)



