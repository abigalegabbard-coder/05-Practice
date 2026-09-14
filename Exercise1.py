invalid_count = 0
while True:
    level_num = input("Enter a level number: ").strip()
    if not level_num.isdigit() :
        print("Invalid entry, not a number please try again: ")
        invalid_count += 1
    elif int(level_num) < 10:
        print("Invalid entry, too low")
        invalid_count += 1

    elif int(level_num) > 50:
        print("Invalid entry, too high")
        invalid_count += 1

    else:
        print("Valid entry")
        print(f"you had {invalid_count} invalid attempts")
        break