while True:
    try:
        password = input("Enter your password: ")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        print("Password accepted!")
        break  # Exit loop if valid

    except ValueError as e:
        print(e)  # Show error message
        print("Please try again.\n")