

# Write a program to find the sum of digits of a number.
# --------------------------------------------------------------
def sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum
print(sum(661))