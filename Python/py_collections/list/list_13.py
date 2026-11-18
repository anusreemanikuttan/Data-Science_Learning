

# 1. Largest prime number in the range of 50 to 200
# --------------------------------------------------

# prime = []
# for num in range(50,201):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#     else:
#             prime.append(num)
# print(prime)
# print("Largest prime number = ",max(prime))


# 2. Largest Harshad number (1 and 500)
# ----------------------------------------

# harshad = []
# for num in range(1,501):
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         temp //= 10
#     if num % sum == 0:
#         harshad.append(num)
# print("Largest Harshad Number 1 and 500: ",max(harshad))


# 3. Largest Fibonacci number below 1000
# ----------------------------------------

# fib = [0,1]
# while True:
#     next_num = fib[-1] + fib[-2]
#     if next_num >= 1000:
#         break
#     fib.append(next_num)
# print("Largest fibonacci number below 1000 =",max(fib))
#


# 4. Wap to find the largest number between 100 and 1000 whose first and last digit are same
# ---------------------------------------------------------------------------------------------

list = []
for i in range(100,1001):
    if i[0] == i[-1]:
        list.append(i)
print("Largest number between 100 and 1000 with same first and last digit: ",max(list))


# 5. Largest perfect number between 1 to 100
# --------------------------------------------------

# perfect = []
# for num in range(1,101):
#     sum = 0
#     for i in range(1,num):
#         if num % i == 0:
#             sum += i
#     if sum == num:
#         perfect.append(num)
# print("Largest Perfect Number =",max(perfect))

# 6. Given a list: numbers = [1,2,3,4], write a program to produce the output [9,8,7,6].

# list = [1,2,3,4]
# new_list = []
# for i in list:
#     new_list.append(sum(list)-i)
# print(new_list)