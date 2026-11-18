# print each element in list in sep line
# ----------------------------------------
# lst = [2,3,4,5,6,7,8,9]
# for i in lst:             # print(*lst, sep="\n")
#     print(i)

# OR

#      0 1 2 3
# lst = [2,3,4,5]
# for i in range(4):
#     print(lst[i])

# So , list is iterable


# wap to find te sum of the list
lst = [1,2,3,4,5,6,7,8,9,10]

sum = 0
for i in lst:
    sum += i
print(sum)