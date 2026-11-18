# Write a Python program that shows a menu to the user and performs a basic arithmetic operation based on their choice.
# 1. Display a menu like this:
#
#    ***** MENU *****
#    1. Addition
#    2. Subtraction
#    3. Multiplication
#    4. Division
#    5. Exit
#    ```
# 2. Ask the user to enter their choice (1 to 4).
# 3. If the choice is 1 to 4:
#   * Ask the user to enter two numbers.
#   * Perform the selected operation and print the result.
# 4. If the user enters an invalid choice:
#    * Print "Wrong choice! Please enter a number between 1 and 5.
#
#  Example Output:
# ***** MENU *****
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter choice: 3
# Enter first number: 5
# Enter second number: 4
# Multiplication = 20



print("***** MENU *****")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
print("```")
while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 5:
        print("Exiting the program..")
        break

    elif choice in (1, 2, 3, 4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            print("Addition", num1 + num2)
        elif choice == 2:
            print("Subtraction", num1 - num2)
        elif choice == 3:
            print("Multiplication", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("Division", num1 / num2)
            else:
                print("ERROR! Cannot Divide By Zero")

    else:
        print("Wrong choice! Please enter a number between 1 and 5.")
