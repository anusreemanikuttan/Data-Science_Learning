

# You are given a list of integers, num_list, which represents a consecutive number series.
# In the list:
#           There is one repeating number.
#           There is one missing number.
# Your task is to wap to:
#           Identify the repeated number.
#           Identify the missing number.
#           Calculate the sum of repeating and missing number.
# --------------------------------------------------------------------------------------------

# num_list = [1,1,3,4]
# num_list = [1,2,2,4]
num_list = [2,3,3,5]
repeated = 0
missing = 0
for i in range(min(num_list),max(num_list)+1):
    if num_list.count(i) > 1:
        repeated = i
    if i not in num_list:     # if num_list.count(i) == 0
        missing = i
print("Repeated Number:",repeated)
print("Missing Number:",missing)
print("Sum of Repeated and Missing Numbers:",repeated + missing)

