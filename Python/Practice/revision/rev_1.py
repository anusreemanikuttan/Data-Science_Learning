

# 1. wap to find the N fibonacci seq numbers in reverse order.
# -----------------------------------------------------------------
# n = int(input("Enter a number: "))
# fib = []
# a = 0
# b = 1
# for i in range(n):
#     fib.append(a)
#     c = a + b
#     a = b
#     b = c
# print("Reverse order of fibonacci seq:",fib[::-1])


# 2. wap to find the word count from a given sentence
# ---------------------------------------------------------
# s = input("Enter a sentence: ")
# words = s.split()
# print("Word count: ", len(words))


# 3. H E L L O
#    H E L L
#    H E L
#    H E
#    H
# ---------------------------------------
# s = "HELLO"
# for i in range(len(s),0,-1):
#     for j in range(i):
#         print(s[j],end=" ")
#     print()

# 4. Find all prime numbers below the given limits and reverse is also prime
# -->print reverse
# ---------------------------------------------------------------------------
# limit = int(input("Enter limit: "))
# prime = []
# for num in range(2,limit):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#     else:
#         prime.append(num)
# for num in prime:
#     rev = int(str(num)[::-1])
#     if rev in prime:
#         print(rev)


# 5. Given a list of integers nums and integer target, return indices of the two numbers
#    such that they add upto the target
# --> nums = [2,7,11,15] , target = 9
# ---> 2 + 7 = 9 , indices of 2 and 7 should print
# -----------------------------------------------------------------------------------------

# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)
#             break


#  Print the following pattern:
# ==============================================
#
# *
# **
# ***
# ****
# *****
#
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print("*",end = "")
#     print()


# 1
# 12
# 123
# 1234
# 12345
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# A
# AB
# ABC
# ABCD
# ABCDE
# #
# for i in range(1,6):
#     for j in range(65, 65+i):
#         print(chr(j), end= "")
#     print()

# OR
#
s = "ABCDE"
for i in range(len(s)):
    for j in range(i+1):
        print(s[j],end= "")
    print()