# write a program to create a list  of words and find all words that
# starts and end with same letter.
# store the words in a new list and print both the
# new list and total count of such words

list = ["mom","dad","dance","click","key","malayalam","food","bulb"]
list1 = []
for i in list:
    if i[0] == i[-1]:
        list1.append(i)
print(list1)
print("Total count of words: ",len(list1))
