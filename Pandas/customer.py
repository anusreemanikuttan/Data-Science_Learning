

import pandas as pd
df = pd.read_csv(r"C:\Users\VICTUS\Data Science - Python\customer1.txt",header=None)
df.columns=["id", "fname", "lname", "age", "prof", "loc"]
# print(df)


# how to check the missing values
# isna()  --> returns a series of true and false
# -------------------------------------------------------------
# print(df.isna().sum())  # count of missing values --> sum()


# either fill or drop the missing value
# fillna() --> fill the missing value
# dropna() --> drop the missing value
# --------------------------------------------------
df1 = df.fillna("india")
print(df1)

print("*" * 80)

print(df1.isna().sum())
