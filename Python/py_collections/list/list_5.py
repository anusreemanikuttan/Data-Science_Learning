# create a list of element in the range of 1 to 100
# print the main list and sum of the main list
# find the even numbers from the given range of elements
# also find the sum of even number
# find the odd numbers from the same range
# also find the sum of odd numbers

list = []
even = []
odd = []
for i in range(1,101):
    list.append(i)
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Main list -",list)
print("Sum of main list -",sum(list))
print("Even list -",even)
print("Sum of Even Numbers - ",sum(even))
print("Odd list",odd)
print("Sum of Odd Numbers - ",sum(odd))