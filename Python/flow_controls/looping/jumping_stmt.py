# Jumping Statements:

# 1. break
# 2. continue
# 3. pass

# break---> used to exit from the loop

# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

# whether the num is prime or not

# num = int(input("Enter a number: "))
# if num <= 1:
#     print(num, "is not a prime number")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#
# with flag

# num = int(input("Enter a number: "))
# flag = False
# for i in range(2,num):
#     if num % i == 0:
#         flag = True
#         break
# if flag:
#     print("Not a prime number")
# else:
#     print("Prime number")


# for i in "priya":
#     if i == 'i':
#         break
#     print(i)

# continue ---> used to skip a condition

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# for i in "priyia":
#     if i == 'i':
#         continue
#     print(i)

# wap to print all the even number in the range of 1 to 50 using 'continue'

# for i in range(1,51):
#     if i % 2 != 0:
#         continue
#     print(i)

# pass ---> it does nothing

# for i in range(1,11):
#     if i==5:
#         pass
#     print(i)

# while True ---> creates an infinite loop,'break' for exit

