
invalid_count = 0

while True:
    pw = input("Enter the password: ").strip().lower()
    if pw != "time":
        print("Invalid attempt")
        invalid_count += 1 
        if pw != "time" and invalid_count > 3:
            print("Too many attempts, account locked")
            break
    elif pw == "time":
        print("Access granted")
        print(f"You had {invalid_count} invalid attempts")
        break