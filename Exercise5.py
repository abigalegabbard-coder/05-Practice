#goal = float(input("Enter your overall goal: $")).strip()
#week1 = (input("Enter your deposit for week 1: $"))
#week2 = float(input("Enter your deposit for week 2: $"))
#week3 = float(input("Enter your deposit for week 3: $"))

week_num = 1

while True:
    goal = input("Enter your overall goal: $").strip()
    week1 = (input("Enter your deposit for week 1: $"))
    if goal.isalpha() or week1.isalpha():
        print("Not a number, please try again")
    else:
        week_num+1
        print(f"You are on week {week_num} with ${week1} saved.")
        break

while True:
    week2 = input("Enter your deposit for week 2: $")
    if not week2.isdigit():
        print("Not a number, please try again")
    else:
        weeknum2 = int(week_num) + 1
        print(f"You are on week {weeknum2} with ${float(week2) + float(week1)}")
        break

while True:
    week3 = input("Enter your deposit for week 3: $")
    if not week3.isdigit():
        print("Not a number, please try again")
    else:
        total = (float(week2) + float(week1))
        weeknum3 = int(weeknum2) + 1
        print(f"You are on week {weeknum3} with ${float(total) + float(week3)}")
        break