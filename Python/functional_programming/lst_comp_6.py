

# 6. Find total number of vowels in a string
# -------------------------------------------
string = input("Enter a string: ")
lst = len([i for i in string if i in "aeiouAEIOU"])
print(lst)