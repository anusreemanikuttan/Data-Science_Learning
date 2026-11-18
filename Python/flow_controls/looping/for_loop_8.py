

#fibonacci seq (first 5 numbers)
# -------------------------------------------
# 0 1 1 2 3 5 8 13 21 34...
n = int(input("Enter a number: "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):  # for i in range(3,6):
    c = a + b
    print(c)
    a = b
    b = c



# patterns
# ============================================

# 1 2 3
# 1 2 3
# 1 2 3

# row ---> i
# column ---> j

# for i in range(1,4):
#     for j in range(1,4):
#         print(j, end=" ")
#     print()


# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5

# for i in range(4):              # for i in range(1,5):
#     for j in range(1,6):
#         print(j, end="  ")
#     print()


# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# for i in range(6):
#     for j in range(1,5):
#         print(j, end=" ")
#     print()


# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

# for i in range(1,4):
#     for j in range(4):
#         print(i, end=" ")
#     print()


# 1  1  1
# 2  2  2
# 3  3  3
# 4  4  4
# 5  5  5

# for i in range(1,6):
#     for j in range(3):
#         print(i, end="  ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

