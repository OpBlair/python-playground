import csv
import json

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
    pass

def save_expenses():
    pass

def add_expense():
    pass

def display_expenses():
    pass

def display_summary():
    pass
