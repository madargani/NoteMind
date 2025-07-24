import pymupdf4llm
import pymupdf
from pathlib import Path

def text_from_pdf(file_path: Path) -> str:
    doc = pymupdf.open(file_path) # open a document
    text = ''
    for page in doc: # iterate the document pages
        text += page.get_text()
    return text

if __name__ == '__main__':
    text = text_from_pdf('tests/sample_notes/globalization_families_and_social_change.pdf')
    print(text)
