

# 1.Write a program to calculate the electricity bill .
# Accept the number of units from user  .
#
#            unit                price
#
#     first 100 unit           No charge
#
#     next  100 unit           Rs 5 per unit
#
#     After 200 units          Rs 10 per unit
#
# # 350  == 100   100   150
#            0  + 500 + 1500 ===2000
#
# # 250 ===100 100  50
#           0  500  500===1000
#
# # 150 === 100 50
#            0  250 ==== 250
# --------------------------------------------------------------------------------

# unit = int(input("Enter number of units: "))
# if unit <= 100:
#     print("No charge")
# elif unit <= 200:
#     print("Bill: ", (unit-100) * 5)
# else:
#     print("Bill: ", 100 * 5 + (unit - 200) * 10)


# 2.Write a program that asks the user for their age and citizenship status (yes or no).
# If the user is 18 or older, check if they are a citizen.
# If both conditions are true, print "Eligible to vote", otherwise print "Not eligible".
# ----------------------------------------------------------------------------------------------
# age = int(input("Enter your age: "))
# citizen = input("Are you a citizen (yes or no)? ")
# if age >= 18 and citizen == "yes":
#     print("Eligible to vote")
# else:
#     print("Not Eligible")


# 3.Ask the user for three angles.
# If the angles sum to 180, check further:
#
#      If all angles are equal → "Equilateral triangle"
#
#      If two angles are equal → "Isosceles triangle"
#
#      Else → "Scalene triangle"
#
#      If the sum isn’t 180, print "Not a triangle".
# -----------------------------------------------------------
# a1 = int(input("Enter 1st angle: "))
# a2 = int(input("Enter 2nd angle: "))
# a3 = int(input("Enter 3rd angle: "))
# sum = a1+a2+a3
# if sum != 180:
#     print("Not a triangle")
# else:
#     if a1 == a2 == a3:
#         print("Equilateral triangle")
#     elif a1 == a2 or a1 == a3 or a2 == a3:
#         print("Isosceles triangle")
#     else:
#         print("Scalene triangle")


# 4. Input from the user. Checks whether the number is positive.
# If it is positive, further check whether it is even or odd.
# -----------------------------------------------------------------
# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 == 0:
#         print("It is even")
#     else:
#         print("It is odd")
# else:
#     print("Number is negative")



# 5. find Largest Among three numbers using Nested if.
# ------------------------------------------------------
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 >= num2:
    if num1 >= num3:
        print(f"{num1} is largest")
    else:
        print(f"{num3} is largest")
else:
    if num2 >= num3:
        print(f"{num2} is largest")
    else:
        print(f"{num3} is largest")