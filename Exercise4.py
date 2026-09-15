entry_count = 0

import random
random_number= random.randint(1, 101)
#I looked up how to do the random number and took the gist of it and applyed it here

while True:
    choice = input("Enter 1 for hello, 2 for a random number from 1 - 100, 3 for how many actions have been completed, or q to quit: ").strip()
    if choice == "1":
        print("hello")
        entry_count += 1
    elif choice == "2":
        print(random_number)
        entry_count += 1
    elif choice == "3":
        print(f"You have completed {entry_count} action(s)")
        entry_count += 1
    elif choice == "q":
        print(f"You completed {entry_count} action(s), and then quit")
        break
    else:
        print("That was not a valid option")