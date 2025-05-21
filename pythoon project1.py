expenses = []
while True:
    item = input("enter expense item: ")
    cost = float(input("enter cost: "))
    expenses.append((item, cost))
    more = input("do you want to add more? (y/n): ")
    if more.lower() != "y":
        break
total = sum(i[1] for i in expenses)
print(f"total expense: {total}")

budget = {"income": 0, "expenses": []}

budget["income"] =float(input("enter your total monthly income: "))

while True:
    item = input("enter expenses name(or 'done' to stop): ")
    if item.lower() == "done":
        break
    amount =float(input(f"enter amount for {item}: "))
    budget["expenses"].append((item,amount))

    total_expenses =sum(i[1] for i in budget["expenses"])
    balance = budget["income"] - total_expense
    print("\n--budget sumaary---")
    print(f"Total Income: {budget['income']}")
    print(f"Total Expenses: {total_expense}")
    print(f"Remaining Balance: {balance}")

budget = {"income": 0, "expenses": []}
budget["income"] = float(input("Enter your total monthly income: "))
while True:
    item = input("Enter expense name (or 'done' to stop): ")
    if item.lower() == "done":
        break
    amount = float(input(f"Enter amount for {item}: "))
    budget["expenses"].append((item, amount))
total_expense = sum(i[1] for i in budget["expenses"])
balance = budget["income"] - total_expense
print("\n--- Budget Summary ---")
print(f"Total Income: {budget['income']}")
print(f"Total Expenses: {total_expense}")
print(f"Remaining Balance: {balance}")









































    
    
     




                     

