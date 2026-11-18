

# Strong Number
#    A number whose sum of factorials of digits equals the number.
#    Example: 145
#    1! + 4! + 5! = 1 + 24 + 120 = 145
#    So, 145 is a Strong number.
#    If not equal, print Not a Strong number.
# Write a program to check whether a number is a Strong Number.
# ----------------------------------------------------------------
def strong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        fact = 1
        for i in range(1,digit+1):
            fact *= i
        sum += fact
        temp //= 10
    if sum == num:
        return "Strong Number"
    else:
        return "Not a Strong Number"
print(strong(145))
print(strong(123))