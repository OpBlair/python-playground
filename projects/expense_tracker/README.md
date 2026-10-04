# Expense Tracker

This project demonstrates practical Python concepts including **File I/O with JSON**, **persistent data storage**, **robust error handling**, **date formatting**, and **dictionary-based data aggregation**.

---

## Features

* **Interactive CLI Menu:** Easy-to-use terminal interface with options to add, view, and summarize expenses.
* **Automated Timestamps:** Automatically records expenses using the current ISO date (`YYYY-MM-DD`).
* **Formatted Terminal Tables:** Neatly displays all recorded entries and category breakdowns with proper currency formatting (`Shs.`).
* **Persistent Storage:** Automatically saves and loads records from a local `expense.json` file.
* **Robust Error Handling:** Gracefully catches invalid numeric entries, empty categories, missing files, and corrupted JSON data without crashing.

---

## Project Structure

```text
expense_tracker/
├── main.py            # Main application script
└── expense.json       # Local data store (auto-generated)
```

---

## Quick Start

### Prerequisites
* Make sure you have **Python 3.x** installed on your system.

### Running the Application

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt and navigate to the project directory:
   ```bash
   cd expense_tracker
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage Guide

When you run `main.py`, you will be greeted with the following interactive menu:

```text
=== Expense Tracker ===
1. Add Expense
2. View all Expenses
3. View Summary by Category
4. Exit
Choose an option: 
```

* **1. Add Expense:** Prompts you to enter an amount and a category (e.g., *Food*, *Transport*, *Utilities*).
* **2. View all Expenses:** Displays a formatted table listing your index, category, amount in `Shs.`, and date.
* **3. View Summary by Category:** Aggregates your total spending per category into a clean summary table.
* **4. Exit:** Safely closes the application.

---

## Future Roadmap

* **[ ] Web API:** Build a RESTful API wrapper around the logic using **FastAPI** or **Flask**.
* **[ ] Cloud Deployment:** Host the API online to make it publicly accessible.
* **[ ] Date Filtering:** Add options to view expenses filtered by month or specific date ranges.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
