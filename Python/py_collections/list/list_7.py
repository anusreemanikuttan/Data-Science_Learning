

# create a list of numbers. Find the position of each element (starting from 1)
# Raise the element to the power of its position.
# Store the results in a new list and display it.

# list = [2,4,3,1]
# pow_list = []
# j = 1   # position starting from 1
# for i in list:
#     pow_list.append(i ** j)
#     j += 1
# print(pow_list)


# using index

list = [2,4,3,1]
pow_list = []
for i in range(len(list)):  # range --> 0 1 2 3 - can be connected to index
    pow_list.append(list[i]**(i+1))
print(pow_list)
