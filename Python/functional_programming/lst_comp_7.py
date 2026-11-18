

# 7. Find all of the words in a string that are less than 4 letters
# --------------------------------------------------------------------
str = input("Enter a string: ")
lst = [i for i in str.split() if len(i) < 4 ]
print(lst)