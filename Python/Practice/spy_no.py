

# Spy Number
#    A number where the sum of digits equals the product of digits.
#    Example: 1124
#    Sum = 1 + 1 + 2 + 4 = 8
#    Product = 1 × 1 × 2 × 4 = 8
#    So, 1124 is a Spy number.
#    If not equal, print Not a Spy number.

def spy(num):
    temp = num
    sum = 0
    product = 1
    while temp > 0:
        digit = temp % 10
        sum += digit
        product *= digit
        temp //= 10
    if sum == product:
        return "Spy Number"
    else:
        return "Not a Spy Number"
print(spy(1124))
print(spy(1143))