

# LIST COMPREHENSION
# =========================================================================

#  1 to 10 range

# lst = []
# for i in range(1,11):
#     lst.append(i)
# print(lst)

# we can divide it into 3 methods
# # var_name = [expression for item in iterable if condition]
# ------------------------------------------------------------
# 1. range of elements added into a list
# 2. range of elements added into a list based on one condition
# 3. range of elements added into a list based on more than one condition

# 1. range of elements added int a list
# Syntax ---->
# # var_name = [expression range]  or var_name = [ print range]
# --------------------------------------------------------------

# 1 to 10 to the list
# lst = [num for num in range(1,11)]
# print(lst)


# 20 to 50 elements into the list using list comprehension
#
# lst = [i for i in range(20,51)]
# print(lst)


# 10 to 5 elements into the list
#
# lst = [i for i in range(10,4,-1)]
# print(lst)


# 1 to 10 elements ---> square added to the lst
#
# lst = [i**2 for i in range(1,11)]            # exp added first
# print(lst)
#
# OR
#
# lst = [2,3,4,5,6]
# sq = [num**2 for num in lst]
# print(sq)


# 2. range of elements added into a list based on one condition
# Syntax ---->
# # var_name = [ print range if condition]
# -------------------------------------------------------------------------

# even numbers in the range of 1 to 10
#
# lst = [i for i in range(1,11) if i % 2 == 0]
# print(lst)


# collect the odd numbers in the range of 1 to 30
#
# lst = [i for i in range(1,31) if i % 2 != 0]
# print(lst)


# collect the numbers that are divisible by 5 in the range of 20 to 50
#
# lst = [i for i in range(20,51) if i % 5 == 0]
# print(lst)


# print the odd numbers cube in the range of 5 to 15
#
# lst = [i**3 for i in range(5,16) if i % 2 != 0]
# print(lst)


# find the sum of even numbers in the range of 1 to 10
#
# lst = sum([i for i in range(1,11) if i % 2 == 0])
# print(lst)


# 1 to 50 range ---> div by 2 and 5 elements
#
# lst = [i for i in range(1,51) if i % 2 == 0 and i % 5 == 0]
# print(lst)


# 3. range of elements added into a list based on more than one condition
# TYPE 1 ---> if else
# Syntax --->
# # var_name = [ print1 if condition1 else print2 for i in range]

# TYPE 2 ----> if elif else (elif is not possible in list comprehension)
# Syntax ---->
# var_name = [ print1 if condition1 else print2 if condition2 else print3 range]
# var_name = [ print1 if cond1 else print2 if cond2 else print3 if cond3 else print4 range]
# ------------------------------------------------------------------------------------------

# 1 to 50 even number ----> even square, odd number --->cube of odd
#
# lst = [i**2 if i % 2 == 0 else i**3 for i in range(1,51)]
# print(lst)


# 1 to 50 range --->
# 1 to 15 ---> small
# 16 to 35 ---> medium
# 36 to 50 ----> large
#
# lst = [(i,"small") if i<=15 else (i,"medium") if 16<=i<=35 else (i,"large") for i in range(1,51)]
# print(lst)


# vowels
#
# word = input("Enter a word: ")
# lst = [i for i in word if i in "aeiouAEIOU"]
# print(lst)

# count of vowels
# word = input("Enter a word: ")
# lst = len([i for i in word if i in "aeiouAEIOU"])
# print(lst)

# consonents count
#
word = input('Enter a word: ')
lst = len([i for i in word if i not in "aeiouAEIOU"])
print(lst)