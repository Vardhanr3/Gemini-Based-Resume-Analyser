import os
import docx2txt
import fitz  # PyMuPDF

def parse_resume(resume_path):
    ext = os.path.splitext(resume_path)[1].lower()

    if ext == ".docx":
        text = docx2txt.process(resume_path)
    elif ext == ".pdf":
        with fitz.open(resume_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
    else:
        raise ValueError("Unsupported file format. Please use a .pdf or .docx file.")
    
    return text