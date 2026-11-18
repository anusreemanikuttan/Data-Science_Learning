# wap to find the vowels from a given word
# Method 1 --->
# def vowels():
#     word = input("Enter a word: ")
#     for i in word:
#         if i in "aeiouAEIOU":
#             print(i)
# vowels()
# vowels()

# Method 2 ---->
# def vowels(word):
#     for i in word:
#         if i in "aeiouAEIOU":
#             print(i)
# vowels("hello")
# vowels("important")

# Method 3 --->
def vowels(word):
    c = ""
    for i in word:
        if i in "aeiouAEIOU":
            c += i + "\n"     # it concatenates the vowels , so set it to the next line
    return c
print(vowels("hello"))

