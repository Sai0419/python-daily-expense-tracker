
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0
    print("\n--- Your Expenses ---")

    for expense in expenses:
        print(f"{expense['name']}: Rs. {expense['amount']:.2f}")
        total += expense["amount"]

    print(f"Total Expenses: Rs. {total:.2f}")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
