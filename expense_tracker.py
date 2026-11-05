"""
Expense Tracker - Python Mini Project
Codomax Digital Solutions | AI & ML Internship

A simple command-line app to add, view, and summarize daily expenses.
Concepts used: variables, lists, dictionaries, loops, functions,
conditions, input validation, file handling (JSON).
"""

import json
import os

DATA_FILE = "expenses.json"


def load_expenses():
    """Load saved expenses from the file (returns an empty list if none)."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    """Save the expenses list to the file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def get_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input("Amount (Rs): "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses):
    """Add a new expense."""
    print("\n--- Add Expense ---")
    title = input("What did you spend on? ").strip().title()
    category = input("Category (Food/Travel/Study/Other): ").strip().title()
    amount = get_amount()

    expenses.append({"title": title, "category": category, "amount": amount})
    save_expenses(expenses)
    print(f"Added: {title} - Rs {amount:.2f}")


def view_expenses(expenses):
    """Show all expenses in a table."""
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'No.':<5}{'Title':<18}{'Category':<12}{'Amount (Rs)':>12}")
    print("-" * 47)
    for i, e in enumerate(expenses, 1):
        print(f"{i:<5}{e['title']:<18}{e['category']:<12}{e['amount']:>12.2f}")


def show_summary(expenses):
    """Show total, average, highest expense, and category-wise totals."""
    print("\n--- Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(e["amount"] for e in expenses)
    highest = max(expenses, key=lambda e: e["amount"])

    print(f"Total spent     : Rs {total:.2f}")
    print(f"Average expense : Rs {total / len(expenses):.2f}")
    print(f"Highest expense : {highest['title']} (Rs {highest['amount']:.2f})")

    print("\nCategory-wise totals:")
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for category, amount in totals.items():
        print(f"  {category:<10}: Rs {amount:.2f}")


def delete_expense(expenses):
    """Delete an expense by its number."""
    view_expenses(expenses)
    if not expenses:
        return
    try:
        num = int(input("\nEnter the number to delete: "))
        removed = expenses.pop(num - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show summary")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
