

# An element in a tuple can be updated by using
# 1. List conversion
# 2. Slicing and Concatenation

tu = (3,8,9,20,10,45,67,3,56,89,100,3,2,4,22,23,24)

# update 67 -----> 1000

lst = list(tu)
lst[6] = 1000
tu = tuple(lst)
print(tu)

# OR
# give index to update and concatenate with new value and index to update + 1
tu = tu[:6] + (1000,) + tu[7:]
print(tu)