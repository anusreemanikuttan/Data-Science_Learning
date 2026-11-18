

# Automorphic Number
#    A number whose square ends with the same number.
#    Example: 25
#    25² = 625 → ends with 25
#    So, 25 is an Automorphic number.
#    If not ending with same digits, print Not an Automorphic number.

def auto(num):
    sq = num * num
    temp = num
    while temp > 0:
        if temp % 10 != sq % 10:
            return "Not an Automorphic Number"
        temp //= 10
        sq //= 10
    return "Automorphic Number"
print(auto(25))
print(auto(24))