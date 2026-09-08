# Expense Tracker

A command-line expense tracker built in Python. This project demonstrates practical file I/O using JSON, persistent data storage, error handling, date formatting, and dictionary-based data aggregation.

## Features

- **Add Expenses:** Record amounts, categories (e.g., Food, Rent, Transport), descriptions, and automated timestamps.
- **Persistent Storage:** Automatically saves and loads records from a local `expenses.json` file.
- **View All Records:** List all recorded expenses neatly formatted in the terminal.
- **Category Summaries:** Automatically aggregate and calculate total spending per category as well as overall expenses.
- **Robust Error Handling:** Gracefully handles invalid numeric entries and missing/corrupted JSON files.

## Project Structure

```text
expense_tracker/
├── main.py
└── expenses.json (auto-generated)