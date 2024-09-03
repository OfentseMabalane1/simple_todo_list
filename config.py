import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
from tkcalendar import Calendar

def create_user_table():
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )''')

def create_tasks_table():
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        date TEXT,
                        time TEXT
                    )''')
        
        c.execute('''PRAGMA table_info(tasks)''')
        columns = [column[1] for column in c.fetchall()]
        if 'date' not in columns:
            c.execute('''ALTER TABLE tasks ADD COLUMN date TEXT''')
        if 'time' not in columns:
            c.execute('''ALTER TABLE tasks ADD COLUMN time TEXT''')
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to create tasks table: {e}')



def register_user():
    username = reg_username_entry.get().strip()
    password = reg_password_entry.get().strip()
    if not username or not password:
        messagebox.showerror('Error', 'Username and password cannot be empty')
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        messagebox.showinfo('Success', 'User registered successfully')
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to register user: {e}')

def login():
    global logged_in_user
    username = login_username_entry.get().strip()
    password = login_password_entry.get().strip()
    if not username or not password:
        messagebox.showerror('Error', 'Username and password cannot be empty')
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
        user = c.fetchone()
        if user:
            logged_in_user = username
            messagebox.showinfo('Success', 'Login successful')
            enable_task_functions()
            login_window.destroy()
            return
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to login: {e}')
    messagebox.showerror('Error', 'Invalid username or password')

def open_login_window():
    global login_window
    login_window = tk.Toplevel(gui_window)
    login_window.title("Login")
    login_window.geometry("300x200")
    login_window.resizable(0, 0)

    login_username_label = tk.Label(login_window, text="Username:", font=("arial", 12, "bold"))
    login_username_label.pack(pady=5)
    global login_username_entry
    login_username_entry = tk.Entry(login_window, font=("Arial", 12))
    login_username_entry.pack(pady=5)

    login_password_label = tk.Label(login_window, text="Password:", font=("arial", 12, "bold"))
    login_password_label.pack(pady=5)
    global login_password_entry
    login_password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
    login_password_entry.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", width=10, font=("arial", 12, "bold"), command=login)
    login_button.pack(pady=10)

    login_window.mainloop()

def open_signup_window():
    global signup_window
    signup_window = tk.Toplevel(gui_window)
    signup_window.title("Sign Up")
    signup_window.geometry("300x200")
    signup_window.resizable(0, 0)

    reg_username_label = tk.Label(signup_window, text="Username:", font=("arial", 12, "bold"))
    reg_username_label.pack(pady=5)
    global reg_username_entry
    reg_username_entry = tk.Entry(signup_window, font=("Arial", 12))
    reg_username_entry.pack(pady=5)

    reg_password_label = tk.Label(signup_window, text="Password:", font=("arial", 12, "bold"))
    reg_password_label.pack(pady=5)
    global reg_password_entry
    reg_password_entry = tk.Entry(signup_window, font=("Arial", 12), show="*")
    reg_password_entry.pack(pady=5)

    register_button = tk.Button(signup_window, text="Register", width=10, font=("arial", 12, "bold"), command=register_user)
    register_button.pack(pady=10)

    signup_window.mainloop()

def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showerror('Error', 'Task name cannot be empty')
        return
    date = cal.selection_get().strftime("%Y-%m-%d")
    time = time_entry.get().strip()
    if not time:
        messagebox.showerror('Error', 'Time cannot be empty')
        return
    try:
        c.execute('INSERT INTO tasks (title, date, time) VALUES (?, ?, ?)', (task, date, time))
        conn.commit()
        show_tasks()
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to add task: {e}')

def show_tasks():
    task_listbox.delete(0, tk.END)
    try:
        c.execute('SELECT title, date, time FROM tasks')
        for row in c.fetchall():
            task_listbox.insert(tk.END, f"{row[0]} - {row[1]} {row[2]}")
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to fetch tasks: {e}')

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index).split(" - ")[0]
        c.execute('DELETE FROM tasks WHERE title = ?', (task,))
        conn.commit()
        show_tasks()
    except IndexError:
        messagebox.showerror('Error', 'No task selected')
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to delete task: {e}')

def delete_all():
    if messagebox.askyesno('Delete all', 'Are you sure you want to delete all tasks?'):
        try:
            c.execute('DELETE FROM tasks')
            conn.commit()
            show_tasks()
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Failed to delete tasks: {e}')

def close():
    try:
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Failed to close database: {e}')
    gui_window.destroy()

def enable_task_functions():
    task_label.config(state=tk.NORMAL)
    task_entry.config(state=tk.NORMAL)
    cal.config(state="normal")
    time_entry.config(state=tk.NORMAL)
    add_button.config(state=tk.NORMAL)
    delete_button.config(state=tk.NORMAL)
    delete_all_button.config(state=tk.NORMAL)
    task_listbox.config(state=tk.NORMAL)

def disable_task_functions():
    task_label.config(state=tk.DISABLED)
    task_entry.config(state=tk.DISABLED)
    cal.config(state="disabled")
    time_entry.config(state=tk.DISABLED)
    add_button.config(state=tk.DISABLED)
    delete_button.config(state=tk.DISABLED)
    delete_all_button.config(state=tk.DISABLED)
    task_listbox.config(state=tk.DISABLED)

# Main GUI code starts here

gui_window = tk.Tk()
gui_window.title("Tasks")
gui_window.geometry("1000x500+450+150")  # Larger window size
gui_window.resizable(0, 0)
gui_window.configure(bg="#B5E5CF")

conn = sqlite3.connect('tasks.db')
c = conn.cursor()
create_tasks_table()

functions_frame = tk.Frame(gui_window, bg="black")
functions_frame.pack(side="top", expand=True, fill="both")

task_label = tk.Label(functions_frame, text="Enter task:", font=("arial", 14, "bold"), bg="black", fg="white")
task_label.place(x=20, y=30)

task_entry = tk.Entry(functions_frame, font=("Arial", 14), width=30, fg="black", bg="white")
task_entry.place(x=180, y=30)

time_label = tk.Label(functions_frame, text="Enter time:", font=("arial", 14, "bold"), bg="black", fg="white")
time_label.place(x=20, y=90)

time_entry = tk.Entry(functions_frame, font=("Arial", 14), width=15, fg="black", bg="white")
time_entry.place(x=180, y=90)

cal = Calendar(functions_frame, selectmode="day", date_pattern="yyyy-mm-dd")
cal.place(x=750, y=10)  # Adjusted position at the top right corner








add_button = tk.Button(functions_frame, text="Add task", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=add_task)
delete_button = tk.Button(functions_frame, text="Delete task", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=delete_task)
delete_all_button = tk.Button(functions_frame, text="Delete all tasks", width=15, font=("arial", 14, "bold"), bg='#D4AC0D', command=delete_all)
exit_button = tk.Button(functions_frame, text="Exit", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=close)

add_button.place(x=20, y=160)
delete_button.place(x=200, y=160)
delete_all_button.place(x=380, y=160)
exit_button.place(x=20, y=400)  # Adjusted position

task_listbox = tk.Listbox(functions_frame, width=92, height=7, font=("bold"), selectmode='SINGLE', bg="WHITE", fg="BLACK", selectbackground="#D4AC0D", selectforeground="BLACK")
task_listbox.place(x=17, y=220)

login_button = tk.Button(functions_frame, text="Login", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=open_login_window)
login_button.place(x=800, y=400)  # Adjusted position

signup_button = tk.Button(functions_frame, text="Sign Up", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=open_signup_window)
signup_button.place(x=600, y=400)  # Adjusted position

disable_task_functions()

show_tasks()

gui_window.mainloop()
