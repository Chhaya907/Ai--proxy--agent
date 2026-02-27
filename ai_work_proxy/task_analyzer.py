import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_task(email_content):
    prompt = f"""
    Extract:
    - Main Task
    - Task Type (bug fix, feature, report, documentation)
    - Urgency level

    Email:
    {email_content}
    """

    response = model.generate_content(prompt)
    return response.text