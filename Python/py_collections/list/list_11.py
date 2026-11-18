
# print unique list from the given list
# -----------------------------------------

list = [1,1,1,2,3,4,4,5,6,7,3,8,11,23,11,45]
list1= []
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)

