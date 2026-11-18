

# Write a program to reverse a given number.
# --------------------------------------------
def reverse(num):
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return rev
print(reverse(345))
