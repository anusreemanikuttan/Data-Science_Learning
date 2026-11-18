 # 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

# for i in range(1,6):
#     for j in range(0,7-i):
#         print(j, end=" ")
#     print()

# 0
# 0 1
# 0 2 4
# 0 3 6 9
#
# for i in range(4):
#     for j in range(i+1):
#         print(j*i,end=" ")
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num = 1
# for i in range(1,6):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()


# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(1,6):
#         print(max(i,j),end=" ")
#     print()


# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,6):
#     for j in range(1,7-i):
#         print('*', end=" ")
#     print()



#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print('*',end="")
#     print()

# 0R
# n= 5
# symbols = 1
# for i in range(5):
#     print(' ' * n, end='')
#     print('*' * symbols)
#     n -= 1
#     symbols += 2


#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i):
#         print('*',end=" ")
#     print()


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print('*',end="")
#     print()
# for i in range(4,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print('*',end="")
#     print()
#
#
# 0R
# n = 5
# for i in range(1,n+1):
#     print(" "* (n-i) + "*"*(2*i-1))
# for i in range(n-1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))




