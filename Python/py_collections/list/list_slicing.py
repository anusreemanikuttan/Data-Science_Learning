

# LIST SLICING
# colon ':' is used to represent slicing
# index numbers is used for slicing
# works like range fn --- doesn't print stop value
# start:stop:step
# var_name[start:stop:step]
# --------------------------------------------
# --------------------------------------------

# list = [2,5,7,8,1,9,10,34,23,6,7,89,45,67]
#         0 1 2 3 4 5  6  7  8 9 10 11 12 13

# print(list[4:10])

# print(list[:10])  # prints index 0 to 9

# print(list[:])  # prints full list

# print(list[::2])  # prints index with step 2

# print(list[::-1])  #prints reverse of the list

# print(list[3::])  #prints from index 3 to end of the list


# SLICING IS APPLICABLE IN STRING TOO...
# wap to check if a given string is pallindrome
# -----------------------------------------------
# word = input("Enter a word: ")
# if word[::-1] == word:             # or done with assigning a rev variable.
#     print("It is a pallindrome")
# else:
#     print("Not a pallindrome")