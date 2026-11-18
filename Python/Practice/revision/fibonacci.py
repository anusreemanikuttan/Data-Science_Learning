

# Write a program to print the Fibonacci Series up to N terms.
# -----------------------------------------------------------------
n = int(input("Enter the number: "))
fib = []
a = 0
b = 1
for i in range(n):
    fib.append(a)
    c = a + b
    a = b
    b = c
print(fib)