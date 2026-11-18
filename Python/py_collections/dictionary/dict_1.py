

# DICTIONARY
# ============================================

# 1. How to define a dictionary?
# ---------------------------------
# {} used to define dict

# values are passed into dictionary like --> key:value pair

# dict = {"anu":30, "anju":34}
# print(dict)
# print(type(dict))

# key    value
# -------------
# anu      30
# anju     34

# create a dict
# id, fname, lname, age, profession, loc
# ---------------------------------------
# dict = {"id":101, "fname":"Anu", "lname":"M", "age":23, "prof":"DS", "loc":"PTA"}
# print(dict)


# 2. Heterogeneous data supported or not?
# ------------------------------------------
# Heterogeneous data are supported


# 3. Duplicate values allowed or not?
# ------------------------------------

# dict = {"id":101, "fname":"Anu", "lname":"M", "age":23, "prof":"DS", "loc":"PTA", "Mark":30, "Mark":24}
# print(dict)
# Therefore, dict doesn't support duplicate keys

# dict = {"id":101, "fname":"Anu", "lname":"M", "age":23, "prof":"DS", "loc":"PTA", "Mark1":30, "Mark2":30}
# print(dict)
# But it supports duplicate values!!!


# 4. Insertion order preserved or not?
# ---------------------------------------
# Insertion order is preserved in dictionary


# 5. Mutable / Immutable
# ------------------------
dict = {"id":101, "fname":"Anu", "lname":"M", "age":23, "prof":"DS", "loc":"PTA", "Mark1":30, "Mark2":30}
print(dict)

# var_name[key] ---> to collect and display
# print(dict["fname"])
# print(dict["age"])

# updating a dict
# ----------------
# age - 24 ---> 27
# dict["age"] = 27
# dict["prof"] = "java"
# print(dict)

# Therefore, Dict is Mutable

# How to add new key value?
# ---------------------------
# var_name[key] = value  ----> new key value added at the end
# dict["salary"] = 1000
# print(dict)