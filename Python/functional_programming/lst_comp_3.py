

# 3. Find all of the numbers from 1–300 that have 3 in them
# ---- [3,13,23,30,31,----
# -------------------------------------------------------------
lst = [i for i in range(1,301) if "3" in str(i)]
print(lst)