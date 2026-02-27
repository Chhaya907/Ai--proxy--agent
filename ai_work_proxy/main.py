from memory import init_db, save_task
from task_analyzer import analyze_task
from planner import create_plan
from executor import execute_task

status = "Away"

def main():
    if status != "Away":
        print("Employee available. Agent sleeping.")
        return

    print("Agent Activated...")

    email_content = "Fix the login authentication bug before tomorrow."

    task = analyze_task(email_content)
    print("Task Analysis:\n", task)

    plan = create_plan(task)
    print("Execution Plan:\n", plan)

    output_file = execute_task(task)
    print("Output saved in:", output_file)

    save_task(task, plan, output_file)

    print("Task completed and stored in memory.")

if __name__ == "__main__":
    init_db()
    main()