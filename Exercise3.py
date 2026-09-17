
#3 - 4 variable inputs that eventually equal 100
# only whole numbers (not zero), displays the total, shows the updated total, when finished: show the final title and valid entry count
#report if the total went over 100

while True:
    entry = input("Enter a whole number under 100: ").strip()
    if not entry.isdigit():
        print("Invalid entry, please enter a number")
    elif int(entry) > 100:
        print("Invalid entry, please enter an number below 100")
    elif int(entry) < 0:
        print("Invalid entry, please enter a number above 0")
    else:
        entry2 = input("Enter another whole number under 100: ")
        if not entry2.isdigit():
            print("Invalid entry, please enter a number")
        elif int(entry2) > 100:
            print("Invalid entry, please enter an number below 100")
        elif int(entry2) < 0:
            print("Invalid entry, please enter a number above 0")
        else:
            entry3 = input("Enter another whole number under 100: ")
            if not entry3.isdigit():
                print("Invalid entry, please enter a number")
            elif int(entry3) > 100:
                print("Invalid entry, please enter an number below 100")
            elif int(entry3) < 0:
                print("Invalid entry, please enter a number above 0")
            else:
                total = int(entry) + int(entry2) + int(entry3)
                print(f"The total is: {int(entry) + int(entry2) + int(entry3)}")
                if total > 100:
                    print("You went over 100")
                elif total < 100:
                    print("You got less than 100")
                break