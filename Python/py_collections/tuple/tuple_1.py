

# TUPLE
# ==================================================================================
# 1.How to define?
# =======================================
# Tuple is used to define using open paranthesis () and tuple().
# Multiple variables are assigned into it
# ----------------------------------------
# tu = (3,5,8,9,10)
# print(tu)
# print(type(tu))

# tu = (1,)         # cannot pass only one value as tuple,it will be an integer
# print(tu)        # but the type want to be tuple then add a comma after the value
# print(type(tu))


# 2. Heterogeneous data supported or not?
# ==============================================
# t = (1,"python",3.4,True,False)
# print(t)

# Therefore, TUPLE supports heterogeneous data


# 3. Duplicate values allowed or not?
# ==============================================
# t = (1,2,2,2,4,"python")
# print(t)

# Therefore , TUPLE supports duplicate values


# 4. Insertion order preserved or not?
# ===============================================
# t = (2,3,1,0,4,5,6)
# print(t)

# It prints in the same order as input, so TUPLE preserves insertion order


# # 5. Mutable / Immutable
# ==============================================
# t = (2,6,7,8,1,2,3)
# t[2] = 76
# print(t)

# Tuple supports indexes but we can't update tuple
# Therefore, TUPLE is immutable.

# Tuple is also iterable
# t = (2,6,7,8,1,2,3)
# for i in t:
#     print(i)