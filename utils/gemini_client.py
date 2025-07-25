import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def analyze_resume(text):
    prompt = f"""
    You are a career advisor AI. Analyze this resume:
    \"\"\"{text}\"\"\"

    1. Summarize the resume’s:
       - Skills
       - Projects
       - Trainings
       - Experience

    2. Suggest 3 job roles this person fits best

    3. Justify how the skills and projects support the suggested roles
    """

    response = model.generate_content(prompt)
    return response.text