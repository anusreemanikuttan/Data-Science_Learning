# ask the user for a number
# list = [1,2,4,5,6,7,8,9]
# check if the given number is present in the given list
# if element if found --- print element found
# if element is not present --- print element is not found

num = int(input("Enter a number: "))
list = [1,2,4,5,6,7,8,9]
if num in list:
    print("Element is found")
else:
    print("Element is not found")
