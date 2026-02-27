import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def create_plan(task_description):
    prompt = f"""
    Create step-by-step execution plan for this task:

    {task_description}
    """

    response = model.generate_content(prompt)
    return response.text