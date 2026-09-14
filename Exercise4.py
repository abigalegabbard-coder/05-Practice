entry_count = 0

while True:
    choice = input("Enter 1 for hello, 2 for a random number from 1 - 100, 3 for how many actions have been completed, or q to quit: ").strip()
    if choice == "1":
        print("hello")
        entry_count += 1
    elif choice == "2":
        print
        entry_count += 1
    elif choice == "3":
        print(f"You have completed {entry_count} actions")
    elif choice == "q":
        print(f"You completed {entry_count} actions, and then quit")
        break
    else:
        print("That was not a valid option")


#make the quit a Q or q input