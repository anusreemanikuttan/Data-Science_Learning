

# Type - 1
# ------------------------
# if condition:
#       if condition:
#               statement
#       else:
#               statement
# else:
#       statement


# Type - 2
# -------------------------
# if condition:
#     statement
# else:
#     if condition:
#         statement
#     else:
#         statement

# Type - 3
# --------------------------------
# if condition:
#     if condition:
#           statement
#     else:
#           statement
# else:
#     if condition:
#         statement
#     else:
#         statement


# positive, negative, zero
# type - 2 -->
#
# num = int(input("Enter Number: "))
# if num > 0:
#     print("Positive")
# else:
#     if num < 0:
#         print("Negative")
#     else:
#         print("Zero")

# type 1 -->
#
num = int(input("Enter Number: "))
if num != 0:
    if num > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")