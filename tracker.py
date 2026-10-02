import json
import os

file_name = "expenses.json"
def calculate_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"] 
    return total
 
def calculate_by_category():
    category_totals = {}
    for expense in expenses:
        expense_cat = expense["category"]
        if expense["category"] in category_totals:
            category_totals[expense_cat] = category_totals[expense["category"]] + expense["amount"]
        else:
            category_totals[expense_cat] = expense["amount"]
    return category_totals

def save_expenses(file_name, expenses):
    with open(file_name, "w") as file:
        json.dump(expenses, file, indent = 4)

def load_expenses():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
               return json.load(file)
            except json.JSONDecodeError:
                print("File corrupted")
                return []
    else:
        return [] 
expenses = load_expenses()

while True:
    print("1. add expense")
    print("2. view expenses")
    print("3. view total spending")
    print("4. view spending by category")
    print("5. exit")
    print("6. delete expense")

    choice = input("choose option: ")
     
    while choice == "1":
        try:
            amount = float(input("What is the expense amount?: "))
        
        except ValueError:
            print("not a number")
        try:
            category = input("What is the expense category?: ")
            
        except ValueError:
            print("Not a string")

        description = input("What is the expense description?: ")
        expense_id = len(expenses) + 1
        expense = {
        "id": expense_id,
        "amount": amount,
        "category": category,
        "description": description 
        }

        expenses.append(expense)
        save_expenses(file_name, expenses)
        break
    if choice == "2":
        if len(expenses) == 0:
            print("No expenses")
        else:
            for expense in expenses:
                print(f"ID: {expense['id']}")
                print(f"Amount: {expense['amount']}")
                print(f"category: {expense['category']}")
                print(f"description: {expense['description']}")
    elif choice == "3":
        print(calculate_total())
    elif choice == "4":
        print(calculate_by_category())
    elif choice == "5":
        save_expenses(file_name, expenses)
        break
    elif choice == "6": 
        expense_id = int(input("Which expense ID do you want to delete?: "))

        found = False

        for expense in expenses:
            if expense["id"] == expense_id:
                expenses.remove(expense)
                found = True 
        if not found:
            print("expense not found")
        else:
            print("expense deleted successfully")

