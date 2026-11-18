

# wap to find the vowels in a string
# ------------------------------------------
# string = input("Enter a string: ")
# for i in string:
#     if i in "aeiouAEIOU":
#         print(i)

# wap to find the vowel count from a given word
# ---------------------------------------------------
string = input("Enter a string: ")
count = 0
for i in string:
    if i in "aeiouAEIOU":
        count += 1
print("Vowel count:",count)

