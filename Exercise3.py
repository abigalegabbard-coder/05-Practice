
#3 - 4 variable inputs that eventually equal 100
# only whole numbers (not zero), displays the total, shows the updated total, when finished: show the final title and valid entry count
#report if the total went over 100

while True:
    entry = input("Enter a whole number under 100: ").strip()
    if not entry.isdigit():
        print("Invalid entry, please enter a number")
    elif int(entry) < 100:
        print("Invalid entry, please enter an number below 100")