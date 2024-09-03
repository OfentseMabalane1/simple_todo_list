# Simple Todo List Application

This is a simple task management application created using Tkinter for the GUI and SQLite for the database. The application allows users to register, log in, add tasks, and manage tasks with a calendar interface.

## Features
- User registration and login
- Add, delete, and view tasks
- Select task date using a calendar
- Secure password storage with SHA-256 hashing

## Requirements
- Python 3.x
- tkcalendar
- python-dotenv

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/OfentseMabalane1/simple_todo_list.git
   cd simple_todo_list

    Create and activate a virtual environment (optional but recommended):

    sh

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

sh

    pip install -r requirements.txt

Usage

    Run the application:

    sh

    python config.py

    Use the GUI to register a new user or log in with an existing account.

    Add tasks by entering the task details and selecting a date from the calendar.

Project Structure

    config.py: Main application file containing the GUI and database logic.
    README.md: Project documentation.
    requirements.txt: List of required packages.
    tasks.db: SQLite database file (generated automatically).

Author

Created by Keitumetse Mabalane, a student at WeThinkCode.
Email: kmabalane023@student.wethinkcode.co.za

perl


### requirements.txt
```txt
tkcalendar
python-dotenv