

# Write a Python script to find all Armstrong numbers in the range from 1 to 10000 and
# add them to a list.
# Then, calculate the sum and the average of these Armstrong numbers. Additionally, determine and
# print the smallest and largest Armstrong numbers within this range.
# ------------------------------------------------------------------------------------------------------
# def armstrg(num):
#     temp = num
#     digits = len(str(num))   # digits
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** digits     # digit and digits
#         temp //=10
#     return sum == num
# list = []
# for i in range(1,10001):
#     if armstrg(i):
#         list.append(i)
# print("Armstrong Numbers:",list)
# sum = sum(list)
# avg = sum / len(list)
# print("Sum:",sum)
# print("Average:",avg)
# print("Smallest Armstrong Number:",min(list))
# print("Largest Armstrong Number:",max(list))


# Write a Python script to find the second smallest number in a given list of integers.
# Then, perform the following tasks:
# Remove all occurrences of the second smallest number from the list.
# Calculate the product of the remaining numbers in the list
# Sort the modified list in descending order and print it.
# ------------------------------------------------------------------------------------------
# num = [10,5,8,3,2,2,7]
# lst = list(set(num))
# lst.sort()
# sec_smallest = lst[1]
# print("Second Smallest",sec_smallest)
# new_lst = []
# for i in num:
#     if i != sec_smallest:
#         new_lst.append(i)
# print("New List:",new_lst)
# product = 1
# for i in new_lst:
#     product *= i
# print("Product:",product)
# new_lst.sort(reverse=True)
# print("Descending Order:",new_lst)


# Write a Python script using list comprehension to perform the following tasks on a given list of integers:
# Create a new list containing all integers from the original list that are both divisible by 3 and greater than 10.
# Create another list containing the square root of each number from the filtered list.
# Filter this new list to keep only those values that are greater than 5.
# Print the final filtered list of square roots.
# # # numbers = [4, 9, 12, 15, 22, 30, 36, 45, 50]

num = [4, 9, 12, 15, 22, 30, 36, 45, 50]
filtered_lst = [i for i in num if i % 3 == 0 and i > 10]
sq_list = [i ** 0.5 for i in filtered_lst]
sq_filtered = [i for i in sq_list if i > 5]
print(sq_filtered)
