

# 1. Create a dict of three students with their marks
     # athul:33, arun:23

# 2. Add a new student into the dict
# 3. Update a student mark (from the existing dict)
# 4. Print key:value (downwards)
# 5. Remove a student from the dict
# -------------------------------------------------------

dict = {"Anu":54, "Athul":33, "Arun":23}
print(dict)

dict["Abhi"] = 56
print("New student:",dict)

dict["Anu"] = 65
print("Updated mark:",dict)

for i in dict:
    print(i,":",dict[i])

dict.pop("Athul")
print("Removed a student:",dict)

