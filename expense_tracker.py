
import csv
from pathlib import Path
from datetime import date

FILE_NAME = Path("expenses.csv")


def initialize_file():
    if not FILE_NAME.exists():
        with FILE_NAME.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    print("\n--- Add Expense ---")

    expense_date = input(
        f"Date (YYYY-MM-DD, Enter for {date.today()}): "
    ).strip() or str(date.today())

    try:
        date.fromisoformat(expense_date)
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    category = input("Category (Food/Travel/Shopping/Education/Other): ").strip()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    with FILE_NAME.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([expense_date, category, description, amount])

    print("Expense saved successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    with FILE_NAME.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No expenses recorded yet.")
        return

    total = 0.0

    for row in rows:
        amount = float(row["Amount"])
        total += amount
        print(
            f'{row["Date"]} | {row["Category"]} | '
            f'{row["Description"]} | ₹{amount:.2f}'
        )

    print(f"\nTotal expenses: ₹{total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses and Total")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Your expenses are saved in expenses.csv. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()