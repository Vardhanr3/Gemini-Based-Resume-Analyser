import docx
import fitz  # PyMuPDF

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_resume(file_path):
    if file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format.")