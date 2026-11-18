

# wap to check a number is pallindrome or not
# ---------------------------------------------------
n = int(input("Enter a number: "))
temp = n
rev = 0
while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
if rev == n:
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")