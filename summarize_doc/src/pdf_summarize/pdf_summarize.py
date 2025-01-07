from ..summarize.helper_function import summarize_text
from PyPDF2 import PdfReader

class PDFSummarize:
    def __init__(self, file_path, summarization_length=5):
        self.file_path = file_path
        raw_text = self.get_pdf_text()
        self.text = summarize_text(raw_text, num_sentences=summarization_length)

    def get_pdf_text(self):
        text = ""
        reader = PdfReader(self.file_path)
        for page in reader.pages:
            text += page.extract_text()
        return text

