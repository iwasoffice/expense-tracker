# expense_tracker.py
import sqlite3
from datetime import datetime
from database import create_table, add_expense, view_expenses, delete_expense, update_expense

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Exit")

def main():
    create_table()
    
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            date = input(f"Enter date (default is {datetime.now().date()}): ") or str(datetime.now().date())
            category = input("Enter category (e.g., food, transport): ")
            add_expense(description, amount, date, category)
        
        elif choice == "2":
            expenses = view_expenses()
            for exp in expenses:
                print(f"{exp[0]} | {exp[1]} | {exp[2]} | {exp[3]} | {exp[4]}")
        
        elif choice == "3":
            exp_id = int(input("Enter expense ID to delete: "))
            delete_expense(exp_id)
        
        elif choice == "4":
            exp_id = int(input("Enter expense ID to update: "))
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            update_expense(exp_id, new_amount, new_category)
        
        elif choice == "5":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
