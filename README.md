# Resume Insight Generator using Gemini AI

## 🔍 Features
- Accepts .docx or .pdf resumes
- Extracts Skills, Projects, Trainings, and Experience
- Uses Gemini AI to suggest job roles and justify match
- Generates a summary report as PDF

## 🚀 Run Locally
```bash
pip install -r requirements.txt
python main.py
```

## 📁 Structure
- `utils/parser.py`: Extracts text from resumes
- `utils/gemini_client.py`: Sends prompt to Gemini AI
- `utils/report.py`: Generates PDF report