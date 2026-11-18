

# list = [15,3,10,6,9,7]
# from the given list create a new list ---->
# [35,47,48,44,41,43]
# --------------------------------------------

list = [15,3,10,6,9,7]
new_list = []
for i in list:
    new_list.append(sum(list)-i)
print(new_list)