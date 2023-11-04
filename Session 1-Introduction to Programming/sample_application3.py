import sys

# Data: Initialize an empty list to store tasks
tasks = []

# Process: Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added: ", task)

# Process: Function to list all tasks
def list_tasks():
    print("Task List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Process: Function to remove a task
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Task removed: ", removed_task)
    else:
        print("Invalid task index.")

# Process: Function to show usage instructions
def show_usage():
    print("Usage:")
    print("add <task_description> - Add a new task")
    print("list - List all tasks")
    print("remove <task_index> - Remove a task by index")
    print("exit - Exit the program")

# Main loop for the command-line app
while True:
    command = input("Enter a command: ").strip()
    command_parts = command.split()

    if command_parts[0] == "add":
        if len(command_parts) > 1:
            task = " ".join(command_parts[1:])
            add_task(task)
        else:
            print("Please provide a task description.")

    elif command_parts[0] == "list":
        list_tasks()

    elif command_parts[0] == "remove":
        if len(command_parts) > 1:
            try:
                task_index = int(command_parts[1])
                remove_task(task_index)
            except ValueError:
                print("Invalid task index.")
        else:
            print("Please provide a task index to remove.")

    elif command_parts[0] == "exit":
        break

    else:
        show_usage()

print("Task manager closed.")
