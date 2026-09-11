then today I did this 'import json
import os
from datetime import date 

FILENAME = "expense.json"

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View all Expenses")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            display_summary()
        elif choice == "4":
            print("Goodbye, exiting... now")
            break
        else:
            print("Invalid choice choose an option between 1 and 4.")

def load_expenses():
    if not os.path.exists(FILENAME):
        print(":( oops! File Not Found.")
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(":( oops! Data File was corrupted. Starting with a new file.")
        return []

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)
    

def add_expense():
    amount_input = input("Enter amount: ")
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a numerical value.")
        return

    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "amount": amount,
        "category": category,
        "date": date.today().isoformat()
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def display_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Index':<6} | {'Category':<15} | {'Amount':<12} | {'Date'}")
    print("-" * 55)
    for index, exp in enumerate(expenses, start=1):
        exp_date = exp.get('date', '')
        print(f"{index:<6} | {exp['category']:<15} | Shs. {exp['amount']:<9,.1f} | {exp_date}")

def display_summary():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    summary = {}
    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0.0) + exp['amount']

    print("\n--- Summary by Category ---")
    print(f"{'Category':<15} | {'Total Amount'}")
    print("-" * 30)
    for cat, total in summary.items():
        print(f"{cat:<15} | Shs. {total:,.1f}")

if __name__ == "__main__":
    main()
"
