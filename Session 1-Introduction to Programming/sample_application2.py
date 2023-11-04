import tkinter as tk

# Data: Initialize an empty list to store tasks
tasks = []

# Process: Function to add a task to the list
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, "end")

# Process: Function to remove a selected task
def remove_task():
    selected_task = listbox_tasks.get("active")
    if selected_task:
        tasks.remove(selected_task)
        update_listbox()

# Process: Function to update the list of tasks in the GUI
def update_listbox():
    listbox_tasks.delete(0, "end")
    for task in tasks:
        listbox_tasks.insert("end", task)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create data: Input field for adding tasks
label_task = tk.Label(app, text="Add a task:")
entry_task = tk.Entry(app)

# Create data: Listbox to display tasks
listbox_tasks = tk.Listbox(app)
listbox_tasks.pack()

# Create a button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task)

# Create a button to remove selected tasks
remove_button = tk.Button(app, text="Remove Task", command=remove_task)

# Create a basic layout for the GUI
label_task.pack()
entry_task.pack()
add_button.pack()
remove_button.pack()

# Start the GUI application
app.mainloop()
