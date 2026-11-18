

# dic with list
# --------------------------------------------------------
dic = {"name":["anu", "anju", "abhi", "manu", "kiran"],
       "age":[23,22,34,24,27],
       "loc":["ekm","pdlm","clt","tvm","plk"]}
import pandas as pd
df = pd.DataFrame(dic)
print(df)
print("*"*25)
print(df.ndim)
print("*"*25)
print(df.shape)
print("*"*25)
print(df.head(3))
print("*"*25)
print(df.tail(2))
print("*"*25)
print(df.dtypes)