# Daily Task Scheduler 

A lightweight, interactive command-line task scheduler built with Python. It allows you to organize your day by adding tasks, viewing your current list, and marking items as complete using a simple menu-driven terminal interface.

## Features 

* **Interactive Menu:** Run the app and navigate options seamlessly without typing command-line arguments.
* **Task Management:** Add new tasks and view their completion status instantly.
* **Completion Tracking:** Mark specific tasks as done using their unique ID.
* **In-Memory Storage:** Fast, lightweight execution with zero external dependencies (ready for JSON persistence later).

## Tech Stack 

* **Language:** Python 3.x
* **Storage:** In-memory lists (Python standard types)

## Project Structure 

```text
task-scheduler/
│
├── tasks.py         # Main interactive application script
└── README.md        # Project documentation

```

## Getting Started 

### Prerequisites

Make sure you have **Python 3.8+** installed on your system.

### Installation

1. Clone the repository or download the project files:
```bash
git clone [https://github.com/opblair/python-playground](https://github.com/opblair/python-playground.git)
cd projects/task-scheduler

```

2. Run the application:
```bash
python main.py

```

## Usage 

When you launch the app, you will be greeted with an interactive menu:

```text
--- Daily Task Scheduler ---
1. Add Task
2. Mark Tasks complete
3. Exit

```

Simply type the number corresponding to the action you want to perform and follow the prompts!

## Future Improvements

* Add JSON file persistence so your tasks save when you close the app.
* Add a delete task option.
* Add due dates and priorities.
