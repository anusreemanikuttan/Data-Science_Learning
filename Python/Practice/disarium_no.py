

# Disarium Number
#    The sum of digits raised to the power of their position equals the number.
#    Example: 135
#    1¹ + 3² + 5³ = 1 + 9 + 125 = 135
#    So, 135 is a Disarium number.
#    If not equal, print Not a Disarium number.
# Write a program to check whether a number is a Disarium Number.
# -----------------------------------------------------------------------
def disarium(num):
    temp = num
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        count -= 1
        temp //= 10
    if sum == num:
        return "Disarium Number"
    else:
        return "Not a Disarium Number"
print(disarium(135))
print(disarium(134))