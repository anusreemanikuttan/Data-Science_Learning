

# Write a program to find the Factorial of a number.
# --------------------------------------------------------
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
print(factorial(5))

# Check whether a number is factorial or not

# def factorial(num):
#     fact = 1
#     i = 1
#     while fact < num:
#         i += 1
#         fact *= i
#     return fact == num
# print(factorial(120))
# print(factorial(100))

# Range of fact

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#         print(i,"! =",fact)
# factorial(10)