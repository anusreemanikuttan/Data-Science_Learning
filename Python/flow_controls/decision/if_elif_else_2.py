

# ask the user for 3 numbers
# check the largest among 3 numbers
# also check the case for all the numbers are equal
# #
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 == num2 == num3:
    print("3 numbers are equal")
elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is largest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")