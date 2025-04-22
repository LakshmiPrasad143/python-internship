import csv
import os
from datetime import datetime
from collections import defaultdict

EXPENSE_FILE = "expenses.csv"
CATEGORIES = ['Food', 'Transport', 'Entertainment', 'Bills', 'Others']

# ----------------------------
# Utility Functions
# ----------------------------

def init_file():
    """Initialize the expense file with headers if it doesn't exist."""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    """Add a new expense entry."""
    try:
        amount = float(input("Enter amount spent: ₹ "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        print("\nCategories: ", ", ".join(CATEGORIES))
        category = input("Enter category: ").capitalize()
        if category not in CATEGORIES:
            print("Invalid category. Added to 'Others'.")
            category = 'Others'

        description = input("Enter a brief description: ")
        date = datetime.now().strftime("%Y-%m-%d")

        with open(EXPENSE_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input. Please enter a numeric amount.")

def read_expenses():
    """Read all expenses from the file."""
    expenses = []
    try:
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Amount'] = float(row['Amount'])
                expenses.append(row)
    except FileNotFoundError:
        print("Expense file not found.")
    return expenses

def monthly_summary():
    """Display monthly expense summary."""
    expenses = read_expenses()
    monthly_totals = defaultdict(float)

    for exp in expenses:
        month = exp['Date'][:7]
        monthly_totals[month] += exp['Amount']

    print("\n📆 Monthly Summary:")
    for month, total in sorted(monthly_totals.items()):
        print(f"{month}: ₹ {total:.2f}")

def category_summary():
    """Display category-wise expense summary."""
    expenses = read_expenses()
    category_totals = defaultdict(float)

    for exp in expenses:
        category_totals[exp['Category']] += exp['Amount']

    print("\n📊 Category-wise Summary:")
    for cat, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat}: ₹ {total:.2f}")

def view_all_expenses():
    """Display all expenses in a readable format."""
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n📋 All Expenses:")
    for exp in expenses:
        print(f"{exp['Date']} | ₹ {exp['Amount']} | {exp['Category']} - {exp['Description']}")

def main_menu():
    """Main CLI menu for the user."""
    init_file()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
