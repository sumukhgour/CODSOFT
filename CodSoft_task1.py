import os
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = {}
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for task, status in tasks.items():
        print(f"[{'X' if status else ' '}] {task}")

def add_task(tasks, new_task):
    tasks[new_task] = False
    print(f"Task '{new_task}' added successfully.")

def complete_task(tasks, task_to_complete):
    if task_to_complete in tasks:
        tasks[task_to_complete] = True
        print(f"Task '{task_to_complete}' marked as completed.")
    else:
        print(f"Task '{task_to_complete}' not found.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_to_complete = input("Enter the task to mark as completed: ")
            complete_task(tasks, task_to_complete)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
