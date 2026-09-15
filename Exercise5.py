#goal = float(input("Enter your overall goal: $")).strip()
#week1 = (input("Enter your deposit for week 1: $"))
#week2 = float(input("Enter your deposit for week 2: $"))
#week3 = float(input("Enter your deposit for week 3: $"))

week_num = 1

while True:
    goal = input("Enter your overall goal: $").strip()
    week1 = (input("Enter your deposit for week 1: $"))
    if not goal.isdigit() or week1.isdigit():
        print("Not a number, please try again")
        week_num += 1
    else:
        print(f"You are on week {week_num} with ${week1} saved.")
        break

while True:
    week2 = input("Enter your deposit for week 2: $")
    if not week2.isdigit():
        print("Not a number, please try again")