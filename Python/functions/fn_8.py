# vowel count
# Method 2 ---->
# def vowels(word):
#     count = 0
#     for i in word:
#         if i in "aeiouAEIOU":
#             count += 1
#     print(count)
# vowels("hello")
# vowels("world")

# Method 3 ---->
def vowels(word):
    count = 0
    for i in word:
        if i in "aeiouAEIOU":
            count += 1
    return count
print(vowels("hello"))
print(vowels("world"))
