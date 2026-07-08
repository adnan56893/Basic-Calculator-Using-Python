print(".................SIMPLE CALCULATOR........................")

while True:
    print("\nSelect Operation:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Subtraction")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("You have successfully exited. Thank you!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Please enter a valid option (1-5)")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 * num2)

    elif choice == 3:
        print("Result:", num1 - num2)

    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)