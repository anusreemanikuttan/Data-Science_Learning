

# 5. Count number of spaces in a string
# string="Python makes it easy to write powerful and readable code quickly"
# --------------------------------------------------------------------------
string = "Python makes it easy to write powerful and readable code quickly"
lst = len([i for i in string if i == " "])
print(lst)


