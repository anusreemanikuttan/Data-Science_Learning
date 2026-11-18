

# Write a program to check whether a number is a Palindrome.
# -----------------------------------------
def pallindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    if rev == num:
        return "Pallindrome Number"
    else:
        return "not a pallindrome number"
print("121 is a", pallindrome(121))
print("123 is ", pallindrome(123))

# given string is pallindrome or not

# def pallindrome(s):
#     rev = s[::-1]
#     if rev == s:
#         return "Word is a pallindrome"
#     else:
#         return "Word is not a pallindrome"
# print(pallindrome("madam"))
# print(pallindrome("hello"))