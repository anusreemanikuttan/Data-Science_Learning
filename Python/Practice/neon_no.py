
# Neon Number
# A number where the sum of digits of its square equals the number itself.
# Example: 9
# 9² = 81
# 8 + 1 = 9
# So, 9 is a Neon number.
# If not equal, print Not a Neon number.

def neon(num):
    sq = num * num
    sum = 0
    while sq > 0:
        sum += sq % 10
        sq //= 10
    if sum == num:
        return "Neon Number"
    else:
        return "Not a Neon Number"
print(neon(9))
print(neon(10))