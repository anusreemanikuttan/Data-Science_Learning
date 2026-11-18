

# if the file has no header add --> header=None
# add seperation --> sep="\t"  default seperation is comma
# -----------------------------------------------
import pandas as pd
df = pd.read_csv(r"C:\Users\VICTUS\Downloads\sample.txt",header=None,sep="\t")

df.columns=["id", "fname", "lname", "age", "phno", "loc"]
print(df)

print("*"*50)
# print(df[["fname","lname"]])  # it is a dataframe , 2D so double square brackets needed for multiple columns
#
# print("*"*50)
# print(df["fname"])  # single bracket for single column
#
# print("*"*50)
# #  new df with fname, lname, age, phno
# df1 = df[["fname", "lname", "age", "phno"]]
# print(df1)


# how to drop a column from df
# drop()
# -----------------------------------------------------------------
# method 1
# print(df.drop("phno",axis=1))   # axis=1 for columns in pandas

# method 2
# print(df.drop(columns=["phno"]))


# new df with fname, lname, age, phno
# #
# df1 = df.drop(columns=["id", "loc"])
# print(df1)


# first 3 details
#  #
# df1 = df.drop(columns=["id", "loc"]).head(3)
# print(df1)


# filtration
# loc[] ---> used for filtering
# syntax -->
# new_df_name = old_df_name.loc[df["col_name"] condition]
# ----------------------------------------------------------

# age > 25 person details
#
# df1 = df.loc[df["age"] > 25]
# print(df1)

# age = 22 , fname, age, loc
#
# df1 = df.loc[df["age"] == 22]
# print(df1[["fname", "age", "loc"]])

# OR
# df1 = df.loc[df["age"]==22] [["fname", "age", "loc"]]  # can do it in a single line with space
# print(df1)

# age = 27, fname, lname, age, phno
#
# df1 = df.loc[df["age"]==27] [["fname", "lname", "age", "phno"]]
# print(df1)

# chennai working ---> fname, lname, age, loc
#
# df1 = df.loc[df["loc"]=="Chennai"] [["fname", "lname", "age", "loc"]]
# print(df1)

# chennai loc and age > 25 --> fname, age , loc
#
# '&' --> and for 2 conditions , binary and
# '|' --> or, binary or
# '~' --> not
# ------------------------------------------------------
# df1 = df.loc[(df["loc"]=="Chennai") & (df["age"]>25)] [["fname", "age", "loc"]]
# print(df1)


# age > 20 and loc --> kochi --> fname, lname, phno, loc
df1 = df.loc[(df["loc"]=="Kochi") & (df["age"]>20)] [["fname", "lname", "phno", "loc"]]
print(df1)