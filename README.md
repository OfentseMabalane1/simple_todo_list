# To-Do List App

## Created by: Keitumetse Mabalane

This is a simple To-Do List application built using Python and Tkinter for the GUI, SQLite for the database, and Pickle for data serialization. The application allows you to add tasks with descriptions, due dates, and due times, delete tasks, and store all data persistently in a database.

---

## Features
- Add new tasks with descriptions, due dates, and due times.
- Delete tasks from the list.
- Persist tasks using SQLite database.
- Error handling for missing task information.

---

## Installation

To run the To-Do List app on your local machine, follow the steps below.

### 1. Clone the Repository

```bash
git clone https://github.com/OfentseMabalane1/todolist.git
cd todolist

2. Create a Virtual Environment (optional but recommended)

It's a good practice to use a virtual environment for Python projects.

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the Required Dependencies

Make sure you have a requirements.txt with the necessary packages. To install dependencies:

pip install -r requirements.txt

If you don't have requirements.txt, you can manually install the dependencies with:

pip install tk sqlite3 pickle5

4. Run the Application

Once everything is set up, you can run the application using:

python todo.py

Usage

When the application starts, you will see the following elements:

    Task Description: A field to input the description of your task.
    Due Date: A field to input the due date of the task (in YYYY-MM-DD format).
    Due Time: A field to input the due time of the task (in HH:MM format).
    Task List: A list that shows all the tasks with their due dates and times.
    Delete Task: Select a task from the list and click to delete it.
Screenshots

Here’s a screenshot of what the To-Do List application looks like:

    Landing Screen
    images/landing.png

    Tasks Added Screen
    images/tasks_added.png

    Deleted Entry Screen
    images/deleted_entry.png

License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
Acknowledgements

    This app was created by Keitumetse Mabalane as part of learning and building a To-Do List application with Python.
    Thanks to Tkinter for the GUI and SQLite for the database.


