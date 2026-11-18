

# Duck Number
#    A number that contains zero(s) but does not start with zero.
#    Example:
#    1203 → contains 0 (Valid)
#    0123 → starts with 0 (Invalid)
#    So, 1203 is a Duck number.
#    If no zero or starts with 0, print Not a Duck number.

def duck(num):
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit == 0:
            return "Duck Number"
        temp //= 10
    return "Not Duck Number"
print(duck(1023))
print(duck(1243))