

# DataFrame
# ==================================

# create a nested list
# with id, fname, lname, age, loc, prof
# collect 6 details

lst = [[101, "Anu", "M", 22, "Pdlm", "DS"],
       [102, "Anju", "K", 25, "EKM", "python"],
       [103, "Kiran", "S", 23, "clt", "java"],
       [104, "Mary", "Smith", 25, "Ny", "python"],
       [105, "Joe", "Biden", 30, "LA", "java"],
       [106, "Justin", "Brown", 28, "Madrid", "java"]]

# import pandas as pd
# df = pd.DataFrame(lst)
# df.columns=["id","fname","lname","age","loc","prof"]
# print(df)

# OR

import pandas as pd
df = pd.DataFrame(lst,columns=["id","fname","lname","age","loc","prof"])
print(df)
print("*"*55)
print(df.ndim)

print("*"*55)
print(df.shape)

print("*"*55)
print(df.head())

print("*"*55)
print(df.tail())

print("*"*55)
print(df.dtypes)  # data types of each column

print("*"*55)

# describe()
# --------------------------
print(df.describe())  # describes integer
print(df.describe(include='str'))
print(df.describe(include="all"))
