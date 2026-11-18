

# SET
# =========================================================

# # 1. How to define a Set?
# ==============================
# Set is fedined using {} and with set()

# st = {2,3,1}
# print(st)
# print(type(st))

# st = {}       # empty set cannot be defined using {} , it returns dict
# print(type(st))


# 2. Heterogeneous data supported or not?
# ==============================================
# st = {1,"python",3.4,True,False}
# print(st)

# It didn't return 'True' because there is 1 in the set
# True is equal to 1 that's why it removes duplicate and printed 1 only without True

# st = {2,"python",3.4,True,False}
# print(st)
# Therefore, it support heterogeneous data


# 3. Duplicate values allowed or not?
# ===========================================
# st = {1,2,2,2,4,"python"}
# print(st)

# Doesn't allow duplicate values


# 4. Insertion order preserved or not?
# =========================================
 
# Therefore, insertion order is not preserved.

# 5. Mutable / Immutable
# ====================================
# st = {5,6,3,2,1}
# print(st[2])

# SET has no indexes but it is MUTABLE.


# st = {2,3,4,}
# print(sum(st))  # 9

# st = {2,3,4,1,3,2}
# print(sum(st))     # 10 duplicates are removed

# st = {34,56,78,78,23,10}
# print(max(st))           #78

# st = {34,56,78,78,23,10}
# print(min(st))             # 10

# st = {23,45,21,9}
# add() --> adding an element
# st.add(34)
# st.add(100)
# print(st)

# update()    # extend is used in list
# st.update((34,56))   # to add multiple values assign it like a collection, either with () or []
# print(st)

# remove() ---> to remove a value
# error if the removing element is not in the set
# st = {3,4,8,9,10}
# st.remove(10)
# print(st)

# discard() ----> removes the element
# it doesn't give an error if the removing element is not in the set
# st = {3,4,8,9,10}
# st.discard(11)
# print(st)

# pop()  ----> removes randomly
# st = {2,34,56,23,12}
# st.pop()
# print(st)

# SET OPERATIONS
# ==========================================
# 1. Union
# 2. Intersection
# 3, Difference
# ------------------------------------------

st1 = {1,2,3,4,5,6,7,8,9,10}
st2 = {5,6,7,8,9,10,11,12,13}

# Union
# ------------------------------------
st3 = st1.union(st2)
print(st3)   # combined 2 sets , removes duplicates

# Intersection
# ------------------------------------
st4 = st1.intersection(st2)
print(st3)

# Difference
# ------------------------------------
st5 = st1.difference(st2)
print(st5)

st6 = st2.difference(st1)
print(st6)