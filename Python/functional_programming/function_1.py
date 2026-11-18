

# FUNCTIONAL PROGRAMMING

# Functional programming used to reduce the length of the program
# =================================================================
# 1. lambda
# 2. map
# 3. filter
# 4. List Comprehension
# -----------------------------------------------------------------

# 1. lambda ---it is an anonymous fn / no name fn
# Syntax of lambda ---->
# # var_name = lambda arguments:expression
# multiple arg can be passed but only one expression can be passed
# -----------------------------------------------------------------
# named fn code ----->
# def add(a,b):
#     return a+b
# print(add(2,3))


# f = lambda a,b:a+b
# print(f(2,3))


# wap to find the multiplication of 3 numbers using lambda fn
#
# f = lambda a,b,c:a*b*c
# print(f(2,3,1))

# wap to find the cube of a number using lambda
#
# f = lambda a:a**3
# print(f(2))
# print(f(3))

# wap to check if a given number is even
#
# is_even = lambda x:x % 2 == 0
# print(is_even(4))
# print(is_even(7))


# 2. map
# if each element need a corresponding output map is used
# mapping
# Syntax of map() ------->
# # var_name = list(map(function,iterable))  # list,tuple can be passed
# ----------------------------------------------------------------------

# using list -->
# list = [1,2,3,4,5] # ----> op - square of elements
# list1 = []
# for i in list:
#     list1.append(i**2)
# print(list1)


# # using map() ----> with named fn
#
# lst = [1, 2, 3, 4, 5]
# def sq(num):
#     return num ** 2
# f = list(map(sq,lst))     #fn is sq and iterable is lst
# print(f)

# with no name fn --->
# lst = [1,2,3,4,5]
# f = list(map(lambda num:num**2,lst))
# print(f)

# wap to find the cube of elements from the given list
#
# lst = [1,2,3,4]
# f = list(map(lambda num:num**3,lst))
# print(f)


# 3. filter()
# filtering using a special condition
# Syntax ---->
# # var_name = list(filter(function,iterable))
# --------------------------------------------------------

# using string --->
# lst = [1,2,3,4,5,6,7,8,9,10] # get even numbers
# lst1 = []
# for i in lst:
#     if i % 2 == 0:
#         lst1.append(i)
# print(lst1)

# using filter --->
# with  name fn --->
#
# lst = [1,2,3,4,5,6,7,8,9,10]
# def even(num):
#     return num % 2 == 0
# f = list(filter(even, lst))
# print(f)

# with no name fn --->
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda num:num % 2 == 0,lst)))

#
# map qns --------------->
# --------------------------------------------------------------
# find the cube of odd numbers from the given list
#
# lst = [1,2,3,4,5,6,7,8,9]
# odd = list(filter(lambda num:num % 2 != 0,lst))
# cube = list(map(lambda odd:odd**3,odd))
# print(cube)


# Convert all the words in the list
# ["cat", "dog", "tiger"] to uppercase using map and lambda
#
# lst = ["cat", "dog", "tiger"]
# f = list(map(lambda word:word.upper(),lst))
# print(f)


# Add 5 to every number in [10, 20, 30, 40] using map and lambda
#
# lst = [10,20,30,40]
# print(list(map(lambda num:num+5,lst)))


# Find the length of each word in ["apple","kiwi","banana"]
# using map and lambda
#
# lst = ["apple", "kiwi", "banana"]
# print(list(map(lambda x:len(x),lst)))


# filter qns --------------------->
# -----------------------------------------------------------------
# From the list [5, 10, 15, 20, 25],
# keep only the numbers greater than 12 using filter and lambda.
#
# lst = [5, 10, 15, 20, 25]
# print(list(filter(lambda num:num>12,lst)))


# From [3, 6, 9, 12, 15],
# filter only the numbers divisible by 6 using filter and lambda.
#
# lst = [3, 6, 9, 12, 15]
# print(list(filter(lambda num:num % 6 == 0,lst)))


# From [11, 22, 33, 44, 55],
# filter out all odd numbers using filter and a lambda.
#
# lst = [11, 22, 33, 44, 55]
# print(list(filter(lambda num:num % 2 != 0,lst)))


# From ["apple", "an", "cat", "ok"],
# filter only the words with length greater than 3 using filter and lambda.
#
# lst = ["apple", "an", "cat", "ok"]
# print(list(filter(lambda word:len(word)>3,lst)))


# From [45, 67, 23, 90, 55],
# filter and print only the passing marks(greater than or equal to 50) using filter and lambda.
#
lst = [45, 67, 23, 90, 55]
print(list(filter(lambda mark:mark >= 50,lst)))