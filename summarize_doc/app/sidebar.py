import streamlit as st
from summarize_doc.src.pdf_summarize.pdf_summarize import PDFSummarize
from summarize_doc.src.txt_summarize.txt_summarize import TxtSummarize

def sidebar_view():
    with st.sidebar:
        st.subheader("Your Document")
        docs_file = st.file_uploader("Upload a document", type=['txt', 'pdf'])
        summarization_type = st.radio("Set summarization type :", key="visiblity", options=["Sentences", "Bullet Points"])
        summarization_length = st.number_input("Number of Sentences", key="num_sentences", min_value=1, max_value=10, value=5, step=1)

        if st.button('Process'):
            with st.spinner("Processing ... "):
                if docs_file.type == 'application/pdf':
                    summarized_text = PDFSummarize(docs_file, summarization_length=summarization_length).text
                    if summarization_type == "Sentences":
                        st.session_state.extracted_text = summarized_text
                    else:
                        summarized_text = summarized_text.replace(". ", ".\n\n")
                        st.session_state.extracted_text = summarized_text
                elif docs_file.type == 'text/plain':
                    summarized_text = TxtSummarize(docs_file).text
                    if summarization_type == "Sentences":
                        st.session_state.extracted_text = summarized_text
                    else:
                        summarized_text = summarized_text.replace(". ", ".\n • \n")
                        st.session_state.extracted_text = summarized_text
                else:
                    st.warning("Please upload a valid file type (txt or pdf)")