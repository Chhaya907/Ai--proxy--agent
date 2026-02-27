import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def execute_task(task_description):
    prompt = f"""
    Generate required output for this task.
    If coding task, generate code.
    If report task, generate structured report.

    Task:
    {task_description}
    """

    response = model.generate_content(prompt)
    output = response.text

    filename = "output.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output)

    return filename