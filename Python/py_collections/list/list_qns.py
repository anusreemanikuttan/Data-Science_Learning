

# 1.Write a program to find the character that appears the most number of times in a string.
# Example: 'banana' → 'a' appears 3 times.
# -------------------------------------------------------------------------------------------
# word = input("Enter a word: ")
# max_count = 0
# max_ch = ""
# for ch in word:
#     count = word.count(ch)
#     if count > max_count:
#         max_count = count
#         max_ch = ch
# print(f"{max_ch} appears {max_count} times.")



# 2. Write a program to find the character that appears the least number of times (excluding spaces).
# Example: 'Mississippi' → 'm' appears once.
# ---------------------------------------------------------------------------------------------------
# word = input("Enter a word: ")
# min_count = len(word)
# min_ch = ""
# for ch in word:
#     if ch != " ":
#         count = word.count(ch)
#         if count < min_count:
#             min_count = count
#             min_ch = ch
# print(f"{min_ch} appears once.")


# 3. Find  the longest occurring word  in the list
#    lst=['apple' , 'orange' , 'apple' , 'grapes' , 'apple', 'banana']
#    ---> o/p  will be apple  (repeated the most)
# -------------------------------------------------------------------------
# list=['apple' , 'orange' , 'apple' , 'grapes' , 'apple', 'banana']
# max_count = 0
# max_word = ""
# for i in list:
#     count = list.count(i)
#     if count > max_count:
#         max_count = count
#         max_word = i
# print(f"{max_word} repeated the most")


# Check for Duplicate Characters
# 4. Write a program to check whether a string has duplicate characters or not.
# Example: 'unique' → Output: Yes (since 'u' appears more than once)

# word = input("Enter a string: ")
# count = 0
# for i in word:
#     count = word.count(i)
#     if count > 1:
#         print(f"Yes it has duplicate characters, since {i} appears more than once. ")
#         break
#     else:
#         print("No, it has no duplicate characters")
#         break


# 5. Write a program to find the first non-repeating character in a string.
# Example: 'swiss' → Output: 'w'

word = input("Enter a string: ")
for i in word:
    if word.count(i) == 1:
        print("First non-repeating character:",i)
        break



        