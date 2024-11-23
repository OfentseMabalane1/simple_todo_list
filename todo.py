import tkinter as tk
import sqlite3
from tkinter import messagebox  

DB_FILE = 'todo.db'

def create_database():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            due_date TEXT,
            due_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_task(description, due_date, due_time):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO tasks (description, due_date, due_time)
        VALUES (?, ?, ?)
    ''', (description, due_date, due_time))
    conn.commit()
    conn.close()

def load_tasks():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def update_task_list():
    tasks = load_tasks()
    task_listbox.delete(0, tk.END)
    for task in tasks:
        if len(task) >= 4:
            task_listbox.insert(tk.END, f"{task[0]} | {task[1]} - Due: {task[2]} {task[3]}")  
        else:
            task_listbox.insert(tk.END, f"{task[1]} - Due Date/Time Not Set")

def add_task():
    description = task_entry.get().strip()  # Get input and remove any leading/trailing whitespace
    due_date = date_entry.get().strip()
    due_time = time_entry.get().strip()

    if description and due_date and due_time:
        save_task(description, due_date, due_time)
        update_task_list()
        error_label.config(text="")
        # Clear the input fields after adding a task
        task_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        error_label.config(text="Please fill in all fields.")

def delete_selected_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = int(selected_task.split(" | ")[0])  
        delete_task(task_id)  
        update_task_list()  
    except tk.TclError:
        messagebox.showwarning("No task selected", "Please select a task to delete.")
    except ValueError:
        messagebox.showwarning("Invalid selection", "Selected task does not have a valid ID.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Setting the background color to black
root.configure(bg='black')

create_database()

# Labels with yellow text on black background
task_label = tk.Label(root, text="Task Description:", bg='black', fg='yellow')
task_label.pack()

# Entry fields with black background and yellow text
task_entry = tk.Entry(root, bg='black', fg='yellow')
task_entry.pack()

date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):", bg='black', fg='yellow')
date_label.pack()

date_entry = tk.Entry(root, bg='black', fg='yellow')
date_entry.pack()

time_label = tk.Label(root, text="Due Time (HH:MM):", bg='black', fg='yellow')
time_label.pack()

time_entry = tk.Entry(root, bg='black', fg='yellow')
time_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task, bg='black', fg='yellow')
add_button.pack()

# Listbox with black background and yellow text
task_listbox = tk.Listbox(root, width=50, height=10, bg='black', fg='yellow')
task_listbox.pack()

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_selected_task, bg='black', fg='yellow')
delete_button.pack()

error_label = tk.Label(root, text="", fg="red", bg='black')  
error_label.pack()

update_task_list()

# Start the Tkinter event loop
root.mainloop()
