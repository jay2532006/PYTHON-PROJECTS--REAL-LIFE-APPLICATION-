import os

def load_tasks(file_name):
    """Load tasks from a file and return them as a list."""
    tasks = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                task, status = line.strip().rsplit('|', 1)
                tasks.append({'task': task, 'completed': status == 'True'})
    return tasks

def save_tasks(file_name, tasks):
    """Save tasks to a file."""
    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append({'task': task, 'completed': False})
    print("Task added successfully!")

def remove_task(tasks, task_number):
    """Remove a task by its number."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: {removed_task['task']}")
    else:
        print("Invalid task number!")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[Completed]" if task['completed'] else "[Incomplete]"
            print(f"{i}. {task['task']} {status}")

def mark_task(tasks, task_number, complete=True):
    """Mark a task as complete or incomplete."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = complete
        status = "completed" if complete else "incomplete"
        print(f"Task {task_number} marked as {status}.")
    else:
        print("Invalid task number!")

def main():
    file_name = 'tasks.txt'
    tasks = load_tasks(file_name)

    while True:
        print("\n--- To-Do List Application ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Mark Task as Incomplete")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task description: ")
            add_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(tasks, task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to mark as complete: "))
                mark_task(tasks, task_number, True)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to mark as incomplete: "))
                mark_task(tasks, task_number, False)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '6':
            save_tasks(file_name, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
