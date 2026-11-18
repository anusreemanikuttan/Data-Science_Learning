
# Write a program to count the number of digits in a number.
# -----------------------------------------------------------------
# def count_dig(num):
#     count = 0
#     while num > 0:
#         count += 1
#         num //= 10
#     return count
# print(count_dig(2345))
# print(count_dig(123))

# OR
# ----------------------------
def count_dig(num):
    return len(str(num))
print(count_dig(56789))
print(count_dig(12))