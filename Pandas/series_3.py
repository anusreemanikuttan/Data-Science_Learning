

# create a series in the range of 10 to 25
# -------------------------------------------
import numpy as np
import pandas as pd
a = np.arange(10,26)
s = pd.Series(a)
# print(s)

# head() --> returns first five elements

# print(s.head())
# print(s.head(2))

# tail() --> collects the last five elements

print(s.tail())
print(s.tail(1))