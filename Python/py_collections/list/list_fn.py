

# LIST FUNCTIONS

# sum()
# max()
# min()
# append
# extend
# insert
# sort
# pop
# len()

# SUM
# ----------------
# lst = [2,3,4,5]
# print(sum(lst))

# OR

# list = sum([2,3,4,5])
# print(list)

# MAX
# -----------------
# lst = [2,4,5,6,7]
# print(max(lst))

# MIN
# --------------
# lst = [2,4,5,6,7]
# print(min(lst))

# APPEND ----> used to add an extra element to the list
# this is a method not a fn
# method is represented using '.'
# only one element can be passed at a time
# duplicate element can also be added
# ---------------------------------------------------------
# lst = [2,3,4,5]
# lst.append(6)
# lst.append(7)
# print(lst)

# EXTEND -----> multiple elements can be added to the list
# ---------------------------------------------------------
# lst = [2,3,1]
# lst.extend([7,5,6])
# print(lst)

# LEN ---- len() --> length
# --------------------------------
# lst = [2,3,4,5]
# print(len(lst))

# Add elements in the range 1 to 50
# ------------------------------------
# list = []
# for i in range(1,51):
#     list.append(i)
# print(list)
# print(sum(list))

# POP -----> to remove an element from the list
# it removes element based on index numbers
# if there's no index passed inside pop(), then it removes the last element.
# -----------------------------------------------------------------------------

# list = [2,3,7,8,9]
# list.pop(0)     # remove can also be used list.remove(value)
# print(list)

# SORT -----> used to sort elements in ascending or descending order
# if no arg passed it sort in ascending order
# --------------------------------------------------------------------

# Ascending
# list = [31,34,2,6,7,8,50]
# list.sort()
# print(list)

# Descending
# list = [31,34,2,6,7,8,50]
# list.sort(reverse=True)
# print(list)

# INSERT -----> to add an element in a specified position
# the element in that position will shift, it doesn't get removed!!
# ------------------------------------------------------------------

# list = [2,3,5,7]
# list.insert(1,100)
# print(list)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# STRING METHODS
# ----------------------------------------------

# len()
# it is a fn
# for string, it also adds the space
# ------------------------------------
# s = 1000
# l = len(str(s))
# print(l)

# s = "python dev"
# print(len(s))


# count()
# it is a method
# ---------------------------------
# s = "apple"
# print(s.count("p"))

# list = ["apple", "orange", "apple", "grapes"]
# print(list.count("orange"))


# index() -----> it returns the index position correspondng to the given character
# ---------------------------------
# s = "pythonoooo"
# print(s.index("o"))  # gets where "o" comes first

# list = [3,4,5,3]
# print(list.index(3))


# lower() -----> to convert the string to lower case
# ---------------------------------------------------
# s = "PYthon"
# print(s.lower())


# upper() ------> to convert the string to upper case
# ----------------------------------------------------
# s = "python"
# print(s.upper())


# capitalize() ------> to capitalize first letter of first word
# --------------------------------------------------------------
# s = "python is easy"
# print(s.capitalize())


# title() ---------> to capitalize first letter of every word in a sentence.
# ---------------------------------------------------------------------------
# s = "python is easy"
# print(s.title())


# isalpha() -----> returns true if the string contains alphabets only.
# no spaces, no special characters , no numbers are supported
# ----------------------------------------------------------------------
# s = "abc123"
# print(s.isalpha())


# isalnum() ------> it supports both alphabets and numbers.
# doesn't support -- no spaces, no special characters
# -------------------------------------------------------------
# s = "abc123"
# print(s.isalnum())


# isdigit() ------> returns true if it is a number
# doesn't support --- no space, no spcl ch, no alphabets.
# -------------------------------------------------------
# s = "123"
# print(s.isdigit())


# replace() ------> to replace old value to a new value
# -------------------------------------------------------------
# s = "python dev"
# print((s.replace("python","java")))


# strip() ------> it is used to remove the white spaces at the begining and ending
# doesn't remove spaces in between
# it can also removes characters at the beginning and ending by mentioning the ch.
# ---------------------------------------------------------------------------------
# s = " abd 123 "
# x = "#ab#c#"
# print(s.strip())
# print((x.strip("#")))

# lstrip() ----> left strip
# rstrip() ----> right strip

# s = "abc##"
# print(s.rstrip("#"))

# s = "#abc##"
# print(s.lstrip("#"))


# split() ------> to split each word in a sentence based on space
# and it returns each word in a list
# -------------------------------------------------------------------------
# s = "python is easy to learn"
# words = s.split()
# for i in words:
#     print(i)

# s = "python/is/easy/to/learn"
# print(s.split())   # deosn't contain space

# so specify where we want to split -----
# s = "python/is/easy/to/learn"
# print(s.split("/"))


         