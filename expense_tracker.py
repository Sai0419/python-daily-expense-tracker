
import json
from pathlib import Path
from datetime import date, datetime

FILE_PATH = Path(__file__).with_name("expenses.json")


def load_expenses():
    if FILE_PATH.exists():
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                print("Saved data format is invalid.")
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses.")
    return []


def save_expenses(expenses):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter expense amount: "))
        if not 0 < amount < float("inf"):
            print("Enter a valid positive amount.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    expense = {
        "name": name,
        "amount": amount,
        "date": date.today().isoformat()
    }

    expenses.append(expense)

    try:
        save_expenses(expenses)
        print("Expense added and saved successfully!")
    except OSError:
        expenses.pop()
        print("Could not save the expense.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0
    print("\n--- All Expenses ---")

    for expense in expenses:
        name = expense.get("name", "Unknown")
        amount = expense.get("amount", 0)
        expense_date = expense.get("date", "Date not recorded")

        print(
            f"Date: {expense_date} | "
            f"{name}: Rs. {amount:.2f}"
        )
        total += amount

    print(f"\nTotal Expenses: Rs. {total:.2f}")


def monthly_total(expenses):
    month = input("Enter month (YYYY-MM, e.g. 2026-10): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM format.")
        return

    total = 0
    count = 0

    print(f"\n--- Expenses for {month} ---")

    for expense in expenses:
        expense_date = expense.get("date", "")

        if expense_date.startswith(month):
            print(
                f"{expense['name']}: "
                f"Rs. {expense['amount']:.2f} "
                f"({expense_date})"
            )
            total += expense["amount"]
            count += 1

    if count == 0:
        print("No dated expenses found for this month.")

    print(f"Monthly Total: Rs. {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- Daily Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            monthly_total(expenses)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
