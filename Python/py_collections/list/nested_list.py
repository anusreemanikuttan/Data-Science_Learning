

# NESTED LIST
# ====================================
           #   0 1 2   0 1  2   0 1
list = [2,3,7,[2,3,6],[8,9,10],[4,5]]
#index->0 1 2   3       4       5

# print(list[3])     #---> returns [2,3,6]

print(list[3][2])    #----> returns index 2 of first sublist

# print(list[4][0])
# #
# print(list[5][1])