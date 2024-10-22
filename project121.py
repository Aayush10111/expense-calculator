class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})

    def view_expenses(self):
        if self.expenses:
            print("Expenses:")
            for expense in self.expenses:
                print(f"Category: {expense['category']}, Amount: ${expense['amount']}")
        else:
            print("No expenses recorded.")

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            for expense in self.expenses:
                file.write(f"{expense['category']},{expense['amount']}\n")

    def load_expenses(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                category, amount = line.strip().split(',')
                self.add_expense(category, float(amount))

def main():
    expense_tracker = ExpenseTracker()
    filename = "expenses.txt"

    try:
        expense_tracker.load_expenses(filename)
        print("Expense data loaded successfully!")
    except FileNotFoundError:
        print("No expense data found.")

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: $"))
            expense_tracker.add_expense(category, amount)
            print("Expense added successfully!")
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            expense_tracker.save_expenses(filename)
            print("Expenses saved to file successfully!")
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

