

# create a dic and convert into series
# id name age loc prof
# -----------------------------------------
# dic = {"id":101, "name": "Anusree", "age":22, "loc":"pdlm", "prof":"DS"}
# import pandas as pd
# s = pd.Series(dic, index= ["name","age","loc"])
# print(s)


# create a list and try to collect the index values
#
lst = [1,2,3,4,5,6]
import pandas as pd
s = pd.Series(lst, index = [5,4,3,2,1,0])  # this case ony possible in dic
print(s)  # not possible in list