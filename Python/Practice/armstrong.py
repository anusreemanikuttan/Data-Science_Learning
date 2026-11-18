

# Write a program to check whether a number is an Armstrong Number.

def armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        return "Armstrong Number"
    else:
        return "not an Armstrong Number"
print("157 is",armstrong(157))
print("370 is",armstrong(370))


# 4 digit armstrong
# def armstrong(num):
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 4
#         temp //= 10
#     if sum == num:
#         return "Armstrong Number"
#     else:
#         return "not an Armstrong Number"
# print("1576 is",armstrong(1576))
# print("9474 is",armstrong(9474))

# in the given range
# def armstrong(start,end):
#     for num in range(start,end+1):
#         temp = num
#         sum = 0
#         while temp > 0:
#             digit = temp % 10
#             sum += digit ** 3
#             temp //= 10
#         if sum == num:
#             print(num,end=" ")
# armstrong(100,1000)


