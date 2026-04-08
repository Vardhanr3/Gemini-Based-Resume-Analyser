from utils.parser import parse_resume
from utils.gemini_client import analyze_resume

def main():
    resume_path = input("Enter the resume file path (PDF or DOCX): ")
    text = parse_resume(resume_path)
    
    print("\nExtracted Text:\n")
    print(text[:1000])  # Show a preview of extracted text

    print("\nAnalyzing Resume with Gemini...\n")
    report = analyze_resume(text)
    print(report)

if __name__ == "__main__":
    main()
