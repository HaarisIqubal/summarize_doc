from ..summarize.helper_function import summarize_text

class TxtSummarize:
    def __init__(self, file_path):
        self.file_path = file_path
        raw_text = self.get_txt_text()
        self.text = summarize_text(raw_text)

    def get_txt_text(self):
        try:
            text = ""
            text = self.file_path.read().decode("utf-8")
            return text
        except Exception as e:
            raise RuntimeError(f"Error reading the file at {self.file_path}: {e}")
    