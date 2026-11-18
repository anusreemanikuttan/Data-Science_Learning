


# Write a program to check whether a number is Prime or not.
# -------------------------------------------------------------
# def prime(num):
#     if num < 2:
#         return "Not Prime"
#     for i in range(2,num):
#         if num % i == 0:
#             return "Not Prime"
#     return "Prime"
# print(prime(2))
# print(prime(14))


# largest prime number between 50 and 200
# -----------------------------------------
# def lar_prime(start,end):
#     largest = 0
#     for num in range(start,end+1):
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#             else:
#                 largest = num
#     return largest
# print("Largest prime number =", lar_prime(1,100))

# Smallest
# ----------------------------------------------
# def small_prime(start,end):
#     for num in range(start,end+1):
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             if num > 1:
#                 return num
# print("Smallest prime number =", small_prime(1,100))

# first 10 prime numbers
# --------------------------------------------
# def prime(n):
#     count = 0
#     num = 2
#     while count < n:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num,end=" ")
#             count += 1
#         num += 1
#     return count
# prime(10)


# Sum of prime
# -----------------------------------------------
# def sum_prime(start, end):
#     sum = 0
#     for num in range(start,end+1):
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             if num > 1:
#                 sum += num
#     return sum
# print(sum_prime(1,100))


# Write a program to print all Prime numbers between 1 and N.
# -----------------------------------------------------------------
def prime(start,end):
    for num in range(start,end+1):
        if num < 2:
            continue
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num,end= " ")
prime(1,20)


