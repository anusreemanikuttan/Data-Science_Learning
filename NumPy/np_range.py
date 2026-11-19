

# arange()  - a range - it is only possible to create one dimension

# import numpy as np
# a = np.arange(1,11)
# print(a)
# print(type(a))
# print(a.ndim)

# create a 1D array from 10 t 25 elements
# ------------------------------------------
# import numpy as np
# a = np.arange(10,26)
# print(a)

# create a 1 to 25
# then make the array in the order 5,5
#
# import numpy as np
# a = np.arange(1,26)
# print(a)
# b = a.reshape([5,5])
# print(b)
# print(b.ndim)
# print(b.shape)

# or
#
# import numpy as np
# a = np.arange(1,26).reshape(5,5)
# print(a)


# linspace()
# ---------------------------------
# import numpy as np
# a = np.linspace(1,20,6)   # num is the equal division
# print(a)

# max()
# 1D array
# -----------------------
# import numpy as np
# a = np.array([7,8,1,9,45,2,3,47,47,89])
# b = np.max(a)
# print(b)

# argmax()
# return index of max value
# -----------------------------
# import numpy as np
# a = np.array([9,1,6,0,2,6,7,1])
# print(np.argmax(a))

# 1D --- min(), argmin()
# ----------------------
# import numpy as np
# a = np.array([7,8,1,9,45,2,3,47,47,89])
# b = np.min(a)
# print(b)

# import numpy as np
# a = np.array([9,1,6,0,2,6,7,1])
# print(np.argmin(a))


# create 2D in (3,3)
# find the max, argmax()
# ----------------------------
# import numpy as np
# a = np.array([[2,3,4],[7,8,9],[2,8,1]])
# print(np.max(a))
# print(np.argmax(a,axis = 1))
# print(np.min(a))
# print(np.argmin(a,axis=1))

# floor(), ceil(), round()
# --------------------------
# 2D array (4,4) -- decimal values

# import numpy as np
# a = np.array([[2.4,4.5,5.2,1.1],[3.4,6.3,2.3,7.5],[6.7,2.3,1.2,3.4],[2.1,3.3,6.7,7.2]])
# print(np.floor(a))  # removes the decimal part
# print(np.ceil(a))
# print(np.round(a))

# if number is even --> maps to lowest
# odd --> maps to highest

# import numpy as np
# a = np.array([2,3,4,1,0])
# for i in a:
#     print(i)

# iterable

# import numpy as np
# a = np.array([[2,2],[3,4]])
# for i in a:
#     for j in i:
#         print(j)