# using fn wap to check if a given number is even or odd

# Method 2 ---

# def even_odd(n):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# even_odd(5)
# even_odd(6)

# Method 3 ---

# def even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(even_odd(5))
# print(even_odd(2))

# Setting Default Value for Argument

def greet(name="guest"):
    print("Hello", name)
greet()