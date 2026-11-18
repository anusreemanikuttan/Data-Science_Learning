

# find the sum of both even and odd numbers below 100
# ------------------------------------------------------
#
even_sum = 0
odd_sum = 0
i = 1
while i < 100:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)