from utils.parser import parse_resume
from utils.gemini_client import analyze_resume
from utils.report import save_pdf

def main():
    resume_path = input("Enter path to resume (.pdf/.docx): ").strip()
    text = parse_resume(resume_path)
    print("✅ Resume extracted.")

    report = analyze_resume(text)
    print("✅ Gemini AI analysis complete.")

    save_pdf(report)
    print("📄 Report saved as output/report.pdf")

if __name__ == "__main__":
    main()