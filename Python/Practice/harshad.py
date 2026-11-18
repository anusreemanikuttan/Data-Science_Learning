

# Given number is harshad or not

# def harshad(num):
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         temp //= 10
#     if num % sum == 0:
#         return "Harshad Number"
#     else:
#         return "not a Harshad Number"
# print("18 is",harshad(18))
# print("19 is",harshad(19))

# largest harshad in the given range

def harshad(start,end):
    largest = 0
    for num in range(start,end+1):
        temp = num
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum += digit
            temp //= 10
        if num % sum == 0:
            largest = num
    return largest
print(harshad(1,100))