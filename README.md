# Gemini-Based Resume Analyzer

An AI-powered Resume Analyzer that uses Google Gemini (Generative AI) to extract, analyze, and generate insights from resumes in PDF and DOCX formats.

---

## Overview

This project automates resume analysis by:

* Extracting text from resumes
* Sending it to the Google Gemini API
* Generating structured insights such as:

  * Skills summary
  * Projects and technologies
  * Experience timeline
  * Certifications
  * Recommended job roles

---

## Features

* Resume Parsing
  Supports `.pdf` and `.docx` formats using:

  * PyMuPDF (fitz) for PDFs
  * docx2txt for DOCX

* Gemini AI Analysis
  Uses the `gemini-2.0-flash` model to generate structured insights

* Output Generation
  Displays results in terminal and supports saving as PDF

* Error Handling
  Handles API quota limits and API errors gracefully

---

## Project Structure

```
Gemini-Based-Resume-Analyser/
│
├── main.py
├── input/
├── output/
│
├── utils/
│   ├── parser.py
│   ├── gemini_client.py
│   ├── pdf_writer.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python
* Google Gemini API

Libraries:

* docx2txt
* PyMuPDF (fitz)
* fpdf
* python-dotenv

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/Vardhanr3/Gemini-Based-Resume-Analyser.git
cd Gemini-Based-Resume-Analyser
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_actual_api_key
```

Important:
Replace this line in `gemini_client.py`:

```
genai.configure(api_key="Azc")
```

with:

```
genai.configure(api_key=api_key)
```

---

## Usage

### Step 1: Place resume

Put your resume inside the `input/` folder
Example:

```
input/resume.pdf
```

### Step 2: Run the program

```
python main.py
```

### Step 3: Enter file path

Example:

```
input/resume.pdf
```

### Step 4: Output

* Extracted text preview is shown in terminal
* Full AI-generated analysis is displayed
* Optional PDF report can be saved in `output/`

---

## How It Works

1. User inputs resume path
2. Text is extracted using parser module
3. Extracted content is sent to Gemini API
4. Gemini generates structured insights
5. Results are displayed or saved

---

## Sample Output

```
Skills:
- Python, Machine Learning, Web Development

Projects:
- Resume Analyzer using Gemini API

Experience:
- Internship at XYZ

Recommended Roles:
- Software Developer
- Data Analyst
```

---

## Limitations

* Requires internet access
* Subject to Gemini API quota limits
* Output quality depends on resume content

---

## Future Improvements

* Web interface using Streamlit
* Drag-and-drop resume upload
* Job description matching
* ATS score calculation
* Multi-resume comparison

---

## Author

Trivardhan (Vardhanr3)
GitHub: [https://github.com/Vardhanr3](https://github.com/Vardhanr3)
* optimize this README for ATS keywords
* or convert this project into a web app for stronger impact on your resume
