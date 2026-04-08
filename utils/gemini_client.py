import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
from google.api_core.exceptions import GoogleAPIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key="AIzaSyBoWRgZWxnQaVyiscLBPjdWybNHTDNxijc")

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(text):
    prompt = f"""
    Analyze the following resume content and extract key information:
    1. Summary of skills
    2. Key projects and technologies
    3. Experience timeline
    4. Certifications or trainings
    5. Recommend suitable job roles

    Resume content:
    {text}
    """
    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return "❌ Gemini API quota exceeded. Please try again later or upgrade your plan."

    except GoogleAPIError as e:
        return f"❌ Gemini API error: {str(e)}"

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
