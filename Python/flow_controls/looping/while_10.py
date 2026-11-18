

# Number based logic
# ========================================================

# 1. Armstrong Number (3 digit)
#    A number that is equal to the sum of cubes of its digits.
#    Example: 153
#    1³ + 5³ + 3³ = 1 + 125 + 27 = 153
#    So, 153 is an Armstrong number.
#    If not equal, print Not an Armstrong number.
# ---------------------------------------------------------
# n = int(input("Enter a number: "))
# temp = n
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == n:
#     print("It's an Armstrong Number")
# else:
#     print("Not an Armstrong Number")



# 2. Harshad (Niven) Number
#    A number that is divisible by the sum of its digits.
#    Example: 18
#    (1 + 8) = 9
#    18 ÷ 9 = 2 (no remainder)
#    So, 18 is a Harshad number.
#    If not divisible, print Not a Harshad number.
# ---------------------------------------------------------------
# n = int(input("Enter a number: "))
# temp = n
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit
#     temp //= 10
# if n % sum == 0:
#     print("It's a Harshad Number")
# else:
#     print("Not a Harshad Number")



# 3. Perfect Number
#    A number whose sum of proper divisors (excluding itself) equals the number.
#    Example: 6
#    Divisors: 1, 2, 3
#    1 + 2 + 3 = 6
#    So, 6 is a Perfect number.
#    If not equal, print Not a Perfect number.
#
# ---------------------------------------------------------------------------------
# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i < n:
#     if n % i == 0:
#         sum += i
#     i += 1
# if n == sum:
#     print("Perfect Number")
# else:
#     print("Not perfect number")


#  wap to find the factorial of a number
# -----------------------------------------
# n = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print(fact)


# 4. Strong Number
#    A number whose sum of factorials of digits equals the number.
#    Example: 145
#    1! + 4! + 5! = 1 + 24 + 120 = 145
#    So, 145 is a Strong number.
#    If not equal, print Not a Strong number.
# ---------------------------------------------------------------------
n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1
    sum += fact
    temp //= 10
if sum == n:
    print("Strong Number")
else:
    print("Not a Strong Number")